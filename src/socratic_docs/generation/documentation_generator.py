"""Documentation Generator - Auto-generate project documentation."""

import logging
from typing import Dict, List

logger = logging.getLogger(__name__)


class DocumentationGenerator:
    """Generate comprehensive project documentation"""

    def __init__(self):
        logger.debug("DocumentationGenerator initialized")

    def generate_comprehensive_readme(self, project: Dict) -> str:
        """Generate comprehensive README"""
        name = project.get("name", "Project")
        description = project.get("description", "")
        features = project.get("features", [])

        readme = f"# {name}\n\n"
        if description:
            readme += f"{description}\n\n"

        if features:
            readme += "## Features\n\n"
            for feature in features:
                readme += f"- {feature}\n"
            readme += "\n"

        readme += "## Installation\n\n```bash\npip install {}\n```\n\n".format(
            name.lower().replace(" ", "-")
        )
        readme += "## Usage\n\nSee documentation for detailed usage.\n"

        return readme

    def generate_api_documentation(self, code_structure: Dict) -> str:
        """Generate API documentation"""
        doc = "# API Reference\n\n"

        classes = code_structure.get("classes", [])
        for cls in classes:
            doc += f"## {cls}\n\n"
            doc += f"Class: `{cls}`\n\n"

        functions = code_structure.get("functions", [])
        if functions:
            doc += "## Functions\n\n"
            for func in functions:
                doc += f"- `{func}()`\n"

        return doc

    def generate_architecture_docs(self, modules: List[str]) -> str:
        """Generate architecture documentation"""
        doc = "# Architecture\n\n"
        doc += "## Modules\n\n"

        for module in modules:
            doc += f"### {module}\n\n"

        return doc

    def generate_setup_guide(self, project: Dict) -> str:
        """Generate setup/installation guide"""
        guide = "# Setup Guide\n\n"
        guide += "## Requirements\n\n"
        guide += "- Python 3.8+\n\n"
        guide += "## Installation\n\n"
        clone_url = project.get('repo_url', 'https://github.com/your-org/your-project')
        guide += "```bash\n"
        guide += f"git clone {clone_url}\n"
        guide += "cd project\n"
        guide += "pip install -e .\n"
        guide += "```\n\n"
        guide += "## Configuration\n\nSee config files for details.\n"

        return guide

    def generate_all(self, project: Dict, code_structure: Dict) -> Dict[str, str]:
        """Generate all documentation"""
        return {
            "README.md": self.generate_comprehensive_readme(project),
            "API.md": self.generate_api_documentation(code_structure),
            "ARCHITECTURE.md": self.generate_architecture_docs(code_structure.get("modules", [])),
            "SETUP.md": self.generate_setup_guide(project),
        }
