class Checks:
    def __init__(self, db, bot):
        self.db = db
        self.bot = bot

    def is_moderator(self, ctx):
        if ctx.guild:
            return ctx.author.id in self.db.get(f"{ctx.guild.id}.moderators.roles") or ctx.author.id in self.db.get(
                f"{ctx.guild.id}.moderators.users")
        else:
            return False

    def send_messages(self, ctx):
        if ctx.guild:
            return ctx.channel.permissions_for(self.bot.user).send_messages
        else:
            return False

    def attach_files(self, ctx):
        if ctx.guild:
            return ctx.channel.permissions_for(self.bot.user).attach_files
        else:
            return False
