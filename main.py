from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 

import requests 

import os


API = "https://apis.xditya.me/lyrics?song="


Ek = Client(
    "Lyrics-Search-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


@Ek.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    TEXT = "Hai {} \n\n**I Am Lyrics Search Bot. Send Me A Song Name, I Will Give You The Lyrics. ** \n\nFor Know More /help"
    BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton("Channel 🔰", url = "https://t.me/UpdateBots1"),InlineKeyboardButton("Support Group ⭕️", url = "https://t.me/SoonYak")],[InlineKeyboardButton("Repo 🗂️", url = "https://github.com/INDOHACKER-XODE/Lyrics-Search-Bot"),InlineKeyboardButton("Deploy 🗃️", url = "https://heroku.com/deploy?template=https://github.com/INDOHACKER-XODE/Lyrics-Search-Bot")],[InlineKeyboardButton("Developer 💡", url = "https://github.com/INDOHACKER-XODE/")]])
    await update.reply_text(
        text=TEXT.format(update.from_user.mention),
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
	
@Ek.on_message(filters.private & filters.command(["help"]))
async def help(bot, update):
    HELP = "Hai {} \n\n**There Is Nothing To Know More.** \n- Send Me A Song Name, I Will Give Lyrics Of That Song. \nBot By @UpdateBots1 "
    HELP_BUTTON = InlineKeyboardMarkup([[InlineKeyboardButton("🧑‍💻 Channel", url = "https://telegram.me/UpdateBots1"),InlineKeyboardButton("🗃️ Source Code", url = "https://github.com/INDOHACKER-XODE/Lyrics-Search-Bot"),InlineKeyboardButton("👤 Owner", url = http://t.me/heorchan")]])
    await update.reply_text(
        text=HELP.format(update.from_user.mention),
        reply_markup=HELP_BUTTON,
        disable_web_page_preview=True,
        quote=True
        )
	
@Ek.on_message(filters.private & filters.command(["about", "source", "repo"]))
async def about(bot, update):
    ABOUT = "**🤖 Bot :** Lyrics Search Bot\n\n**🧑‍💻 Developer :** [Kim](https://github.com/INDOHACKER-XODE)\n\n**💻 Channel :** @UpdateBots1\n\n**☎️ Support :** @heorchan \n\n**🗂️ Source Code :** [Lyrics Search Bot](https://github.com/INDOHACKER-XODE/Lyrics-Search-Bot)\n\n**⚙️ Language :** Python 3\n\n**🛡️ Framework :** Pyrogram"
    await update.reply_text(
	text=ABOUT,
	disable_web_page_preview=True,
	quote=True
	)

@Ek.on_message(filters.private & filters.text)
async def sng(bot, message):
        hy = await message.reply_text("`Searching 🔎`")
        song = message.text
        chat_id = message.from_user.id
        rpl = lyrics(song) 
        try:
                await hy.delete()
                await Ek.send_message(chat_id, text = rpl, reply_to_message_id = message.message_id, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Dev 🔗 ", url = f"github.com/INDOHACKER-XODE")], [InlineKeyboardButton("🧑‍💻 Channel", url = "https://telegram.me/UpdateBots1"),InlineKeyboardButton("🗃️ Source Code", url = "https://github.com/INDOHACKER-XODE/Lyrics-Search-Bot")]]))
        except requests.ConnectionError as exception:
        	await hy.delete()
        	await message.reply_text(f"I Can't Find A Song With `{song}`", quote = True, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🧑‍💻 Developer", url = f"github.com/INDOHACKER-XODE")], [InlineKeyboardButton("🧑‍💻 Channel", url = "https://telegram.me/UpdateBots1"),InlineKeyboardButton("🗃️ Source Code", url = "https://github.com/INDOHACKER-XODE/Lyrics-Search-Bot"),InlineKeyboardButton ("👤 Owner", url = http://t.me/heorchan")]]))


def search(song):
        r = requests.get(API + song)
        find = r.json()
        return find
       
def lyrics(song):
        fin = search(song)
        text = f'**🎶 Successfully Extracted Lyrics Of {song} 🎶**\n\n\n\n'
        text += f'`{fin["lyrics"]}`'
        text += '\n\n\n**Made With ❤️ By @UpdateBots1 / @heorchan**'
        return text


Ek.run()
