import requests
import os
from urllib.parse import urlparse

def baixar_html(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("[+] HTML baixado com sucesso.")
            return response.text
        else:
            print(f"[!] Erro ao acessar o site: {response.status_code}")
            return None
    except Exception as e:
        print(f"[!] Erro durante a requisição: {e}")
        return None

def salvar_arquivo(html, url):
    dominio = urlparse(url).netloc.replace(".", "_")
    pasta = "paginas"
    os.makedirs(pasta, exist_ok=True)
    caminho = os.path.join(pasta, f"{dominio}.html")

    with open(caminho, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"[+] HTML salvo em: {caminho}")

def main():
    print("=== Clonador Educacional de Sites ===")
    url = input("Digite a URL do site (com http:// ou https://): ").strip()

    html = baixar_html(url)
    if html:
        salvar_arquivo(html, url)

if __name__ == "__main__":
    main()
