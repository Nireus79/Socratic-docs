# Automatic Documentation Generation - Complete Technical Documentation

**Version:** 1.0
**Last Updated:** March 2026
**Scope:** socratic-docs - AI-Powered Documentation Generation System

---

## Table of Contents

1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Documentation Types](#documentation-types)
4. [Core Components](#core-components)
5. [Usage Guide](#usage-guide)
6. [Configuration](#configuration)
7. [Best Practices](#best-practices)
8. [Integration Guide](#integration-guide)
9. [API Reference](#api-reference)
10. [Examples](#examples)

---

## Overview

The **socratic-docs** module automatically generates comprehensive, high-quality documentation for software projects using AI analysis and best practices. It eliminates the manual burden of documentation maintenance while ensuring consistency and completeness.

### Key Capabilities

- **README Generation**: Professional project overviews with features, installation, usage
- **API Documentation**: Auto-generated API reference from code inspection
- **Architecture Documentation**: System design and component relationship documentation
- **Setup Guides**: Installation and configuration instructions
- **Automatic Updates**: Re-generate docs when codebase changes
- **Multi-Format Output**: Markdown, HTML, and other formats
- **Intelligent Content Generation**: Context-aware, technically accurate documentation

### Quick Start

```python
from socratic_docs.generation import DocumentationGenerator

# Initialize generator
generator = DocumentationGenerator(project_path="/path/to/project")

# Generate all documentation types
generator.generate_all()

# Or generate specific documentation
generator.generate_readme()
generator.generate_api_docs()
generator.generate_architecture_docs()
generator.generate_setup_guide()

# Check generated files
print(generator.get_documentation_map())
```

### Use Cases

1. **New Project Documentation**: Quickly document a new project
2. **Documentation Maintenance**: Keep docs in sync with code changes
3. **Multi-Project Documentation**: Generate docs for multiple projects consistently
4. **API Documentation**: Auto-generate comprehensive API references
5. **Onboarding Guides**: Create setup and configuration guides for new users
6. **Architecture Documentation**: Document system design and components

---

## Architecture

### System Components

```
Source Code Analysis
│
├── Code Inspector
│   ├── Parse modules and functions
│   ├── Extract docstrings
│   ├── Identify dependencies
│   └── Analyze structure
│
├── Documentation Generator
│   ├── README Generator
│   ├── API Documentation Generator
│   ├── Architecture Documentation Generator
│   └── Setup Guide Generator
│
└── Output Formatters
    ├── Markdown Formatter
    ├── HTML Formatter
    └── PDF Formatter
```

### Design Philosophy

1. **Intelligent Analysis**: Use AST and semantic analysis to understand code
2. **Template-Based**: Generate consistent documentation using templates
3. **AI-Enhanced**: Leverage AI to write clear, accurate documentation
4. **Modular Generation**: Generate different documentation types independently
5. **Configurable Output**: Customize generated docs per project

---

## Documentation Types

### 1. README Documentation

**Purpose**: Project overview for new users and contributors

**Generated Sections**:
- Project title and description
- Key features with feature highlights
- Installation instructions
- Quick start guide
- Configuration options
- API overview
- Examples
- Contributing guidelines
- License information

**Example Structure**:
```markdown
# Project Name

One-paragraph project description.

## Features

- Feature 1 with description
- Feature 2 with description
- Feature 3 with description

## Installation

```bash
pip install project-name
```

## Quick Start

```python
from project import Module
module = Module(config)
module.execute()
```

## Configuration

[Configuration options]

## Examples

[Code examples]

## Contributing

[Contribution guidelines]

## License

[License info]
```

### 2. API Documentation

**Purpose**: Detailed API reference for developers

**Generated Content**:
- Module overview
- Class definitions with attributes
- Method signatures with parameters
- Return type documentation
- Exception documentation
- Usage examples

**Example Structure**:
```markdown
# API Reference

## Module: core.calculator

### Class: Calculator

Performs mathematical calculations.

#### Methods

##### calculate(expression: str) -> float

Evaluate a mathematical expression.

**Parameters**:
- `expression` (str): Mathematical expression to evaluate

**Returns**: float - Result of the expression

**Raises**:
- `ValueError`: If expression is invalid

**Example**:
```python
calc = Calculator()
result = calc.calculate("2 + 2")
```
```

### 3. Architecture Documentation

**Purpose**: System design and component relationships

**Generated Content**:
- System architecture overview
- Component descriptions
- Module relationships
- Data flow diagrams
- Design patterns used
- Scalability considerations

**Example Structure**:
```markdown
# Architecture

## System Overview

[High-level system description]

## Components

### Component 1: Core Engine
[Description, responsibilities, interfaces]

### Component 2: Data Layer
[Description, responsibilities, interfaces]

## Data Flow

[Data flow through system]

## Design Patterns

- Pattern 1: Usage and benefits
- Pattern 2: Usage and benefits
```

### 4. Setup Guide

**Purpose**: Installation and configuration instructions

**Generated Content**:
- Prerequisites and requirements
- Installation steps (pip, source, Docker)
- Configuration instructions
- Verification steps
- Common issues and solutions
- Advanced setup options

**Example Structure**:
```markdown
# Setup Guide

## Prerequisites

- Python 3.8+
- PostgreSQL 12+
- Redis 6+

## Installation

### Using pip (Recommended)

```bash
pip install project
```

### From source

```bash
git clone https://github.com/project/repo
cd repo
pip install -e .
```

## Configuration

[Configuration steps]

## Verification

[How to verify installation]

## Troubleshooting

[Common issues and solutions]
```

---

## Core Components

### DocumentationGenerator

Main orchestrator for all documentation generation.

```python
class DocumentationGenerator:
    """Generate comprehensive project documentation."""

    def __init__(self, project_path: str, config: Optional[Dict] = None):
        """Initialize generator.

        Args:
            project_path: Root path to project
            config: Configuration options
        """

    def generate_all(self) -> Dict[str, str]:
        """Generate all documentation types."""

    def generate_readme(self) -> str:
        """Generate README.md"""

    def generate_api_docs(self) -> str:
        """Generate API documentation"""

    def generate_architecture_docs(self) -> str:
        """Generate architecture documentation"""

    def generate_setup_guide(self) -> str:
        """Generate setup guide"""

    def get_documentation_map(self) -> Dict[str, str]:
        """Get mapping of doc types to file paths"""
```

### CodeAnalyzer

Analyzes project structure and code.

```python
class CodeAnalyzer:
    """Analyze project code structure."""

    def get_project_structure(self) -> Dict:
        """Get project module structure"""

    def extract_module_docstrings(self) -> Dict[str, str]:
        """Extract docstrings from all modules"""

    def analyze_dependencies(self) -> List[str]:
        """Find project dependencies"""

    def get_class_definitions(self) -> Dict:
        """Extract class definitions and methods"""

    def identify_entry_points(self) -> List[str]:
        """Identify main entry points"""
```

### TemplateRenderer

Renders documentation from templates.

```python
class TemplateRenderer:
    """Render documentation from templates."""

    def render_readme(self, project_info: Dict) -> str:
        """Render README template"""

    def render_api_docs(self, api_info: Dict) -> str:
        """Render API documentation template"""

    def render_architecture(self, arch_info: Dict) -> str:
        """Render architecture documentation template"""

    def render_setup_guide(self, setup_info: Dict) -> str:
        """Render setup guide template"""
```

---

## Usage Guide

### Basic Generation

```python
from socratic_docs.generation import DocumentationGenerator

# Initialize with project path
generator = DocumentationGenerator(project_path="/path/to/my/project")

# Generate all documentation
docs = generator.generate_all()

# Files are written to project/docs/ automatically
```

### Selective Generation

```python
# Generate only specific documentation
generator.generate_readme()  # Writes to project/README.md
generator.generate_api_docs()  # Writes to project/docs/API.md
generator.generate_architecture_docs()  # Writes to project/docs/ARCHITECTURE.md
```

### Custom Configuration

```python
# Configure generation behavior
config = {
    "include_examples": True,
    "include_diagrams": True,
    "max_doc_length": 5000,  # Maximum tokens per doc section
    "language": "en",
    "style": "technical",
}

generator = DocumentationGenerator(
    project_path="/path/to/project",
    config=config
)

docs = generator.generate_all()
```

### Watching for Changes

```python
from socratic_docs.generation import DocumentationWatcher

# Auto-regenerate docs when code changes
watcher = DocumentationWatcher(project_path="/path/to/project")
watcher.start()  # Blocks until stopped

# Or watch in background
watcher.start_watching()
# ... continue other work ...
watcher.stop_watching()
```

---

## Configuration

### Generator Configuration

```python
config = {
    # Content generation
    "include_examples": True,           # Include code examples
    "include_diagrams": True,           # Include architecture diagrams
    "include_api_reference": True,      # Include API docs
    "max_doc_length": 5000,             # Max tokens per section

    # Output format
    "output_format": "markdown",        # markdown, html, or both
    "style_guide": "google",            # google, numpy, or sphinx

    # Language and tone
    "language": "en",                   # English, etc.
    "tone": "technical",                # technical or user-friendly
    "technical_level": "intermediate",  # beginner, intermediate, advanced

    # Features
    "include_changelog": False,         # Include CHANGELOG
    "include_contributing": True,       # Include CONTRIBUTING guide
    "include_troubleshooting": True,    # Include troubleshooting section

    # AI settings
    "model": "claude-3",                # Model to use for generation
    "temperature": 0.7,                 # Generation temperature
    "include_ai_warnings": False,       # Warn docs are AI-generated
}
```

### Template Customization

```python
from socratic_docs.generation import DocumentationGenerator

# Use custom templates
custom_templates = {
    "readme": "path/to/custom_readme_template.md",
    "api": "path/to/custom_api_template.md",
    "architecture": "path/to/custom_arch_template.md",
}

generator = DocumentationGenerator(
    project_path="/path/to/project",
    config={"custom_templates": custom_templates}
)
```

---

## Best Practices

### 1. Generate Regularly

```python
# Regenerate docs when code changes
def on_code_changed():
    generator = DocumentationGenerator(project_path)
    generator.generate_all()
    print("Documentation updated")

# Run in CI/CD pipeline
# Generate docs on every commit
```

### 2. Review and Customize

```python
# Review generated documentation
generated_docs = generator.generate_all()

# Make manual improvements
# Example: Add project-specific sections
# Add real-world examples
# Include domain-specific terminology
```

### 3. Include Code Examples

```python
# Generated docs include code examples
# Ensure examples in docstrings are accurate
# Examples should be copy-paste ready

def calculate_score(items, weights):
    """Calculate weighted score.

    Args:
        items: List of item values
        weights: Corresponding weights

    Returns:
        float: Weighted score

    Example:
        >>> items = [10, 20, 30]
        >>> weights = [0.2, 0.3, 0.5]
        >>> calculate_score(items, weights)
        23.0
    """
```

### 4. Maintain Docstrings

```python
# Good: Comprehensive docstrings
def process_data(input_path, output_path, format="json"):
    """Process input data and write results.

    Reads input file, applies transformations, and writes output.
    Supports multiple formats and compression.

    Args:
        input_path (str): Path to input file
        output_path (str): Path to write output
        format (str): Output format (json, csv, parquet)

    Returns:
        bool: True if successful

    Raises:
        FileNotFoundError: If input file not found
        ValueError: If format is unsupported

    Example:
        >>> process_data("input.csv", "output.json")
        True
    """
```

### 5. Keep Documentation DRY

```python
# Avoid duplication between docstrings and docs
# Let generator extract from canonical docstrings
# Update docstrings first, regenerate docs

# Update docstring once
def my_function():
    """Updated description."""
    pass

# Re-generate all docs
generator.generate_all()
```

---

## Integration Guide

### With Socratic Projects

```python
from socratic_docs.generation import DocumentationGenerator

# Generate docs for Socratic project
generator = DocumentationGenerator(
    project_path="/path/to/Socrates",
    config={
        "include_ai_features": True,
        "include_agent_descriptions": True,
    }
)

# Generate comprehensive documentation
docs = generator.generate_all()
print(f"Generated {len(docs)} documentation files")
```

### With CI/CD Pipeline

```yaml
# .github/workflows/generate-docs.yml
name: Generate Documentation

on:
  push:
    branches: [main]
    paths:
      - 'src/**'
      - 'docs/**'

jobs:
  generate-docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
      - name: Install dependencies
        run: pip install socratic-docs
      - name: Generate documentation
        run: |
          python -c "
          from socratic_docs.generation import DocumentationGenerator
          gen = DocumentationGenerator('.')
          gen.generate_all()
          "
      - name: Commit changes
        run: |
          git add docs/
          git commit -m 'docs: auto-generated documentation'
          git push
```

### With Documentation Websites

```python
# Generate docs for ReadTheDocs or similar
from socratic_docs.generation import DocumentationGenerator

generator = DocumentationGenerator(project_path=".")

# Generate in docs/ for ReadTheDocs
docs = generator.generate_all()

# Output structure:
# docs/
#   README.md (copied from root)
#   API.md
#   ARCHITECTURE.md
#   SETUP.md
```

---

## API Reference

### DocumentationGenerator

```python
class DocumentationGenerator:
    """Generate comprehensive project documentation."""

    def __init__(
        self,
        project_path: str,
        config: Optional[Dict] = None
    ):
        """Initialize generator."""

    def generate_all(self) -> Dict[str, str]:
        """Generate all documentation types.

        Returns:
            Dict mapping doc types to file paths
        """

    def generate_readme(self) -> str:
        """Generate README documentation."""

    def generate_api_docs(self) -> str:
        """Generate API reference."""

    def generate_architecture_docs(self) -> str:
        """Generate architecture documentation."""

    def generate_setup_guide(self) -> str:
        """Generate setup and installation guide."""

    def get_documentation_map(self) -> Dict[str, str]:
        """Get all generated documentation file paths."""
```

### DocumentationWatcher

```python
class DocumentationWatcher:
    """Watch for code changes and regenerate docs."""

    def __init__(self, project_path: str):
        """Initialize watcher."""

    def start(self):
        """Start watching (blocks until stopped)."""

    def start_watching(self):
        """Start watching in background thread."""

    def stop_watching(self):
        """Stop background watching."""
```

---

## Examples

### Example 1: Generate Docs for New Project

```python
from socratic_docs.generation import DocumentationGenerator

# New project
generator = DocumentationGenerator(project_path="/path/to/new_project")

# Generate all docs at once
docs = generator.generate_all()

# Result:
# /path/to/new_project/
#   README.md (generated)
#   docs/
#     API.md (generated)
#     ARCHITECTURE.md (generated)
#     SETUP.md (generated)
```

### Example 2: Custom Configuration

```python
# Configure for specific project type
config = {
    "include_examples": True,
    "include_diagrams": True,
    "style_guide": "google",
    "tone": "user-friendly",
    "include_troubleshooting": True,
}

generator = DocumentationGenerator(
    project_path="/path/to/project",
    config=config
)

docs = generator.generate_all()
```

### Example 3: Watching for Changes

```python
from socratic_docs.generation import DocumentationWatcher
import threading

# Watch in background
watcher = DocumentationWatcher(project_path="/path/to/project")
watcher.start_watching()

# Do other work
# Docs auto-regenerate when code changes

# Later, stop watching
watcher.stop_watching()
```

### Example 4: Integration with Development Workflow

```python
from socratic_docs.generation import DocumentationGenerator
import subprocess

def update_documentation():
    """Update project documentation."""
    generator = DocumentationGenerator(".")
    docs = generator.generate_all()

    # Commit generated docs
    subprocess.run(["git", "add", "docs/", "README.md"])
    subprocess.run(["git", "commit", "-m", "docs: auto-generated"])

    print("Documentation updated and committed")

# Call on every release
if __name__ == "__main__":
    update_documentation()
```

---

## Summary

The **socratic-docs** module provides:

- **Automatic README generation**: Professional project overviews
- **API documentation**: Auto-generated API references
- **Architecture documentation**: System design documentation
- **Setup guides**: Installation and configuration instructions
- **Intelligent generation**: Context-aware, technically accurate
- **Observable output**: Review and customize generated docs
- **Continuous updates**: Keep docs in sync with code

Enable it to eliminate documentation maintenance burden while maintaining comprehensive, professional documentation.
