import json

from discord.ext import commands

from utils import checks, embed


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open("./modules/misc/commands.json", mode="r") as file:
            self.help_dict = json.load(file)

    @commands.command()
    @commands.check(checks.send_messages)
    async def help(self, ctx, *, command=None):
        await ctx.channel.trigger_typing()
        _help = self.help_dict.get(command.lower(), None)
        if command is None:
            text = "".join(f"`{name}`- {info['brief']}\n" for name, info in self.help_dict.items())

            text += f"\nFor more info on a command, use `{self.bot.command_prefix}help <command>`"
            await ctx.reply(embed=embed.info("Help", text, guild_id=ctx.guild.id), mention_author=False)
        elif _help is None:
            await ctx.reply(embed=embed.error("No such command", guild_id=ctx.guild.id), mention_author=False)
        else:
            await ctx.reply(
                embed=embed.info(f"Showing help for the command '{command}'", _help["desc"], guild_id=ctx.guild.id),
                mention_author=False,
            )


def setup(bot):
    bot.add_cog(Help(bot))
