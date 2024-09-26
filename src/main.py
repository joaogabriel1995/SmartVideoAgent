from agents.video_insights_agents import VideosInsightsAgents 
from agents.text_classification_agent import TextClassificationAgent 

from agents.leader_agent import LeaderAgent 

from tasks.video_insights_tasks import VideosInsightsTasks 
from tasks.text_classification_task import TextClassificationTask 

from tools.huggingFaceTool import HuggingFaceTool

from crewai import Crew,Process
from dotenv import load_dotenv
import os

load_dotenv()
HUGGING_FACE_KEY = os.getenv('HUGGING_FACE_KEY')
class VideosInsightsCrew:

    def __init__(self, input_file):
        self.input_file = input_file

    def run(self):

        # tools

        huggingFaceTool =HuggingFaceTool(HUGGING_FACE_KEY, "https://api-inference.huggingface.co/models/facebook/bart-large-mnli")


        #agents Class
        videos_insights_agents = VideosInsightsAgents()
        leader_agent = LeaderAgent()
        text_classification_agent = TextClassificationAgent()


        #agents 
        create_video_insights_agent = videos_insights_agents.create_video_insights_agent()
        leader_agent = leader_agent.leader_agent()
        classification_agent = text_classification_agent.text_classification_agent()

        #task Class
        videos_insights_tasks = VideosInsightsTasks()
        text_classification_task = TextClassificationTask(huggingFaceTool)

        #task
        text_classification_task = text_classification_task.text_classification(
            classification_agent,
            self.input_file
        )
        analyze_video_task = videos_insights_tasks.analyze_video_task(
            create_video_insights_agent, 
            self.input_file,
            text_classification_task
        )

        crew = Crew(
            agents=[
                classification_agent,
                create_video_insights_agent],
            tasks=[
                text_classification_task,
                analyze_video_task, 
                ],
            verbose=True,
            process=Process.hierarchical,  
            manager_agent=leader_agent  

        )

        result = crew.kickoff()
        return result
    

if __name__ == "__main__":
    print("## Welcome to Trip Planner Crew")
    print('-------------------------------')
    # trip_crew = VideosInsightsCrew("./TESTO EM GEL VALE A PENA？ - IRONBERG PODCAST CORTES.txt")
    trip_crew = VideosInsightsCrew("./TODAS AS DÚVIDAS SOBRE UM SNIPER ｜ ATIRADOR DE ELITE – ACHISMOS #114.txt")

    result = trip_crew.run()