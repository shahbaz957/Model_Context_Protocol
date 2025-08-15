from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
import asyncio

async def main():
    client = MultiServerMCPClient(
        {
            'math': {
                "command":"python",
                "args" : ["./mathserver.py"] ,# ensure correct absolute path
                "transport" : "stdio"
            },
            "weather" : {
                "url" : "http://127.0.0.1:8000/mcp",
                "transport" : "streamable_http"
            }
            
        }
    )

    tools = await client.get_tools()
    model = ChatGroq(model='llama-3.3-70b-versatile')

    agent = create_react_agent(model , tools,    prompt=(
        "You are a math assistant. "
        "When using the multiply tool, always pass only integers. "
        "Do not nest tool calls. "
        "If you need to compute something first, call add() separately "
        "and then pass its result into multiply()."
    ))
    math_response = await agent.ainvoke(
        {'messages' : [{"role" : "user" , "content" : "What is (3+6) x 10"}]}
    )
    print("Math _ Response : " , math_response['messages'][-1].content)
    w_response = await agent.ainvoke(
        {'messages' : [{"role" : "user" , "content" : "What is the weather in California"}]}
    )
    print("Weather _ Server _ Response : " , w_response['messages'][-1].content)


asyncio.run(main())