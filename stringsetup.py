import os
os.system("pip install telethon")
os.system("pip install pyrogram")
from pyrogram import Client
from telethon.sessions import StringSession
from telethon.sync import TelegramClient


print("•••   TigerUserBOT  SESSION  GENERATOR   •••")
print("\nHello!! Welcome to WarBot Session Generator\n")
okvai = input("Enter 69 to continue: ")
if okvai == "69":
    print("Choose the string session type: \n1. TigerUserBOT \n2. Music Bot")
    library = input("\nYour Choice: ")
    if library == "1":
        print("\nTelethon Session For TigerUserBOT")
        APP_ID = int(input("\nEnter APP ID here: "))
        API_HASH = input("\nEnter API HASH here: ")
        with TelegramClient(StringSession(), APP_ID, API_HASH) as hellbot:
            print("\nYour TigerUserBOT Session Is sent in your Telegram Saved Messages.")
            warbot.send_message("me", f"#TigerUserBOT #TigerUserBOT_SESSION \n\n`{warbot.session.save()}`")
    elif library == "2":
        print("Pyrogram Session for Music Bot")
        APP_ID = int(input("\nEnter APP ID here: "))
        API_HASH = input("\nEnter API HASH here: ")
        with Client(':memory:', api_id=APP_ID, api_hash=API_HASH) as hellbot:
            print("\nYour WarBot Session Is sent in your Telegram Saved Messages.")
            warbot.send_message("me", f"#TigerUserBOT_MUSIC #TigerUserBOT_SESSION\n\n`{warbot.export_session_string()}`")
    else:
        print("Please Enter 1 or 2 only.")
else:
    print("DONE")
