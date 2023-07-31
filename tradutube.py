import subprocess
import os
from translate import Translator

# Idiomas mais falados na internet (em ordem de uso)
languages = ['en', 'zh-cn', 'es', 'ja', 'hi', 'ar', 'pt', 'bn', 'ru', 'de', 'jv', 'id', 'sw', 'fr', 'ur', 'tr', 'it',  'ko', 'th']

# Pede ao usuário que insira uma frase para ser traduzida
phrase = input("Insira a frase para ser traduzida: ")


# Pede ao usuário que escolha entre guia anônima ou normal
tab_option = input("Escolha a opção de guia (anônima/normal): ")
if tab_option.lower() == "anônima":
    incognito_mode = True
else:
    incognito_mode = False

# Verifica qual navegador está sendo utilizado para abrir o link
if os.name == 'posix':  # Unix/Linux/MacOS
    chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
elif os.name == 'nt':  # Windows
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
else:
    print("Navegador não suportado.")

# Faz a tradução da frase para cada um dos idiomas
for language in languages:

    # Faz a tradução
    translator = Translator(to_lang=language)
    translation = translator.translate(phrase)

    # Seleciona o site de vídeos escolhido
    site_url = 'https://www.youtube.com/results?search_query='

    if site_url is not None:
        # Cria a URL para a pesquisa no site de vídeos escolhido
        url = f"{site_url}{translation.replace(' ', '+')}"


    # Restante do código do segundo commit...

    # Abre o link em uma guia anônima ou normal do navegador
    if incognito_mode:
        subprocess.run([chrome_path, "--incognito", url])  # Para sistemas Unix/Linux/MacOS com Google Chrome instalado
    elif os.name == 'nt':  # Windows
        subprocess.run([chrome_path, url])
    else:
        print("Navegador não suportado.")