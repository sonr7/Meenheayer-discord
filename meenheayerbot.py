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
            if 'answer:' in message.content:
                answer, youranswer = message.content.split(':')
                if youranswer == answer_kana:
                    seikai = f'正解!{answer_kana}({answer_kanji})だよ！'
                    await message.channel.send(seikai)
                elif youranswer != answer_kana:
                    huseikai = f'不正解!{answer_kana}({answer_kanji})だよ！'
                    await message.channel.send(huseikai)
            elif '' in message.content:
                time.sleep(1)
                count += 1
                 
client.run(token)              
