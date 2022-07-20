import torch
import transformers
import os

from transformers import BertTokenizer
from transformers import BertModel


# download the model

# model_dir = "hfl/chinese-roberta-wwm-ext-large" # change the dir of the model(name or path)
# model_cache = "./pretrained/roberta-wwm-large" # change the cache dir (local path to store the model)

# file_path = __file__
# print(os.path[0])

def download(model_dir, model_cache):
    print("Begin to download...")
    print(f"The model you want to download is {model_dir}.")
    print(f"The local path to store is {model_cache}.")

    isBert = input("Download pretrained Bert models. (y/n)")
    if isBert:
        print("Download the tokenizer...")
        tokenizer = BertTokenizer.from_pretrained(model_dir, cache_dir=model_cache)
        print("The tokenizer is downloaded.")

        print("Download the pretrained model...")
        model = BertModel.from_pretrained(model_dir, cache_dir=model_cache)
        print("The pretrained model is downloaded.")

    print("Download Finished.")