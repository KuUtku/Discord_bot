import discord
from discord.ext import commands
import random
import os
import glob 

# Bot prefix'i (örnek: !ping yazarsan çalışır)
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# Bot hazır olduğunda çalışır
@bot.event
async def on_ready():
    print(f'✅ Bot giriş yaptı: {bot.user}')

# Basit bir komut: !ping
@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

# Argüman alan komut: !selam Ahmet
@bot.command()
async def selam(ctx, isim: str = "kullanıcı"):
    await ctx.send(f"Merhaba {isim}! 👋")

# Hata yakalama (isteğe bağlı)
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"❌ Hata oluştu: {error}")

#Mem Gönderme
@bot.command()
async def mem(ctx):
    images = glob.glob('images/*')
    if not images:
        await ctx.send("❌ Mem bulunamadı.")
        return
    path = random.choice(images)
    await ctx.send(file=discord.File(path))

#
@bot.command()
async def temiz(ctx):
    await ctx.send(f"Çevre kirliliği, doğal kaynakların yanlış kullanımı ve atıkların kontrolsüz bir şekilde çevreye bırakılması sonucu oluşan ciddi bir sorundur. Bu kirliliğin azaltılmasında geri dönüşüm önemli bir rol oynar. Kâğıt, plastik, cam ve metal gibi materyallerin yeniden işlenmesi hem doğayı korur hem de enerji tasarrufu sağlar. Geri dönüşüme destek vererek daha temiz, sağlıklı ve sürdürülebilir bir çevre oluşturmak mümkündür.")

bot.run("TOKEN")
