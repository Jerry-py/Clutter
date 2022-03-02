import sys
import traceback

import discord

# noinspection PyUnresolvedReferences
import requests
from discord import RequestsWebhookAdapter, Webhook
from discord.ext import commands

import config
from utils import color, embed, get_txt


class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, "on_error"):
            return
        if cog := ctx.cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return
        ignored = (commands.CommandNotFound, commands.DisabledCommand)
        error = getattr(error, "original", error)
        if isinstance(error, ignored):
            return
        if isinstance(error, commands.MissingRequiredArgument):
            return await ctx.reply(
                embed=embed.error("Please give all the required arguments", guild_id=ctx.guild.id), mention_author=False
            )
        if isinstance(error, (commands.CheckFailure, commands.CheckAnyFailure)):
            return await ctx.reply(
                embed=embed.error("You cannot use this command", guild_id=ctx.guild.id), mention_author=False
            )
        print(color.red(f"\nIgnoring exception in command {ctx.command}:"), file=sys.stderr)
        _traceback = traceback.format_exception(type(error), error, error.__traceback__)
        _traceback = "".join(_traceback)
        print(color.red(_traceback))
        webhook = Webhook.from_url(config.error_webhook, adapter=RequestsWebhookAdapter())
        webhook.send(file=discord.File(get_txt("error", f"Error Type: {type(error)}\nError: {error}\n\n{_traceback}")))
        await ctx.reply(embed=embed.error("An unexpected error occured", guild_id=ctx.guild.id), mention_author=False)


def setup(bot):
    bot.add_cog(ErrorHandler(bot))
