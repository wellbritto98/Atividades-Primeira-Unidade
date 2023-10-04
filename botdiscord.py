import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logado como {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # Não queremos que o bot responda a si mesmo
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!iniciar cadastro'):
            if message.author.guild_permissions.administrator:
                response = 'Clique nos emojis abaixo para cadastro'
                msg = await message.reply(response, mention_author=False)
                await msg.add_reaction('👍')
            else:
                response = 'Você não tem permissões suficientes para usar este comando.'
                await message.reply(response, mention_author=True)

    @client.event
    async def on_reaction_add(reaction, user):
            if reaction.emoji == '👍':
                guild = reaction.message.guild
                await guild.create_private_text_channel('Tickets', overwrites=None, reason=None)
                await reaction.message.channel.send('Created a ticket!')            



intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTE1MTIzOTY3ODMxODYyMDc3Nw.GdpyYn.R5ftKbC6NG4-VpAdnJn_vWOKyE_19gAt3pXNTs') # Não se esqueça de substituir pelo seu token real e mantê-lo seguro
