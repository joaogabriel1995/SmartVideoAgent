
from crewai import Agent



class TextClassificationAgent():
    

    def text_classification_agent(self):
        return  Agent(
            role='Agente de Classificação de Sentimentos',
            goal='Analisar textos e determinar o sentimento (positivo, negativo ou neutro)',
            backstory=(
                "Você é um especialista em análise de sentimentos e consegue identificar com precisão o tom emocional de qualquer texto. "
                "Sua tarefa é fornecer uma classificação clara e concisa, seja positiva, negativa ou neutra."
            ),
            allow_delegation=False,  # Este agente não delega
            tools=[],  # Adicione uma ferramenta se necessário, como ferramentas de NLP
            verbose=True
        )            
