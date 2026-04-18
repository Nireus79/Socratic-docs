"""Documentation Module - Auto-generate project documentation"""

from socratic_docs.api_documentation import APIDocumentationGenerator, SphinxIntegration
from socratic_docs.generation.documentation_generator import DocumentationGenerator

__all__ = [
    "DocumentationGenerator",
    "APIDocumentationGenerator",
    "SphinxIntegration",
]
