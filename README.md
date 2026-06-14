<p align="center">
  <img alt="IPilot" src="https://img.shields.io/badge/IPilot-IP%20Mascot%20Workflow-6e41e2?style=for-the-badge&logo=robot&logoColor=white">
</p>

<p align="center">
  <a href="https://github.com/LewisHinton/IPilot/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/badge/license-MIT-blue.svg"></a>
  <a href="https://github.com/LewisHinton/IPilot/actions/workflows/validate.yml"><img alt="CI" src="https://github.com/LewisHinton/IPilot/actions/workflows/validate.yml/badge.svg"></a>
  <a href="https://github.com/LewisHinton/IPilot/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/LewisHinton/IPilot?style=social"></a>
</p>

# IPilot

Human-in-the-loop IP mascot asset workflow for agent Skills.

IPilot helps teams turn an existing mascot, avatar, brand figure, or IP character into consistent visual asset concepts: sticker packs, memes, campaign visuals, platform social posts, occasion-based visuals, physical material concepts, and image-generation prompt packs.

It is not a generic image generator. IPilot preserves the character's visual grammar first, then expands assets inside safe constraints.

## How to Install

Clone the repository:

```bash
git clone https://github.com/LewisHinton/IPilot.git
cd IPilot
```

Codex CLI / Codex editor / Codex desktop:

```bash
cp -R . ~/.codex/skills/ipilot
```

Windows PowerShell:

```powershell
Copy-Item -Recurse . "$env:USERPROFILE\.codex\skills\ipilot" -Force
```

Claude Code / Claude-compatible Skill runtimes:

1. Keep `SKILL.md` at the root of the `IPilot` folder.
2. Preserve `references/`, `templates/`, `examples/`, `sample_briefs/`, and `scripts/`.
3. Import, copy, symlink, or upload the folder according to your runtime's Skill mechanism.
4. If your runtime expects a portable bundle, zip the folder contents without changing structure.

Manual prompt-pack use:

1. Open `SKILL.md`.
2. Load the relevant files in `references/`.
3. Ask your model to follow IPilot for the current mascot project.

## Demo GIF

![IPilot demo](assets/demo/ipilot-demo.gif)

## Quick Start

After installation, try:

```text
@ipilot
I own this mascot. Use the reference image to create a 6-piece sticker pack.
Keep the character consistent and ask before image generation.
```

IPilot should:

1. classify the reference image as the source of truth;
2. extract visual anchors, line language, drawing style, color ratio, and forbidden drift;
3. confirm the sticker-pack direction and text handling;
4. generate sticker concepts with captions, prompts, and negative prompts separated;
5. ask before image generation unless auto-generation was explicitly authorized;
6. review generated images for identity drift, style drift, text errors, and safety.

## Why Star This

IPilot solves a common production failure: teams have a recognizable character, but every new prompt slowly changes its identity.

It gives agent runtimes a repeatable workflow for:

- keeping reference-image fidelity instead of silently averaging visual references;
- separating invariant features, flexible features, forbidden changes, and safety constraints;
- routing requests into the right material type before generating details;
- adapting output for platforms, occasions, audiences, and physical usage contexts;
- keeping the user in the loop with short recaps, micro-confirmations, and approval gates;
- separating captions, visual prompts, text-layout notes, safety notes, and production handoff notes.

## Core Workflow

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

## What It Protects

| Layer | What It Tracks |
|---|---|
| Identity anchors | species / object type, silhouette, accessories, emblem, costume, facial landmarks |
| Line language | outline weight, line closure, stroke style, internal detail density |
| Drawing style | chibi, flat vector, 3D toy, pixel, hand-drawn, shading, texture |
| Color system | primary / secondary / accent / neutral colors and approximate ratios |
| Shape construction | head-to-body ratio, eye scale, limb structure, accessory scale, balance |
| Production quality | complete construction, clean fills, no broken elements, no random text |
| Brand safety | no hateful, sexualized, political-persuasion, harassing, or off-brand content |

## Human-in-the-Loop by Default

IPilot should not rush from a user request to image generation.

- **Gate 0: Material type confirmation** when the asset type is unclear.
- **Gate 1: Asset direction confirmation** after opportunity mapping.
- **Gate 2: Concept approval before image generation** after prompts and safety review.
- **Gate 3: Post-generation decision** after image output.

Between gates, IPilot uses micro-confirmations such as:

- "I will treat this uploaded image as the official source of truth unless you say otherwise."
- "I will keep Chinese text as a separate layer to avoid text-rendering errors."
- "I will use balanced reference fidelity for social stickers."

## Ecosystem Support

| Environment | Install / Use |
|---|---|
| Codex CLI | copy to `~/.codex/skills/ipilot` |
| Codex editor / desktop | copy to the Codex skills directory or install as a workspace Skill |
| Claude Code and similar CLI agents | import, copy, symlink, or point the agent at the folder |
| Claude app / web Skill flows | upload or import a zipped Skill folder when supported |
| Other SKILL.md-compatible agents | preserve folder structure and point the agent at `SKILL.md` |
| No Skill runtime | manually load `SKILL.md` plus relevant `references/` files |

## Application Domains

| Domain | Typical Outputs |
|---|---|
| Brand marketing | campaign cards, launch visuals, social covers, product announcement graphics |
| Community operations | reaction stickers, welcome stickers, contributor badges, group memes |
| Education and campus orgs | workshop stickers, exam-season cards, club mascot assets, explainer thumbnails |
| Open-source projects | mascot stickers, README banners, release celebration cards, contributor rewards |
| Events and conferences | booth posters, badges, flyers, attendee stickers, QR-code cards |
| Physical merchandise | sticker sheets, keychains, postcards, packaging inserts |
| Occasion-based campaigns | IP birthday visuals, holiday greetings, anniversary cards, countdown series |
| Consistency review | generated-image QA, reference conflict resolution, prompt drift diagnosis |

## Validate a Brief

```bash
python scripts/validate_ip_brief.py sample_briefs/tensor-cat-brief.md
python scripts/check_release_readiness.py
```

## Repository Map

```text
IPilot/
|-- SKILL.md
|-- LICENSE
|-- README.md
|-- CONTRIBUTING.md
|-- SECURITY.md
|-- templates/
|-- references/
|-- examples/
|-- sample_briefs/
`-- scripts/
```

## Key References

- `references/human-in-the-loop-dialogue.md`: conversational cadence and mandatory pauses.
- `references/reference-image-intake.md`: source-of-truth handling for uploaded IP images.
- `references/ip-consistency-system.md`: deep visual grammar rules.
- `references/material-type-router.md`: asset routing before detailed concepts.
- `references/confirmation-gates.md`: approval gates before production and generation.
- `references/image-generation-protocol.md`: prompt structure and generation readiness checks.
- `references/brand-safety-checklist.md`: safety review for brand-safe mascot output.

## Community and Trust

- Use `CONTRIBUTING.md` before opening pull requests.
- Use GitHub issue templates for bugs, feature requests, and real-world use cases.
- Use `SECURITY.md` for prompt-injection, unsafe-instruction, or script-behavior concerns.
- Do not upload private reference art, brand guidelines, or unreleased mascot assets unless you have rights to share them.

## Safety Boundaries

IPilot must not generate or recommend:

- hateful, discriminatory, harassing, or demeaning content;
- sexualized mascot content, especially for childlike or brand-safe IPs;
- political persuasion or propaganda assets;
- profanity or vulgar humor unless explicitly allowed and still brand-safe;
- imitation of copyrighted characters, famous mascots, or living artists' distinctive styles unless the user owns the relevant rights;
- content that contradicts the user-provided forbidden topics or forbidden visual changes.

## GitHub Release Checklist

- [ ] Confirm `LICENSE` matches the intended open-source license.
- [ ] Add repo description: `Human-in-the-loop IP mascot asset workflow for agent Skills`.
- [ ] Use topics: `codex-skill`, `mascot`, `brand-safety`, `image-generation`, `prompt-engineering`, `human-in-the-loop`, `ip-consistency`, `creative-ai`.
- [ ] Keep GitHub Actions validation enabled.
- [ ] Run `python scripts/check_release_readiness.py`.

## 中文版

IPilot 是一个面向 AI Agent Skill 生态的 IP 吉祥物资产生产工作流。

它适合已经拥有 IP 形象、品牌角色、吉祥物或头像角色的团队。IPilot 的重点不是“从零生成一个角色”，而是先保护已有角色的视觉语法，再延展出表情包、梗图、活动视觉、平台社交图、节日视觉、线下物料概念和图像生成提示词。

### 安装

```bash
git clone https://github.com/LewisHinton/IPilot.git
cd IPilot
```

Codex:

```bash
cp -R . ~/.codex/skills/ipilot
```

Windows PowerShell:

```powershell
Copy-Item -Recurse . "$env:USERPROFILE\.codex\skills\ipilot" -Force
```

Claude Code 或其他支持 `SKILL.md` 的工具：

1. 保持 `SKILL.md` 在 `IPilot` 文件夹根目录。
2. 保留 `references/`、`templates/`、`examples/`、`sample_briefs/`、`scripts/`。
3. 按你的工具要求导入、复制、软链接或上传整个文件夹。

### 快速开始

```text
@ipilot
我已经有一个吉祥物参考图。请基于它创作 6 个表情包。
保持角色一致，并在生成图片前先问我确认。
```

IPilot 会先识别参考图角色特征，提取固定视觉锚点，确认素材方向，再输出概念、文案、图像提示词、负面约束和安全检查。

### 适用场景

- 品牌吉祥物表情包
- 社群互动贴纸
- 小红书、微信、B 站、抖音等平台视觉
- IP 生日、节日、周年、倒计时视觉
- 线下贴纸、徽章、亚克力、明信片等物料概念
- 已生成图片的一致性和安全审查

## Status

Current release: **v0.8 release candidate**.
