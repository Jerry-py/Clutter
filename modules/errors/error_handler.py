import sys

import discord
import traceback
from discord import Webhook, RequestsWebhookAdapter
from discord.ext import commands

import config
from utils import embed, color


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
                await ctx.reply(embed=embed.error(ctx.guild.id, f'You cannot use this command in DMs'),
                                mention_author=False)
            except (discord.HTTPException, discord.Forbidden):
                pass
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply(embed=embed.error(ctx.guild.id, "Please give all the required arguments"),
                            mention_author=False)
        elif isinstance(error, commands.MissingAnyRole):
            await ctx.reply(embed=embed.error(ctx.guild.id, "You cannot use this command"), mention_author=False)
        else:
            print(color.red("\nIgnoring exception in command {}:".format(ctx.command)), file=sys.stderr)
            _traceback = traceback.format_exception(type(error), error, error.__traceback__)
            _traceback = "".join(_traceback)
            print(color.red(_traceback))
            with open("./errorlogs/error.txt", mode="w") as file:
                file.write(f"Error Type: {type(error)}\nError: {error}\n\n{_traceback}")
            with open("./errorlogs/error.txt", mode="rb") as file:
                webhook = Webhook.from_url(config.error_webhook, adapter=RequestsWebhookAdapter())
                webhook.send(file=discord.File(file))
            await ctx.reply(embed=embed.error(ctx.guild.id, "An unexpected error occured"), mention_author=False)


def setup(bot):
    bot.add_cog(ErrorHandler(bot))
