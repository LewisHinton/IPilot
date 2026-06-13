# Contributing to IPilot

IPilot is a Codex Skill for existing-IP mascot asset production. Contributions should make the workflow more reliable, safer, easier to use, or easier to validate.

## Good Contributions

- Better human-in-the-loop dialogue patterns.
- Stronger reference-image consistency rules.
- Clearer material routing for stickers, memes, campaign visuals, occasion assets, or physical materials.
- More realistic examples and sample briefs.
- Validator improvements that stay dependency-light.
- Safety and production-quality checks that reduce identity drift or unsafe output.

## Keep Changes Focused

- Preserve the core principle: visual grammar first, creativity second.
- Do not turn IPilot into a generic image generator.
- Keep captions, image prompts, safety notes, and production handoff notes separated.
- Prefer concise reference modules over adding long instructions to `SKILL.md`.
- Do not add copyrighted mascot examples unless you own or can use the rights.

## Local Checks

Run the release-readiness check:

```bash
python scripts/check_release_readiness.py
```

Run a sample brief check:

```bash
python scripts/validate_ip_brief.py sample_briefs/tensor-cat-brief.md
```

## Pull Request Checklist

- The change is inside the IPilot workflow scope.
- Relevant Markdown files are internally consistent.
- Examples still follow the confirmation-gated workflow.
- Reference-image examples identify source of truth and forbidden drift.
- Physical material examples include audience and usage context.
- Occasion examples include occasion type, timing, tone, and cultural sensitivity when relevant.
- `python scripts/check_release_readiness.py` passes.

