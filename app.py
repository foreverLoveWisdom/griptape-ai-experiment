from dotenv import load_dotenv
import os
from griptape.structures import Agent
from griptape.tools import WebScraper

load_dotenv()

# Create an Agent and give it a tool
agent = Agent(tools=[WebScraper(off_prompt=False)])

# Run the Agent
agent.run("Hi, can you summarize http://griptape.ai for me?")
