from fastmcp import FastMCP
import datetime
# Create an MCP server
mcp = FastMCP("time")
# Add an addition tool
@mcp.tool()
async def current_time():
    """Return the current UTC datetime."""
    return datetime.datetime.utcnow().isoformat() + "Z"
