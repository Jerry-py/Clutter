import discord
from discord.ext import commands
from utils import embed

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(description="Lists all commands", help="Lists all commands.\nIf the command is specified, it will show the full description and aliases of the command.")
    @commands.guild_only()
    async def help(self, ctx, *, command=None):
        help_text = ""
        if command is None:
            title = "Commands list"
            for command in self.bot.commands:
                help_text += f"`{command.name}` - {command.description}\n"
        else:
            _command = None
            for _command in self.bot.commands:
                if _command.name == command:
                    command = _command
                    break
            if command is None:
                return await ctx.reply(embed=embed.error(ctx.guild.id, "No such command"), mention_author=False)
            title = f"Showing info for the command '{command.name}'"
            if command.aliases != []:
                aliases = "\n\n**Aliases:**"
                for alias in command.aliases:
                    aliases += f" `{alias}`"
            else:
                aliases = ""
            help_text += f"**Usage:** `{command.usage}`\n\n{command.help}{aliases}"
        await ctx.reply(embed=embed.main(ctx.guild.id, title, help_text), mention_author=False)
        


    

def setup(bot):
    bot.add_cog(Help(bot))