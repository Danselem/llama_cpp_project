# llama_cpp_project
An llama cpp project for Apple Metal.

Option 1: Cloning the Repository
Clone this repository:

git clone https://github.com/Danselem/llama_cpp_project.git
Change to the cloned repository directory:

```bash
cd vllm_project
```
Create a virtual environment


```bash
python3.10 -m venv .venv
```

Activate the virtual environment
```bash
source .venv/bin/activate
```

```bash
CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python
```

Install the required Python packages:

```bash
pip install --upgrade pip
pip install -r requirements.txt


```bash
serve run llm:llm_builder model_path='.model/qwen1_5-0_5b-chat-q8_0.gguf'

serve run llm:llm_builder model_path='.model/mistral-7b-instruct-v0.2.Q4_K_M.gguf'

serve run app:llm_builder model_path='Qwen/Qwen1.5-0.5B-Chat-GGUF'
```

curl -k -d '{"prompt": "tell me a joke", "max_tokens": 128}' -X POST http://localhost:8000


127.0.0.1:8265