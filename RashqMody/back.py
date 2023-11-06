from pyrogram import Client as app, filters
from pyrogram.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mk
import time
from kvsqlite.sync import Client as mody
db = mody("data.sqlite", 'fuck')

@app.on_callback_query(filters.regex("^back$"))
async def dailygiftt(app,query):
    user_id = query.from_user.id
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
ID : `{query.from_user.id}`'''
    await query.edit_message_text(rk, reply_markup=keys)
