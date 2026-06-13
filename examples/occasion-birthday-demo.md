# Example: Occasion-Based IP Birthday Asset

This example demonstrates how IPilot handles an occasion-based asset when the user wants an IP birthday visual but has not yet decided the exact production format.

## User request

> Tensor Cat's birthday is coming. Help me make birthday materials, but I am not sure whether we should make a poster, stickers, or a small campaign series.

## Step 1 - Material type confirmation

IPilot should not immediately generate images. It should first output a menu.

| Option | Material Type | Route | Best For | Why It Fits Tensor Cat | Required Next Info | Priority |
|---|---|---|---|---|---|---|
| A | IP birthday key visual | occasion / digital | main announcement | Gives the IP a ceremonial anchor image | platform and date | High |
| B | Birthday sticker mini-pack | occasion / community | WeChat group interaction | Fits Tensor Cat's expressive and anxious personality | humor boundary | High |
| C | Birthday countdown series | occasion / digital | multi-day campaign | Builds anticipation before the birthday | publishing schedule | Medium |
| D | Birthday thank-you card | occasion / digital | post-event retention | Reinforces community warmth | audience and copy | Medium |
| E | Physical birthday postcard | occasion / physical | offline event giveaway | Useful if the club has an in-person meetup | audience and print constraints | Low |

Confirmation prompt:

> Which option should we produce first? A, B, C, D, E, or should IPilot combine A + B into a small birthday asset pack?

## Step 2 - User confirms A + B

The Skill now generates detailed concepts.

## IP birthday key visual concept

- Asset Type: IP birthday key visual
- Platform: WeChat group poster and Bilibili dynamic image
- Scene: Tensor Cat stands beside a small birthday cake shaped like a neural network node graph.
- IP Action: holding a tiny sparkler in one paw and a laptop in the other.
- Facial Expression: proud but slightly nervous.
- Caption: Happy Birthday, Tensor Cat! 今天也在认真陪你学 AI.
- Visual Prompt: Create a clean vector social card featuring Tensor Cat, a white mechanical cat mascot with round glasses, a blue hoodie, glowing green eyes, and a laptop-shaped backpack. Tensor Cat stands beside a small birthday cake decorated like a neural-network node graph, holding a tiny sparkler and looking proud but slightly nervous. Use a warm campus technology community atmosphere, blue and neon green accent colors, cute but professional style. Preserve the character's round glasses, blue hoodie, glowing green eyes, and laptop-shaped backpack. Avoid famous robot cat resemblance, politics, vulgarity, and unrelated characters. Keep text as a separate design layer.
- IP Consistency Notes: preserves species, accessories, color logic, and personality.
- Safety Notes: low risk; no offensive or sensitive content.

## Birthday sticker mini-pack

| Sticker | Emotion | Action | Caption | Safety Note |
|---|---|---|---|---|
| 1 | proud | holding cake | 今天我过生日，也顺便 debug 你的人生 | mild self-deprecation; safe |
| 2 | anxious | hiding behind laptop | 别催太大声，我还没 compile 好 | safe technical joke |
| 3 | touched | holding fan letters | 谢谢你陪我学到现在 | warm and safe |
| 4 | energetic | raising sparkler | 今晚 loss 也要降! | safe community joke |
| 5 | sleepy | hugging cake | 生日愿望: 少一点 bug | safe and platform-friendly |

## Confirmation before image generation

IPilot should ask:

> Do you want me to generate the birthday key visual now, or first polish the prompts and captions?



