from fastmcp import FastMCP
# Create an MCP server
mcp = FastMCP("multiply")
# Add an addition tool
@mcp.tool
async def multiply(a: float, b: float) -> float:
    """Multiply two numbers (async example)."""
    return a * b