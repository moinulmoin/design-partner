"""Package integrity checks; requires PyYAML, not a behavioral evaluation."""

from pathlib import Path
import re
import yaml


def require(condition, message):
    if not condition:
        raise ValueError(message)


def headings(text):
    counts = {}
    anchors = set()
    in_fence = False
    for line in text.splitlines():
        if line.startswith(('```', '~~~')):
            in_fence = not in_fence
        if in_fence:
            continue
        match = re.match(r'^#{1,6}\s+(.+?)(?:\s+#+)?$', line)
        if match:
            slug = re.sub(r'[^\w\- ]', '', match[1].lower()).replace(' ', '-')
            count = counts.get(slug, 0)
            counts[slug] = count + 1
            anchors.add(f'{slug}-{count}' if count else slug)
    return anchors


def validate(root):
    skill = root / "skills" / "design"
    entry = skill / "SKILL.md"
    text = entry.read_text()
    match = re.match(r'\A---\n(.*?)\n---(?:\n|$)', text, re.S)
    require(match is not None, 'Missing or unterminated YAML frontmatter')
    frontmatter = yaml.safe_load(match[1])
    require(isinstance(frontmatter, dict), 'Frontmatter must be a mapping')
    require(frontmatter.get('name') == 'design', 'Unexpected skill name')
    require(isinstance(frontmatter.get('description'), str) and frontmatter['description'].strip(), 'Missing description')
    metadata = yaml.safe_load((skill / 'agents' / 'openai.yaml').read_text())
    require(isinstance(metadata, dict) and isinstance(metadata.get('interface'), dict), 'Missing interface mapping')
    interface = metadata['interface']
    for key in ('display_name', 'short_description', 'default_prompt'):
        require(isinstance(interface.get(key), str) and interface[key].strip(), f'Missing {key}')
    require('$design' in interface['default_prompt'], 'Missing explicit invocation')
    markdown = list(skill.rglob("*.md"))
    for path in markdown:
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            if "://" in target:
                continue
            filename, _, anchor = target.partition('#')
            resolved = (path.parent / filename).resolve() if filename else path.resolve()
            require(resolved.is_relative_to(skill.resolve()), f'Non-portable link: {target}')
            require(resolved.is_file(), f'Broken link in {path}: {target}')
            if anchor:
                require(anchor in headings(resolved.read_text()), f'Broken heading in {path}: {target}')
    print(f"PASS: frontmatter, UI metadata, and links in {len(markdown)} Markdown files")
    print("Not evaluated: model behavior, visual quality, or accessibility outcomes")


if __name__ == "__main__":
    validate(Path(__file__).resolve().parents[1])
