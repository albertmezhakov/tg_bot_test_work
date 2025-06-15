from app.interfaces.bot.features import features
from app.interfaces.bot.keyboards.keyboard_entry import KeyboardEntry

menu_kb = KeyboardEntry(features=[[features.send_tap], [features.rating], [features.set_info]])

cancel_kb = KeyboardEntry(features=[[features.cancel]])

tap_kb = KeyboardEntry(features=[[features.tap_btn]])
