from crewai import Task
from textwrap import dedent
from datetime import date
from tools.huggingFaceTool import HuggingFaceTool

class VideosInsightsTasks:

    def analyze_video_task(self, agent, input_file, classified_transcript):
        with open(input_file, 'r') as file:
            content = file.read()  # Lê o conteúdo do arquivo
            print(content)  # Exibe o conteúdo do arquivo
            return Task(
                description=dedent(f"""
                    Analisar o conteúdo de um arquivo de transcrição de vídeo, o documento gerado pelo agente de classificação:
                    {classified_transcript}

                    Sugerir os melhores momentos para cortes estratégicos.
                    Utilize técnicas de análise de texto para identificar mudanças de tema, ritmo ou momentos importantes.
                    Certifique-se de que os momentos selecionados maximizem o impacto e a fluidez do vídeo final.
                    Transcrição fornecida:
                    {content}
                    Identifique pontos altos do conteúdo: Procure partes onde o apresentador demonstra mais entusiasmo ou compartilha informações importantes.
                    Encontre momentos emocionalmente impactantes: Segmentos que provocam humor, surpresa ou inspiração tendem a engajar mais.
                    Busque por frases marcantes ou citações: Destaque expressões memoráveis ou insights profundos.
                    Aproveite conteúdos visualmente atraentes: Selecione momentos com elementos visuais interessantes ou demonstrações práticas.
                    Identifique tópicos em alta ou tendências: Aborde assuntos que estão em evidência para aumentar a relevância.
                    Utilize cliffhangers ou teasers: Escolha trechos que deixem o espectador curioso.
                    Foque em histórias completas e concisas: Conte mini-histórias com início, meio e fim em até 1 minuto.
                    Analise palavras-chave na transcrição: Identifique termos populares ou muito pesquisados para potencializar o alcance.
                    Para criar nomes chamativos:

                    Use palavras de ação e termos poderosos: Utilize verbos fortes e adjetivos impactantes.
                    Crie senso de urgência ou curiosidade: Títulos que provocam questionamentos incentivam cliques.
                    Seja objetivo e direto: Títulos curtos e claros são mais eficazes em formatos curtos.
                    Inclua números ou listas quando relevante: Números chamam atenção e organizam o conteúdo.
                    Utilize perguntas provocativas: Engaje o espectador desde o início com perguntas.
                    Incorpore palavras-chave relevantes: Melhore a otimização de busca (SEO) do conteúdo.
                    Evite clickbait exagerado: Garanta que o título reflita o conteúdo real para não frustrar o público.
                    Personalize para o público-alvo: Adapte a linguagem e o estilo ao perfil dos espectadores.
                """),
                agent=agent,
                expected_output='''Gerar uma lista com os 10 momentos mais destacados para cortes estratégicos em um vídeo, com base na transcrição fornecida.
                    1. **Título atrativo:** Sugestões de títulos com elementos chamativos (incluindo clickbait) que aumentem o apelo do vídeo, especialmente considerando o estilo de grandes criadores de conteúdo no YouTube e TikTok.
                    2. **Justificativa:** Breve explicação do motivo da escolha do corte, levando em conta o impacto visual, emocional ou informativo.
                    3. **Timestamp:** Tempo inicial e final do corte em segundos decorridos.
                    4. **Resumo do corte:** Indicar a hora e minuto de início e fim do corte (convertido dos timestamps).
                    Os cortes devem ser selecionados para maximizar engajamento, mantendo fluidez e impacto. A análise deve identificar momentos de mudança de tema, clímax ou trechos que se destacam. 
                    Os cortes devem ter no MíNIMO 50 segundos. Se estiver fora desse intervalo de tempo não poderá ser utilizado.
                    Pegar cortes distribuidos pelo video ou seja, cortes que estão no inicio da transcrição, no meio e no fim.
                                        ''',
                tools=[]
            )
