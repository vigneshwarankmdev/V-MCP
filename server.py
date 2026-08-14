# server.py
import os

from fastmcp import FastMCP

# 1. Initialize the MCP server and give it a name
mcp = FastMCP("My First Calculator Server")

# 2. Define a function and register it as an AI tool using the decorator
@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """
    Add two numbers together.
    
    The AI reads this docstring to understand what the tool does, 
    what parameters it expects, and when it should use it.
    """
    return a + b


@mcp.tool()
def subtract_numbers(a: int, b: int) -> int:
    """
    Subtract the second number from the first number.
    """
    return a - b

if __name__ == "__main__":
    # Auto-switch to HTTP in hosted environments (Render sets PORT).
    default_transport = "streamable-http" if os.getenv("PORT") else "stdio"
    transport = os.getenv("FASTMCP_TRANSPORT", default_transport).lower()

    if transport in {"http", "streamable-http", "sse"}:
        host = os.getenv("HOST", "0.0.0.0")
        port = int(os.getenv("PORT", "8000"))
        path = os.getenv("FASTMCP_PATH", "/mcp")
        mcp.run(transport=transport, host=host, port=port, path=path)
    else:
        mcp.run(transport="stdio")
