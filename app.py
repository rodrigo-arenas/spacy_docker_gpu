import spacy
import torch
from flask import Flask

app = Flask(__name__)

# Check GPU support

print(f"PyTorch GPU V1: {torch.cuda.is_available()}")
print(f"Spacy GPU V1: {spacy.prefer_gpu()}")

spacy_model_list = ["en_core_web_sm", "en_core_web_trf"]

for base_model in spacy_model_list:
    if not spacy.util.is_package(base_model):
        spacy.cli.download(base_model)

# Check if models affect GPU support as reported by some users

print(f"PyTorch GPU V2: {torch.cuda.is_available()}")
print(f"Spacy GPU V2: {spacy.prefer_gpu()}")


@app.route('/')
def hello():
    return "hello"


@app.route('/spacy')
def get_cupy_gpu():
    return f"{spacy.prefer_gpu()}"


@app.route('/torch')
def get_torch_gpu():
    return f"{torch.cuda.is_available()}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5501, debug=True)
