from pyrogram import Client as app, filters
from pyrogram.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mk
import time
from kvsqlite.sync import Client as mody
db = mody("data.sqlite", 'fuck')
def trend():
    k = db.keys("user_%")
    users = []
    for i in k:
        try:
            g = db.get(i[0])
            d = g["id"]
            users.append(g)
        except:
            continue
    data = users
    sorted_users = sorted(data, key=lambda x: len(x["users"]), reverse=True)
    result_string = "⌁︙- المستخدمين الاكثر مشاركة للرابط  :  \n\n"
    for user in sorted_users[:5]:
        result_string += f"🏅: ({len(user['users'])}) ↫ [{user['id']}](tg://user?id={user['id']})\n"
    return (result_string)
@app.on_callback_query(filters.regex("^account$"))
async def dailygiftt(app,query):
    user_id = query.from_user.id
    chats = db.get('force')
    force_msg = str(db.get("force_msg"))
    from .force import check_channel_member
    for i in chats:
      if not await check_channel_member(app, i, user_id):
        k = f'''{force_msg}\n\n• @{i}'''
        return await query.edit_message_text(k, reply_markup=mk([[btn(f'اضغط هنا للاشتراك 🧬', url=f't.me/{i}')]]))
    info = db.get(f"user_{query.from_user.id}")
    keys = mk(
        [
            [btn(text='رجوع', callback_data='back')]
        ]
    )
    if info:
        coins = float(info['coins'])
        users = len(info['users'])
        buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
        trans = int(db.get(f"user_{user_id}_trans")) if db.exists(f"user_{user_id}_trans") else 0
        y = trend()
        rk = f"""⌁︙معلومات حسابك في بوت زد إي↫⤈
⌁︙رصيد حسابك الحالي ↫ {coins} $
⌁︙عدد مشاركاتك لرابط الدعوة ↫ {users}
⌁︙عدد الطلبات التي قمت بطلبها ↫ {buys}
⌁︙عدد  تحويلاتك ↫ {trans}
{y}"""
        await query.edit_message_text(rk, reply_markup=keys)