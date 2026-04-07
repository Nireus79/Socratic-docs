"""Report generation for socratic-docs."""

import json
import logging
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


@dataclass
class Report:
    """Represents a generated report."""

    report_id: str
    title: str
    content: str
    format: str
    created_at: datetime
    updated_at: datetime
    metadata: Dict[str, Any]


class ReportGenerator:
    """Generate HTML and PDF reports."""

    def __init__(self, output_dir: str = "./reports"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.reports: Dict[str, Report] = {}

    async def generate_html_report(self, title: str, sections: List[Dict[str, Any]]) -> str:
        """Generate HTML report."""
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{title}</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                h1 {{ color: #333; }}
                section {{ margin-top: 20px; border-bottom: 1px solid #ddd; padding-bottom: 20px; }}
            </style>
        </head>
        <body>
            <h1>{title}</h1>
            <p>Generated: {datetime.now().isoformat()}</p>
        """

        for section in sections:
            html_content += f"<section><h2>{section.get('title', 'Untitled')}</h2>"
            html_content += f"<p>{section.get('content', '')}</p></section>"

        html_content += "</body></html>"

        report_id = f"html_{datetime.now().timestamp()}"
        filepath = self.output_dir / f"{report_id}.html"

        with open(filepath, "w") as f:
            f.write(html_content)

        report = Report(
            report_id=report_id,
            title=title,
            content=html_content,
            format="html",
            created_at=datetime.now(),
            updated_at=datetime.now(),
            metadata={"filepath": str(filepath)},
        )

        self.reports[report_id] = report
        logger.info(f"Generated HTML report {report_id}")
        return str(filepath)

    async def generate_api_documentation(
        self, api_name: str, endpoints: List[Dict[str, Any]]
    ) -> str:
        """Generate API documentation."""
        doc_content = f"# API Documentation: {api_name}\n\n"
        doc_content += f"Generated: {datetime.now().isoformat()}\n\n"

        for endpoint in endpoints:
            method = endpoint.get("method", "GET")
            path = endpoint.get("path", "/")
            doc_content += f"## {method} {path}\n"
            description = endpoint.get("description", "No description")
            doc_content += f"Description: {description}\n"

            if endpoint.get("parameters"):
                doc_content += "### Parameters\n"
                for param in endpoint["parameters"]:
                    name = param.get("name")
                    param_type = param.get("type", "string")
                    doc_content += f"- `{name}`: {param_type}\n"

            if endpoint.get("response"):
                doc_content += "### Response\n```json\n"
                doc_content += json.dumps(endpoint["response"], indent=2)
                doc_content += "\n```\n"

            doc_content += "\n"

        report_id = f"api_doc_{api_name}_{datetime.now().timestamp()}"
        filepath = self.output_dir / f"{report_id}.md"

        with open(filepath, "w") as f:
            f.write(doc_content)

        logger.info(f"Generated API documentation {report_id}")
        return str(filepath)

    async def generate_changelog(self, app_name: str, versions: List[Dict[str, Any]]) -> str:
        """Generate changelog from version history."""
        changelog = f"# Changelog - {app_name}\n\n"

        sorted_versions = sorted(versions, key=lambda x: x.get("date", ""), reverse=True)
        for version in sorted_versions:
            version_num = version.get("version", "Unknown")
            version_date = version.get("date", "Unknown date")
            changelog += f"## {version_num} - {version_date}\n\n"

            if version.get("added"):
                changelog += "### Added\n"
                for item in version["added"]:
                    changelog += f"- {item}\n"
                changelog += "\n"

            if version.get("fixed"):
                changelog += "### Fixed\n"
                for item in version["fixed"]:
                    changelog += f"- {item}\n"
                changelog += "\n"

            if version.get("changed"):
                changelog += "### Changed\n"
                for item in version["changed"]:
                    changelog += f"- {item}\n"
                changelog += "\n"

        report_id = f"changelog_{app_name}_{datetime.now().timestamp()}"
        filepath = self.output_dir / f"{report_id}.md"

        with open(filepath, "w") as f:
            f.write(changelog)

        logger.info(f"Generated changelog {report_id}")
        return str(filepath)

    async def get_report(self, report_id: str) -> Optional[Report]:
        """Retrieve a report."""
        return self.reports.get(report_id)

    async def export_report(self, report_id: str, export_format: str = "json") -> str:
        """Export report in specified format."""
        if report_id not in self.reports:
            raise ValueError(f"Report {report_id} not found")

        report = self.reports[report_id]

        if export_format == "json":
            filepath = self.output_dir / f"{report_id}.json"
            with open(filepath, "w") as f:
                json.dump(asdict(report), f, indent=2, default=str)
            return str(filepath)
        else:
            raise ValueError(f"Unsupported export format: {export_format}")
