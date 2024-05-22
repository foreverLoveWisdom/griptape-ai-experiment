from dotenv import load_dotenv
import os
import pprint
from anthropic import Anthropic
from griptape.structures import Agent
from griptape.drivers import AnthropicPromptDriver, OpenAiEmbeddingDriver

from griptape.config import StructureConfig, StructureGlobalDriversConfig
from griptape.tools import WebScraper, FileManager, TaskMemoryClient

load_dotenv()

# client = Anthropic(
#     api_key=os.getenv("ANTHROPIC_API_KEY"),
# )

# response = client.messages.create(
#     max_tokens=4096,
#     temperature=0.0,
#     system="Act as master of the game of 20 questions, answering questions about the world.",
#     messages=[
#         {
#             "role": "user",
#             "content": f"what is the capital of France?",
#         }
#     ],
#     model="claude-3-haiku-20240307",
# )

# pprint.pprint(response.content)


# agent = Agent(
#     config=StructureConfig(
#         global_drivers=StructureGlobalDriversConfig(
#             prompt_driver=AnthropicPromptDriver(
#                 model="claude-3-haiku-20240307",
#                 api_key=os.environ["ANTHROPIC_API_KEY"],
#             )
#         )
#     ),
#     input_template="Load {{args[0]}}, summarize it, and store it in a file called {{args[1]}}",
#     tools=[WebScraper(), TaskMemoryClient(off_prompt=True), FileManager()],
# )

# agent.run("https://en.wikipedia.org/wiki/LangChain", "test.txt")


file_manager_tool = FileManager()

agent = Agent(
    config=StructureConfig(
        global_drivers=StructureGlobalDriversConfig(
            prompt_driver=AnthropicPromptDriver(
                model="claude-3-haiku-20240307",
                api_key=os.environ["ANTHROPIC_API_KEY"],
            ),
            embedding_driver=OpenAiEmbeddingDriver(),
        )
    ),
    tools=[file_manager_tool],
)

filename = "sample.txt"
content = "\n\n\nThis is a sample file.\n\n\n"

with open(filename, "w") as f:
    f.write(content)

agent.run("Can you get me the sample.txt file?")
