# Socratic Docs

Automated documentation generation, code extraction, and project management for Python projects.

## Overview

Socratic Docs provides a comprehensive toolkit for generating, managing, and organizing project documentation. It automates the tedious process of creating documentation artifacts and managing project structure through git integration.

## Features

### Core Modules

1. **CodeExtractor** - Extract and analyze source code
   - Parse Python modules and classes
   - Extract function signatures and docstrings
   - Generate code inventories
   - Support for package analysis

2. **DocumentationGenerator** - Generate comprehensive documentation
   - Auto-generate README.md with project overview
   - Create API reference documentation
   - Generate architecture documentation
   - Produce setup and installation guides

3. **MultiFileCodeSplitter** - Split large codebases into organized files
   - Organize code by module/package
   - Generate file structure
   - Support for custom naming conventions
   - Preserve code relationships

4. **ProjectTemplateGenerator** - Create project scaffolding
   - Generate boilerplate project structures
   - Create standardized layouts
   - Support multiple project types
   - Include configuration files

5. **ArtifactSaver** - Save documentation and artifacts
   - Write files to disk
   - Organize by directory
   - Support multiple formats (markdown, text, code)
   - Create index files

6. **GitRepositoryManager** - Manage git repositories
   - Initialize repositories
   - Add and commit files
   - Track documentation changes
   - Integrate with version control

7. **GitInitializer** - Setup git for projects
   - Initialize new repositories
   - Configure git settings
   - Create initial commits
   - Setup .gitignore files

## Installation

### Basic Installation

```bash
pip install socratic-docs
```

### With Optional Dependencies

```bash
# With git integration
pip install socratic-docs[all]
```

## Quick Start

### Example 1: Extract Code and Generate Documentation

```python
from socratic_docs import CodeExtractor, DocumentationGenerator, ArtifactSaver

# Step 1: Extract code information
extractor = CodeExtractor()
code_info = extractor.extract_from_package("my_package")

# Step 2: Generate documentation
generator = DocumentationGenerator()
docs = generator.generate_all(code_info)
# docs contains README.md, API.md, ARCHITECTURE.md, SETUP.md

# Step 3: Save artifacts
saver = ArtifactSaver(output_dir="./docs_output")
saver.save_documents(docs)
saver.create_index()
```

### Example 2: Generate Project Template

```python
from socratic_docs import ProjectTemplateGenerator

generator = ProjectTemplateGenerator()

template = generator.generate_template(
    project_name="my_awesome_project",
    project_type="library",
    description="An awesome Python library",
    author="Your Name"
)
```

### Example 3: Git Integration Workflow

```python
from socratic_docs import (
    GitInitializer,
    CodeExtractor,
    DocumentationGenerator,
    GitRepositoryManager,
    ArtifactSaver
)

# Initialize a new git repository
git_init = GitInitializer(repo_path="./my_project")
git_init.initialize()

# Extract code and generate docs
extractor = CodeExtractor()
code_info = extractor.extract_from_package("my_package")

generator = DocumentationGenerator()
docs = generator.generate_all(code_info)

# Save and commit
saver = ArtifactSaver(output_dir="./my_project/docs")
saver.save_documents(docs)

git_mgr = GitRepositoryManager(repo_path="./my_project")
git_mgr.add_files("docs/")
git_mgr.commit("docs: Add auto-generated documentation")
```

### Example 4: Split Large Codebase

```python
from socratic_docs import MultiFileCodeSplitter

splitter = MultiFileCodeSplitter()

result = splitter.split_by_module(
    input_file="monolithic_app.py",
    output_dir="./modular_structure"
)
```

## Use Cases

### Documentation for Open Source Projects
- Auto-generate comprehensive README and API docs
- Keep documentation in sync with code
- Generate changelog and architecture guides
- Create installation and setup guides

### Internal Documentation
- Document enterprise applications
- Generate code inventories
- Create architecture diagrams
- Track project structure changes

### Project Scaffolding
- Quickly bootstrap new projects
- Ensure consistent project structure
- Auto-configure build tools
- Generate config files

### Documentation as Code
- Version control documentation with code
- Generate docs from code docstrings
- Automate documentation updates
- Integrate with CI/CD pipelines

## Integration with Socratic Ecosystem

- **socratic-nexus**: Use LLMs to improve documentation generation
- **socratic-analyzer**: Analyze code quality and document findings
- **socratic-workflow**: Integrate documentation generation into workflows
- **socratic-learning**: Track improvements in documentation quality

## Architecture

See [ARCHITECTURE.md](ARCHITECTURE.md) for detailed architecture documentation.

## API Reference

See [docs/API_REFERENCE.md](docs/API_REFERENCE.md) for complete API documentation.

## Examples

See the [examples/](examples/) directory for complete, runnable examples:

- `01_extract_and_generate.py` - Extract code and generate documentation
- `02_project_templates.py` - Generate project scaffolding
- `03_git_workflow.py` - Git-based documentation workflow

## Contributing

Contributions are welcome!

## License

MIT License - see LICENSE for details.

## Support

- Documentation: https://github.com/Nireus79/socratic-docs
- Issues: https://github.com/Nireus79/socratic-docs/issues
