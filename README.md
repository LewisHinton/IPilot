<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/IPilot-IP%20Mascot%20Workflow-6e41e2?style=for-the-badge&logo=robot&logoColor=white&labelColor=1a1a2e">
    <img alt="IPilot" src="https://img.shields.io/badge/IPilot-IP%20Mascot%20Workflow-6e41e2?style=for-the-badge&logo=robot&logoColor=white&labelColor=f5f3ff">
  </picture>
</p>

<p align="center">
  <a href="https://github.com/LewisHinton/IPilot/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/badge/license-MIT-blue.svg"></a>
  <a href="https://github.com/LewisHinton/IPilot/actions/workflows/validate.yml"><img alt="CI" src="https://github.com/LewisHinton/IPilot/actions/workflows/validate.yml/badge.svg"></a>
  <a href="https://github.com/LewisHinton/IPilot/releases"><img alt="Release" src="https://img.shields.io/badge/release-v0.8--rc-6e41e2.svg"></a>
  <a href="https://github.com/LewisHinton/IPilot/blob/main/CONTRIBUTING.md"><img alt="PRs Welcome" src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg"></a>
  <a href="https://github.com/LewisHinton/IPilot/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/LewisHinton/IPilot?style=social"></a>
</p>

<br>

# 🎯 IPilot

**Human-in-the-loop IP mascot asset workflow for agent Skills.**

IPilot helps teams turn an existing mascot, avatar, brand figure, or IP character into consistent visual asset concepts: sticker packs, memes, campaign visuals, platform social posts, occasion-based visuals, physical material concepts, and image-generation prompt packs.

> **It is not a generic image generator.** Its default job is to preserve an IP's visual grammar first, then generate creative assets inside safe constraints.

---

## 📑 Table of Contents

- [Why Star This](#why-star-this)
- [30-Second Demo](#30-second-demo)
- [Core Workflow](#core-workflow)
- [What It Protects](#what-it-protects)
- [Human-in-the-Loop by Default](#human-in-the-loop-by-default)
- [Use Cases](#use-cases)
- [How to Install](#how-to-install)
- [Ecosystem Support](#ecosystem-support)
- [Application Domains](#application-domains)
- [Quick Start Prompt](#quick-start-prompt)
- [Validate a Brief](#validate-a-brief)
- [Repository Map](#repository-map)
- [Key References](#key-references)
- [Community and Trust](#community-and-trust)
- [Example Prompts](#example-prompts)
- [Safety Boundaries](#safety-boundaries)
- [GitHub Release Checklist](#github-release-checklist)
- [Status](#status)

---

## Why Star This 🌟

IPilot is built for a real production failure mode: teams have a recognizable character, but every new prompt slowly changes the identity.

It gives agent runtimes a repeatable workflow for:

- keeping reference-image fidelity instead of silently averaging visual references;
- separating invariant features, flexible features, forbidden changes, and safety constraints;
- routing requests into the right material type before generating details;
- adapting output for platforms, occasions, audiences, and physical usage contexts;
- keeping the user in the loop with short recaps, micro-confirmations, and approval gates;
- separating captions, visual prompts, text-layout notes, safety notes, and production handoff notes.

---

## 30-Second Demo ⚡

Ask:

```text
@ipilot
Use my mascot reference image to create 5 WeChat reaction stickers.
Keep the headphones, teal-white color system, round face, and circuit-pattern tail.
Use a cute but not childish tone.
```

IPilot should:

1. classify the reference image as the source of truth;
2. extract visual anchors, line language, drawing style, color ratio, and forbidden drift;
3. confirm the sticker-pack direction and text handling;
4. generate sticker concepts with captions, prompts, and negative prompts separated;
5. ask before image generation unless auto-generation was explicitly authorized;
6. review generated images for identity drift, style drift, text errors, and safety.

---

## Core Workflow 🔄

```text
Guided IP intake
-> Reference image intake, if references exist
-> IP consistency profile
-> Deep visual consistency profile
-> Material type routing
-> Human confirmation gate
-> Asset concepts
-> Safety and consistency review
-> Image generation or prompt handoff
-> Post-generation review
-> Text layout and production handoff
```

---

## What It Protects 🛡️

IPilot treats IP consistency as visual grammar, not a vague style note.

| Layer | What It Tracks |
|---|---|
| Identity anchors | species / object type, silhouette, accessories, emblem, costume, facial landmarks |
| Line language | outline weight, line closure, stroke style, internal detail density |
| Drawing style | chibi, flat vector, 3D toy, pixel, hand-drawn, shading, texture |
| Color system | primary / secondary / accent / neutral colors and approximate ratios |
| Shape construction | head-to-body ratio, eye scale, limb structure, accessory scale, balance |
| Production quality | complete construction, clean fills, no broken elements, no random text |
| Brand safety | no hateful, sexualized, political-persuasion, harassing, or off-brand content |

---

## Human-in-the-Loop by Default 🧑‍💻

IPilot should not rush from a user request to image generation.

It uses:

- **Gate 0: Material type confirmation** when the asset type is unclear.
- **Gate 1: Asset direction confirmation** after opportunity mapping.
- **Gate 2: Concept approval before image generation** after prompts and safety review.
- **Gate 3: Post-generation decision** after image output.

Between those gates, it uses micro-confirmations such as:

- "I will treat this uploaded image as the official source of truth unless you say otherwise."
- "I will keep Chinese text as a separate layer to avoid text-rendering errors."
- "I will use balanced reference fidelity for social stickers."

The goal is more conversation where it matters, without turning every request into a long form.

---

## Use Cases 📦

- Brand mascot sticker packs
- Community reaction images
- Meme concepts that stay brand-safe
- Platform-adapted campaign cards
- Xiaohongshu, WeChat, Bilibili, Douyin, X, and Instagram social assets
- IP birthday visuals, holiday cards, seasonal campaigns, and anniversary visuals
- Physical material concepts such as stickers, badges, acrylic stands, postcards, flyers, booth posters, and package inserts
- Reference-image intake and multi-reference conflict resolution
- Consistency and safety review for existing drafts or generated images
- Prompt packs for image-generation tools

---

## How to Install 📥

Pick your tool and run the commands.

---

### Claude Code

Install once, use everywhere with `@ipilot`:

```bash
git clone https://github.com/LewisHinton/IPilot.git
mv IPilot ~/.claude/skills/ipilot
```

Or, install inside a single project:

```bash
git clone https://github.com/LewisHinton/IPilot.git .claude/skills/ipilot
```

Restart Claude Code, then try:

```text
@ipilot I own a mascot. Help me build an IP consistency profile.
```

If `@ipilot` isn't recognized, make sure:
- the folder is named exactly `ipilot`
- `SKILL.md` is directly inside it (not nested deeper)
- you restarted Claude Code after copying

---

### Codex

IPilot is a standard SKILL.md folder. Check the Codex documentation for how to install custom Skills in your version (CLI, Editor, or Desktop).

---

### Other tools

IPilot works with any tool that reads `SKILL.md` files. Point your tool at the cloned folder. If your tool expects a zip, zip the folder contents (not the folder itself).

---

### No tool? No problem.

Open `SKILL.md`, copy its contents, paste into ChatGPT / Claude / any capable LLM. Add reference files from `references/` when you need them.

---

## Ecosystem Support 🌐

| Environment | How to use |
|---|---|
| Claude Code | `@ipilot` after copying to `~/.claude/skills/ipilot` |
| Codex | Check Codex docs for Skill installation |
| Other SKILL.md tools | Point at the cloned folder |
| No Skill runtime | Copy-paste `SKILL.md` into any capable LLM |

---

## Application Domains 🏢

IPilot is strongest when an organization already owns a mascot or brand figure and needs repeatable asset production.

| Domain | Typical Outputs |
|---|---|
| Brand marketing | campaign cards, launch visuals, social covers, product announcement graphics |
| Community operations | reaction stickers, welcome stickers, contributor badges, group memes |
| Education and campus orgs | workshop stickers, exam-season cards, club mascot assets, explainer thumbnails |
| Open-source projects | mascot stickers, README banners, release celebration cards, contributor rewards |
| Events and conferences | booth posters, badges, flyers, attendee stickers, QR-code cards |
| Physical merchandise | sticker sheets, acrylic stands, keychains, postcards, packaging inserts |
| Occasion-based campaigns | IP birthday visuals, holiday greetings, anniversary cards, countdown series |
| Consistency review | generated-image QA, reference conflict resolution, prompt drift diagnosis |

---

## Quick Start Prompt 🚀

After installation, try:

```text
@ipilot
I own this mascot. Use the reference image to create a 6-piece sticker pack.
Keep the character consistent and ask before image generation.
```

---

## Validate a Brief ✅

IPilot includes a dependency-light validator for Markdown IP briefs.

```bash
python scripts/validate_ip_brief.py sample_briefs/tensor-cat-brief.md
```

Run all release-readiness checks:

```bash
python scripts/check_release_readiness.py
```

The validator checks for required semantic fields while staying flexible enough for human-written briefs.

---

## Repository Map 📁

```text
IPilot/
├── SKILL.md                         # central skill workflow
├── LICENSE                          # MIT License
├── README.md                        # GitHub-facing overview
├── CONTRIBUTING.md                  # contribution guide
├── SECURITY.md                      # security policy for Skill usage
├── AGENTS.md                        # repo-level agent instructions
├── CHANGELOG.md                     # release notes
├── templates/                       # reusable input and output templates
├── references/                      # detailed workflow modules
│   ├── human-in-the-loop-dialogue.md
│   ├── reference-image-intake.md
│   ├── ip-consistency-system.md
│   ├── material-type-router.md
│   ├── confirmation-gates.md
│   ├── image-generation-protocol.md
│   └── ...
├── examples/                        # complete workflow demos
├── sample_briefs/                   # validator-friendly sample briefs
└── scripts/
    └── validate_ip_brief.py
```

---

## Key References 📚

- [`references/human-in-the-loop-dialogue.md`](references/human-in-the-loop-dialogue.md): conversational cadence and mandatory pauses.
- [`references/reference-image-intake.md`](references/reference-image-intake.md): source-of-truth handling for uploaded IP images.
- [`references/ip-consistency-system.md`](references/ip-consistency-system.md): deep visual grammar rules.
- [`references/material-type-router.md`](references/material-type-router.md): asset routing before detailed concepts.
- [`references/confirmation-gates.md`](references/confirmation-gates.md): approval gates before production and generation.
- [`references/image-generation-protocol.md`](references/image-generation-protocol.md): prompt structure and generation readiness checks.
- [`references/brand-safety-checklist.md`](references/brand-safety-checklist.md): safety review for brand-safe mascot output.

---

## Community and Trust 🤝

- Use [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening pull requests.
- Use GitHub issue templates for bugs, feature requests, and real-world use cases.
- Use [`SECURITY.md`](SECURITY.md) for prompt-injection, unsafe-instruction, or script-behavior concerns.
- Do not upload private reference art, brand guidelines, or unreleased mascot assets unless you have rights to share them.

---

## Example Prompts 💬

**Sticker pack:**

```text
@ipilot
Based on this official mascot reference, create 8 chat stickers for a developer community.
Tone: warm, smart, slightly funny. Keep text as separate layers.
```

**Campaign visual:**

```text
@ipilot
Use our existing IP character to design a product launch card for Xiaohongshu.
Ask me for platform and text constraints before detailed concepts.
```

**Physical material:**

```text
@ipilot
Create badge and acrylic stand concepts for our mascot.
Audience: conference visitors and community contributors.
Preserve the mascot's exact silhouette and color ratio.
```

**Review:**

```text
@ipilot
Review these generated mascot images for identity drift, style drift, color drift, text errors, and brand safety.
```

---

## Safety Boundaries 🛑

IPilot must not generate or recommend:

- hateful, discriminatory, harassing, or demeaning content;
- sexualized mascot content, especially for childlike or brand-safe IPs;
- political persuasion or propaganda assets;
- profanity or vulgar humor unless explicitly allowed and still brand-safe;
- imitation of copyrighted characters, famous mascots, or living artists' distinctive styles unless the user owns the relevant rights;
- content that contradicts the user-provided forbidden topics or forbidden visual changes.

---

## GitHub Release Checklist 📋

Before publishing the repository:

- [ ] confirm the [`LICENSE`](LICENSE) file matches the intended open-source license;
- [ ] add a short repo description: `Human-in-the-loop IP mascot asset workflow for agent Skills`;
- [ ] use topics such as `codex-skill`, `mascot`, `brand-safety`, `image-generation`, `prompt-engineering`, `human-in-the-loop`, `ip-consistency`, and `creative-ai`;
- [ ] keep the GitHub Actions validation workflow enabled;
- [ ] keep issue templates, [`CONTRIBUTING.md`](CONTRIBUTING.md), and [`SECURITY.md`](SECURITY.md) in the published repo;
- [ ] verify sample briefs with `python scripts/validate_ip_brief.py`;
- [ ] run `python scripts/check_release_readiness.py`;
- [ ] run a real mascot example and add screenshots or anonymized output snippets if you have permission.

---

## Status 📊

Current release: **v0.8 release candidate**.

This version emphasizes human-in-the-loop dialogue, reference-image fidelity, deep IP consistency, material routing, platform / occasion / physical context, and brand-safe image-generation readiness.

---

<p align="center">
  <sub>Built with ❤️ for IP owners who want their mascot to stay recognizable across every asset.</sub>
</p>
