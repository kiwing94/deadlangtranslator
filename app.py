
from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Load dictionaries
def load_dictionary(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Load dictionaries for each language
koine_dict = load_dictionary('koine_greek.json')
latin_dict = load_dictionary('latin.json')
sumerian_dict = load_dictionary('sumerian.json')
sanskrit_dict = load_dictionary('sanskrit.json')

# Main translation function
def translate(word, from_lang, to_lang):
    if from_lang == "english":
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

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        word = request.form['word']
        from_lang = request.form['from_lang']
        to_lang = request.form['to_lang']
        result = translate(word, from_lang, to_lang)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
