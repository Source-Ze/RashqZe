from pyrogram import Client as app, filters
from pyrogram.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mk
import time
import pyrogram.errors
from .start_msg import startm
from kvsqlite.sync import Client as xxx
from  pyrogram.enums import ChatMemberStatus
from kvsqlite.sync import Client as mody
import random
db = mody("data.sqlite", 'fuck')

@app.on_message(filters.private & filters.regex("^/start (.*?)"))
async def sm(app, msg):
    user_id = msg.from_user.id
    join_user = msg.from_user.id
    to_user = int(msg.text.split("/start ")[1])
    if db.get("ban_list") is None:
        db.set('ban_list', [])
        pass
    if user_id in db.get("ban_list"):
        return
    if db.exists(f"user_{user_id}"):
        if user_id == to_user:
            await app.send_message(user_id, "لا يمكنك الدخول عبر الرابط الخاص بك ❌")
            await startm(app, msg)
    else:
        user_info = db.get(f'user_{user_id}')
        coin_msg = str(db.get("coin_msg"))
        code = random.randint(100000, 999999)
        verified = False
        ask1 = await app.ask(user_id, f'•︙ارسل الان كود التحقق هذا للتاكد من انك لست روبوت : {code} ', filters=filters.user(user_id))
        while not verified:
            try:
                user_code = int(ask1.text)
                if user_code == code:
                    await ask1.reply("• تم التحقق بنجاح من أنك لست روبوت ✅\n\n• ارسل /start")
                    info = {'coins': 0.2, 'id': user_id, 'premium': False, 'admin': False, "phone": [], "users": [], "date": str(time.time())}
                    db.set(f'user_{user_id}', info)
                    xxe = db.get("admin_list")
                    sc = set(xxe)
                    xxx = sorted(sc)
                    count = 0
                    mon = 0
                    users = db.keys()
                    for i in users:
                        if "user_" in str(i[0]):
                            count+=1
                    for i in xxx:
                        await app.send_message(i,f"٭ **تم دخول شخص جديد الى البوت الخاص بك 👾**\n\n•__ معلومات العضو الجديد .__\n\n• الاسم : {msg.from_user.mention}\n• المعرف : @{msg.from_user.username}\n• الايدي : `{msg.from_user.id}`\n\n**• عدد الاعضاء الكلي** : {count}")
                    verified = True
                    someinfo = db.get(f"user_{to_user}")
                    someinfo['users'].append(join_user)
                    cq = 0.1 if not float(db.get("invite_price")) else float(db.get("invite_price"))
                    someinfo['coins'] = float(someinfo['coins']) + cq
                    coinss = someinfo['coins']
                    db.set(f'user_{to_user}', someinfo)
                    info = db.get(f"user_{msg.from_user.id}")
                    if info:
                        coins = info['coins']
                    await app.send_message(to_user, f'• قام : {msg.from_user.mention} بالدخول الى الرابط الخاص وحصلت على {cq} نقطه ✨\n• عدد نقاطك الان : {coinss}')
                    await startm(app, msg)
                else:
                    
                    ask1 = await app.ask(user_id, f'• عذرا الكود الذي ارسلته غير صحيح\n• اعد ارسال الكود مره اخرى', filters=filters.user(user_id))
            except Exception as x:
                print(x)
                
                ask1 = await app.ask(user_id, f'• يرجي إرسال قيمة رقمية فقط : ( ارقام فقط )\n• اعد ارسال الكود مره اخرى', filters=filters.user(user_id))