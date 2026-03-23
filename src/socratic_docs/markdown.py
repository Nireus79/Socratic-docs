"""
Markdown document builder utilities.
"""


class MarkdownBuilder:
    """Helper class for building markdown documents."""

    @staticmethod
    def heading(text: str, level: int = 1) -> str:
        """Create a markdown heading."""
        return f"{'#' * level} {text}\n\n"

    @staticmethod
    def paragraph(text: str) -> str:
        """Create a paragraph."""
        return f"{text}\n\n"

    @staticmethod
    def bold(text: str) -> str:
        """Make text bold."""
        return f"**{text}**"

    @staticmethod
    def italic(text: str) -> str:
        """Make text italic."""
        return f"*{text}*"

    @staticmethod
    def code_inline(text: str) -> str:
        """Create inline code."""
        return f"`{text}`"

    @staticmethod
    def code_block(code: str, language: str = "") -> str:
        """Create a code block."""
        return f"```{language}\n{code}\n```\n\n"

    @staticmethod
    def bullet_list(items: list) -> str:
        """Create a bullet list."""
        return "".join(f"- {item}\n" for item in items) + "\n"

    @staticmethod
    def numbered_list(items: list) -> str:
        """Create a numbered list."""
        return "".join(f"{i+1}. {item}\n" for i, item in enumerate(items)) + "\n"

    @staticmethod
    def link(text: str, url: str) -> str:
        """Create a link."""
        return f"[{text}]({url})"

    @staticmethod
    def image(alt: str, url: str) -> str:
        """Create an image."""
        return f"![{alt}]({url})"

    @staticmethod
    def line_break() -> str:
        """Create a line break."""
        return "\n"

    @staticmethod
    def horizontal_rule() -> str:
        """Create a horizontal rule."""
        return "---\n\n"

    @staticmethod
    def table(headers: list, rows: list) -> str:
        """Create a markdown table."""
        doc = "| " + " | ".join(headers) + " |\n"
        doc += "| " + " | ".join(["---"] * len(headers)) + " |\n"
        for row in rows:
            doc += "| " + " | ".join(str(cell) for cell in row) + " |\n"
        return doc + "\n"

    @staticmethod
    def blockquote(text: str) -> str:
        """Create a blockquote."""
        return f"> {text}\n\n"
