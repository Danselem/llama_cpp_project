from starlette.requests import Request
from typing import Dict
from ray import serve
from ray.serve import Application
from llama_cpp import Llama

@serve.deployment
class LlamaDeployment:
    def __init__(self, model_path: str):
        self._llm = Llama(model_path=model_path)

    async def __call__(self, http_request: Request) -> Dict:
        input_json = await http_request.json()
        prompt = input_json["prompt"]
        max_tokens = input_json.get("max_tokens", 64)
        # return self._llm(prompt, max_tokens=max_tokens)

        response = self._llm.create_chat_completion(
            messages = [
                {"role": "system", "content": "You are an assistant who perfectly\
                    answers correct answers \
                    to your question with the best of your ability.\
                        In the case you have no idea of how to answer the question, \
                            decline politely"},
                {
                    "role": "user",
                    "content": {prompt}
                }
            ]
            )

        return response["choices"][0]['message']['content']


def llm_builder(args: Dict[str, str]) -> Application:
    return LlamaDeployment.bind(args["model_path"])
