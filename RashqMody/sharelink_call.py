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
    result_string = "•<strong> المستخدمين الاكثر مشاركة لرابط الدعوى :</strong>\n"
    for user in sorted_users[:5]:
        result_string += f"🏅: ({len(user['users'])}) -> [{user['id']}](tg://user?id={user['id']})\n"
    return (result_string)
@app.on_callback_query(filters.regex("^sharelink$"))
async def sharelinkk(app, query):
    user_id = query.from_user.id
    bot_username = None
    chats = db.get('force')
    force_msg = str(db.get("force_msg"))
    from .force import check_channel_member
    for i in chats:
      if not await check_channel_member(app, i, user_id):
        k = f'''{force_msg}\n\n• @{i}'''
        return await query.edit_message_text(k, reply_markup=mk([[btn(f'اضغط هنا للاشتراك 🧬', url=f't.me/{i}')]]))
    cq = 0.1 if not db.get("invite_price") else db.get("invite_price")
    try:
        c  = await app.get_me()
        bot_username = c.username
        info = db.get(f"user_{query.from_user.id}")
        users = len(info['users'])
        coin_msg = str(db.get("coin_msg"))
    except:
        await query.edit_message_text("حدث خطأ بالبوت ، حاول لاحقاً .")
        return
    keys = mk(
        [
            [btn(text='رجوع', callback_data='back')],
        ]
    )
    link = f"https://t.me/{bot_username}?start={user_id}"
    y = trend()
    rk = f"""انسخ الرابط ثم قم بمشاركته مع اصدقائك 📥 .\n\n⌁︙كل شخص يقوم بالدخول الى الرابط الخاص بك سوف تحصل على {cq} $ 💰 .\nوالعضو الذي يدخل سوف يحصل على 0.02💰\n⌁︙رصيدك الحالي ↫ $\n\n⌁︙رابط الدعوة الخاص بك :\n{link}\n⌁︙مشاركتك للرابط : {users} 🌀\n{y}"""
    await query.edit_message_text(rk, reply_markup=keys)