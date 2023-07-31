# Importe apenas as bibliotecas necessárias para esta etapa
from translate import Translator

# Pede ao usuário que insira uma frase para ser traduzida
phrase = input("Insira a frase para ser traduzida: ")

# Idioma de destino para a tradução
target_language = 'en'

# Faz a tradução da frase
translator = Translator(to_lang=target_language)
translation = translator.translate(phrase)

print(f"Frase traduzida para {target_language}: {translation}")
