import discord
import random
from discord.ext import commands
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="p!",
                   guild_subscriptions=True,
                   intents=intents, help_command=None)  #change prefix if you want
from keep_alive import keep_alive  #import the code from your file
token = "Nzk1NTgzNDE1OTYwNjAwNTk2.X_Leyw.R7Phk4dJV4YN3ZLuzpnMWeClqZ8"  #from your discord developer platform
OWNER = 739444667782791178
async def get_help_embed():
    em = discord.Embed(title="help command", description="", color=discord.Color.green())
    em.description += f"**1. {bot.command_prefix}help #list every command and music command\n"
    em.description += f"**2. {bot.command_prefix}hi #hi user\n"
    em.description += f"3. {bot.command_prefix}create #create welcome and goodbye channel\n"
    em.description += f"4. {bot.command_prefix}invite #get bot invite\n"
    em.description += f"5. {bot.command_prefix}credit #get person who teach me how to code and creator of the bot\n"
    em.description += f"6. {bot.command_prefix}template #bot repost will update if top.gg add this bot are els it will take long\n"
    em.description += f"7. {bot.command_prefix}logo #get user logo\n"
    em.description += f"8. {bot.command_prefix}userinfo #get user info\n"
    em.description += f"9. {bot.command_prefix}serverinfo #get server info\n"
    em.description += f"10. {bot.command_prefix}panda #just for fun\n"
    em.description += f"-----moderation command----\n"
    em.description += f"11. {bot.command_prefix}ban #get user ban\n"
    em.description += f"12. {bot.command_prefix}unban #get user unban\n"
    em.description += f"13. {bot.command_prefix}kick #get user kick\n"
    em.description += f"14. {bot.command_prefix}mute #get user mute i think it does not work maybe it work\n"
    em.description += f"15. {bot.command_prefix}unmute #get user unmute\n"
    em.description += f"16. {bot.command_prefix}clear #clear how many you want\n"
    em.description += f"----bot info----\n"
    em.description += f"17. {bot.command_prefix}debug #Which the bot connected in 0 are 1 channels\n"
    em.description += f"18. {bot.command_prefix}ping #pong get the ping of the bot\n"
    em.description += f"----music command----\n"
    em.description += f"19. {bot.command_prefix}play #play on youtube spotify and other\n"
    em.description += f"20. {bot.command_prefix}pause #pause the music\n"
    em.description += f"21. {bot.command_prefix}resume #resume the music\n"
    em.description += f"22. {bot.command_prefix}loop #music will be loop\n"
    em.description += f"23. {bot.command_prefix}nowplaying #it say what song now play btw you can use the command like this p!np it works to\n"
    em.description += f"24. {bot.command_prefix}stop #stop the music\n"
    em.description += f"26. {bot.command_prefix}Skip #Skip the music\n"
    em.description += f"27. {bot.command_prefix}search #search the music on yt\n"
    em.description += f"28. {bot.command_prefix}queue #get server queue  \n"
    em.description += f"29. {bot.command_prefix}volume #to set the volume \n"
    em.description += f"30. {bot.command_prefix}clear-queue #get clear queue on the server\n"
    em.description += f"31. {bot.command_prefix}filter #change song filters but how long the song is how longger it takes\n"
    em.description += f"32. {bot.command_prefix}w-filters #get list list of filters what enabled are disabled is\n"
    em.description += f"----all filters----\n"
    em.description += f"To use filters,p!filters (the filter). Example :p!filters 8d\n"
    em.description += f"8d, gate, haas, phaser, treble, tremolo, vibrato, reverse, karaoke, flanger, mcompand, pulsator, subboost, bassboost, vaporwave, nightcore, normalizer, surrounding\n"
    em.set_footer(text="Thanks for using me!", icon_url=bot.user.avatar_url)
    return em


@bot.event  #make ur bot online
async def on_ready():
	await bot.change_presence(activity=discord.Activity(
	    type=discord.ActivityType.listening,
	    name=f"{len(bot.guilds)} servers!|use p!help to get help"))
	print(f"Hello I am {bot.user.name}-{bot.user.id}")

@bot.event
async def on_guild_join(guild):
    embed = discord.Embed(title='pandagamerfx Bot', color=0xaa0000)
    embed.add_field(name="What's up everyone? I am **pandagamerfx Bot**.", value='\nTry typing `p!help` to get started.', inline=False)
    embed.set_footer(text='Thanks for adding pandagamerfx Bot to your server!')
    await guild.system_channel.send(embed=embed)
    


@bot.event
async def on_member_join(member):
	channel = discord.utils.get(member.guild.channels, name='welcome')

	embed = discord.Embed(
	    title=f"welcome to {member.guild.name}!",
	    description=f"Thank you for joining {member.mention}!",
	    colour=discord.Colour.green())
	embed.set_thumbnail(url=member.avatar_url)

	await channel.send(embed=embed)
	print(f"{member.name} joined server")


@bot.event
async def on_member_remove(member):
	channel = discord.utils.get(member.guild.channels, name='goodbye')

	embed = discord.Embed(title=f"goodbye {member.guild.name}!",
	                      description=f"{member.mention} leave the server!",
	                      colour=discord.Colour.green())
	embed.set_thumbnail(url=member.avatar_url)

	await channel.send(embed=embed)

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        em = await get_help_embed()
        await message.channel.send(embed=em)

    await bot.process_commands(message)

@bot.command()
async def help(ctx):
    em = await get_help_embed()
    await ctx.send(embed=em)
            
@bot.command()
async def hi(ctx):
	await ctx.send(f"hi {ctx.author.name}")
	#await ctx.send(embed=embed)

@bot.command()
async def panda(ctx):
	await ctx.send(f"your a panda :panda_face:")
	#await ctx.send(embed=embed)







@bot.command()
async def logo(ctx, avamember: discord.Member = None):
 userAvatarUrl = avamember.avatar_url
 await ctx.send(userAvatarUrl)
 await ctx.send(f"request by {ctx.author.name}")


@commands.has_permissions(kick_members=True)
@bot.command()
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
	await user.kick(reason=reason)
	ban = discord.Embed(
	    title=f":boom: kick {user.name}!",
	    description=f"Reason: {reason}\nBy: {ctx.author.mention}")

	await ctx.message.delete()
	await ctx.channel.send(embed=ban)
	await user.send(embed=ban)


@commands.has_permissions(ban_members=True)
@bot.command()
async def ban(ctx, user: discord.Member, *, reason="No reason provided"):
	await user.ban(reason=reason)
	ban = discord.Embed(
	    title=f":boom: Banned {user.name}!",
	    description=f"Reason: {reason}\nBy: {ctx.author.mention}")

	await ctx.message.delete()
	await ctx.channel.send(embed=ban)
	await user.send(embed=ban)


@commands.has_permissions(ban_members=True)
@bot.command()
async def unban(ctx, *, member=None):
	BanList = await ctx.guild.bans()
	MemberDiscrim = member.split('#')
	MemberName = member.split('#' + MemberDiscrim[0])
	user_found = False
	for BanEntry in BanList:
		user = BanEntry.user
		if (MemberName[0]) == (user.name):
			await ctx.guild.unban(user)
			await ctx.send(
			    f"{user.name} has been unbanned successful \n By: {ctx.author.mention}"
			)
			user_found = True
			break
		if user_found == False:
			await ctx.send("Member not found!GG")




@bot.command()
async def userinfo(ctx):
	user = ctx.message.mentions[0]

	embed = discord.Embed(
	    title="USER INFO",
	    description=f"Here is the info we retrieved about {user}",
	    colour=user.colour)
	embed.set_thumbnail(url=user.avatar_url)
	embed.add_field(name="NAME", value=user.name, inline=True)
	embed.add_field(name="NICKNAME", value=user.nick, inline=True)
	embed.add_field(name="ID", value=user.id, inline=True)
	embed.add_field(name="STATUS", value=user.status, inline=True)
	embed.add_field(name="TOP ROLE", value=user.top_role.name, inline=True)
	await ctx.send(embed=embed)


@bot.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
	guild = ctx.guild
	mutedRole = discord.utils.get(guild.roles, name="Muted")

	if not mutedRole:
		mutedRole = await guild.create_role(name="Muted")

		for channel in guild.channels:
			await channel.set_permissions(mutedRole,
			                              speak=False,
			                              send_messages=False,
			                              read_message_history=True,
			                              read_messages=False)

	await member.add_roles(mutedRole, reason=reason)
	await ctx.send(f"Muted {member.mention} for reason {reason}")
	await member.send(f"You were muted in the server {guild.name} for {reason}"
	                  )


@bot.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
	mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

	await member.remove_roles(mutedRole)
	await ctx.send(f"Unmuted {member.mention}")
	await member.send(f"You were unmuted in the server {ctx.guild.name}")


@bot.command(name="clear")
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
	await ctx.channel.purge(limit=amount)


@bot.command()
async def serverinfo(ctx):
	name = str(ctx.guild.name)
	description = str(ctx.guild.description)

	owner = str(ctx.guild.owner)
	id = str(ctx.guild.id)
	region = str(ctx.guild.region)
	memberCount = str(ctx.guild.member_count)

	icon = str(ctx.guild.icon_url)

	embed = discord.Embed(title=name + " Server Information",
	                      description=description,
	                      color=discord.Color.blue())
	embed.set_thumbnail(url=icon)
	embed.add_field(name="Owner", value=owner, inline=True)
	embed.add_field(name="Server ID", value=id, inline=True)
	embed.add_field(name="Region", value=region, inline=True)
	embed.add_field(name="Member Count", value=memberCount, inline=True)

	await ctx.send(embed=embed)


@bot.command(name='shutdown')
async def shutdown(ctx):
	can_do = False
	response = "You're not my owner!  Only an owner can use that command!"
	if ctx.author.id == OWNER:
		response = "Okay, {}!  See you soon! but only music command work still".format(
		    ctx.author.name)
		can_do = True
	await ctx.send(response)
	if can_do:
		print("Shutting down...")
		await bot.close()



# and a total of {len(bot.users)} are using me!
@bot.command()
async def invite(ctx):
	embed = discord.Embed(
	    title=f"{bot.user.name}'s invite",
	    description=
	    "Click [here](https://discord.com/oauth2/authorize?client_id=795583415960600596&permissions=8&scope=bot%20applications.commands) to invite"
	)
	await ctx.send(embed=embed)

# and a total of {len(bot.users)} are using me!
@bot.command()
async def credit(ctx):
	embed = discord.Embed(
	    title=f"{bot.user.name}'s support the server",
	    description=
	    "Click [here](https://discord.gg/UgSvKwQT3g) to join jonse AJ discord server and Click [here](https://discord.gg/YxvZzXbS5Z) to support pandagamerfx discord server")
	await ctx.send(embed=embed)

# and a total of {len(bot.users)} are using me!
@bot.command()
async def template(ctx):
	embed = discord.Embed(
	    title=f"{bot.user.name}'s template",
	    description=
	    "Click [here](https://github.com/pandagamerfx2748/pandagamerfx-bot-template) to copy to template"
	)
	await ctx.send(embed=embed)


@bot.command()
async def create(ctx):
  guild = ctx.guild
  category = await guild.create_category("info")
  await guild.create_text_channel("welcome", overwrites=None, category=category, reason=None)  
  await guild.create_text_channel("goodbye", overwrites=None, category=category, reason=None)  

  await ctx.send(f"hi {ctx.author.name} info has been build complete")



#bot.load_extension('cogs.v')
keep_alive()  #make you bot online for 1 hour when u close the tab
bot.run(token)  #start your bot
