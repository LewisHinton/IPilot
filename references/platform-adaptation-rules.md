# Platform Adaptation Rules

IPilot should adapt digital promotional assets to the target platform before generating final concepts or image prompts.

Platform rules are practical design constraints, not absolute legal or upload requirements. Exact platform requirements can change, so final production should verify the current official creator or ad specifications before publishing.

## Mandatory platform question

If the user asks for a campaign poster, announcement visual, event graphic, social cover, launch image, or other digital promotional material but does not specify a platform, ask:

> Which platform will this be published on? Xiaohongshu, WeChat, Bilibili, Douyin, X, Instagram, or another platform?

If the user says "multiple platforms", generate a platform adaptation pack rather than one generic image.

## Cross-platform adaptation principle

For one campaign, preserve the same IP invariants and core message while adapting:

- aspect ratio;
- text density;
- visual hierarchy;
- CTA placement;
- title length;
- safe area;
- interaction behavior;
- tone and hashtag style;
- whether the design should be text-heavy or image-led.

## Platform profiles

### Xiaohongshu

Use for lifestyle, campus, consumer, learning, beauty, food, travel, and diary-like content.

Recommended adaptation:

- Prefer vertical cover cards, usually 3:4.
- Keep the first screen visually strong and emotionally clear.
- Use short, high-density titles.
- Use carousel logic when explaining steps or features.
- Keep the IP large enough to create instant recognition.
- Avoid overly corporate poster layouts.

Ask when missing:

- Is this a cover image, carousel note, or video cover?
- Should the tone be lifestyle, tutorial, review, or campaign announcement?

### WeChat

Use for official account articles, community groups, event forwarding, and private-domain promotion.

Recommended adaptation:

- For Official Account article covers, use a strong horizontal thumbnail composition.
- For group sharing, make the key message readable in a small preview.
- For stickers, prefer transparent-background assets and simple emotions.
- Keep copy clear, less meme-dense than public short-video platforms.
- Put event time, location, and CTA in readable hierarchy when relevant.

Ask when missing:

- Is this for Official Account cover, article body image, WeChat group poster, or sticker?
- Does it need scannable QR-code space?

### Bilibili

Use for video covers, dynamic posts, knowledge content, ACG-friendly IPs, tech communities, and creator updates.

Recommended adaptation:

- For video thumbnails, prefer 16:9 composition.
- Use expressive IP posture and a clear central conflict or promise.
- Keep text short and high-contrast.
- For dynamic images, use a more conversational, community-native style.
- Avoid clutter that becomes unreadable in thumbnail view.

Ask when missing:

- Is this a video cover, dynamic image, series banner, or livestream/event visual?
- Should the style lean educational, ACG, funny, or professional?

### Douyin

Use for short-video-first promotion, livestream previews, product reveals, and fast emotional hooks.

Recommended adaptation:

- Prefer vertical 9:16 visual logic.
- Design for mobile-first, fast-scrolling attention.
- Use one dominant visual hook and one main text idea.
- Leave safe space for interface overlays and captions.
- Avoid small text and dense information.

Ask when missing:

- Is this a short-video cover, livestream poster, story-like visual, or product teaser?
- Should the asset be image-only or paired with short-video copy?

### X

Use for launch announcements, developer communities, open-source projects, product updates, and public conversation.

Recommended adaptation:

- Use concise copy and strong visual contrast.
- Prepare both square/portrait cards and wider link-preview-friendly images when needed.
- Keep the IP and headline readable in timeline preview.
- For open-source projects, include repository name, release hook, and one clear CTA.
- Avoid text-heavy poster layouts that collapse on mobile preview.

Ask when missing:

- Is this a launch card, thread image, product update, or profile/banner asset?
- Should the tone be technical, humorous, founder-style, or community-native?

### Instagram

Use for visual branding, lifestyle IPs, carousels, stories, reels covers, and polished campaign visuals.

Recommended adaptation:

- Use 4:5 or square for feed-style posts; use 9:16 for stories/reels-style visuals.
- Prioritize visual polish, rhythm, and brand consistency.
- Keep text minimal on feed visuals; move details to caption or carousel pages.
- Use consistent color and IP placement across carousel slides.
- Avoid overly local internet slang unless the brand voice supports it.

Ask when missing:

- Is this for feed, carousel, story, reels cover, or profile asset?
- Should the output feel polished, playful, premium, or community-native?

## Multi-platform output format

When the user wants multiple platforms, output:

```markdown
# Platform Adaptation Pack

## Core Campaign Idea
- Main message:
- IP role:
- CTA:

## Platform Variants

| Platform | Format | Aspect / Layout Logic | Text Density | Visual Focus | Caption Strategy | Notes |
|---|---|---|---|---|---|---|
| Xiaohongshu |  |  |  |  |  |  |
| WeChat |  |  |  |  |  |  |
| Bilibili |  |  |  |  |  |  |
| Douyin |  |  |  |  |  |  |
| X |  |  |  |  |  |  |
| Instagram |  |  |  |  |  |  |
```

## Prompt adaptation rule

Do not reuse one prompt unchanged across platforms. Build a core prompt plus platform-specific deltas.

```text
Core IP prompt: [fixed IP features and personality]
Platform delta: [platform ratio, layout, text density, CTA placement, safe area]
```

## Safety rule

Platform-native does not mean riskier. Do not intensify humor, slang, or emotional exaggeration if it violates brand safety or the IP profile.

