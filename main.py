import os
from dotenv import load_dotenv
from langchain.agents import create_agent

load_dotenv()
model=os.getenv("MODEL")
agent=create_agent(model=model)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "1+1 isleminin sonucu kactir?d"}]}
)

print(result["messages"][-1].content_blocks)
