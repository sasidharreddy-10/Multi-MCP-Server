from .add.server import mcp as add_mcp
from .multiply.server import mcp as multiply_mcp
from .time.server import mcp as time_mcp
from .fetch_url.server import mcp as url_mcp

__all__ = ['add_mcp', 'multiply_mcp', 'time_mcp', 'url_mcp']