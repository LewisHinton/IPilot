# Changelog

## v0.8 release candidate

- Added `references/human-in-the-loop-dialogue.md` for conversational cadence, micro-confirmations, mandatory pauses, and fast-path behavior.
- Updated `SKILL.md` so human-in-the-loop dialogue applies throughout the default workflow, not only at major confirmation gates.
- Expanded `references/confirmation-gates.md` with Gate 0 material-type confirmation and clearer concept-vs-generation approval boundaries.
- Updated guided intake and production workflow references to prefer short conversational loops over long questionnaires.
- Reworked `README.md` for GitHub release readiness with clearer positioning, quick start, examples, repository map, safety boundaries, release checklist, and recommended topics.
- Added `.gitignore` for Python cache, local environments, editor files, and local generated outputs.
- Added `scripts/check_release_readiness.py` and `.github/workflows/validate.yml` for dependency-free release checks in CI.
- Added `CONTRIBUTING.md` and `.github/pull_request_template.md` to make community contributions easier to review.
- Expanded `README.md` with How to Install, ecosystem support for CLI/editor/Skill runtimes, and common application domains.
- Added `SECURITY.md`, GitHub issue templates, and `examples/README.md` to improve trust, community intake, and example discoverability.
- Moved How to Install earlier in `README.md`, added a demo GIF, added a clearer Quick Start, and added a Chinese section.

## v0.7 release candidate

- Added reference-image intake as a first-class pre-production workflow for uploaded or existing IP images.
- Added `references/reference-image-intake.md`.
- Added `references/multi-reference-consistency.md`.
- Added `templates/reference-image-intake-template.md`.
- Added `templates/reference-image-analysis-report-template.md`.
- Added `examples/reference-image-workflow-demo.md`.
- Added `sample_briefs/reference-image-brief.md`.
- Updated `SKILL.md` with Mode L -Reference Image Intake Specialist, reference source-of-truth handling, reference fidelity scoring, and reference-aware generation prompts.
- Updated image-generation and post-generation review rules to check identity drift, style drift, color drift, proportion drift, structural defects, and production integrity.
- Updated README and AGENTS with reference-image workflow and multi-reference constraints.
- Updated validator with reference-image recommended fields.

## v0.6 draft

- Deepened IP consistency from simple fixed features into a visual grammar system covering identity anchors, line language, drawing style, color ratio, shape construction, flexible motion space, and production quality.
- Added `references/ip-consistency-system.md`.
- Added `references/visual-quality-control.md`.
- Added `references/text-layout-and-font-guidelines.md`.
- Added `references/trend-adaptation-rules.md`.
- Added `references/production-workflow.md`.
- Added `templates/ip-visual-consistency-profile-template.md`.
- Added `templates/production-handoff-template.md`.
- Added `examples/deep-ip-consistency-demo.md`.
- Added `sample_briefs/deep-consistency-brief.md`.
- Updated `SKILL.md` with Mode K -Deep IP Consistency Director and deeper image-generation quality constraints.
- Updated image-generation protocol with visual grammar, production quality, text-layer handoff, and stricter revision prompt rules.
- Updated README and AGENTS to position IPilot as an end-to-end IP asset production workflow.
- Updated validator with deep consistency recommended fields.

## v0.5 draft

- Added comprehensive material taxonomy covering identity assets, community interaction assets, meme assets, digital promotional assets, occasion-based assets, educational assets, lifecycle assets, physical materials, and hybrid asset systems.
- Added `references/material-taxonomy.md`.
- Added `references/occasion-based-assets.md` for IP birthday visuals, holiday greetings, festival posters, anniversaries, seasonal cards, countdown series, and milestone assets.
- Added `templates/material-type-confirmation-template.md`.
- Added `templates/occasion-asset-brief-template.md`.
- Added `examples/occasion-birthday-demo.md`.
- Added `sample_briefs/occasion-birthday-brief.md`.
- Updated `SKILL.md` with Material Type Confirmation logic and Mode J -Occasion-Based Asset Designer.
- Updated `references/material-type-router.md` so unclear asset requests pause for material-type confirmation before detailed concept generation.
- Updated guided intake questions with occasion-based asset questions.
- Updated validator with occasion-based recommended fields.
- Updated README and AGENTS guidance for v0.5 workflows.

## v0.4 draft

- Added material-type routing before detailed concept generation.
- Added `references/material-type-router.md`.
- Added `references/platform-adaptation-rules.md` for Xiaohongshu, WeChat, Bilibili, Douyin, X, and Instagram-oriented digital promotional assets.
- Added `references/physical-material-audience-rules.md` for tangible materials such as stickers, badges, acrylic stands, keychains, postcards, flyers, package inserts, and booth materials.
- Added `templates/platform-adaptation-brief-template.md`.
- Added `templates/physical-material-brief-template.md`.
- Updated `SKILL.md` with Platform Adaptation Strategist and Physical Material Designer modes.
- Updated guided intake questions so digital promotional assets ask for target platform and physical materials ask for audience orientation.
- Updated asset opportunity and output templates with route, platform, and physical production fields.
- Added `sample_briefs/physical-material-brief.md`.
- Updated README and AGENTS guidance for v0.4 workflows.

## v0.3 draft

- Added Asset Opportunity Map workflow for users who do not know which material types to create.
- Added `references/asset-opportunity-map.md`.
- Added `references/confirmation-gates.md` for human-in-the-loop decision points.
- Added `templates/asset-opportunity-map-template.md`.
- Updated `SKILL.md` with Asset Opportunity Strategist mode and confirmation gates.
- Updated guided intake questions to include material-type discovery.
- Updated IP brief template with asset discovery fields.
- Updated validator so a brief may specify either `Asset Types Needed` or `Asset Discovery Needed`.

## v0.2 draft

- Reframed IPilot as an existing-IP asset production Skill.
- Added `AGENTS.md` for repository-level guidance.
- Strengthened the central `SKILL.md` workflow.
- Added explicit guided intake stages.
- Added image-generation trigger and no-trigger conditions.
- Renamed safety reference to `brand-safety-checklist.md`.
- Added validator-friendly sample briefs.
- Improved examples with consistency and safety reviews.

## v0.1 draft

- Initial repository skeleton.
- Added basic Skill instruction, templates, references, examples, and validator script.


