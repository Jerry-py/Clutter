import sys
import traceback

import discord
from discord import Webhook, RequestsWebhookAdapter
from discord.ext import commands

import config
from utils import embed, color, get_txt


class ErrorHandler(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return
        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return
        ignored = (commands.CommandNotFound, commands.DisabledCommand)
        error = getattr(error, 'original', error)
        if isinstance(error, ignored):
            return
        elif isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.reply(embed=embed.error(f'You cannot use this command in DMs', id=ctx.guild.id),
                                mention_author=False)
            except (discord.HTTPException, discord.Forbidden):
                pass
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply(embed=embed.error("Please give all the required arguments", id=ctx.guild.id),
                            mention_author=False)
        elif isinstance(error, commands.MissingAnyRole):
            await ctx.reply(embed=embed.error("You cannot use this command", id=ctx.guild.id), mention_author=False)
        else:
            print(color.red("\nIgnoring exception in command {}:".format(ctx.command)), file=sys.stderr)
            _traceback = traceback.format_exception(type(error), error, error.__traceback__)
            _traceback = "".join(_traceback)
            print(color.red(_traceback))
            webhook = Webhook.from_url(config.error_webhook, adapter=RequestsWebhookAdapter())
            webhook.send(
                file=discord.File(get_txt("error", f"Error Type: {type(error)}\nError: {error}\n\n{_traceback}")))
            await ctx.reply(embed=embed.error("An unexpected error occured", id=ctx.guild.id), mention_author=False)


def setup(bot):
    bot.add_cog(ErrorHandler(bot))
