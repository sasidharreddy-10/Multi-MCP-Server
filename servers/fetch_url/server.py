from fastmcp import FastMCP
# Create an MCP server
mcp = FastMCP("Demo")
# Add an addition tool
@mcp.tool
async def fetch_url(url: str) -> dict:
    """
    Fetch a URL (async) and return a small result summary.
    Note: keep external calls small & safe in production servers.
    """
    async with httpx.AsyncClient() as client:
        r = await client.get(url, timeout=10.0)
        snippet = (r.text or "")[:300]
        return {"status_code": r.status_code, "snippet": snippet}
