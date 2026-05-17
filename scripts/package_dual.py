#!/usr/bin/env python3
"""
Dual Skill Packager — Creates both .skill and versioned .zip
package_dual.py v1.0 | 2026-02-10

Enforces the mandatory dual-packaging standard:
  .skill  → interface-loadable (drag-and-drop into Claude)
  .zip    → manual deployment (extract to /mnt/skills/user/)

Usage:
    python package_dual.py <skill-folder> --version <X.Y> [--output <dir>]

Example:
    python package_dual.py ./solid8 --version 1.0
    python package_dual.py ./devcom5 --version 1.0 --output /mnt/user-data/outputs
"""

import sys
import zipfile
import fnmatch
import argparse
from pathlib import Path

EXCLUDE_DIRS = {"__pycache__", "node_modules", ".git", "evals"}
EXCLUDE_GLOBS = {"*.pyc"}
EXCLUDE_FILES = {".DS_Store", "Thumbs.db"}


def should_exclude(rel_path: Path) -> bool:
    parts = rel_path.parts
    if any(part in EXCLUDE_DIRS for part in parts):
        return True
    if rel_path.name in EXCLUDE_FILES:
        return True
    return any(fnmatch.fnmatch(rel_path.name, pat) for pat in EXCLUDE_GLOBS)


def validate_skill(skill_path: Path) -> tuple[bool, str]:
    """Minimal validation before packaging."""
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return False, "SKILL.md not found"
    content = skill_md.read_text()
    if not content.startswith("---"):
        return False, "No YAML frontmatter found"
    if "name:" not in content.split("---")[1]:
        return False, "Missing 'name' in frontmatter"
    if "description:" not in content.split("---")[1]:
        return False, "Missing 'description' in frontmatter"
    return True, "Valid"


def create_zip(skill_path: Path, output_path: Path) -> int:
    """Create a zip archive of skill, return file count."""
    count = 0
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for file_path in sorted(skill_path.rglob('*')):
            if not file_path.is_file():
                continue
            arcname = file_path.relative_to(skill_path.parent)
            if should_exclude(arcname):
                continue
            zf.write(file_path, arcname)
            count += 1
    return count


def main():
    parser = argparse.ArgumentParser(description="Dual skill packager (.skill + .zip)")
    parser.add_argument("skill_folder", help="Path to skill folder")
    parser.add_argument("--version", "-v", required=True, help="Version (e.g., 1.0)")
    parser.add_argument("--output", "-o", default=".", help="Output directory")
    args = parser.parse_args()

    skill_path = Path(args.skill_folder).resolve()
    output_dir = Path(args.output).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    if not skill_path.is_dir():
        print(f"❌ Not a directory: {skill_path}")
        sys.exit(1)

    # Validate
    valid, msg = validate_skill(skill_path)
    if not valid:
        print(f"❌ Validation failed: {msg}")
        sys.exit(1)
    print(f"✅ {msg}")

    skill_name = skill_path.name

    # .skill file (no version in name)
    skill_file = output_dir / f"{skill_name}.skill"
    count = create_zip(skill_path, skill_file)
    print(f"📦 {skill_file.name} ({count} files, {skill_file.stat().st_size / 1024:.1f} KB)")

    # .zip file (versioned)
    zip_file = output_dir / f"{skill_name}-v{args.version}.zip"
    create_zip(skill_path, zip_file)
    print(f"📦 {zip_file.name} ({count} files, {zip_file.stat().st_size / 1024:.1f} KB)")

    print(f"\n✅ Dual packaging complete: {skill_name}")
    print(f"   .skill → drag into Claude interface")
    print(f"   .zip   → extract to /mnt/skills/user/{skill_name}/")


if __name__ == "__main__":
    main()
