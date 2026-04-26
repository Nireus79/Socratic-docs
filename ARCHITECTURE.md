# socratic-docs Architecture

Documentation generation and code management library.

## System Overview

socratic-docs provides a modular pipeline for extracting code information, generating documentation, managing project structure, and integrating with version control.

## Pipeline Architecture

```
Source Code
    |
    v
CodeExtractor
    |
    +---> Analyze modules, classes, functions
    |
    v
DocumentationGenerator
    |
    +---> Generate README.md, API docs, Architecture
    |
    v
MultiFileCodeSplitter / ProjectTemplateGenerator
    |
    +---> Organize code structure or create templates
    |
    v
ArtifactSaver
    |
    +---> Save files to disk
    |
    v
GitRepositoryManager / GitInitializer
    |
    +---> Track changes in version control
    |
    v
Documentation Output
```

## Core Components

### 1. CodeExtractor
Analyzes Python source code and extracts structural information.

**Responsibilities**:
- Parse Python modules and packages
- Extract class definitions and methods
- Extract function signatures
- Extract docstrings and comments
- Generate code inventory
- Support for nested packages

**Output**:
```python
{
    "modules": [{
        "name": "module_name",
        "docstring": "...",
        "classes": [{
            "name": "ClassName",
            "methods": [...],
            "docstring": "..."
        }],
        "functions": [...]
    }]
}
```

### 2. DocumentationGenerator
Creates comprehensive documentation from code information.

**Responsibilities**:
- Generate README.md files
- Create API reference documentation
- Generate architecture documentation
- Produce setup and installation guides
- Format docstrings into markdown
- Create index files

**Output Formats**:
- README.md - Project overview and quick start
- API.md - Complete API reference
- ARCHITECTURE.md - System design and components
- SETUP.md - Installation and configuration

### 3. MultiFileCodeSplitter
Organizes monolithic code into modular structure.

**Responsibilities**:
- Split large files into smaller modules
- Organize code by functionality
- Create package structure
- Generate __init__.py files
- Preserve code relationships
- Create organization index

**Supported Strategies**:
- Split by module/package
- Split by class/function
- Split by feature domain
- Custom splitting logic

### 4. ProjectTemplateGenerator
Creates standardized project scaffolding.

**Responsibilities**:
- Generate project directory structure
- Create boilerplate files
- Add configuration files (pyproject.toml, setup.py)
- Create .gitignore files
- Generate README templates
- Support multiple project types

**Supported Templates**:
- Python Library
- CLI Tool
- Web Application
- Data Science Project
- Plugin/Extension

### 5. ArtifactSaver
Persists documentation and code artifacts to disk.

**Responsibilities**:
- Write files to specified directories
- Organize files by category
- Support multiple formats
- Create directory structure
- Generate index files
- Handle file naming conventions

**Supported Formats**:
- Markdown (.md)
- Python (.py)
- Text (.txt)
- JSON (.json)
- YAML (.yml)

### 6. GitRepositoryManager
Manages version control integration.

**Responsibilities**:
- Initialize git repositories
- Stage and commit changes
- Push to remote repositories
- Track documentation changes
- Generate commit messages
- Manage branch operations

**Operations**:
- git init
- git add / git commit
- git push / git pull
- Branch management
- Remote configuration

### 7. GitInitializer
Sets up git repositories for new projects.

**Responsibilities**:
- Initialize repository
- Create initial commit
- Configure git settings
- Generate .gitignore
- Setup remote URLs
- Create default branches

**Capabilities**:
- Repository initialization
- User configuration
- SSH/HTTPS setup
- License and README creation
- Initial project structure

## Data Flow

### Extract and Generate Workflow

```
1. Source Code
        |
        v
2. CodeExtractor.extract_from_package()
        |
        +---> Classes, functions, docstrings
        |
        v
3. Code Information (structured data)
        |
        v
4. DocumentationGenerator.generate_all()
        |
        +---> README.md, API.md, ARCHITECTURE.md
        |
        v
5. Documentation Dictionary
        |
        v
6. ArtifactSaver.save_documents()
        |
        +---> Write to disk
        |
        v
7. Files in output_dir/
```

### Git Integration Workflow

```
1. Documentation Generated
        |
        v
2. ArtifactSaver saves to disk
        |
        v
3. GitRepositoryManager initialized
        |
        +---> Points to project repo
        |
        v
4. add_files() stages changes
        |
        v
5. commit() creates git commit
        |
        v
6. (Optional) push() to remote
```

### Project Scaffolding Workflow

```
1. ProjectTemplateGenerator.generate_template()
        |
        +---> Input: project name, type, author
        |
        v
2. Create directory structure
        |
        v
3. Generate boilerplate files
        |
        +---> pyproject.toml
        +---> setup.py (if needed)
        +---> LICENSE
        +---> .gitignore
        |
        v
4. Create package directory
        |
        v
5. Initialize git (optional)
        |
        v
6. Output: Ready-to-use project
```

## Integration Points

### With socratic-nexus
- Use LLM to improve documentation quality
- Generate better API descriptions
- Create more comprehensive guides

### With socratic-analyzer
- Analyze code structure before extraction
- Identify documentation gaps
- Evaluate documentation completeness

### With socratic-workflow
- Integrate documentation generation into workflows
- Schedule periodic documentation updates
- Trigger documentation on code changes

### With socratic-learning
- Track documentation improvements
- Learn from documentation patterns
- Improve generation quality over time

## Extension Points

### Custom Extractors
```python
class CustomExtractor(CodeExtractor):
    def extract_custom_info(self, source):
        # Custom extraction logic
        pass
```

### Custom Generators
```python
class CustomGenerator(DocumentationGenerator):
    def generate_custom_format(self, code_info):
        # Custom documentation generation
        pass
```

### Custom Templates
```python
templates = {
    "my_type": {
        "structure": {...},
        "files": {...}
    }
}
```

## Performance Characteristics

- **Extraction**: O(n) where n = number of source files
- **Generation**: O(m) where m = extracted elements
- **Saving**: O(d) where d = number of documents
- **Memory**: Depends on source code size

## Error Handling

- Input validation for all extractors
- Graceful handling of parsing errors
- Fallback for missing documentation
- Clear error messages for failures

---

Part of the Socratic Ecosystem | Modular Documentation Pipeline
