# Text Layout and Font Guidelines

Image models may render Chinese and complex typography inconsistently. IPilot can design text layout, but should usually recommend keeping text as a separate design layer for final production.

## Default rule

- For stickers, posters, birthday visuals, holiday visuals, and campaign cards, provide the text content and layout plan separately from the image prompt.
- Ask the image model to leave clean space for text when final typography matters.
- Recommend font style categories instead of relying on the image model to render exact Chinese characters.

## When text can be inside the image

Text may be included directly when:

- the user explicitly requests it;
- the text is short;
- exact typography is not mission-critical;
- the user accepts possible manual correction.

## Recommended output fields

Every text-heavy asset should include:

```markdown
## Text Plan
- Main title:
- Subtitle:
- CTA:
- Date / time:
- Hashtag:
- Placement:
- Hierarchy:
- Font direction:
- Color direction:
- Manual layout note:
```

## Font recommendation categories

Use categories, not proprietary font assumptions:

| Tone | Font direction |
|---|---|
| Cute / soft | rounded sans-serif, soft handwritten display font |
| Professional | clean geometric sans-serif |
| Premium | elegant serif or high-contrast display font |
| Tech / AI | geometric sans-serif, monospaced accent font |
| Youth / social | bold rounded display font |
| Festival / birthday | playful display font with high readability |

## Prompt instruction examples

For text-free visual base:

```text
Do not render any text inside the image. Leave clean negative space in the upper-right area for later typography.
```

For short text inside image:

```text
Include only the short text "Happy Birthday" on a simple sign held by the mascot. Keep typography clean and readable.
```

For Chinese typography handoff:

```text
Do not render Chinese text directly. Leave a blank sign area for manual Chinese text layout in a design tool.
```

## Recommended external layout tools

IPilot may recommend that the user finalize typography in tools such as Figma, Canva, Photoshop, Illustrator, Procreate, or other layout tools. The Skill should provide typography direction, hierarchy, and placement, not pretend that text rendering is always stable inside generated images.

