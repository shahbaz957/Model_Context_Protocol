from mcp.server.fastmcp import FastMCP
## this is jsut the server name
mcp = FastMCP("Math")

@mcp.tool()
def add(a : int , b : int) -> int :
    """
    Add two numbers
    """
    return a+b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """
    Multiply two numbers. Parameters must be integers only.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("multiply() expects integers only, not objects.")
    return a * b


if __name__ == "__main__":
    mcp.run(transport="stdio")

