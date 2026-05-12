# Production Deployment - Socratic Docs

Automated documentation generation and management.

## Production Checklist

- [x] Automated code extraction and parsing
- [x] Documentation generation from source
- [x] Git integration for version tracking
- [x] Multi-format output (Markdown, HTML, PDF)
- [x] Project structure management
- [x] CI/CD integration support

## Setup

```python
from socratic_docs import DocumentationGenerator

gen = DocumentationGenerator(
    project_path='/path/to/project',
    output_format='markdown',
)

# Generate comprehensive documentation
gen.generate_all()

# Outputs to ./docs/
```

## Git Integration

```python
# Track documentation in git
gen.commit_changes(
    message="docs: auto-generated from code",
    author="Documentation Bot",
)

# Keep docs in sync with code
```

## CI/CD Integration

```yaml
# In GitHub Actions
- name: Generate Documentation
  run: |
    pip install socratic-docs
    socratic-docs generate
    git add docs/
    git commit -m "docs: auto-generated"
    git push
```

