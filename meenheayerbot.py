import discord
import os
import asyncio
import random
import time
import tracemalloc
from datetime import datetime

token = os.environ.get('DISCORD_BOT_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print('こんちゃす！')
    
with open('MeenheayerQuiz.txt') as f:
    quiz_dict = {line.split(':')[0]: line.split('^')[-1] for line in f.readlines()}

@client.event
async def on_message(message):
    if 'Quiz' in message.content:
        chosen = random.choice(list(quiz_dict))
        await message.channel.send(chosen)
        answer_kana = quiz_dict[chosen][0]
        answer_kanji = quiz_dict[chosen][1]
        count = 0
        while count <= 20:
            try:
                def check(m):
                    return m.channel.id == message.channel.id and m.content.startswith("answer")
                answer_message = await client.wait_for("message", check=check, timeout=20)
                answer, youranswer = m.content.split()
                if youranswer == answer_kana:
                    seikai = f'正解!{answer_kana}({answer_kanji})だよ！'
                    await message.channel.send(seikai)
                elif youranswer != answer_kana:
                    huseikai = f'不正解!{answer_kana}({answer_kanji})だよ！'
                    await message.channel.send(huseikai)
            except asyncio.TimeoutError:
                    await message.channel.send('時間切れ!')
                 
client.run(token)              
