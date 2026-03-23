"""
Socratic Docs - Documentation generation from code structure

Generates comprehensive documentation from code structure and metadata.
"""

__version__ = "0.1.0"

from .generator import DocumentationGenerator
from .markdown import MarkdownBuilder

__all__ = [
    "DocumentationGenerator",
    "MarkdownBuilder",
]
