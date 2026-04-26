"""
Example 3: Git Workflow Integration

Demonstrates using GitRepositoryManager and GitInitializer for version
control integration with documentation generation.
"""

from socratic_docs import (
    GitInitializer,
    GitRepositoryManager,
    CodeExtractor,
    DocumentationGenerator,
    ArtifactSaver
)


def git_workflow_example():
    """
    Complete workflow: Initialize -> Extract -> Generate -> Commit
    """
    print("=" * 70)
    print("GIT WORKFLOW INTEGRATION")
    print("=" * 70)
    print()

    # Step 1: Initialize git repository
    print("Step 1: Initialize git repository...")
    print("-" * 70)

    git_init = GitInitializer(repo_path="./my_project")

    print("Initializing repository: ./my_project")
    print("  - Creating .git directory")
    print("  - Creating .gitignore")
    print("  - Setting up git config")
    print()

    # Step 2: Extract and generate
    print("Step 2: Extract code and generate documentation...")
    print("-" * 70)

    extractor = CodeExtractor()
    code_info = extractor.extract_from_package("src.my_module")

    generator = DocumentationGenerator()
    docs = generator.generate_all(code_info)

    print(f"Generated documentation files")
    for doc_name in sorted(docs.keys()):
        print(f"  - {doc_name}")
    print()

    # Step 3: Save documentation
    print("Step 3: Save documentation artifacts...")
    print("-" * 70)

    saver = ArtifactSaver(output_dir="./my_project/docs")
    saver.save_documents(docs)

    print("Saved to: ./my_project/docs/")
    print()

    # Step 4: Commit to git
    print("Step 4: Commit to git repository...")
    print("-" * 70)

    git_mgr = GitRepositoryManager(repo_path="./my_project")

    print("Adding files...")
    git_mgr.add_files("docs/")

    print("Creating commit...")
    git_mgr.commit(
        message="docs: Add auto-generated documentation",
        description="Generated from source code extraction and analysis"
    )

    print("Commit created successfully")
    print()

    print("[OK] Git workflow complete!")


if __name__ == "__main__":
    git_workflow_example()
