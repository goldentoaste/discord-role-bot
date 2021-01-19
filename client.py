# bot.py
import os
import discord
from discord import *
import re
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import EmojiConverter

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
intent = Intents.all()

bot = commands.Bot(command_prefix="!", intent=intent)
emojiConverter = EmojiConverter()
events = dict()


@bot.command(name="testing", pass_context=True)
async def assign_roles(context, arg: str):
    print("detected command")
    print(arg)
    await context.send(":weary:")


# @bot.command(name="assignrole", pass_context=True)
# async def assign_roles(context, arg: str):

#     args = arg.split("|")
#     out = ""
#     current_event = dict()

#     for role in args:

#         if not re.match(
#             "(:\w+:)\:\w+",
#             role,
#         ):
#             await context.send("bad formatting! do: emote+role|emote+role|...")
#             return
#         temp = role.split("+")
#         current_event[temp[0]] = temp[1]
#         out += f"React {temp[0]} for role: {temp[1]}\n"
#     out = out[:-1]
#     m = await context.send(out)
#     for emoji in current_event.keys():
#         await m.add_reaction(emoji)

#     events[m.id] = current_event


@bot.event
async def on_message(message: Message):
    if message.author.bot:
        return

    if message.content.startswith("!assignroles "):
        args = message.content.removeprefix("!assignroles ").split("|")
        out = ""
        current_event = dict()

        for role in args:
            temp = role.split("+")

            current_event[temp[0]] = temp[1]
            out += f"React {temp[0]} for role: {temp[1]}\n"
        out = out[:-1]
        m = await message.channel.send(out)
        for emoji in current_event.keys():
            await m.add_reaction(emoji)

        events[m.id] = current_event


@bot.event
async def on_ready():
    print("bot is ready!")


@bot.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return
    print("entering adding")
    id = reaction.message.id
    if id in events.keys():
        print(reaction.emoji, list(events[id].keys()))
        if str(reaction.emoji) in events[id].keys():
            role = discord.utils.get(user.guild.roles, name=events[id][reaction.emoji])
            print(role)
            await user.add_roles(role)


@bot.event
async def on_raw_reaction_remove(payload: RawReactionActionEvent):
    print("entering removing")

    guild = bot.get_guild(int(payload.guild_id))

    member = await guild.fetch_member(int(payload.user_id))
    if member.bot:
        return

    id = payload.message_id
    print(id, list(events.keys()))

    if id in events.keys():
        print(payload.emoji, list(events[id].keys()))
        if str(payload.emoji) in events[id].keys():
            print("stuff")
            role = discord.utils.get(guild.roles, name=events[id][str(payload.emoji)])
            print(role)
            await member.remove_roles(role)


bot.run(TOKEN)
#!assignrole :robot:+bot tuner|:hammer:+Engg nerds|:computer:+Comp Sci