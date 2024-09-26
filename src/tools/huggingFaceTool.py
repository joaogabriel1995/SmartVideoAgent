from crewai import Agent, Task, Crew, Process
import requests
# Ferramenta Hugging Face personalizada
from langchain.tools import tool

class HuggingFaceTool:

    # Inicializa a ferramenta com a chave da API e o nome do modelo Hugging Face
    def __init__(self, api_key: str, api_url: str):
        """
        Construtor para a classe HuggingFaceTool.

        Args:
            api_key (str): A chave de API necessária para acessar o Hugging Face.
            model_name (str): O nome do modelo Hugging Face a ser utilizado.
        """
        self.api_key = api_key
        # Define a URL da API do Hugging Face com base no modelo fornecido
        self.api_url = api_url
        # Cabeçalhos de autorização para autenticar a chamada à API
        self.headers = {"Authorization": "Bearer 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"}

    # @tool("Hugging Face Model Inference")
    def call_model(self, input_text: str, candidate_labels):
        """
        Método para chamar o modelo do Hugging Face.

        Args:
            input_text (str): O texto de entrada que será enviado ao modelo Hugging Face.

        Returns:
            dict: A resposta da API, incluindo o resultado do modelo ou um erro em caso de falha.
        """
        # Cria o payload com o texto de entrada
        payload = {"inputs": input_text,
                       "parameters": {"candidate_labels": candidate_labels},
                   }
        # Faz uma requisição POST para a API do Hugging Face
        response = requests.post(self.api_url, headers=self.headers, json=payload)
        # Verifica se a resposta foi bem-sucedida (código 200)
        if response.status_code == 200:
            # Retorna a resposta da API em formato JSON
            print("HuggingFaceToolHuggingFaceToolHuggingFaceToolHuggingFaceToolHuggingFaceToolHuggingFaceToolHuggingFaceToolHuggingFaceToolHuggingFaceToolHuggingFaceTool",response.json() )
            return response.json()
        else:
            # Retorna uma mensagem de erro caso a requisição falhe
            return {"error": response.text}



if __name__ == "__main__":
    from dotenv import load_dotenv

    import os
    HUGGING_FACE_KEY = os.getenv('HUGGING_FACE_KEY')
    load_dotenv()
    huggingFaceTool =HuggingFaceTool(HUGGING_FACE_KEY, "https://api-inference.huggingface.co/models/facebook/bart-large-mnli")

    content = {
    "inputs": "I love the product! It's amazing and works perfectly.",
    "parameters": {"candidate_labels": ["positive", "neutral", "negative"]},

    }
    data = huggingFaceTool.call_model(content)
    print(data)