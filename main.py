import discord
from discord.ext import commands
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="p!",
    guild_subscriptions=True, intents=intents
    )  #change prefix if you want
from keep_alive import keep_alive  #import the code from your file
token = "your-bot-token"  #from your discord developer platform
OWNER =#your discord id

@bot.event #make ur bot online
async def on_ready():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name=f"{len(bot.guilds)} servers!|use p!help to get help"))  
  print(f"Hello I am {bot.user.name}-{bot.user.id}")

@bot.event
async def on_member_join(member):
        channel=discord.utils.get(member.guild.channels,name='welcome')
       
        embed= discord.Embed(title=f"welcome to {member.guild.name}!",description= f"Thank you for joining {member.mention}!",colour=discord.Colour.green())
        embed.set_thumbnail(url=member.avatar_url)

        await channel.send(embed=embed)
        print(f"{member.name} joined server")
        
@bot.event
async def on_member_remove(member):
        channel=discord.utils.get(member.guild.channels,name='goodbye')
       
        embed= discord.Embed(title=f"goodbye {member.guild.name}!",description= f"{member.mention} leave the server!",colour=discord.Colour.green())
        embed.set_thumbnail(url=member.avatar_url)

        await channel.send(embed=embed)

@bot.command()
async def hi(ctx):
	await ctx.send(f"hi {ctx.author.name}")
	#await ctx.send(embed=embed)

@bot.command()
async def create(ctx):
  guild = ctx.message.guild
  await guild.create_text_channel('welcome')
  await guild.create_text_channel('goodbye')

bot.remove_command("help")
@bot.command()
async def help(ctx, args=None):
    help_embed = discord.Embed(title="pandagamerfx bot Help command!")
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
    user = ctx.message.mentions[0]

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

@bot.command(name="clear") 
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
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
   
  embed = discord.Embed(
      title=name + " Server Information",
      description=description,
      color=discord.Color.blue()
    )
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
        response = "Okay, {}!  See you soon! but only music command work still".format(ctx.author.name)
        can_do = True
    await ctx.send(response)
    if can_do:        
        print("Shutting down...")
        await bot.close()

#bot.load_extension('cogs.v')
keep_alive()  #make you bot online for 1 hour when u close the tab
bot.run(token)  #start your bot
