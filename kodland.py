import discord
import random
import os
import webbrowser
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Бот {client.user} включен.')
@client.event
async def on_message(message):
    if message.content == ('Ишак') or message.content == ('ишак') or message.content == ('Ишак ты тут?'):
        await message.channel.send("Я тут!")
    else:
        ()
    if message.content.startswith('ты топ!') or message.content.startswith('Ты топ!'):
        await message.channel.send("Спасибо брат!")
    else:
        ()
    if message.content.startswith('Как дела?'):
        await message.channel.send("супер!")
    else:
        ()
    if message.content == ("/ibot.spam"):
        await message.channel.send("Установите количество сообщений!(10,50,100,500,1000,5000,10000)")
        await message.channel.send("Далее,напишите сообщение так: /ibot.spam.10 . Вместо 10 может быть 50,100 и т.д")
    else:
        ()
    if message.content == ("Привет ишак") or message.content == ("Привет") or message.content == ("привет")  or message.content == ("привет ишак") or message.content == ("Ишак привет") or message.content == ("ишак привет"):
        await message.channel.send("Привет!") or message.channel.send("Приветик!")
    else:
        ()
    if message.content == ("Канал астры") or message.content == ("Канал Астры") or message.content == ("канал астры") or message.content == ("канал Астры"):
        await message.channel.send("[**?**] Канал называется Lolsaur, ссылка ниже!")
        await message.channel.send("[**?**] https://www.youtube.com/@lolsaur!")
    if message.content == ("Тг") or message.content == ("тг") or message.content == ("телега") or message.content == ("Телега"):
        await message.channel.send("[**?**] В этом тг-канале написано о стримах астры,почему их нет и т.д!")
        await message.channel.send("[**?**] https://t.me/lolsaurcommunity")
    else:
        ()
    if message.content == ("Скиньте айпи") or message.content == ("скиньте айпи") or message.content == ("Айпи") or message.content == ("айпи"):
        await message.channel.send("[**?**] На сервере нет никаких модов,только текстур паки,которые вы можете попросить у админов(При заходе скачиваются)")
        await message.channel.send("[**?**] Politrg.aternos.me")
    if message.content.startswith("Ишак кто твой создатель?"):
        await message.channel.send("Здраствуйте!Мой создатель - perritik.Этот бот написан на языке программирования Python.Совместно со школой программирования KODLAND!")
    else:
        ()
    if message.content == ("ibot.help"):
        await message.channel.send("***Список комманд:***")
        await message.channel.send("[**?**]Если вы напишете (Айпи) - Вам скинут айпи сервера. ")
        await message.channel.send("[**?**]Если вы напишете (Тг) - Вам скинут тг-канал Астры. ")
        await message.channel.send("[**?**]Если вы напишете (Канал астры) - Вам скинут ютуб-канал Астры.")
        await message.channel.send("[**?**]Если вы напишете (Так-же есть команды по типу: привет,ты топ! и другие.)")
        await message.channel.send("**По поводу идей для новых комманд, обращатся к** ***perrritik.***")
    else:
        ()
    if message.content == ("Зачем нужна экология?") or message.content == ("зачем нужна экология?"):
        await message.channel.send("***[?]Экология определённо нужна для того что бы зачитить нашу планету и позаботиться о ней.Да, не каждый думает об этом но если хотябы 1 страна возьмётся за это, и призовёт других думать о планете,то мы сплотимся и сделаем это!***")
    else:
        ()
    if message.content == ("Что такое экология?") or message.content == ("что такое экология?"):
        await message.channel.send("***[?]Эколо́гия (от др.-греч. οἶκος — жилище, местопребывание и λόγος — учение) — естественная наука (раздел биологии).***")
        await message.channel.send("***[?]В просторечии под экологией часто понимается состояние окружающей среды, а под экологическими проблемами — вопросы охраны окружающей среды от воздействия антропогенных факторов[2][3][4]. Экологизм — общественное движение за усиление мер охраны окружающей среды и за предотвращение разрушения среды обитания.***")
    else:
        ()
client.run("YOUR TOKEN")
