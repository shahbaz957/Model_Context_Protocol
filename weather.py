from mcp.server.fastmcp import FastMCP

mcp = FastMCP('Weather')

@mcp.tool()
async def get_weather(location : str) -> str:
    """Get the weather of Given location"""
    return "Its always rainy in California"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")