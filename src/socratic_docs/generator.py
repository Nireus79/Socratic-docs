"""
Documentation generator from code structure.
"""

import logging
from typing import Any, Dict, List, Optional

from .markdown import MarkdownBuilder

logger = logging.getLogger(__name__)


class DocumentationGenerator:
    """
    Generate documentation from code structure.

    Creates comprehensive documentation including:
    - README files
    - API documentation
    - Architecture guides
    - Setup guides
    """

    def __init__(self) -> None:
        """Initialize the documentation generator."""
        self.builder = MarkdownBuilder()

    def generate_comprehensive_readme(
        self,
        project_name: str,
        description: str,
        features: Optional[List[str]] = None,
        installation: Optional[str] = None,
        usage: Optional[str] = None
    ) -> str:
        """
        Generate a comprehensive README.

        Args:
            project_name: Name of the project
            description: Project description
            features: List of features
            installation: Installation instructions
            usage: Usage examples

        Returns:
            Generated README markdown
        """
        doc = self.builder.heading(project_name, 1)
        doc += self.builder.paragraph(description)

        if features:
            doc += self.builder.heading("Features", 2)
            doc += self.builder.bullet_list(features)

        if installation:
            doc += self.builder.heading("Installation", 2)
            doc += self.builder.code_block(installation, "bash")

        if usage:
            doc += self.builder.heading("Usage", 2)
            doc += self.builder.code_block(usage, "python")

        logger.info(f"Generated README for {project_name}")
        return doc

    def generate_api_documentation(self, code_structure: Dict[str, Any]) -> str:
        """
        Generate API documentation from code structure.

        Args:
            code_structure: Code structure with classes and functions

        Returns:
            API documentation markdown
        """
        doc = self.builder.heading("API Documentation", 1)

        # Document classes
        if "classes" in code_structure:
            doc += self.builder.heading("Classes", 2)
            for cls in code_structure["classes"]:
                doc += self.builder.heading(cls.get("name", "Unknown"), 3)
                if "description" in cls:
                    doc += self.builder.paragraph(cls["description"])
                if "methods" in cls:
                    doc += self.builder.heading("Methods", 4)
                    for method in cls["methods"]:
                        doc += self.builder.code_inline(method)
                        doc += self.builder.line_break()

        # Document functions
        if "functions" in code_structure:
            doc += self.builder.heading("Functions", 2)
            for func in code_structure["functions"]:
                doc += self.builder.heading(func.get("name", "Unknown"), 3)
                if "description" in func:
                    doc += self.builder.paragraph(func["description"])
                if "params" in func:
                    doc += self.builder.heading("Parameters", 4)
                    doc += self.builder.bullet_list(func["params"])

        logger.info("Generated API documentation")
        return doc

    def generate_architecture_docs(self, modules: List[str]) -> str:
        """
        Generate architecture documentation.

        Args:
            modules: List of module names

        Returns:
            Architecture documentation markdown
        """
        doc = self.builder.heading("Architecture", 1)
        doc += self.builder.paragraph("System architecture overview")

        doc += self.builder.heading("Modules", 2)
        doc += self.builder.bullet_list(modules)

        doc += self.builder.heading("Module Interactions", 2)
        doc += self.builder.paragraph(
            "The modules interact through well-defined interfaces and APIs."
        )

        logger.info(f"Generated architecture documentation for {len(modules)} modules")
        return doc

    def generate_setup_guide(self, project: Dict[str, Any]) -> str:
        """
        Generate setup and installation guide.

        Args:
            project: Project metadata

        Returns:
            Setup guide markdown
        """
        doc = self.builder.heading("Setup Guide", 1)

        project_name = project.get("name", "Project")
        doc += self.builder.heading("Installation", 2)
        doc += self.builder.code_block(
            f"pip install {project_name.lower().replace(' ', '-')}",
            "bash"
        )

        doc += self.builder.heading("Configuration", 2)
        if "config" in project:
            doc += self.builder.paragraph("Configuration options:")
            doc += self.builder.bullet_list(project["config"])

        doc += self.builder.heading("Quick Start", 2)
        doc += self.builder.code_block(
            f"# Import the package\nfrom {project_name.lower().replace(' ', '_')} import main",
            "python"
        )

        logger.info(f"Generated setup guide for {project_name}")
        return doc

    def generate_all(
        self,
        project: Dict[str, Any],
        code_structure: Dict[str, Any]
    ) -> Dict[str, str]:
        """
        Generate all documentation at once.

        Args:
            project: Project metadata
            code_structure: Code structure

        Returns:
            Dictionary with all generated documentation
        """
        docs = {
            "README.md": self.generate_comprehensive_readme(
                project.get("name", "Project"),
                project.get("description", ""),
                project.get("features", []),
            ),
            "API.md": self.generate_api_documentation(code_structure),
            "ARCHITECTURE.md": self.generate_architecture_docs(
                code_structure.get("modules", [])
            ),
            "SETUP.md": self.generate_setup_guide(project),
        }

        logger.info("Generated complete documentation set")
        return docs
