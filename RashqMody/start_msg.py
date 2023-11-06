from pyrogram import Client as app, filters
from pyrogram.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mk
import time
import pyrogram.errors
from kvsqlite.sync import Client as xxx
from  pyrogram.enums import ChatMemberStatus
from kvsqlite.sync import Client as mody
db = mody("data.sqlite", 'fuck')

@app.on_message(filters.private & filters.regex("^/start$"), group=5)
async def startm(app, msg):
    user_id = msg.from_user.id
    if db.get("ban_list") is None:
        db.set('ban_list', [])
        pass
    if user_id in db.get("ban_list"):
        return
    if db.exists(f"user_{user_id}"):
        coin = float(db.get(f'user_{user_id}')['coins'])
        start_msg = str(db.get("start_msg"))
        keys = mk(
        [
            [btn(text=f' رصيدك : {coin} $ ', callback_data='lol')],
            [btn(text=' طلب رشق اعضاء ', callback_data='member')],
            [btn(text=' تجميع النقاط ', callback_data='sharelink'), btn(text=' شراء رصيد ', url='https://t.me/EK_N1')],
            [btn(text='معلومات حسابك', callback_data='account'), btn(text=' تحويل رصيد ', callback_data='tran')],
            [btn(text='معلومات الطلب', callback_data='id_requests')],
        ]
    )
        rk = f'''︎{start_msg}
⌁︙الايدي الخاص بك ↫⤈
ID : `{msg.from_user.id}`'''
        await app.send_message(msg.from_user.id,rk, reply_markup=keys)
    else:
        keys = mk(
        [
            [btn(text='اضغط هنا للتحقق', callback_data='send_code')], 
        ]
    )
        rk =f'''︎• **مرحبا بك {msg.from_user.mention} في بوت رشق الفراعنة**

• **بما انك عضو جديد في البوت ينبغي التحقق من انك لست روبوت ، رجاء اضغط علي الزر بالاسفل'''
        await app.send_message(msg.from_user.id,rk, reply_markup=keys)
