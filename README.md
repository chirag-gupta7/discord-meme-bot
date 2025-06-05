# discord-meme-bot

# 🤖 Discord Meme Bot - Your Server's Comedy Companion!

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Discord.py](https://img.shields.io/badge/discord.py-2.0+-green.svg)](https://discordpy.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Bring endless laughter to your Discord server with our feature-packed meme bot! 🎭**

## 🌟 What Makes This Bot Special?

Hey there, Discord enthusiast! 👋 Are you tired of those awkward silent moments in your server? Does your community need a spark of humor? Well, you've just discovered your new best friend - a Discord Meme Bot that's about to transform your server into the most entertaining place on the internet!

![Bot Demo](screenshot1.png)
*Watch our bot in action - bringing smiles one meme at a time!*

## ✨ Features That'll Blow Your Mind

### 🎯 Core Meme Functions

#### 1. **Random Meme Generator** (`!meme`)
- **What it does**: Fetches random memes from popular subreddits
- **Why you'll love it**: Never runs out of fresh content!
- **How to use**: Simply type `!meme` and watch the magic happen
- **Pro tip**: Works great during those "dead chat" moments

![Random Meme Feature](screenshot2.png)
*Random memes keeping the chat alive 24/7*

#### 2. **Category-Specific Memes** (`!meme [category]`)
- **What it does**: Get memes from specific categories (programming, gaming, wholesome, etc.)
- **Available categories**: 
  - `programming` - For the code warriors 💻
  - `gaming` - Gamers unite! 🎮
  - `wholesome` - Feel-good content 🥰
  - `dank` - For the meme connoisseurs 😎
- **Usage**: `!meme programming` or `!meme gaming`

#### 3. **Meme of the Day** (`!motd`)
- **What it does**: Curates the best meme of the day
- **Special feature**: Updates daily with trending content
- **Perfect for**: Starting conversations and daily engagement

### 🛠️ Utility Functions

#### 4. **Meme Search** (`!search [keyword]`)
- **What it does**: Find memes based on specific keywords
- **Example**: `!search cats` finds all the cat memes your heart desires
- **Smart feature**: Uses advanced filtering to find the best matches

![Search Feature](screenshot3.png)
*Finding the perfect meme has never been easier*

#### 5. **Custom Meme Creation** (`!create`)
- **What it does**: Interactive meme creator with templates
- **Process**: Bot guides you through template selection and text addition
- **Templates include**: Drake format, Distracted Boyfriend, Woman Yelling at Cat, and more!

#### 6. **Meme Leaderboard** (`!leaderboard`)
- **What it does**: Shows who's the meme king/queen of your server
- **Tracks**: Most memes shared, highest rated memes, most active meme users
- **Competitive fun**: Adds gamification to your server

### 🎮 Interactive Features

#### 7. **Meme Rating System** (React with 👍/👎)
- **What it does**: Community-driven meme quality control
- **How it works**: Users react to rate memes, building a quality database
- **Benefit**: Better memes surface to the top over time

#### 8. **Daily Meme Challenge** (`!challenge`)
- **What it does**: Daily themed meme challenges for server members
- **Examples**: "Funniest Programming Bug", "Best Gaming Fail", etc.
- **Rewards**: Special roles and recognition for winners

![Daily Challenge](screenshot4.png)
*Daily challenges keeping your community engaged*

## 🚀 Quick Setup Guide

### Prerequisites
Before we dive in, make sure you have:
- Python 3.8 or higher 🐍
- A Discord account and server (obviously! 😄)
- Basic understanding of Discord bots (don't worry, we'll guide you!)

### Installation Steps

1. **Clone this awesome repository**
   ```bash
   git clone https://github.com/yourusername/discord-meme-bot.git
   cd discord-meme-bot
   ```

2. **Install dependencies** (the bot's superpowers!)
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your bot token**
   - Create a `.env` file in the project root
   - Add your Discord bot token:
     ```
     DISCORD_TOKEN=your_bot_token_here
     REDDIT_CLIENT_ID=your_reddit_client_id
     REDDIT_CLIENT_SECRET=your_reddit_client_secret
     ```

4. **Run the bot** and watch the magic unfold!
   ```bash
   python bot.py
   ```

![Setup Success](screenshot5.png)
*Successfully deployed and ready to meme!*

## 📖 Command Reference

| Command | Description | Example | Fun Factor |
|---------|-------------|---------|------------|
| `!meme` | Random meme | `!meme` | 🔥🔥🔥🔥🔥 |
| `!meme [category]` | Category-specific | `!meme programming` | 🔥🔥🔥🔥 |
| `!motd` | Meme of the day | `!motd` | 🔥🔥🔥🔥 |
| `!search [term]` | Search memes | `!search cats` | 🔥🔥🔥 |
| `!create` | Make custom meme | `!create` | 🔥🔥🔥🔥🔥 |
| `!leaderboard` | Top memers | `!leaderboard` | 🔥🔥🔥 |
| `!challenge` | Daily challenge | `!challenge` | 🔥🔥🔥🔥 |
| `!help` | Show all commands | `!help` | 🔥🔥 |

## 🎯 Pro Tips for Maximum Fun

### For Server Admins:
- **Set up dedicated channels**: Create `#memes` and `#meme-challenges` for organized fun
- **Configure permissions**: Ensure the bot has necessary permissions (Send Messages, Attach Files, Add Reactions)
- **Daily routine**: Use `!motd` in your morning announcements

### For Users:
- **Rate memes responsibly**: Your ratings help improve everyone's experience
- **Participate in challenges**: Great way to earn recognition and have fun
- **Use categories**: Specific categories often have higher quality, targeted humor

## 🔧 Configuration Options

The bot comes with several customizable options:

```python
# Bot settings you can modify
MEME_COOLDOWN = 30  # Seconds between meme requests per user
MAX_MEMES_PER_HOUR = 10  # Prevent spam
ENABLE_NSFW = False  # Set to True for NSFW channels
AUTO_REACTIONS = True  # Bot auto-adds rating reactions
```

## 🤝 Contributing to the Fun

Want to make this bot even more awesome? We'd love your help!

### Ways to Contribute:
- **Add new meme sources**: Know a great meme API? Share it!
- **Improve templates**: Design new meme templates
- **Bug fixes**: Found something wonky? Fix it and submit a PR!
- **Feature requests**: Got a cool idea? Open an issue!

### Development Setup:
```bash
# Fork the repo, then:
git clone https://github.com/yourusername/discord-meme-bot.git
cd discord-meme-bot
pip install -r requirements-dev.txt
# Make your changes and submit a PR!
```

## 🐛 Troubleshooting

### Common Issues & Solutions:

**Bot not responding?**
- Check if the bot is online in your server
- Verify bot permissions (Send Messages, Attach Files)
- Ensure your command prefix is correct (`!` by default)

**Memes not loading?**
- Check your internet connection
- Verify Reddit API credentials in `.env`
- Some subreddits might be temporarily unavailable

**Rate limiting issues?**
- The bot has built-in cooldowns to prevent spam
- Wait a moment between commands
- Check if you've hit the hourly limit

## 📊 Bot Statistics

Our bot is actively bringing joy to servers worldwide!

![Bot Stats](screenshot6.png)
*Current usage statistics and happy servers*

## 🎉 Success Stories

> *"This bot turned our dead server into the most active one in our community! The daily challenges are absolutely brilliant!"* - Server Admin, GamingHub Discord

> *"Finally, a meme bot that actually understands what's funny. The search feature is a game-changer!"* - Regular User, CodeCommunity

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. Feel free to use, modify, and distribute!

## 🙏 Acknowledgments

- **Discord.py community** for the amazing library
- **Reddit API** for endless meme content
- **All contributors** who make this project awesome
- **You** for choosing our bot! 🎉

## 📞 Support & Community

Need help or want to chat about memes? Join our community!

- **Discord Server**: [Join our support server](discord-invite-link)
- **GitHub Issues**: Report bugs or request features
- **Documentation**: Full API docs available in `/docs`

---

**Made with ❤️ and lots of ☕ by meme enthusiasts, for meme enthusiasts!**

*Remember: Life's too short for bad memes. Let our bot handle the good ones! 😄*

