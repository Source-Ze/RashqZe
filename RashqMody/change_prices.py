from pyrogram import Client as app, filters
from pyrogram import Client as temp
from pyrogram.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mk
import time
from kvsqlite.sync import Client

db = Client("data.sqlite", 'fuck')

admins = db.get('admin_list')

@app.on_callback_query(filters.regex("^set_start$"), group=14)
async def startmsg(app, query):
    user_id = query.from_user.id
    code = "start_msg"
    np = db.get(code)
    if np is None:
        np = "لا يوجد"
    else:
        np = db.get(code)
    ask2 = await app.ask(user_id, f'• الكليشة الحالية : `{np}`\n\n• ارسل الكليشة الجديدة')
    if ask2.text:
        try:
            db.set("start_msg", str(ask2.text))
            await ask2.reply("تم التعيين بنجاح")
        except:
            await ask2.reply("حدث خطا ما ")
            return
@app.on_callback_query(filters.regex("^set_api$"), group=14)
async def setapi(app, query):
    user_id = query.from_user.id
    code = "api_key"
    np = db.get(code)
    if np is None:
        np = "لا يوجد"
    else:
        np = db.get(code)
    ask2 = await app.ask(user_id, f'• الـ Api الحالي : `{np}`\n\n• ارسل api جديد :')
    if ask2.text:
        try:
            db.set("api_key", str(ask2.text))
            await ask2.reply(f"**تم تعيين api حسابك بنجاح ✅**")
        except:
            await ask2.reply("حدث خطا ما ")
            return
@app.on_callback_query(filters.regex("^id_service$"), group=14)
async def id(app, query):
    user_id = query.from_user.id
    code = "id_service"
    np = db.get(code)
    if np is None:
        np = "لا يوجد"
    else:
        np = db.get(code)
    ask2 = await app.ask(user_id, f'• ايدي الخدمة الحالي : `{np}`\n\n• ارسل اي دي الخدمة الجديد')
    if ask2.text:
        try:
            db.set("id_service", int(ask2.text))
            await ask2.reply(f"**تم تعيين ايدي الخدمة بنجاح ✅**")
        except:
            await ask2.reply("حدث خطا ما ")
            return
@app.on_callback_query(filters.regex("^set_domain$"), group=14)
async def dom(app, query):
    user_id = query.from_user.id
    code = "set_domain"
    np = db.get(code)
    if np is None:
        np = "لا يوجد"
    else:
        np = db.get(code)
    ask2 = await app.ask(user_id, f'• الدومين الحالي : `{np}`\n\n• ارسل الكليشة الجديدة')
    if ask2.text:
        try:
            db.set("set_domain", str(ask2.text))
            await ask2.reply(f"**تم تعيين الدومين بنجاح ✅**")
        except:
            await ask2.reply("حدث خطا ما ")
            return
@app.on_callback_query(filters.regex("^invite_coin$"), group=14)
async def invit(app, query):
    user_id = query.from_user.id
    code = "invite_price"
    np = 1 if not db.get(code) else db.get(code)
    ask2 = await app.ask(user_id, f'• سعر كل دعوة : `{np}`$\n\n• ارسل السعر الجديد , يمكنك ارسال رقم عشري')
    if ask2.text:
        try:
            db.set("invite_price", float(ask2.text))
            await ask2.reply("تم تعيين السعر بنجاح")
        except:
            await ask2.reply("حدث خطا ما ")
            return
@app.on_callback_query(filters.regex("^transfer$"), group=14)
async def trans(app, query):
    user_id = query.from_user.id
    code = "transfer"
    np = 100 if not db.get(code) else db.get(code)
    ask2 = await app.ask(user_id, f'• الحد الادني من التحويل : `{np}`$\n\n• ارسل الحد الادني الجديد')
    if ask2.text:
        try:
            db.set("transfer", int(ask2.text))
            await ask2.reply(f"**تم تعيين الحد الادني بنجاح ✅**")
        except:
            await ask2.reply("حدث خطا ما ")
            return
@app.on_callback_query(filters.regex("^member_price$"), group=14)
async def memb(app, query):
    user_id = query.from_user.id
    code = "member_price"
    np = 0.2 if not db.get(code) else db.get(code)
    ask2 = await app.ask(user_id, f'• تعيين سعر رشق العضو الواحد : `{np}`$\n\n• ارسل الحد الادني الجديد , يمكنك ارسال رقم عشرى')
    if ask2.text:
        try:
            db.set("member_price", float(ask2.text))
            await ask2.reply("تم تعيين السعر بنجاح")
        except:
            await ask2.reply("حدث خطا ما ")
            return
@app.on_callback_query(filters.regex("^force_msg$"), group=14)
async def forcemsk(app, query):
    user_id = query.from_user.id
    code = "force_msg"
    np = db.get(code)
    if np is None:
        np = "لا يوجد"
    ask2 = await app.ask(user_id, f'• كليشة الاشتراك الاجبارى الحالية : `{np}`$\n\n• ارسل الكليشة الجديدة :')
    if ask2.text:
        try:
            db.set("force_msg", str(ask2.text))
            await ask2.reply(f"**تم تعيين كليشة الاشتراك الاجبارى بنجاح ✅**")
        except:
            await ask2.reply("حدث خطا ما ")
            return