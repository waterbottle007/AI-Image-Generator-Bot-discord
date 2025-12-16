AI Art Generator Bot

A classic Discord bot that generates AI artwork from text prompts using the **Pollinations API**. Built with **Python** and **Discord.py** to demonstrate asynchronous API handling.
## Made for fun as a small first project
## 🚀 Features
- **Real-time Generation:** Converts text prompts (e.g., "Cyberpunk city") into images instantly.
- **Asynchronous Processing:** Uses `aiohttp` to handle non-blocking requests, ensuring the bot stays responsive.
- **Auto-Cleanup:** Automatically deletes generated images from chat after 5 minutes to keep the server clean.
- **Memory Optimization:** Streams images directly from RAM (`io.BytesIO`) without creating temporary files on the disk.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Libraries:** `discord.py`, `aiohttp`
- **API:** Pollinations.ai (REST)
