# User Tag Bot

A Telegram bot for tagging users in groups with various message formats.

## Features

- Tag all users in a group
- Good morning/night tagging
- Hello tagging
- Shayari tagging
- Admin-only commands
- Rate limiting to prevent spam

## Commands

- `/start` - Show welcome message
- `/mention` or `/all` - Tag all users
- `/tagall` - General tagging
- `/gntag` or `/tagmember` - Good night tagging
- `/gmtag` - Good morning tagging
- `/gn` - Good night tagging
- `/hi` - Hello tagging
- `/shayari` - Shayari tagging
- `/alloff` - Stop tagging
- `/gmstop` or `/gnstop` or `/cancle` - Stop tagging

## Deployment

### Railway Deployment

1. Fork this repository
2. Create a new project on Railway
3. Connect your GitHub repository
4. Add the following environment variables:
   - `API_ID` - Your Telegram API ID
   - `API_HASH` - Your Telegram API Hash
   - `BOT_TOKEN` - Your bot token from @BotFather
   - `BOT_NAME` - Your bot's name

### Local Development

1. Clone the repository
2. Create a `.env` file with the required environment variables
3. Install dependencies: `pip install -r requirements.txt`
4. Run the bot: `python main.py`

## Security

- All sensitive credentials are stored as environment variables
- Admin-only commands for tagging
- Rate limiting to prevent spam
- Session files are ignored by git

## License

MIT License 