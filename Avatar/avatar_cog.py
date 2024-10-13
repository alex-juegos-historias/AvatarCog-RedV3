import discord
from redbot.core import commands
from datetime import datetime

class Avatar(commands.Cog):
    """Cog para mostrar el avatar de un usuario y su información."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="avatar")
    async def avatar(self, ctx, user: discord.Member = None):
        """Muestra el avatar del usuario mencionado, o tu avatar si no mencionas a nadie."""
        user = user or ctx.author  # Si no se menciona un usuario, usa el que ejecutó el comando
        avatar_url = user.avatar.url  # Obtén el URL del avatar

        embed = discord.Embed(
            title=f"Avatar de {user.display_name}",
            color=discord.Color.blue()
        )
        embed.set_image(url=avatar_url)  # Añade la imagen del avatar al embed

        await ctx.send(embed=embed)

    @commands.command(name="avatarinfo")
    async def avatar_info(self, ctx, user: discord.Member = None):
        """Muestra información detallada del usuario junto con su avatar."""
        user = user or ctx.author  # Usa el autor si no se menciona a nadie

        # Creando el embed con la información del usuario
        embed = discord.Embed(
            title=f"Información de {user.display_name}",
            color=discord.Color.green(),
            timestamp=datetime.utcnow()  # Establece la hora actual
        )
        
        embed.set_thumbnail(url=user.avatar.url)  # Miniatura con el avatar del usuario

        # Añadir la información del usuario al embed
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="Username", value=user.name, inline=True)
        embed.add_field(name="Discriminador", value=f"#{user.discriminator}", inline=True)
        embed.add_field(name="Apodo", value=user.display_name, inline=True)
        embed.add_field(name="Estado", value=user.status, inline=True)
        embed.add_field(name="Bot", value="Sí" if user.bot else "No", inline=True)
        
        # Información adicional como fechas de creación y de ingreso al servidor
        embed.add_field(
            name="Cuenta creada el",
            value=user.created_at.strftime("%d/%m/%Y %H:%M:%S"),
            inline=False
        )
        embed.add_field(
            name="Se unió al servidor el",
            value=user.joined_at.strftime("%d/%m/%Y %H:%M:%S"),
            inline=False
        )

        embed.set_footer(text=f"Solicitado por {ctx.author.display_name}", icon_url=ctx.author.avatar.url)

        await ctx.send(embed=embed)
    @commands.command()
    async def avatarcog(self, ctx):
        """Dueño de la Cog"""
        # Your code will go here
        await ctx.send("**Creada por:** alex_juegos_historias")
        await ctx.send("**Desarrollada por:** alex_juegos_historias")