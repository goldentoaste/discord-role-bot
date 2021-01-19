@bot.command(name="assignrole", pass_context=True)
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
