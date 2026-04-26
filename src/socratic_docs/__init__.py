from __future__ import annotations

"""
Socratic Docs - Documentation and Parsing

Extracted from Socrates v1.3.3
"""

from .artifact_saver import ArtifactSaver
from .code_extractor import CodeExtractor
from .documentation_generator import DocumentationGenerator
from .git_initializer import GitInitializer
from .git_repository_manager import GitRepositoryManager
from .multi_file_splitter import MultiFileCodeSplitter
from .project_templates import ProjectTemplate

__version__ = "0.2.0"
__all__ = [
    "ArtifactSaver",
    "CodeExtractor",
    "DocumentationGenerator",
    "GitInitializer",
    "GitRepositoryManager",
    "MultiFileCodeSplitter",
    "ProjectTemplate",
]
