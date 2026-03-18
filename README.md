# Socratic Docs

Automated documentation generation for projects.

## Features

- **DocumentationGenerator**: Auto-generate project documentation
  - Comprehensive README.md
  - API reference documentation
  - Architecture documentation
  - Setup/installation guides

## Installation

```bash
pip install socratic-docs
```

## Usage

```python
from socratic_docs import DocumentationGenerator

generator = DocumentationGenerator()

project = {
    "name": "My Project",
    "description": "A great project",
    "features": ["Feature 1", "Feature 2"],
    "repo_url": "https://github.com/user/project"
}

code_structure = {
    "classes": ["ClassA", "ClassB"],
    "functions": ["func1", "func2"],
    "modules": ["module1", "module2"]
}

docs = generator.generate_all(project, code_structure)
# Returns dict with README.md, API.md, ARCHITECTURE.md, SETUP.md
```

## Documentation

- **[Documentation Generation Guide](docs/DOCUMENTATION_GENERATION.md)** - Complete guide to automatic documentation generation, including README generation, API documentation, architecture documentation, and setup guides

## License

MIT
