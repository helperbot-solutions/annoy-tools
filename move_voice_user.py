#!/usr/bin/env python3
import discord
import lib.params as pm
import asyncio
import time
import sys
import os

BOT_TOKEN = os.environ['DISCORDBOT']

client = discord.Client()


@client.event
async def on_ready():
    print('\n')
    print('------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


def check_correct_input(input_message, func, *func_args, **func_kwargs):
    print()
    correct_input = False
    while not correct_input:
        print(input_message)
        try:
            return_val = func(*func_args, **func_kwargs)
            if return_val is not None:
                correct_input = True
            else:
                raise ValueError("Channel ID not found")
        except Exception as e:
            print("\nERROR: {}".format(str(sys.exc_info())))
            time.sleep(0.5)
    return return_val


async def move_user():
    await client.wait_until_ready()

    def get_channel():
        global client
        channel = client.get_channel(input(" []: "))
        print("Voice Channel: {}".format(channel))
        return channel
    channel = check_correct_input("Please input the channel id:", get_channel)

    def get_member_id(channel):
        member = channel.server.get_member(input(" []: "))
        print("Member: {}".format(member))
        return member
    member = check_correct_input("Please input the user id:", get_member_id,
                                 channel)

    while not client.is_closed:
        await client.move_member(member, channel)
        print("Moved {}, to voice channel {}".format(member.nick,
                                                     channel.name))
        await asyncio.sleep(1)

client.loop.create_task(move_user())
client.run(BOT_TOKEN)
