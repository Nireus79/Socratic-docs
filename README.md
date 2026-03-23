# Socratic Docs

Documentation generation from code structure and metadata for the Socratic AI platform.

## Features

- **Automated Generation**: Generate docs from code structure
- **Multiple Formats**: README, API docs, architecture guides, setup guides
- **Markdown Builder**: Utilities for building markdown documents
- **Flexible Input**: Works with custom code structure metadata
- **Batch Generation**: Generate multiple documentation files at once

## Installation

```bash
pip install socratic-docs
```

## Quick Start

```python
from socratic_docs import DocumentationGenerator

generator = DocumentationGenerator()

# Generate README
readme = generator.generate_comprehensive_readme(
    project_name="My Project",
    description="A great project",
    features=["Feature 1", "Feature 2"],
)

# Generate API documentation
api_docs = generator.generate_api_documentation({
    "classes": [
        {"name": "MyClass", "methods": ["method1", "method2"]}
    ]
})

# Generate all documentation
docs = generator.generate_all(
    project={"name": "My Project"},
    code_structure={"modules": ["module1", "module2"]}
)
```

## Components

### DocumentationGenerator

Main generator class for creating documentation.

### MarkdownBuilder

Utilities for building markdown documents.

```python
from socratic_docs import MarkdownBuilder

builder = MarkdownBuilder()
text = builder.heading("Title", 1)
text += builder.paragraph("Description")
text += builder.code_block("code", "python")
```

## License

MIT
