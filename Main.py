import discord
from discord.ext import commands

# Préfixe du bot
prefix = "+"
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user.name}')

@bot.command(name='ban')
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} a été banni.')

@bot.command(name='kick')
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} a été expulsé.')

@bot.command(name='mute')
async def mute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)
    await ctx.send(f'{member.mention} a été rendu muet.')

@bot.command(name='purge')
async def purge(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f'{amount} messages ont été supprimés.')

@bot.command(name='help')
    await ctx.send(' **en cours...**')
# Remplacez "TOKEN" par le token réel de votre bot

async function login() {
  try {
    await client.login(process.env.TOKEN);
    console.log(`\x1b[36m%s\x1b[0m`, `|    🐇 Logged in as ${client.user.tag}`);
  } catch (error) {
    console.error('Failed to log in:', error);
    process.exit(1);
  }
}
