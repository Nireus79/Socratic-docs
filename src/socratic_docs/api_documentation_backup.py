\"\"\"
API documentation generation and Sphinx integration.

This module provides tools for generating API documentation from various sources
including OpenAPI specifications and endpoint definitions, as well as integrating
with Sphinx for comprehensive documentation generation.
\"\"\"

import logging
import json
import os
from typing import Any, Dict, List, Optional
from dataclasses import dataclass

from .markdown import MarkdownBuilder

logger = logging.getLogger(__name__)


@dataclass
class APIEndpoint:
    \"\"\"Represents an API endpoint.

    Attributes:
        name: Endpoint name or identifier
        method: HTTP method (GET, POST, PUT, DELETE, etc.)
        path: URL path for the endpoint
        description: Human-readable endpoint description
        parameters: List of parameter definitions (name, type, description)
        returns: Return value definition (type and description)
        examples: List of usage examples
        tags: Categorization tags for the endpoint
    \"\"\"
    name: str
    method: str
    path: str
    description: str
    parameters: List[Dict[str, str]]
    returns: Dict[str, str]
    examples: List[str]
    tags: List[str]
