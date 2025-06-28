from spellchecker import SpellChecker
from langdetect import detect

def spellcheck_english(text):
    spell = SpellChecker(language='en')
    words = text.lower().split()
    misspelled = spell.unknown(words)
    return list(misspelled)

def check_text_language(text):
    try:
        lang = detect(text)
    except:
        lang = "unknown"
    return lang