"""
Example 2: Project Template Generation

Demonstrates using ProjectTemplateGenerator to scaffold new projects.
"""

from socratic_docs import ProjectTemplateGenerator


def template_generation_example():
    """
    Create a project scaffold with standardized structure.
    """
    print("=" * 70)
    print("PROJECT TEMPLATE GENERATION")
    print("=" * 70)
    print()

    generator = ProjectTemplateGenerator()

    # Generate a library project template
    print("Step 1: Generate library project template...")
    print("-" * 70)

    template = generator.generate_template(
        project_name="awesome_lib",
        project_type="library",
        description="An awesome Python library for data processing",
        author="Your Name",
        author_email="you@example.com"
    )

    print(f"Project: {template['project_name']}")
    print(f"Type: {template['project_type']}")
    print(f"Description: {template['description']}")
    print()

    # Show generated structure
    print("Step 2: Available project templates...")
    print("-" * 70)

    project_types = ["library", "cli", "web", "data_science"]
    for ptype in project_types:
        print(f"  - {ptype}")
    print()

    print("[OK] Template generation complete!")


if __name__ == "__main__":
    template_generation_example()
