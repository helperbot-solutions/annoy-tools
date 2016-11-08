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


async def youtube_video_link_give(check_words, video_link, message):
    if any(s in message.content.lower() for s in check_words):
        msg = ("Were you looking for this? " + video_link)
        await client.send_message(message.channel, msg)


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    # Send a link to the "Click Noice" video when the word 'noice' is mentioned
    youtube_link = "https://www.youtube.com/watch?v=3WAOxKOmR90"
    await youtube_video_link_give(('noice', 'nice', 'noiice', 'noicce'),
                                  youtube_link, message)

    # Send a link to the "Yeah Boi" video when the word 'yeah' or 'boi'/'boy'
    # is mentioned
    youtube_link = "https://www.youtube.com/watch?v=fvtQYsckLxk&t=1m5s"
    await youtube_video_link_give(('yeah', 'yeh', 'boi', 'boy'), youtube_link,
                                  message)

    # Send a link to the "Time to Stop" video when the word 'stop' or 'time' is
    # mentioned
    youtube_link = "https://www.youtube.com/watch?v=2k0SmqbBIpQ"
    await youtube_video_link_give(('stop',), youtube_link,
                                  message)


client.loop.create_task(presence_set())
client.run(BOT_TOKEN)
