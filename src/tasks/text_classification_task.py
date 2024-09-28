from crewai import Task
from textwrap import dedent
from datetime import date
from tools.huggingFaceTool import HuggingFaceTool
from tools.splite_text import Helpers

class TextClassificationTask:
    def __init__(self,huggingFaceToolInstance: HuggingFaceTool):
        self.huggingFaceToolInstance = huggingFaceToolInstance


    def text_classification(self, agent, input_file, candidate_labels=["felicidade", "tristeza", "surpresa", "raiva"]):
        
            # helpers = Helpers().split_text(input_file)  # Helper para dividir o texto
            text = []
            with open(input_file, 'r') as file:
                content = file.read()  # Lê o conteúdo do arquivo
                # segmentos = content.split("Texto")
                # split = []
            
            # for i in range(len(helpers)):
            classification = self.huggingFaceToolInstance.call_model(content, candidate_labels)
            text.append(classification)
            
            return Task(
                description=dedent(f"""
                    Analisar o conteúdo de uma transcrição de vídeo e classificar os momentos em sentimentos: positivos, neutros e negativos.
                    Certifique-se de destacar os momentos que maximizam o impacto emocional e contribuem para a fluidez do vídeo final.
                    
                    **Transcrição fornecida:**
                    {text}
                    
                    Utilizando a ferramenta self.huggingFaceToolInstance.call_model(content, candidate_labels)
                    gere as seguintes classificações;

                    **Objetivo:**
                    Classificar cada segmento da transcrição com uma das três etiquetas:
                    - Felicidade
                    - Tristeza
                    - Surpresa
                    - Raiva
                    Use uma abordagem objetiva e consistente na classificação.
                """),
                agent=agent,
                expected_output=dedent(f"""
                                
                    Um relatório detalhado com os momentos classificados de acordo com os seguintes sentimentos:
                    - Felicidade: Identificar momentos que causam emoções de felicidade.
                    - Tristeza: Identificar momentos que causam emoções de Tristeza.
                    - Surpresa: Identificar momentos que causam emoções de Surpresa.
                    - Raiva: Identificar momentos que causam emoções de Raiva.         

                    Relatório entregue em formato de tabela:
                    - Segmento (por tempo ou trecho)
                    - Classificação (felicidade", "tristeza", "surpresa", "raiva)
                    - Justificativa para a classificação
                    - Especifique qual ferramenta foi utilizada para a classificação
                    - retorne o array com as porcentagens da ferramenta utilizada

                    
                """),
                tools=[self.huggingFaceToolInstance.call_model]
            )
