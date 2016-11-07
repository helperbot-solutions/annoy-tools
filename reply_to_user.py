#!/usr/bin/env python3
import discord
import asyncio
import random
import os

BOT_TOKEN = os.environ['DISCORDBOT']

client = discord.Client()


async def presence_set():
    await client.wait_until_ready()
    await client.change_presence(game=discord.Game
                                 (name="with the Discord API"))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    msg = ('Howdy <@{}>. You said: "{}". Here is your profile image: \n{}'
           .format(str(message.author.id), message.content,
                   str(message.author.avatar_url)))
    mes = await client.send_message(message.channel, msg)


client.loop.create_task(presence_set())
client.run(BOT_TOKEN)
