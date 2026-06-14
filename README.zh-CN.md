<p align="center">
  <img alt="IPilot" src="https://img.shields.io/badge/IPilot-IP%20Mascot%20Workflow-6e41e2?style=for-the-badge&logo=robot&logoColor=white">
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.zh-CN.md">中文</a>
</p>

# IPilot

面向 Agent Skill 生态的 human-in-the-loop IP 吉祥物资产生产工作流。

IPilot 适合已经拥有 IP 形象、品牌角色、吉祥物或头像角色的团队。它的重点不是“从零生成一个角色”，而是先保护已有角色的视觉语法，再稳定延展出表情包、梗图、活动视觉、平台社交图、节日视觉、线下物料概念和图像生成提示词。

## 如何安装

克隆仓库：

```bash
git clone https://github.com/LewisHinton/IPilot.git
cd IPilot
```

Codex CLI / Codex 编辑器 / Codex Desktop：

```bash
cp -R . ~/.codex/skills/ipilot
```

Windows PowerShell：

```powershell
Copy-Item -Recurse . "$env:USERPROFILE\.codex\skills\ipilot" -Force
```

Claude Code 或其他兼容 `SKILL.md` 的工具：

1. 保持 `SKILL.md` 位于 `IPilot` 文件夹根目录。
2. 保留 `references/`、`templates/`、`examples/`、`sample_briefs/`、`scripts/`。
3. 按你的工具要求导入、复制、软链接或上传整个文件夹。
4. 如果工具要求 zip 包，打包文件夹内容时不要改变目录结构。

没有 Skill 运行时也可以使用：

1. 打开 `SKILL.md`。
2. 按任务加载相关 `references/` 文件。
3. 让你的模型按 IPilot 工作流处理当前吉祥物项目。

## Demo GIF

![IPilot demo](assets/demo/ipilot-demo.gif)

## 快速开始

```text
@ipilot
我已经有一个吉祥物参考图。请基于它创作 6 个表情包。
保持角色一致，并在生成图片前先问我确认。
```

IPilot 会先识别参考图角色特征，提取固定视觉锚点，确认素材方向，再输出概念、文案、图像提示词、负面约束和安全检查。

## 为什么值得 Star

很多团队都有一个已经被用户认识的 IP 角色，但每次新提示词都会让角色慢慢变形：颜色变了、线条变了、比例变了、道具丢了、语气也跑偏了。

IPilot 用一套可重复的流程解决这个问题：

- 先识别参考图的权威性，而不是把多张图混在一起平均；
- 区分固定特征、可变特征、禁止变化和安全约束；
- 先确认素材类型，再进入详细创作；
- 适配平台、节日、受众和线下物料场景；
- 在关键节点让用户确认，不直接跳到图像生成；
- 分离文案、图像提示词、排版建议、安全说明和交付说明。

## 核心流程

```text
IP 信息收集
-> 参考图角色分析
-> IP 一致性档案
-> 深度视觉一致性档案
-> 素材类型路由
-> 用户确认门
-> 资产概念
-> 安全与一致性检查
-> 图像生成或提示词交付
-> 生成后审查
-> 文字排版与生产交付说明
```

## 默认 human-in-the-loop

- Gate 0：素材类型确认。
- Gate 1：资产方向确认。
- Gate 2：图像生成前的概念确认。
- Gate 3：生成后接受、微调或重生成确认。

## 生态支持

| 环境 | 使用方式 |
|---|---|
| Codex CLI | 复制到 `~/.codex/skills/ipilot` |
| Codex 编辑器 / Desktop | 复制到 Codex skills 目录，或作为 workspace Skill 使用 |
| Claude Code 等 CLI Agent | 导入、复制、软链接，或让 agent 指向该文件夹 |
| Claude app / web Skill flows | 在支持时上传或导入 zip Skill 文件夹 |
| 其他兼容 `SKILL.md` 的 Agent | 保持目录结构，让 Agent 读取 `SKILL.md` |
| 没有 Skill 运行时 | 手动加载 `SKILL.md` 和相关 `references/` |

## 适用场景

| 场景 | 常见输出 |
|---|---|
| 品牌营销 | 活动卡片、发布视觉、社交封面 |
| 社群运营 | 表情包、欢迎贴纸、贡献者徽章 |
| 教育与校园组织 | 课程表情包、考试季卡片、讲解缩略图 |
| 开源项目 | 吉祥物贴纸、README 横幅、版本发布庆祝图 |
| 活动与会议 | 展位海报、徽章、传单、签到贴纸 |
| 线下物料 | 贴纸、钥匙扣、明信片、包装插卡 |
| 节日与纪念日 | IP 生日图、节日祝福、周年卡片 |
| 一致性审查 | 生成图 QA、参考图冲突分析 |

## 校验

```bash
python scripts/validate_ip_brief.py sample_briefs/tensor-cat-brief.md
python scripts/check_release_readiness.py
```

## 安全边界

IPilot 不应生成或推荐仇恨、歧视、骚扰、性化吉祥物、政治劝服、侵权模仿、或用户明确禁止的内容。

## 状态

当前版本：**v0.8 release candidate**。
