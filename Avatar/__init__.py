from .avatar_cog import Avatar

async def setup(bot):
    await bot.add_cog(Avatar(bot))
