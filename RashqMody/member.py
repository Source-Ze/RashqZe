from pyrogram import Client as app, filters
from pyrogram.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mk
import time
import requests
from kvsqlite.sync import Client as mody
import datetime
db = mody("data.sqlite", 'fuck')
def check_user(user_id):
    users = db.get(f"user_{user_id}_request")
    now = time.time()    
    WAIT_TIME = 40  #هنا اكتب عدد الثواني بين كل طلب مثلا 3 دقائق بين كل طلب
    if  db.exists(f"user_{user_id}_request"):
        last_time = users['time']
        elapsed_time = now - last_time
        if elapsed_time < WAIT_TIME:
            remaining_time = WAIT_TIME - elapsed_time
            return int(remaining_time)
        else:
            
            users['time'] = now
            db.set(f'user_{user_id}_request', users)
            return None
    else:
        users = {}
        users['time'] = now
        db.set(f'user_{user_id}_request', users)
        return None

@app.on_callback_query(filters.regex("^member$"))
async def dailygiftt(app,query):
    user_id = query.from_user.id
    chats = db.get('force')
    force_msg = str(db.get("force_msg"))
    from .force import check_channel_member
    for i in chats:
      if not await check_channel_member(app, i, user_id):
        k = f'''{force_msg}\n\n• @{i}'''
        return await query.edit_message_text(k, reply_markup=mk([[btn(f'اضغط هنا للاشتراك 🧬', url=f't.me/{i}')]]))
    f = check_user(query.from_user.id)    
    if f is None:
        user_info = db.get(f'user_{user_id}')
        domain = str(db.get("set_domain"))
        api_key = str(db.get("api_key"))
        id_service = str(db.get("id_service"))
        await app.delete_messages(query.message.chat.id, query.message.id)
        member_price = float(db.get("member_price")) if db.exists("member_price") else 0.2
        price_all = float(member_price) * 1000
        ask = await app.ask(user_id, f'⌁︙ارسل عدد الرشق المطلوب يجب ان \n⌁︙يتراوح بين 500 ~ 30000\n⌁︙كل 1000 عضو ب {price_all}$')
        if ask.text:
            try:
                count = int(ask.text)
            except:
                await ask.reply("برجاء ارسال رقم فقط ، اعد المحاولة مره اخري")
                return
            
            ask1 = await app.ask(user_id, '⌁︙ارسل رابط القناة او الكروب . \n⌁︙يمكنك ارسال رابط عام او خاص .')
            if ask1.text and "t.me" in ask1.text:
                try:
                    channel_and_post = ask1.text.replace('https://t.me/', '').split('/')
                    channel = channel_and_post[0]
                    chan_id = channel
                    chat_info = await app.get_chat(chan_id)
                    subscribers_count = chat_info.members_count
                except Exception as e:
                    await ask1.reply(f"• رجاء ارسل رابط القناة بشكل صحيح\n• {e}")
            x = count * float(member_price) / 2
            if float(x) > float(user_info['coins']):
                await ask1.reply(f"عفوًا، ليس لديك رصيد كافي لشراء هذا العدد من الرشق\nتحتاج الي : {x} $")
                return
            if count <500:
                await ask1.reply("يجب ان ترسل عدد الرشق بصورة صحيحة")
                return
            if count >30000:
                await ask1.reply("يجب ان ترسل عدد الرشق بصورة صحيحة")
                return
            viewff = member_price * count
            ask3 = await app.ask(user_id, f'⌁︙معلومات عن طلبك قبل تأكيد الطلب\n⌁︙الرابط ↫⤈\n{ask1.text}\n⌁︙عدد الرشق ↫ {count}\n⌁︙التكلفة ↫ {viewff}$\n• ⋯ • ⋯ • ⋯ • ⋯ • ⋯ •• ⋯ • ⋯ • ⋯ • ⋯ •\n⌁︙ارسل /ok لتأكيد او /cancel للإلغاء')
            if ask3.text == "/ok":
                try:
                    link = ask1.text
                    viewff = member_price * count
                    url = f"https://{domain}/api/v2?key={api_key}&action=add&service={id_service}&quantity={count}&link={link}"
                    v2 = requests.get(url)
                    data = v2.json()
                    subscribers_count = chat_info.members_count
                    order = data['order']
                    await ask1.reply(f"⌁︙تم خصم {viewff}$ من رصيدك وتسجيل طلبك  \n⌁︙الرابط ↫ {ask1.text}\n⌁︙العدد المطلوب ↫ {count}\n⌁︙عدد الاعضاء قبل الرشق ↫ {subscribers_count}\n⌁︙الايدي الخاص بطلبك ↫ {order} ")
                    viewff = member_price * count
                    user_info['coins'] = float(user_info['coins']) - float(viewff) 
                    db.set(f"user_{user_id}", user_info)
                    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
                    count_buys = buys + 1
                    db.set(f"user_{user_id}_buys", int(count_buys))
                    f = check_user(query.from_user.id)
                except Exception as e:
                    await ask1.reply(f"خطا غير متوقع : {e}")
            if ask3.text == "/cancel":
                await ask3.reply("تم الغاء الطلب")
    else:
        duration = datetime.timedelta(seconds=f)
        now = datetime.datetime.now()
        target_datetime = now + duration
        date_str = target_datetime.strftime('%Y/%m/%d')
        rk = "⌁︙ لا يمكنك طلب أكثر من طلب بنفس الوقت\n⌁︙ يرجى الانتضار ريثما يكتمل طلبك"
        await query.edit_message_text(rk)