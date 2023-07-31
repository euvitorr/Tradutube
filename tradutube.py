import subprocess
import os
from translate import Translator

# Idiomas mais falados na internet (em ordem de uso)
languages = ['en', 'zh-cn', 'es', 'ja', 'hi', 'ar', 'pt', 'bn', 'ru', 'de', 'jv', 'id', 'sw', 'fr', 'ur', 'tr', 'it',  'ko', 'th']

# Pede ao usuário que insira uma frase para ser traduzida
phrase = input("Insira a frase para ser traduzida: ")

# Faz a tradução da frase para cada um dos idiomas
for language in languages:
    # Faz a tradução
    translator = Translator(to_lang=language)
    translation = translator.translate(phrase)

    # Exibe a frase traduzida
    print(f"Frase traduzida para {language}: {translation}")
