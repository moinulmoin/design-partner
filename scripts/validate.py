"""Dependency-free integrity checks, not a behavioral skill evaluation."""

from pathlib import Path
import re


def validate(root):
    skill = root / "skills" / "design"
    entry = skill / "SKILL.md"
    text = entry.read_text()
    assert text.startswith("---\n"), "Missing YAML frontmatter"
    frontmatter = text.split("---", 2)[1]
    assert re.search(r"^name: design$", frontmatter, re.M), "Unexpected skill name"
    assert re.search(r"^description: .+", frontmatter, re.M), "Missing description"
    metadata = (skill / "agents" / "openai.yaml").read_text()
    assert 'display_name: "Design Partner"' in metadata, "Missing UI name"
    assert "$design" in metadata, "Missing explicit invocation"
    markdown = list(skill.rglob("*.md"))
    for path in markdown:
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            if "://" in target or target.startswith("#"):
                continue
            resolved = (path.parent / target.split("#")[0]).resolve()
            assert resolved.is_relative_to(skill.resolve()), f"Non-portable link: {target}"
            assert resolved.is_file(), f"Broken link in {path}: {target}"
    print(f"PASS: frontmatter, UI metadata, and links in {len(markdown)} Markdown files")
    print("Not evaluated: model behavior, visual quality, or accessibility outcomes")


if __name__ == "__main__":
    validate(Path(__file__).resolve().parents[1])
