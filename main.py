import asyncio
import random
import schedule
import time
from telegram import Bot

BOT_TOKEN = "7299232651:AAFLOqGb7TTb-RaVD_sO_tx4dcWOypDemmM"
CHAT_ID = "1013935611"

bot = Bot(token=BOT_TOKEN)

# 💧 Cute water reminder messages
messages = [
    "💧 Bebu, take a sip of water now 🥺",
    "✨ Stay hydrated, my night queen 💙",
    "🍼 Even vampires need water 😛",
    "🌙 Stay hydrated my katlububu! Palububu!  Water please 😘",
    "🚰 Just a reminder from your bot-boyfriend: DRINK!",
    "💖 Every drop keeps your glow alive! Hydrate miao 🐱",
    "☕ You’ve had coffee. Now water, please 💧",
    "🫧 Hydrate that cute brain of yours!",
    "🥤 Time to water the goddess 🌸"
]

# 🔁 Function to send a random message
async def send_water_reminder():
    message = random.choice(messages)
    await bot.send_message(chat_id=CHAT_ID, text=message)
    print(f"Sent: {message}")

# 🔄 Wrapper for schedule (sync loop for async send)
def run_schedule():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    while True:
        schedule.run_pending()
        time.sleep(30)

# ⏰ Schedule messages from 4 PM to 10 AM
schedule_times = [
    "16:00", "18:00", "20:00", "22:00", "00:00",
    "02:00", "04:00", "06:00", "08:00", "10:00"
]

for t in schedule_times:
    schedule.every().day.at(t).do(lambda: asyncio.run(send_water_reminder()))

print("💧 Water reminder bot started for night shift queen...")

# 🚀 Start the loop
run_schedule()

