from pyrogram import Client as app, filters
from pyrogram.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mk
import time
import requests
from kvsqlite.sync import Client as mody
db = mody("data.sqlite", 'fuck')

@app.on_callback_query(filters.regex("^id_requests$"))
async def dailygiftt(app,query):
    user_id = query.from_user.id
    chats = db.get('force')
    force_msg = str(db.get("force_msg"))
    from .force import check_channel_member
    for i in chats:
      if not await check_channel_member(app, i, user_id):
        k = f'''{force_msg}\n\n• @{i}'''
        return await query.edit_message_text(k, reply_markup=mk([[btn(f'اضغط هنا للاشتراك 🧬', url=f't.me/{i}')]]))
    user_info = db.get(f'user_{user_id}')
    domain = str(db.get("set_domain"))
    api_key = str(db.get("api_key"))
    id_service = str(db.get("id_service"))
    ask = await app.ask(user_id, f'⌁︙ارسل اي دي الطلب الخاص بك')
    if ask.text:
        try:
            count = int(ask.text)
        except:
            await ask.reply("ارسل ايدي الطلب بشكل صحيح")
            return
        try:
            url = f"https://{domain}/api/v2?key={api_key}&action=status&order={count}"
            v2 = requests.get(url)
            data = v2.json()
            await ask.reply(f"⌁︙تفاصيل عن طلبك↫⤈\n⌁︙العدد المطلوب↫  عضو\n⌁︙العدد قبل الرشق↫  عضو\n⌁︙العدد المتبقي من الرشق ↫  عضو\n⌁︙الرابط ↫⤈")
        except Exception as e:
            await ask.reply(f"رجاء ارسل ايدي الطلب بشكل صحيح")
            return