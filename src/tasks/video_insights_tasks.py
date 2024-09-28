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

                    **Objetivo:**
                    Identificar e sugerir o máximo de momentos possíveis para cortes estratégicos que possam ser transformados em vídeos curtos de até 1 minuto.

                    **Instruções:**
                    - Utilize técnicas de análise de texto para identificar mudanças de tema, momentos de maior impacto ou destaque.
                    - Selecione trechos que maximizem o engajamento, mantendo fluidez e impacto.
                    - Os cortes devem ter entre **50 a 60 segundos**. Cortes fora desse intervalo não poderão ser utilizados.
                    - Distribua os cortes ao longo de todo o vídeo: inclua trechos do início, meio e fim da transcrição.
                    - Cada corte será postado separadamente como um vídeo curto (short).

                    **Transcrição fornecida:**
                    {content}

                    **Dicas para seleção de cortes:**
                    - **Pontos altos do conteúdo:** Partes onde o apresentador demonstra mais entusiasmo ou compartilha informações importantes.
                    - **Momentos emocionalmente impactantes:** Segmentos que provocam humor, surpresa ou inspiração.
                    - **Frases marcantes ou citações:** Expressões memoráveis ou insights profundos.
                    - **Conteúdos visualmente atraentes:** Momentos com elementos visuais interessantes ou demonstrações práticas.
                    - **Tópicos em alta ou tendências:** Assuntos que estão em evidência para aumentar a relevância.
                    - **Cliffhangers ou teasers:** Trechos que deixam o espectador curioso.
                    - **Histórias completas e concisas:** Mini-histórias com início, meio e fim em até 1 minuto.
                    - **Palavras-chave populares:** Termos muito pesquisados para potencializar o alcance.

                    **Dicas para criação de títulos chamativos:**
                    - Use palavras de ação e termos poderosos (verbos fortes e adjetivos impactantes).
                    - Crie senso de urgência ou curiosidade.
                    - Seja objetivo e direto; títulos curtos e claros são mais eficazes.
                    - Inclua números ou listas quando relevante.
                    - Utilize perguntas provocativas.
                    - Incorpore palavras-chave relevantes para SEO.
                    - Evite clickbait exagerado; o título deve refletir o conteúdo real.
                    - Personalize para o público-alvo; adapte a linguagem e o estilo.

                    Sempre responda em português (pt-BR).
                """),
                agent=agent,
                expected_output=dedent(f"""
                    **Instruções para o Output:**

                    Gere uma lista com o **máximo de momentos destacados possíveis** para cortes estratégicos no vídeo, com base na transcrição fornecida.

                    Para **cada corte**, forneça:

                    1. **Título atrativo:** Sugestão de um título chamativo (incluindo elementos de clickbait) que aumente o apelo do vídeo, especialmente considerando o estilo de grandes criadores de conteúdo no YouTube e TikTok.
                    2. **Justificativa:** Breve explicação do motivo da escolha do corte, levando em conta o impacto visual, emocional ou informativo.
                    3. **Timestamp:** Tempo inicial e final do corte em segundos decorridos.
                    4. **Resumo do corte:** Breve descrição do conteúdo do corte.

                    **Observações:**
                    - Certifique-se de que cada corte tenha entre **50 a 60 segundos**.
                    - Os cortes devem estar distribuídos ao longo de todo o vídeo.
                    - Lembre-se de que esses cortes serão postados separadamente como vídeos curtos.

                    **Exemplo de Output:**

                    **Corte 1:**
                    1. **Título atrativo:** "Descubra o Segredo por Trás do Sucesso Repentino!"
                    2. **Justificativa:** Momento em que o apresentador revela insights surpreendentes sobre estratégias eficazes.
                    3. **Timestamp:** Início: 120s, Fim: 180s
                    4. **Resumo do corte:** O apresentador compartilha dicas valiosas sobre como alcançar o sucesso em pouco tempo.

                    (Repita o formato para cada corte identificado.)
                """),
                tools=[]
            )
