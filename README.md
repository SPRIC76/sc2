# SC2 — Skill Creator 2

Enhanced agent skill for **creating, improving, and packaging** Cursor / Claude skills with stricter quality and **mandatory dual output**.

**Voice:** Standards enforcer — quality and packaging, not creative writing.

## What SC2 adds

SC2 supplements the base skill-creator workflow with:

| Requirement | Detail |
|-------------|--------|
| Dual packaging | Every skill ships as `{name}.skill` **and** `{name}-vX.Y.zip` |
| Validation | Frontmatter, references, scripts, no orphan files |
| Documentation | Progressive disclosure; references stay scannable |

## Install (Cursor)

```text
~/.cursor/skills/sc2/
# or
.cursor/skills/sc2/
```

Copy this entire folder. Pair with Cursor's built-in **create-skill** guidance for the full authoring workflow; SC2 is the stricter **packaging overlay**.

## Usage

```bash
python scripts/package_dual.py <path/to/skill-folder> --version <X.Y> [--output <dir>]
```

**Example:**

```bash
python scripts/package_dual.py ./my-skill --version 1.0 --output ./dist
```

Produces:

| File | Purpose |
|------|---------|
| `my-skill.skill` | Drag-and-drop load (Claude Desktop / compatible UIs) |
| `my-skill-v1.0.zip` | Versioned archive for manual deployment |

Both are zip archives with `my-skill/SKILL.md` as the root entry.

## Platform notes

| Platform | Install path |
|----------|--------------|
| **Cursor** | `~/.cursor/skills/<name>/` or `.cursor/skills/<name>/` |
| **Claude Desktop** | Skills folder per app settings; `.skill` drag-and-drop |
| **Claude Code / agent** | Extract `.zip` to your agent skills directory |

The SKILL.md references Claude paths like `/mnt/skills/user/` for Claude-hosted environments. On Cursor, use the paths above.

## Pre-package checklist

- [ ] `SKILL.md` frontmatter: `name` (kebab-case) + `description` (with triggers)
- [ ] Body under ~500 lines; depth in `references/`
- [ ] All referenced files exist
- [ ] No `__pycache__`, `.pyc`, `node_modules`, junk files

## Repository layout

```text
SKILL.md
scripts/package_dual.py
```

## License

MIT — see [LICENSE](LICENSE). Copyright (c) 2025 SPRIC76.
