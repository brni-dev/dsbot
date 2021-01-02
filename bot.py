import random, string, math, platform, discord, os, sys, traceback, time, subprocess, asyncio, requests, json, urllib, aiohttp
from dotenv import load_dotenv
from discord.ext import commands
from discord import Member
from discord.ext.commands import Bot, has_permissions, CheckFailure, BadArgument
from bs4 import BeautifulSoup
import urllib.request as urllib2

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
bot = commands.Bot(command_prefix='$')
client = discord.Client()
bot.remove_command("help")
auth = 374964708165287940
banned = ["!", "$", "%", "&", "(", ")", "*", "+", ",", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "]", "\\", "^", "{", "|", "}", "~", "-"]
charlie_meme_url = "https://twitter.com/DevilMayAngry/status/1334568205818294272?s=09"

#def make_soup(url):
#    html = urlopen(url).read()
#    return BeautifulSoup(html)

#def get_images(url):
#    soup = make_soup(url)
    #this makes a list of bs4 element tags
#    images = [img for img in soup.findAll('img')]
#    print(str(len(images)) + "memes found.")
    #compile our unicode list of image links
#    image_links = [each.get('src') for each in images]
#    for each in image_links:
#        filename=each.split('/')[-1]
#        urllib.urlretrieve(each, filename)
#    return image_links

#a standard call looks like this
#get_images('http://www.wookmark.com')

#await asyncio.sleep(5)
#0x8c00ff - color purple

@bot.event
async def on_ready():
    print(f'Fuck yeah! {bot.user.name} connected to discord! B)')
    await bot.change_presence(activity=discord.Game(name="$help"))

@bot.command()
async def help(ctx):
    help=discord.Embed(title="Help", color=0x8c00ff)
    help.add_field(name="help", value="`$help`", inline=False)
    help.add_field(name="ban", value="`$ban @member`", inline=False)
    help.add_field(name="kick", value="`$kick @member`", inline=False)
    help.add_field(name="userinfo", value="`$userinfo @member`", inline=False)
    help.add_field(name="botinfo", value="`$botinfo`", inline=False)
    help.add_field(name="ascii", value="`$ascii [text]`", inline=False)
    help.add_field(name="toilet", value="`$toilet [text]`", inline=False)
    help.add_field(name="gayness", value="`$gayness @member`", inline=False)
    help.add_field(name="iq", value="`$iq @member`", inline=False)
    help.add_field(name="activity", value="`$activity [activity] [text]`", inline=False)
    help.add_field(name="status", value="`$status [status]`", inline=False)
    help.add_field(name="cmd", value="`$cmd [command]`", inline=False)
    help.add_field(name="ping", value="`$ping`", inline=False)
    help.add_field(name="ddos", value="`$ddos @member`", inline=False)
    help.add_field(name="performtest", value="`$performtest`", inline=False)
    help.add_field(name="nickname", value="`$nickname @member [newnickname]`\n`$nickname @member [remove]`", inline=False)
    help.add_field(name="invite", value="`$invite`", inline=False)
    help.add_field(name="purge", value="`$purge [amount]`", inline=False)
    help.add_field(name="nuke", value="`$nuke`", inline=False)
    help.add_field(name="say", value="`$say [text]`", inline=False)
    help.add_field(name="channel", value="`$channel [method] [text]`", inline=False)
    help.add_field(name="emoji", value="`$emoji [method] [text]`", inline=False)
    help.add_field(name="reddit", value="`$reddit [sortby] [subreddit]`", inline=False)
    help.set_footer(text=f"Requested by {ctx.message.author}")
    await ctx.send(embed=help)

#@bot.command()
#async def math(ctx, num1: str, op=None, num2: str):
#    try:
#        if op == None:
#            await ctx.send("You didn't satisfy (an) argument/s!")
#        if op == "+":
#            return ctx.send(f"Result: {num1 + num2 as float}")
#        if op == "-":
#            return ctx.send(f"Result: {num1 - num2 as float}")
#        if op == "*":
#            return ctx.send(f"Result: {num1 * num2 as float}")
#        if op == "/":
#            return ctx.send(f"Result: {num1 / num2 as float}")
#        if op == "%":
#            return ctx.send(f"Result: {num1 % num2 as int}%")
#    except ZeroDivisionError:
#        error=discord.Embed(title="Zero Division Error", description=f"`Error log: {e}`", color=0xff0000)
#        error.set_footer(text=f"Error caused by {ctx.message.author}")
#        ctx.send(embed=error)

@bot.command()
async def ddos(ctx, member: discord.Member):
    sleep = asyncio.sleep(0.1)
    cont = f"Preparing to DDoS **{member}!**\n`3 seconds remaining...`"
    message = await ctx.channel.send(cont)
    edit = message.edit
    await asyncio.sleep(1.5)
    cont = f"Preparing to DDoS **{member}!**\n`2 seconds remaining...`"
    await edit(content=cont)
    await asyncio.sleep(1.5)
    cont = f"Preparing to DDoS **{member}!**\n`1 seconds remaining...`"
    await edit(content=cont)
    await asyncio.sleep(1.5)
    cont = f"Preparing to DDoS **{member}!**\n`0 seconds remaining...`"
    await edit(content=cont)
    await asyncio.sleep(1.5)
    for i in range(10):
        await asyncio.sleep(1.5)
        await edit(content=f"`Loading... ( | )`")
        await sleep
        await edit(content=f"`Loading... ( \ )`")
        await sleep
        await edit(content=f"`Loading... ( - )`")
        await sleep
        await edit(content=f"`Loading... ( / )`")
    await edit(content=f"`Sent {str(random.randint(20118, 54028))} to **{member}**!`")
    await asyncio.sleep(1)
    await edit(content=f"`Successfully DDoS'd {member}!`")

@bot.command(pass_context=True)
async def reddit(ctx, type, *, subr):
    try:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://www.reddit.com/r/{subr}/new.json?sort={type}') as r:
                res = await r.json()
                e = res['data']['children']
                dist = res['data']['dist'] - 1
                ran = random.randint(0, dist)
                reddit=discord.Embed(title="Post Link", url=e[ran]['data']['url'], color=0xff0000)
                reddit.set_image(url=e[ran]['data']['url'])
                reddit.set_footer(text=f"Requested by {ctx.message.author}\nFrom r/{subr}")
                await ctx.send(embed=reddit)
    except Exception as e:
        error=discord.Embed(title="Subreddit not found/Type not found!", description=f"`Error log: {e}`", color=0xff0000)
        error.set_footer(text=f"Error caused by {ctx.message.author}")
        await ctx.send(embed=error)

"""
@bot.command()
@has_permissions(manage_emojis=True)
async def emoji(ctx, type, *, emoji):
    try:
        if type == "create":
            embed=discord.Embed(title="Emoji created!", description=f"Successfully created an emoji named: **{emoji}**", color=0x8c00ff)
            embed.set_footer(text=f"Emoji created by {ctx.message.author}")
            await ctx.send(embed=embed)
        elif type == "edit":
            embed=discord.Embed(title="Emoji edited!", description=f"Successfully edited an emoji named: **{emoji}**", color=0x8c00ff)
            embed.set_footer(text=f"Emoji created by {ctx.message.author}")
            await ctx.send(embed=embed)


@bot.command()
@has_permissions(manage_channels=True)
async def channel(ctx, type, *, inp):
    try:
        if type == "name":
            await ctx.channel.edit(name=inp)
            await ctx.send("done")
        elif type == "add":
            await ctx.channel.add(name=inp)
        elif type == "remove":
            await ctx.channel.delete()
    except:
"""

@bot.command()
async def status(ctx, type):
    if ctx.message.author.id == auth:
        if type == "idle":
            await bot.change_presence(status=discord.Status.idle)
            embed=discord.Embed(title="Bot presence changed!", description=f"Successfully changed the bot status to: **Idle**", color=0x8c00ff)
            embed.set_footer(text=f"Bot status changed by {ctx.message.author}")
            await ctx.send(embed=embed)
        elif type == "dnd":
            await bot.change_presence(status=discord.Status.dnd)
            embed=discord.Embed(title="Bot presence changed!", description=f"Successfully changed the bot status to: **Do Not Disturb**", color=0x8c00ff)
            embed.set_footer(text=f"Bot status changed by {ctx.message.author}")
            await ctx.send(embed=embed)
        elif type == "offline":
            await bot.change_presence(status=discord.Status.offline)
            embed=discord.Embed(title="Bot presence changed!", description=f"Successfully changed the bot status to: **Offline**", color=0x8c00ff)
            embed.set_footer(text=f"Bot status changed by {ctx.message.author}")
            await ctx.send(embed=embed)
        elif type == "online":
            await bot.change_presence(status=discord.Status)
            embed=discord.Embed(title="Bot presence changed!", description=f"Successfully changed the bot status to: **Online**", color=0x8c00ff)
            embed.set_footer(text=f"Bot status changed by {ctx.message.author}")
            await ctx.send(embed=embed)
    else:
        error=discord.Embed(title="Error!", description=f"Restricted command; **{ctx.message.author.name}** isn't Borny", color=0xff0000)
        error.set_footer(text=f"Error caused by {ctx.message.author}")
        await ctx.send(embed=error)

@bot.command()
async def iq(ctx, member: discord.Member):
    ran = str(random.randint(0, 130))
    if member.id == auth:
        ran = str(random.randint(110, 130))
    iq=discord.Embed(title="IQ", description=f"The estimated IQ of {member.name} is {ran}", color=0xff00ff)
    iq.set_footer(text=f"Requested by {ctx.message.author}")
    await ctx.send(embed=iq)

@bot.command()
async def activity(ctx, type, *, var):
    if ctx.message.author.id == auth:
        if type == "play":
            await bot.change_presence(activity=discord.Game(name=var))
            embed=discord.Embed(title="Bot presence changed!", description=f"Successfully changed the bot activity to:\nType - **Playing**\nText - **{var}**", color=0x8c00ff)
            embed.set_footer(text=f"Bot activity changed by {ctx.message.author}")
            await ctx.send(embed=embed)
        elif type == "stream":
            await bot.change_presence(activity=discord.Streaming(name=var, url="https://discord.gg/b2qrHFY5hA"))
            embed=discord.Embed(title="Bot presence changed!", description=f"Successfully changed the bot activity to:\nType - **Streaming**\nText - **{var}**", color=0x8c00ff)
            embed.set_footer(text=f"Bot activity changed by {ctx.message.author}")
            await ctx.send(embed=embed)
        elif type == "listen":
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=var))
            embed=discord.Embed(title="Bot presence changed!", description=f"Successfully changed the bot activity to:\nType - **Listening**\nText - **{var}**", color=0x8c00ff)
            embed.set_footer(text=f"Bot activity changed by {ctx.message.author}")
            await ctx.send(embed=embed)
        elif type == "watch":
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=var))
            embed=discord.Embed(title="Bot presence changed!", description=f"Successfully changed the bot activity to:\nType - **Watching**\nText - **{var}**", color=0x8c00ff)
            embed.set_footer(text=f"Bot activity changed by {ctx.message.author}")
            await ctx.send(embed=embed)
    else:
        error=discord.Embed(title="Error!", description=f"Restricted command; **{ctx.message.author.name}** isn't Borny", color=0xff0000)
        error.set_footer(text=f"Error caused by {ctx.message.author}")
        await ctx.send(embed=error)

@bot.command()
async def ascii(ctx, *, inp):
    for i in banned:
        if i in inp:
            error=discord.Embed(title="Error!", description=f"Yeah, that type of character (`{i}`), no", color=0xff0000)
            error.set_footer(text=f"Error caused by {ctx.message.author}")
            await ctx.send(embed=error)
            return
    output = subprocess.check_output(f"figlet {inp}", shell=True)
    out = str(output.decode("utf-8"))
    await ctx.channel.send(f"```text\n{out} ```")

@bot.command()
async def toilet(ctx, *, inp):
    for i in banned:
        if i in inp:
            error=discord.Embed(title="Error!", description=f"Yeah, that type of character (`{i}`), no", color=0xff0000)
            error.set_footer(text=f"Error caused by {ctx.message.author}")
            await ctx.send(embed=error)
            return
    output = subprocess.check_output(f"toilet {inp}", shell=True)
    out = str(output.decode("utf-8"))
    await ctx.channel.send(f"```text\n{out} ```")

#@bot.command()
#async def base64(ctx, type, *, message):
#    if type == "encode":
#        get = requests.get("url")
#        parse = json.loads(get.text)
#        print(parse["link"])

@bot.command()
async def reminder(ctx):
    response = "Hey everyone! Lets have a daily reminder that\nhttps://cdn.discordapp.com/attachments/780398110136074273/785260629850062898/20201206_224512.jpg"
    await ctx.send(response)

@bot.command()
async def performtest(ctx):
    response = "```test performed successfully```"
    await ctx.send(response)

@bot.command()
async def userinfo(ctx, member: discord.Member):
    author = ctx.message.author
    userid = str(member.id)
    pfp = str(member.avatar_url)
    created_at = str(member.created_at)
    joined_at = str(member.joined_at)
    display_name = member.display_name

    uinfo=discord.Embed(title="Profile Picture Link", url=f"{pfp}",color=0xff0000)
    uinfo.add_field(name="Name", value=f"{member}", inline=False)
    uinfo.add_field(name="Nickname", value=f"{display_name}", inline=False)
    uinfo.add_field(name="UserID", value=f"{userid}", inline=False)
    uinfo.add_field(name="Created at", value=f"{created_at}", inline=False)
    uinfo.add_field(name="Joined at", value=f"{joined_at}", inline=False)
    uinfo.set_footer(text=f"Requested by {author}")
    await ctx.send(embed=uinfo)

@bot.command()
@has_permissions(manage_nicknames=True)
async def nickname(ctx, member: discord.Member, *, nnick):
    if nnick == "remove":
        await member.edit(nick="")
        nick=discord.Embed(title="Removed nickname!", description=f'Removed **{member.name}**\'s nickname', color=0x8c00ff)
        nick.set_footer(text=f"Nickname removed by {ctx.message.author}")
        await ctx.send(embed=nick)
        return
    await member.edit(nick=nnick)
    nick=discord.Embed(title="New Nickname!", description=f'Assigned **{member}** a new nickname called: "{nnick}"', color=0x8c00ff)
    nick.set_footer(text=f"Nickname changed by {ctx.message.author}")
    await ctx.send(embed=nick)

@bot.command()
async def ping(ctx):
    var = round(bot.latency, 1 * 1000)
    ping=discord.Embed(title="Pong!", description=f"Latency: {str(var)} things", color=0x00ff00)
    ping.set_footer(text=f"Requested by {ctx.message.author}")
    await ctx.send(embed=ping)

@bot.command()
@has_permissions(ban_members=True)
async def ban (ctx, member:discord.User=None, reason=None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You didn't mention anybody or you mentioned yourself!")
        return
    await ctx.guild.ban(member, reason=reason)
    pfp = member.avatar_url
    ban=discord.Embed(title="Banned! :hammer:", description=f"{member.name}'s ID is {member.id}", color=0xff0000)
    ban.set_author(name=f"{member}")
    ban.set_image(url=pfp)
    ban.set_footer(text=f"Banned by {ctx.message.author}")
    await ctx.send(embed=ban)

@bot.command()
@has_permissions(kick_members=True)
async def kick (ctx, member:discord.User=None, reason=None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You didn't mention anybody or you mentioned yourself!")
        return
    await ctx.guild.kick(member, reason=reason)
    pfp = member.avatar_url
    kick=discord.Embed(title="Kicked!", description=f"{member.name}'s ID is {member.id}", color=0xff0000)
    kick.set_author(name=f"{member}")
    kick.set_image(url=pfp)
    kick.set_footer(text=f"Kicked by {ctx.message.author}")
    await ctx.send(embed=kick)

#@bot.command()
#@has_permissions(kick_members=True)
#async def mute(ctx, member: discord.Member):
#    muted_role = discord.utils.get(member.guild.roles, name = "muted noob")
#    await member.add_roles(muted_role)
#    await ctx.channel.send(f"Shut up! {member} has been muted")

#@bot.command()
#@has_permissions(kick_members=True)
#async def unmute(ctx, member: discord.Member):
#    muted_role = discord.utils.get(member.guild.roles, name = "muted noob")
#    await member.remove_roles(muted_role)
#    await ctx.channel.send(f"Fine you can speak. {member} has been unmuted")

@bot.command()
async def gayness(ctx, member: discord.Member):
    try:
        if member.id == auth:
            await ctx.channel.send(f"brni isnt gay u absolute noob")
            return
        elif member.id == 706666532809474069:
            await ctx.channel.send(f"<@706666532809474069> is 100% gay, like if i had a cent for when he was gay, i'd have an unlimited amount of money lmao")
            return
        elif member.id == bot.user.id:
            await ctx.channel.send("im not gay lol")
            return
        gayness=discord.Embed(title="Gayness", description=f"{member.name} is " + str(random.randint(0, 100)) + "% gay :gay_pride_flag:", color=0xff00ff)
        gayness.set_footer(text=f"Requested by {ctx.message.author}")
        await ctx.send(embed=gayness)
    except:
        await ctx.channel.send("error occured or smthin lol")

@bot.command()
async def invite(ctx):
    invite=discord.Embed(title="Invite Link", description=f"Hey there **{ctx.message.author.name}**! Here's the invite link to this bots server! Enjoy!", url="https://discord.gg/b2qrHFY5hA", color=0x00ff00)
    invite.set_footer(text=f"Requested by {ctx.message.author}")
    await ctx.send(embed=invite)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=3):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"```text\nPurged {amount} message(s)!```", delete_after=2)

@bot.command()
async def botinfo(ctx):
    def linux_distribution():
        try:
            return platform.linux_distribution()
        except:
            return "N/A"

    info=discord.Embed(title="Bot Info", description="Information on what the bot is running on", color=0x8c00ff)
    info.add_field(name="python_ver", value=sys.version.split('\n'), inline=False)
    info.add_field(name="dist", value=str(platform.dist()), inline=False)
    info.add_field(name="linux_distribution", value=linux_distribution(), inline=False)
    info.add_field(name="system", value=platform.system(), inline=False)
    info.add_field(name="machine", value=platform.machine(), inline=False)
    info.add_field(name="platform", value=platform.platform(), inline=False)
    info.add_field(name="uname", value=platform.uname(), inline=False)
    info.add_field(name="version", value=platform.version(), inline=False)
    info.add_field(name="mac_ver", value=platform.mac_ver(), inline=False)
    info.set_footer(text=f"Requested by {ctx.message.author}")
    await ctx.send(embed=info)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def nuke(ctx):
    await ctx.channel.purge(limit=None)
    nuke=discord.Embed(title="Boom!", description=f"**{ctx.message.author}** nuked this channel! :boom:", color=0xff8800)
    await ctx.send(embed=nuke)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def say(ctx, *, var):
    if ctx.message.author.id == auth:
        await ctx.channel.purge(limit=1)
        await ctx.channel.send(var)
    else:
        error=discord.Embed(title="Error!", description=f"Restricted command; **{ctx.message.author.name}** isn't Borny", color=0xff0000)
        error.set_footer(text=f"Error caused by {ctx.message.author}")
        await ctx.send(embed=error)

@bot.command()
async def cmd(ctx, *, command):
    if ctx.message.author.id == auth:
        os.system(command)
        output = subprocess.check_output(command, shell=True)
        out = str(output.decode("utf-8"))
        cmd=discord.Embed(title="Output", description="```text\n" + out + "```", color=0x8c00ff)
        await ctx.send(embed=cmd)
    else:
        error=discord.Embed(title="Error!", description=f"Restricted command; **{ctx.message.author.name}** isn't Borny", color=0xff0000)
        error.set_footer(text=f"Error caused by {ctx.message.author}")
        await ctx.send(embed=error)

bot.run(TOKEN)
