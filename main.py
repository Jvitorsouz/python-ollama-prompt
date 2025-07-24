import requests

def enviar_prompt(prompt: str, modelo: str = "llama3") -> str:
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": modelo,
        "prompt": prompt,
        "stream": False  # stream=False retorna tudo de uma vez
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()
    data = response.json()
    return data["response"]

# Exemplo de uso
if __name__ == "__main__":
    prompt_usuario = input("Digite seu prompt: ")
    resposta = enviar_prompt(prompt_usuario)
    print("\nResposta da IA:\n", resposta)
