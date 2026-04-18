"""Documentation Module - Auto-generate project documentation"""

from socratic_docs.generation.documentation_generator import DocumentationGenerator
from socratic_docs.api_documentation import APIDocumentationGenerator, SphinxIntegration

__all__ = [
    "DocumentationGenerator",
    "APIDocumentationGenerator",
    "SphinxIntegration",
]
