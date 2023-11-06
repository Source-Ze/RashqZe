from pyrogram import Client as app, filters
from pyrogram.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mk
import time
from kvsqlite.sync import Client as mody
db = mody("data.sqlite", 'fuck')
@app.on_callback_query(filters.regex("^setting_bot$"))
async def dailygiftt(app,query):
    user_id = query.from_user.id
    keys = mk(
        [
            
            [btn('اضافة نقاط لشخص', 'add_coins'), btn('خصم نقاط من شخص', 'less_coin')],
            [btn('جلب معلومات شخص', 'get_infos')],
            [btn('تعيين api key', 'set_api'), btn('تعيين Domain الموقع', 'set_domain')],
            [btn('تعيين id خدمة رشق الاعضاء', 'id_service')],
            [btn('تعيين سعر رشق العضو الواحد', 'member_price')],
            [btn('تعيين الحد الادني للتحويل', 'transfer')], 
            [btn('تعيين عدد مشاركة رابط الدعوه', 'invite_coin')],
            [btn('تعيين كليشة الاشتراك الاجبارى', 'force_msg')],
            [btn('• رجوع •', 'back_admin')],
        ]
    )
    info = db.get(f"user_{query.from_user.id}")
    if info:
        rk = f"""- مرحباً عزيزي المطور ︎{query.from_user.mention} 🔥 

- يمكن للعضو ارسال /id لارسال الايدي الخاص به"""
        await query.edit_message_text(rk, reply_markup=keys)
