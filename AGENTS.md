# AGENTS.md

## Project

IPilot is an open-source Skill for generating brand-safe, creative, and IP-consistent visual asset concepts for users who already own an IP character, mascot, avatar, or brand figure.

The default user has an existing IP. Do not treat IPilot as a generic image generator or a from-scratch character design tool unless the user explicitly asks for IP profile building.

## Core principle

Preserve visual grammar first. Generate creativity second.

The Skill should always distinguish:

1. invariant features: traits that must not change;
2. variable features: traits that may change by asset;
3. forbidden changes: visual, tonal, contextual, or legal constraints;
4. safety constraints: risks that must be reviewed before delivery;
5. material routes: identity, community, meme, digital promotional, occasion-based, educational, lifecycle, physical, or hybrid assets;
6. material-type confirmation: the user must confirm the exact type before detailed concepts unless auto-pick is authorized;
7. asset opportunities: material types that fit the IP, platform, audience, campaign goal, and physical usage context;
8. platform adaptation: publishing-platform-specific format, text density, and interaction behavior;
9. physical material audience orientation: who receives and uses tangible materials;
10. confirmation gates and dialogue cadence: user approval points, short recaps, micro-confirmations, and pauses before detailed production and image generation;
11. generation conditions: when image generation is allowed;
12. deep IP consistency: identity anchors, line language, drawing style, color ratio, shape construction, and production quality;
13. text-layout handoff: typography direction and separate text layers when rendered text is unreliable;
14. trend adaptation: support trend-based assets while preserving IP identity and avoiding unsafe copying.

## Repository layout

- `SKILL.md`: central Skill instruction and operational workflow.
- `README.md`: public-facing project explanation.
- `templates/`: reusable input and output templates, including material type confirmation, occasion-based, and asset opportunity templates.
- `references/`: guided questions, human-in-the-loop dialogue, material taxonomy, material routing, occasion-based assets, platform adaptation, physical material rules, deep IP consistency, visual quality control, text layout, trend adaptation, production workflow, asset opportunity map, confirmation gates, safety checklist, image-generation protocol.
- `examples/`: complete demo cases showing the full workflow.
- `sample_briefs/`: validator-friendly brief files.
- `scripts/`: lightweight helper scripts.

## Writing style

Use clear, direct English. Prefer operational instructions over vague marketing language. Use structured Markdown with explicit headings, bullet points, and tables when helpful.

Avoid:

- generic AI hype;
- abstract claims without workflow implications;
- long paragraphs that are hard to scan;
- mixing captions, image prompts, and safety notes.

## Safety constraints

IPilot must not generate or recommend:

- hateful, discriminatory, harassing, or demeaning content;
- sexualized mascot content, especially for childlike or brand-safe IPs;
- political persuasion or propaganda assets;
- profanity or vulgar humor unless explicitly allowed and still brand-safe;
- imitation of copyrighted characters, famous mascots, or living artists' distinctive styles unless the user owns the relevant rights;
- content that contradicts the user-provided forbidden topics or forbidden visual changes.


## Reference-image constraints

When reference images are present, IPilot must:

1. classify each reference by role: primary, style, pose, expression, material, outdated, or negative;
2. identify the source of truth before generation;
3. extract visual anchors, line language, drawing style, color ratio, shape construction, and rendering rules;
4. flag conflicts between references rather than silently averaging them;
5. ask the user to resolve identity-critical conflicts before generation;
6. convert negative references into explicit avoid rules;
7. include reference fidelity level in generation and review.

## Human-in-the-loop constraints

IPilot should recommend material types when the user does not know what to create. Do this through a Material Type Confirmation Menu or Asset Opportunity Map rather than immediately producing detailed concepts.

IPilot should keep users in the loop through short conversational turns: recap what is known, state assumptions, ask the next smallest useful question, and pause when the answer changes identity, direction, safety, or generation.

For digital promotional assets, ask for the target publishing platform before detailed concept generation when the platform is missing.

For occasion-based assets such as IP birthday visuals, holiday cards, festival posters, anniversary visuals, seasonal campaigns, or milestone cards, ask for occasion type, date/window, platform, tone, output format, and cultural constraints when missing.

For physical or tangible materials, ask for the audience orientation and physical usage context before detailed concept generation when those details are missing.

Use confirmation gates before:

1. confirming the material type and asset direction, unless the user already selected one;
2. invoking image generation, unless the user explicitly authorized automatic generation and the reference-image source of truth is clear;
3. accepting or regenerating generated images.

If the user asks IPilot to auto-pick, choose the safest high-priority option and state the reason.

## Image generation constraints

Invoke image generation only when:

1. the user wants visual output;
2. the IP profile has enough invariant visual features and reference-image roles are clear if references are used;
3. the target material type is clear; for digital promotional assets, the platform is clear; for occasion-based assets, the occasion context is clear; for physical assets, the audience orientation and usage context are clear;
4. the concept passes consistency and brand safety review;
5. the prompt includes the invariant features, reference-derived constraints, and negative constraints;
6. any required reference image has been uploaded or is accessible in the current environment.

If these conditions are not met, ask concise guided questions or produce a prompt pack instead of invoking image generation.

Generated or prompted images should be complete and production-usable: preserve line language, drawing style, color ratio, visual anchors, coherent construction, clean color fills, and closed outlines when appropriate. Poses, expressions, scenes, props, and trend themes may vary if they do not weaken recognizability.

## Production-system scope

IPilot should be treated as an end-to-end IP asset production workflow: intake, material routing, platform/audience/occasion clarification, deep consistency profile, creative direction, confirmation, concept generation, safety review, image generation or prompt pack, post-generation review, text layout guidance, and production handoff notes.

For physical materials, include supplier-confirmation reminders for final DPI, bleed, cut lines, material, color mode, and file format. Do not pretend to replace vendor-specific production requirements.

## Done criteria

A change is done only when:

- relevant Markdown files are internally consistent;
- examples follow the Skill workflow, including reference-image handling when relevant;
- digital promotional assets include platform adaptation when relevant;
- occasion-based assets include occasion context, date/window, tone, and cultural-sensitivity notes when relevant;
- physical materials include audience orientation and production-context notes when relevant;
- captions, visual prompts, text-layout plans, and safety notes remain separated;
- deep IP consistency constraints are represented when the task depends on stable character appearance;
- `scripts/validate_ip_brief.py` runs without external dependencies;
- the change summary states assumptions and modified files.

