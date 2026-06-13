# Asset Opportunity Map

IPilot should not assume that users already know which asset type they need. After building the IP Consistency Profile, the Skill should recommend a focused set of asset opportunities based on the IP profile, brand context, audience, platform, and campaign goal.

The Asset Opportunity Map is a human-in-the-loop decision stage. It helps users choose what to produce before the Skill spends effort on detailed concepts or image generation.

## When to use

Use this stage when:

- the user says they want IP assets but does not specify exact asset types;
- the user asks for ideas, directions, or suggestions;
- the user provides an IP profile but has weak campaign planning;
- the requested platform or use case could support multiple asset formats;
- the request could be either digital promotional content or physical material;
- the Skill needs user confirmation before detailed concept generation.

Skip this stage only when the user clearly requests a specific asset type and wants immediate generation.

## Material type confirmation first

If the user has not clearly selected a material type, IPilot should first present a **Material Type Confirmation Menu**. The menu should include practical options such as sticker pack, meme pack, IP birthday visual, holiday greeting card, campaign poster, platform social post, physical sticker sheet, badge, acrylic stand, or multi-asset campaign pack.

After the user confirms the material type, generate detailed concepts. If the user explicitly authorizes IPilot to choose, select the safest high-priority option and state the choice.

## Asset categories

### 1. Identity assets

Use when the IP needs clearer recognition or introduction.

Examples:

- IP introduction card
- mascot profile poster
- avatar or profile image
- brand banner
- visual identity reference sheet
- signature pose set

### 2. Community assets

Use when the goal is social interaction, group chat, or community participation.

Examples:

- reaction sticker pack
- chat emoji pack
- comment reply images
- community challenge cards
- welcome stickers
- contributor or fan badges

### 3. Meme and humor assets

Use when the brand allows humor and wants shareable content.

Examples:

- meme concept pack
- reaction meme templates
- four-panel comic concepts
- relatable pain-point memes
- seasonal meme pack
- platform-native joke cards

### 4. Campaign and conversion assets

Use when the user has an event, product launch, promotion, sign-up, release, or public announcement.

Examples:

- campaign poster concept
- event announcement visual
- launch countdown cards
- product feature cards
- call-to-action card
- coupon or reward visual
- social media cover image

### 5. Occasion-based assets

Use when the asset is tied to an IP birthday, holiday, festival, anniversary, seasonal moment, milestone, or community ritual.

Examples:

- IP birthday key visual
- birthday sticker mini-pack
- birthday countdown series
- holiday greeting card
- festival poster
- anniversary visual
- seasonal campaign card
- milestone celebration card
- year-end thank-you card

### 6. Educational and explanatory assets

Use when the IP represents a learning project, technical community, course, science communicator, or knowledge brand.

Examples:

- concept explainer card
- learning progress sticker
- tutorial thumbnail
- error-state reaction image
- glossary card
- step-by-step visual card

### 7. Retention and lifecycle assets

Use when the brand needs recurring content rather than one-time posts.

Examples:

- weekly mood sticker
- milestone celebration card
- seasonal festival pack
- anniversary badge
- user achievement sticker
- release note mascot image

### 8. Platform-native digital assets

Use when the platform strongly shapes the output format.

Examples:

- WeChat sticker set
- Xiaohongshu cover card
- Bilibili dynamic image
- GitHub README mascot banner
- Discord / Telegram sticker pack
- Douyin short-video cover
- X / Twitter announcement card
- Instagram story card

### 9. Physical and tangible materials

Use when the user wants offline distribution, merch, event materials, or physical brand touchpoints.

Examples:

- sticker sheet
- badge / pin concept
- acrylic standee
- keychain
- tote bag graphic
- T-shirt graphic
- postcard or thank-you card
- package insert
- flyer / handout
- booth poster
- coupon card
- event standee

## Recommendation format

Output 5-8 recommended asset opportunities unless the user asks for more.

```markdown
# Asset Opportunity Map

## Recommended Asset Opportunities

| Option | Asset Type | Route | Goal | Why It Fits This IP | Creative Angle | Platform / Physical / Occasion Fit | Risk Level | Priority |
|---|---|---|---|---|---|---|---|---|
| A |  | digital / physical / hybrid |  |  |  |  | Low / Medium / High | High / Medium / Low |

## Recommended Production Path

1. Start with: [asset type]
2. Then expand into: [asset type]
3. Save for later: [asset type]

## Confirmation Needed

Please choose one of these options:

- A: [asset type]
- B: [asset type]
- C: [asset type]
- Let IPilot choose the safest and most useful option.
```

## Recommendation rules

Prefer asset types that are:

- useful for the user's stated platform;
- compatible with the IP's fixed visual features;
- compatible with the IP's personality and humor style;
- safe for the target audience;
- easy to revise;
- repeatable as a series;
- feasible for image generation or design production.

Avoid recommending asset types that:

- require details the user has not provided;
- rely on text-heavy image rendering unless the user accepts separate caption layers;
- push the IP into forbidden changes;
- create avoidable brand safety risk;
- depend on copyrighted-character imitation.

## Human confirmation rule

After presenting the Asset Opportunity Map, pause for user confirmation before generating detailed concepts, unless the user has explicitly asked IPilot to choose and proceed.

If the chosen option is a digital promotional asset and the target platform is missing, ask for the target platform before detailed concept generation.

If the chosen option is a physical material and the audience orientation is missing, ask for the audience style, distribution context, and physical usage scenario before detailed concept generation.

If the chosen option is an occasion-based asset and the occasion type, date/window, output format, or platform is missing, ask for those details before detailed concept generation.

If the user asks for a recommendation, choose the safest high-priority option and explain why briefly.

