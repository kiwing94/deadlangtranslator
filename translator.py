
import json

# Load the language dictionaries
def load_dictionary(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Define the dictionaries (loaded once)
koine_dict = load_dictionary('koine_greek.json')
latin_dict = load_dictionary('latin.json')
sumerian_dict = load_dictionary('sumerian.json')
sanskrit_dict = load_dictionary('sanskrit.json')

# Main translation function
def translate(word, from_lang, to_lang):
    if from_lang == "english":
        # Translate from English to another language
        if to_lang == "sanskrit":
            return sanskrit_dict.get(word, "Word not found in Sanskrit dictionary")
        elif to_lang == "koine":
            return koine_dict.get(word, "Word not found in Koine Greek dictionary")
        elif to_lang == "latin":
            return latin_dict.get(word, "Word not found in Latin dictionary")
        elif to_lang == "sumerian":
            return sumerian_dict.get(word, "Word not found in Sumerian dictionary")
        else:
            return "Target language not supported"
    else:
        return "Source language not supported"

# Example test for the translation
word = "peace"
from_lang = "english"
to_lang = "sanskrit"

result = translate(word, from_lang, to_lang)
print(f"Translation of '{word}' from {from_lang} to {to_lang}: {result}")
