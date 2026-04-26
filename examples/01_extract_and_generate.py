"""
Example 1: Extract Code and Generate Documentation

Demonstrates extracting code information and generating comprehensive
documentation from a Python package.
"""

from socratic_docs import CodeExtractor, DocumentationGenerator, ArtifactSaver


def extract_and_generate_example():
    """
    Complete workflow: Extract -> Generate -> Save
    """
    print("=" * 70)
    print("EXTRACT AND GENERATE DOCUMENTATION")
    print("=" * 70)
    print()

    # Step 1: Extract code information
    print("Step 1: Extracting code information...")
    print("-" * 70)

    extractor = CodeExtractor()

    # Would extract from actual package in real usage
    code_info = {
        "modules": [
            {
                "name": "core",
                "docstring": "Core functionality module",
                "classes": [
                    {
                        "name": "Calculator",
                        "docstring": "Simple calculator class",
                        "methods": [
                            {
                                "name": "add",
                                "docstring": "Add two numbers",
                                "signature": "add(a: float, b: float) -> float"
                            }
                        ]
                    }
                ]
            }
        ]
    }

    print(f"Extracted modules: {len(code_info['modules'])}")
    for module in code_info['modules']:
        print(f"  - {module['name']}")
    print()

    # Step 2: Generate documentation
    print("Step 2: Generating documentation...")
    print("-" * 70)

    generator = DocumentationGenerator()
    docs = generator.generate_all(code_info)

    print(f"Generated documents:")
    for doc_name in sorted(docs.keys()):
        print(f"  - {doc_name}")
    print()

    # Step 3: Save artifacts
    print("Step 3: Saving documentation artifacts...")
    print("-" * 70)

    saver = ArtifactSaver(output_dir="./docs_example")
    saver.save_documents(docs)
    saver.create_index()

    print("Files saved to: ./docs_example/")
    print("[OK] Documentation generation complete!")


if __name__ == "__main__":
    extract_and_generate_example()
