import discord
from discord.ext import commands
import aiohttp
import io
import urllib.parse

# Setup bot permissions
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Replace with your actual token
TOKEN = "actual token"

@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def art(ctx, *, prompt: str):
    # Let user know we are processing
    loading_msg = await ctx.send(f"🎨 **Generating:** *{prompt}*...\nPlease wait...")

    try:
        # Encode prompt for URL (e.g. spaces -> %20)
        safe_prompt = urllib.parse.quote(prompt)
        api_url = f"https://image.pollinations.ai/prompt/{safe_prompt}"

        async with aiohttp.ClientSession() as session:
            async with session.get(api_url) as response:
                if response.status == 200:
                    image_data = await response.read()
                    
                    # Convert bytes to discord file
                    file = discord.File(io.BytesIO(image_data), filename="art.png")
                    
                    # Send final image and auto-delete after 5 mins
                    await ctx.send(f"✨ Result for {ctx.author.mention}", file=file, delete_after=300)
                    
                    # Cleanup loading msg
                    await loading_msg.delete()
                else:
                    await ctx.send(f"❌ API Error: {response.status}")

    except Exception as e:
        await ctx.send(f"❌ Error: {e}")

bot.run(TOKEN)