from discord import Intents, Client, Message
from typing import Final
import mod
import os
from dotenv import load_dotenv

load_dotenv()  # load env
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")

intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)
moderator: mod = mod.mod()


@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')


@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    username: str = str(message.author)
    user_message: str = message.content

    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    if moderator.check(user_message) == 1:
        await message.delete()
        await message.author.send(f"""
        :triangular_flag_on_post: Your message in **{message.guild}** was removed for hateful or offensive content. :triangular_flag_on_post: 
        **Channel**: {channel}
        **Message**: "{user_message}"   
""") # NOQA


def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()
