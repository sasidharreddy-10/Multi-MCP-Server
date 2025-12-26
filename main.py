from fastmcp import FastMCP
from servers import add_mcp
from servers import multiply_mcp
from servers import time_mcp
from servers import url_mcp

app = FastMCP(name="root")

app.mount(add_mcp)
app.mount(multiply_mcp)
app.mount(time_mcp)
app.mount(url_mcp)

if __name__ == "__main__":
    app.run(transport='streamable-http')
