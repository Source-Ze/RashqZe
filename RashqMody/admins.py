from pyrogram import Client as app, filters
from pyrogram.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mk
import time
from kvsqlite.sync import Client as mody
db = mody("data.sqlite", 'fuck')

@app.on_callback_query(filters.regex("^back_admin$"))
async def dailygiftt(app,query):
    user_id = query.from_user.id
    keys = mk(
        [
            
            [btn('اخر تحديثات البوت 🧬', url='https://t.me/UI_XB')],
            [btn('عمل البوت : ✅', 'startt'), btn('اشعار الدخول : ✅', 'startt')],
            [btn('قسم تغيير الكلايش', 'set_start')],
            [btn('قسم الاشتراك الاجبارى', 'setforce'), btn('قسم الادمنية', 'admins_bot')],
            [btn('قسم الاذاعة', 'brods'), btn('قسم الاحصائيات', 'stats')],
            [btn('• اعدادات بوت الرشق •', 'setting_bot')],
        ]
    )
    
    rk = f"""**• اهلا بك في لوحه الأدمن الخاصه بالبوت 🤖**

- يمكنك التحكم في البوت الخاص بك من هنا \n\n==================="""
    await query.edit_message_text(rk, reply_markup=keys)
