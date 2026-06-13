# Security Policy

IPilot is a Skill package. It contains instructions, references, templates, examples, and lightweight validation scripts. Because Skills can influence agent behavior, treat third-party modifications with the same care you would apply to automation code.

## Supported Scope

Security reports are in scope when they relate to:

- unsafe instructions that could make agents bypass user confirmation;
- prompt-injection patterns inside Skill instructions, examples, or templates;
- scripts that perform unexpected filesystem, network, or shell actions;
- guidance that encourages unsafe IP usage, harassment, political persuasion, sexualized mascot content, or copyrighted-character imitation;
- release assets that misrepresent installation, execution, or trust boundaries.

## Out of Scope

- A user's own private mascot brief or private reference image.
- Downstream image-generation model behavior that contradicts the prompt after IPilot provided safe constraints.
- Third-party forks that substantially modify the Skill.
- License-selection disputes.

## Reporting

If this repository has GitHub security advisories enabled, use a private security advisory first.

If not, open an issue with:

- affected file path;
- exact unsafe instruction, prompt, script behavior, or example;
- why it creates risk;
- suggested safer wording or behavior.

Do not include private mascot art, confidential brand guidelines, or proprietary IP references in public issues.

## Security Design Principles

- Preserve user confirmation before image generation unless auto-generation is explicit.
- Keep prompts, captions, safety notes, and production handoff notes separated.
- Keep validation scripts dependency-light and transparent.
- Avoid hidden network calls, hidden shell execution, or environment-specific assumptions.
- Treat reference images as user-owned source material, not public training examples.

