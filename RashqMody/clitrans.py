from pyrogram import Client as app, filters
from pyrogram.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mk
import time
from kvsqlite.sync import Client as mody
db = mody("data.sqlite", 'fuck')

@app.on_callback_query(filters.regex("^tran$"))
async def dailygiftt(app,query):
    user_info = db.get(f"user_{query.from_user.id}")
    user_id = query.from_user.id
    transfer = int(db.get("transfer")) if db.exists("transfer") else 1
    ask1 = await app.ask(query.from_user.id,"ارسل ايدي الشخص 🆔 ")
    try:
        ids = int(ask1.text)
    except:
        await ask1.reply("برجاء ارسال رقم فقط ، اعد المحاولة مره اخري")
        return
    if not db.exists(f'user_{ids}'):
        keys = mk(
        [
            [btn('رجوع', 'back')]
        ]
    )
        await ask1.reply("عذراً الشخص غير موجود فالبوت ❌", reply_markup=keys)
        return
    else:
        keys = mk(
        [
            [btn('رجوع', 'back_home')]
        ]
    )
        ask2 = await app.ask(query.from_user.id,"حسنا الان ارسل عدد النقاط اللي تريد ترسلها ", filters.user(query.from_user.id))
        try:
            amount = float(ask2.text)
        except:
            await ask2.reply("برجاء ارسال رقم فقط ، اعد المحاولة مره اخري")
            return
        if amount <transfer:
            await ask2.reply(f"المبلغ جدا صغير ، اقل مبلغ يمكن تحويله هو {transfer}")
            return
        if amount >= float(user_info['coins']):
            await ask2.reply("للاسف نقاطك غير كافية لتحويل هذا المبلغ")
        else:
            to_user = db.get(f"user_{ids}")
            coin_msg = str(db.get("coin_msg"))
            trans = int(db.get(f"user_{user_id}_trans")) if db.exists(f"user_{user_id}_trans") else 0
            count_trans = trans + 1
            db.set(f"user_{user_id}_trans", int(count_trans))
            await app.send_message(chat_id=ids, text=f"• تم اضافة نقاط الي حسابك ✅\nالمبلغ : {amount} ︎{coin_msg} .\n• من : `{query.from_user.mention}`",reply_markup=mk([[btn(text='رجوع',callback_data='back')]]))
            to_user['coins'] = int(to_user['coins']) + int(amount)
            db.set(f"user_{ids}", to_user)
            await ask2.reply(f"تمت عملية التحويل بنجاح ✅\nالى : {ids}", reply_markup=keys)
            user_info['coins'] = int(user_info['coins']) - int(amount)
            db.set(f"user_{query.from_user.id}", user_info)
            xxe = db.get("admin_list")
            sc = set(xxe)
            xxx = sorted(sc)
            for i in xxx:
                await app.send_message(i, f"**• عزيزي الادمن** : \n\n**• تمت عملية تحويل نقاط جديده ♻️**\n• المبلغ : {amount}\n• من: {query.from_user.mention}\n• ايديه : `{query.from_user.id}`\n\n• الى : `{ids}`\n• رصيد الشخص الذي قام بالتحويل الان : `{user_info['coins']}`")
            return