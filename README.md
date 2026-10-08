# The Dice Code

A Discord bot for rolling dice, written in Python. This bot allows users to perform various dice rolls (including D&D style rolls like d20, d12, etc.) directly in Discord.

## Features

- Standard dice rolls (`/roll [number]d[die]`)
- Rolls with modifiers (`/roll [number]d[die] [+/-modifier]`)
- Advantage rolls (`/+ad roll d[die]`)
- Disadvantage rolls (`/-dad roll d[die]`)
- Custom insults for invalid rolls!

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/The-dice-code.git
   cd The-dice-code
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your Discord Bot Token:
   - Open `Codes/main.py`
   - Replace the empty string in `client.run('')` at the end of the file with your actual Discord Bot Token.

## Usage

Run the bot using:
```bash
python Codes/main.py
```

Invite your bot to your Discord server and try rolling some dice!
