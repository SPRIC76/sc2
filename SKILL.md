---
name: sc2
description: >
  Enhanced skill creator with mandatory dual-packaging (.skill + .zip),
  validation, and comprehensive reference material. Piggybacks the base Anthropic
  skill-creator with stricter output standards. Use when creating, improving,
  or packaging skills. ALWAYS produces both .skill (interface-loadable) and
  versioned .zip (manual deployment). Enforces documentation completeness
  and user-friendly reference material in every skill.
---

# Skill Creator — Packaging & Quality Standards

This skill supplements the base `skill-creator` (in `/mnt/skills/examples/`).
Read base SKILL.md first for full workflow, then apply these standards on top.

## Mandatory Packaging Standard

**Every skill output MUST include both formats:**

| Format | Purpose | Naming |
|--------|---------|--------|
| `.skill` | Direct interface loading (drag-and-drop) | `{name}.skill` |
| `.zip` | Manual download/deployment to `/mnt/skills/user/` | `{name}-v{X.Y}.zip` |

Both are zip archives with `{skillname}/SKILL.md` as root entry.
The `.skill` file has no version in filename (always current).
The `.zip` includes version for archive/deployment clarity.

### Packaging Procedure

**ALWAYS use `scripts/package_dual.py`** instead of the base `package_skill.py`:

```bash
scripts/package_dual.py <path/to/skill-folder> --version <X.Y> [--output <dir>]
```

This produces both files in one command. If the script is unavailable,
package manually:

```bash
cd <parent-of-skill-folder>
zip -r <output>/skillname.skill skillname/
cp <output>/skillname.skill <output>/skillname-vX.Y.zip
```

**Present BOTH files to the user.** Never present only one format.

### Pre-Package Checklist

Before packaging, verify:

| Check | Requirement |
|-------|------------|
| SKILL.md frontmatter | `name` (kebab-case) + `description` (with triggers) |
| SKILL.md body | < 500 lines, progressive disclosure to references |
| References | All referenced files exist, concise, user-friendly |
| Scripts | All referenced scripts exist, documented, runnable |
| No orphans | Every file referenced from SKILL.md or another file |
| No junk | No `__pycache__`, `.pyc`, `.DS_Store`, `node_modules` |

### Documentation Completeness

Every skill MUST have:

1. **SKILL.md** — Core instructions, triggers, workflow, anti-patterns
2. **references/** — Any supporting docs referenced from SKILL.md
   - Each reference file must justify its existence (not duplicating SKILL.md)
   - Concise and scannable (tables over prose, imperative form)
   - Include version/date header
3. **scripts/** (if applicable) — Executable code with docstrings

**User-friendly standard:** A new user reading only SKILL.md should understand
what the skill does, when it triggers, and how to use it. References provide
depth, not prerequisites.

### Version Tracking

Every skill file set should note:
- Skill version in archive filename
- Creation date in SKILL.md or references
- Former names/versions in footnote if renamed

---

## Integration with Base Skill-Creator

This overlay modifies these base workflow steps:

**"Package and Present" (line ~340):** Replace single `.skill` output with
dual packaging. Always present both files via `present_files`.

**"Final Report" (line ~555):** After copying best skill back, run dual
packaging. Present both `.skill` and `.zip` to user.

**"Immediate Feedback Loop":** When showing early outputs, still use
dual packaging if presenting a testable skill.

All other base workflow steps (interview, research, init, writing guide,
eval, improve, benchmark) remain unchanged.
