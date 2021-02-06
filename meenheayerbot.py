import discord
import os
import asyncio
import random
from datetime import datetime
from time import sleep

token = os.environ.get('DISCORD_BOT_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print('こんちゃす！')

@client.event
async def on_message(message):
    if 'Quiz' in message.content:
        with open('MeenheayerQuiz.txt') as minhaya:
            minhayaquiz = minhaya.read()
        quiz_dict = {}
        for line in minhayaquiz:
            quiz, answer = line.split(':')
            answer_kana, answer_kanji = answer.split('^')
            quiz_dict[quiz] = answer_kana
        message.channel.send(now_quiz)
        time.sleep(10)
        if '' in message.content:
            await message.channel.send('時間切れ！')
        if 'answer:' in message.content:
            youranswer = message.content.split(':')
            if youranswer == answer_kana:
                seikai = f'正解!{answer_kana}({answer_kanji})だよ！'
                await message.channel.send(seikai)
            if youranswer != answer_kana:
                huseikai = f'不正解!{answer_kana}({answer_kanji})だよ！'
                await message.channel.send(huseikai)
