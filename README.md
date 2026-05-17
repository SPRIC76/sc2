# SC2 — Skill Creator 2

Enhanced agent skill for **creating, improving, and packaging** Cursor / Claude skills with stricter quality and **mandatory dual output**.

**Voice:** Standards enforcer — quality and packaging, not creative writing.

## Install via skills.sh CLI

```bash
npx skills add SPRIC76/sc2
```

**Badge snippet:**

```markdown
[![skills.sh](https://skills.sh/b/SPRIC76/sc2)](https://skills.sh/SPRIC76/sc2)
```

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

## Install (Claude Desktop)

### Method A: Drag-and-drop

1. Package the `sc2/` folder as `sc2.skill`.
2. Drag `sc2.skill` into Claude Desktop.
3. Confirm SC2 appears in your installed skills.

### Method B: Manual folder install

1. Find your Claude skills directory in app settings/docs.
2. Copy the `sc2/` folder into that location.
3. Restart Claude Desktop to reload skills.

If your environment uses managed paths (for example `/mnt/skills/user/`), copy `sc2/` there.

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

## Other IDEs and agents

SC2 can be used anywhere an agent runtime supports folder-based skill instructions:

- Import/copy the `sc2/` folder as a skill package.
- Ensure the runtime can execute `scripts/package_dual.py` (Python 3.10+ recommended).
- If the IDE has no skill system, you can still run the packager manually from a terminal.

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
