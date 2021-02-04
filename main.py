import discord
from discord.ext import commands
bot = commands.Bot(command_prefix="p!")  #change prefix if you want
from keep_alive import keep_alive  #import the code from your file
token = "#your bot token"  #from your discord developer platform
OWNER = #your id but not other user id

@bot.event #make ur bot online
async def on_ready():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="say anything"))
  print(f"Hello I am {bot.user.name}-{bot.user.id}")

@bot.command()
async def hi(ctx):
	await ctx.send(f"hi {ctx.author.name}")
	#await ctx.send(embed=embed)

@bot.command(name='shutdown') 
async def shutdown(ctx):
    can_do = False
    response = "You're not my owner!  Only an owner can use that command! dumb"
    if ctx.author.id == OWNER:
        response = "Okay, {}!  See you soon! but only music command work still".format(ctx.author.name)
        can_do = True
    await ctx.send(response)
    if can_do:        
        print("Shutting down...")
        await bot.close()
#don't use this command are als it will shutdown the bot that is why to use owner id


@bot.command()
async def servers(ctx):
	embed = discord.Embed(
	    title=f"{bot.user.name} server count!",
	    description=f"{len(bot.guilds)} servers",
	    colour=discord.Colour.teal())
	await ctx.send(embed=embed)
# and a total of {len(bot.users)} are using me!

@bot.command()
async def invite(ctx):
	embed = discord.Embed(
	    title=f"{bot.user.name}'s invite",
	    description=
	    "Click [here](#yourbot invite) to invite"
	)
	await ctx.send(embed=embed)

@bot.command()
async def credit(ctx):
	embed = discord.Embed(
	    title=f"{bot.user.name}'s support the server",
	    description=
	    "Click [here](https://discord.gg/UgSvKwQT3g) to join jonse AJ discord server and Click [here](https://discord.gg/YxvZzXbS5Z) to support pandagamerfx discord server")
	await ctx.send(embed=embed)

@bot.command()
async def repost(ctx):
	embed = discord.Embed(
	    title=f"{bot.user.name}'s sub to the owner",
	    description=
	    "Click [here]( https://youtube.com/c/pandagamerfx ) ")
	await ctx.send(embed=embed)

bot.remove_command("help")
@bot.command()
async def help(ctx, args=None):
    help_embed = discord.Embed(title=" {bot.user.name} Help command!")
    command_names_list = [x.name for x in bot.commands]

    # If there are no arguments, just list the commands:
    if not args:
        help_embed.add_field(
            name="List of supported commands:",
            value="\n".join([str(i+1)+". "+x.name for i,x in enumerate(bot.commands)]),
            inline=False
        )
        help_embed.add_field(
            name="Details",
            value="sorry boss no details ",
            inline=False
        )

    # If the argument is a command, get the help text from that command:
    elif args in command_names_list:
        help_embed.add_field(
            name=args,
            value=bot.get_command(args).help
        )

    # If someone is just trolling:
    else:
        help_embed.add_field(
            name="Nope.",
            value="Don't think I got that command, boss!"
        )

    await ctx.send(embed=help_embed)

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
            await ctx.send(f"{user.name} has been unbanned successful \n By: {ctx.author.mention}")
            user_found = True
            break
          if user_found == False:
            await ctx.send("Member not found!GG")

@bot.command()
async def logo(ctx,avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)
    await ctx.send(f"request by {ctx.author.name}")

@bot.command()
async def userinfo(ctx):
    user = ctx.author

    embed=discord.Embed(title="USER INFO", description=f"Here is the info we retrieved about {user}", colour=user.colour)
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
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f"Muted {member.mention} for reason {reason}")
    await member.send(f"You were muted in the server {guild.name} for {reason}")

@bot.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    await ctx.send(f"Unmuted {member.mention}")
    await member.send(f"You were unmuted in the server {ctx.guild.name}")

@bot.command()
async def clear(ctx,n=1):
    await ctx.channel.purge(limit=n)

#bot.load_extension('cogs.v')
keep_alive()  #make you bot online for 1 hour when u close the tab but if you want 24/7 online go to uptime website are the apk version
bot.run(token)  #start your bot
#easy peasy!-by jonse(Aj) <3
#any questions?
