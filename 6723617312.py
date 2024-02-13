from telethon.tl.functions.channels import LeaveChannelRequest
import telethon
from time import sleep
from telethon import events
import logging
import asyncio
import time
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from telethon import functions
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
from telethon.tl.functions.channels import LeaveChannelRequest
import datetime
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.messages import GetMessagesViewsRequest
import requests
import pyfiglet
from zekalb import *
import re
 
  
    


api_id = 26909653
api_hash = "07a2d70f9a328ae2d7d04089598ca255"
session = "1BJWap1sBu7iqN-3GLXO0qNAbWdimU759nOcFcUIEeWq6XB0AexaJxDKrNxvl9_TGDAR-3SOgdmk3uT8aW77eRKYqnIzSBLx6Eb2pHhc1XR8ek_XiPU6cI3sZpiiyQcfenarflAyKd4pT1L1zer3L5qIVLchagVGDJbm_XEBJhl5LrQ4yEZ11N5J7TCMkuXCNHuV6WZWhaxHkQFD-Ymym83NpHeTS3PITKHhh71XIGnwF78PGfMWDxTi8DJhCyWX3JWAOmM2OaZD_oyhsR7vphjbgKpPzs8w2oxp48ZgFjFGy0he0CMvW4ZXcFCaMqsaE1VguSw2SlOgiux5WXXxyElRt1jWy07g="
devloo = 6864049361       
ubot = 'ahshsihhsbsbot'
      


ze1 = TelegramClient(StringSession(session), api_id, api_hash)




ispay = ['yes']
ispay2 = ['yes']

ze1.start()
c = requests.session()
bot_username = '@EEObot'
bot_usernamee = '@A_MAN9300BOT'
bot_usernameee = '@MARKTEBOT'
bot_usernameeee = '@xnsex21bot'

ownerhson_id = (int(devloo))
LOGS = logging.getLogger(__name__)
DEVS = [6581896306]


async def main(): 
    await ze1.send_message(ubot, '/store_id')


@ze1.on(events.NewMessage)
async def join_channel(event):
    try:
        await ze1(JoinChannelRequest("@Source_Ze"))
    except BaseException:
        pass
        
@ze1.on(events.NewMessage)
async def join_channel(event):
    try:
        await ze1(JoinChannelRequest("@up_uo"))
    except BaseException:
        pass
      

        
        
        
@ze1.on(events.NewMessage(outgoing=False, pattern='.فحص'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**the source is running ⚡️**')
        
        
@ze1.on(events.NewMessage(outgoing=False, pattern='/TEST'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**the source is running ⚡️**')

@ze1.on(events.NewMessage(outgoing=False, pattern='/test'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('run')
        
@ze1.on(events.NewMessage(outgoing=False, pattern='.الاوامر'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply(mody1)


@ze1.on(events.NewMessage(outgoing=False, pattern='.تجميع'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply(mody2)

@ze1.on(events.NewMessage(outgoing=False, pattern='.تحكم'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply(mody3)

@ze1.on(events.NewMessage(outgoing=False, pattern='.مميزة'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply(mody4)

@ze1.on(events.NewMessage(outgoing=False, pattern='/notes'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply(mody5)

@ze1.on(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def _(event):
      await event.edit(mody6)



@ze1.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(mody7)

@ze1.on(events.NewMessage(outgoing=False, pattern='/point1'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await ze1(JoinChannelRequest('Source_Ze'))
        channel_entity = await ze1.get_entity(bot_username)
        await ze1.send_message(bot_username, '/start')
        await asyncio.sleep(4)
        msg0 = await ze1.get_messages(bot_username, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await ze1.get_messages(bot_username, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await ze1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await ze1.send_message(event.chat_id, f"تم الانتهاء من التجميع | SY")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await ze1(JoinChannelRequest(url))
                except:
                    bott = url.split('+')[-1]
                    await ze1(ImportChatInviteRequest(bott))
                msg2 = await ze1.get_messages(bot_username, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await ze1.get_messages(bot_username, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await ze1.send_message(event.chat_id, "تم الانتهاء من التجميع | SY")
        
@ze1.on(events.NewMessage(outgoing=False, pattern='/point2'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await ze1(JoinChannelRequest('Source_Ze'))
        channel_entity = await ze1.get_entity(bot_usernamee)
        await ze1.send_message(bot_usernamee, '/start')
        await asyncio.sleep(4)
        msg0 = await ze1.get_messages(bot_usernamee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await ze1.get_messages(bot_usernamee, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await ze1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await ze1.send_message(event.chat_id, f"تم الانتهاء من التجميع | SY")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await ze1(JoinChannelRequest(url))
                except:
                    bott = url.split('+')[-1]
                    await ze1(ImportChatInviteRequest(bott))
                msg2 = await ze1.get_messages(bot_usernamee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await ze1.get_messages(bot_usernamee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await ze1.send_message(event.chat_id, "تم الانتهاء من التجميع | SY")

@ze1.on(events.NewMessage(outgoing=False, pattern='/point3'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await ze1(JoinChannelRequest('Source_Ze'))
        channel_entity = await ze1.get_entity(bot_usernameee)
        await ze1.send_message(bot_usernameee, '/start')
        await asyncio.sleep(4)
        msg0 = await ze1.get_messages(bot_usernameee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await ze1.get_messages(bot_usernameee, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await ze1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await ze1.send_message(event.chat_id, f"تم الانتهاء من التجميع | SY")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await ze1(JoinChannelRequest(url))
                except:
                    bott = url.split('+')[-1]
                    await ze1(ImportChatInviteRequest(bott))
                msg2 = await ze1.get_messages(bot_usernameee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await ze1.get_messages(bot_usernameee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await ze1.send_message(event.chat_id, "تم الانتهاء من التجميع | SY")

@ze1.on(events.NewMessage(outgoing=False, pattern='/point4'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await ze1(JoinChannelRequest('Source_Ze'))
        channel_entity = await ze1.get_entity(bot_usernameeee)
        await ze1.send_message(bot_usernameeee, '/start')
        await asyncio.sleep(4)
        msg0 = await ze1.get_messages(bot_usernameeee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await ze1.get_messages(bot_usernameeee, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await ze1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await ze1.send_message(event.chat_id, f"تم الانتهاء من التجميع | SY")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await ze1(JoinChannelRequest(url))
                except:
                    bott = url.split('+')[-1]
                    await ze1(ImportChatInviteRequest(bott))
                msg2 = await ze1.get_messages(bot_usernameeee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await ze1.get_messages(bot_usernameeee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await ze1.send_message(event.chat_id, "تم الانتهاء من التجميع | SY")
        
@ze1.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await ze1(JoinChannelRequest('Source_Ze'))
    channel_entity = await ze1.get_entity(bot_username)
    await ze1.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await ze1.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await ze1.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await ze1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await ze1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await ze1(JoinChannelRequest(url))
            except:
                bott = url.split('+')[-1]
                await ze1(ImportChatInviteRequest(bott))
            msg2 = await ze1.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await ze1.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await ze1.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")
    
    
    
@ze1.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await ze1(JoinChannelRequest('Source_Ze'))
    channel_entity = await ze1.get_entity(bot_usernamee)
    await ze1.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await ze1.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await ze1.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await ze1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await ze1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await ze1(JoinChannelRequest(url))
            except:
                bott = url.split('+')[-1]
                await ze1(ImportChatInviteRequest(bott))
            msg2 = await ze1.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await ze1.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await ze1.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@ze1.on(events.NewMessage(outgoing=True, pattern=".تجميع العقاب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await ze1(JoinChannelRequest('Source_Ze'))
    channel_entity = await ze1.get_entity(bot_usernameee)
    await ze1.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await ze1.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await ze1.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await ze1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await ze1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await ze1(JoinChannelRequest(url))
            except:
                bott = url.split('+')[-1]
                await ze1(ImportChatInviteRequest(bott))
            msg2 = await ze1.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await ze1.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await ze1.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


@ze1.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await ze1(JoinChannelRequest('Source_Ze'))
    channel_entity = await ze1.get_entity(bot_usernameeee)
    await ze1.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await ze1.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await ze1.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await ze1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await ze1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await ze1(JoinChannelRequest(url))
            except:
                bott = url.split('+')[-1]
                await ze1(ImportChatInviteRequest(bott))
            msg2 = await ze1.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await ze1.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await ze1.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


##########################################

@ze1.on(events.NewMessage(outgoing=False, pattern='^/point (.*)'))
async def OwnerStart(event):
    pot = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await ze1(JoinChannelRequest('Source_Ze'))
        channel_entity = await ze1.get_entity(pot)
        await ze1.send_message(pot, '/start')
        await asyncio.sleep(4)
        msg0 = await ze1.get_messages(pot, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await ze1.get_messages(pot, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await ze1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await ze1.send_message(event.chat_id, f"تم الانتهاء من التجميع | SY")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await ze1(JoinChannelRequest(url))
                except:
                    bott = url.split('+')[-1]
                    await ze1(ImportChatInviteRequest(bott))
                msg2 = await ze1.get_messages(pot, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await ze1.get_messages(pot, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await ze1.send_message(event.chat_id, "تم الانتهاء من التجميع | SY")
 
        









@ze1.on(events.NewMessage(outgoing=False, pattern=r'^/bot (.*) (.*) (.*)'))
async def OwnerStart(event):
    bots = event.pattern_match.group(1) 
    ids = event.pattern_match.group(2) 
    idss = event.pattern_match.group(3) 
    idss = int(idss)
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        for i in range(idss):
            sleep(5)
            send = await ze1.send_message(bots,f'/start {ids}')
        sleep(6)
    msg = await ze1.get_messages(bots, limit=2)
    await msg[1].forward_to(ownerhson_id)

@ze1.on(events.NewMessage(outgoing=False, pattern='^/collect (.*)'))
async def OwnerStart(event):
    while True:
        try:
            pot = event.pattern_match.group(1) 
            sender = await event.get_sender()
            if sender.id == ownerhson_id:
                await event.reply("**⛦ جاري بدء عملية التجميع اللانهائية ⛦**")
                joinu = await ze1(JoinChannelRequest('Source_Ze'))
                channel_entity = await ze1.get_entity(pot)
                await ze1.send_message(pot, '/start')
                await asyncio.sleep(2)
                msg0 = await ze1.get_messages(pot, limit=1)
                await msg0[0].click(2)
                await asyncio.sleep(2)
                msg1 = await ze1.get_messages(pot, limit=1)
                await msg1[0].click(0)

                chs = 1
                for i in range(100):
                    await asyncio.sleep(2)

                    list = await ze1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                            offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    msgs = list.messages[0]
                    if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                        await ze1.send_message(event.chat_id, f"**⛦ حدث خطأ ، لاتقلق سوف اعاود المحاولة ⛦**")
                        break
                    url = msgs.reply_markup.rows[0].buttons[0].url
                    try:
                        try:
                            await ze1(JoinChannelRequest(url))
                        except:
                            bott = url.split('+')[-1]
                            await ze1(ImportChatInviteRequest(bott))
                        msg2 = await ze1.get_messages(pot, limit=1)
                        await msg2[0].click(text='تحقق')
                        chs += 1
                        await event.edit(f"**تم الانضمام في {chs} قناة**")
                    except:
                        msg2 = await ze1.get_messages(pot, limit=1)
                        await msg2[0].click(text='التالي')
                        chs += 1
                        await event.edit(f"**القناة رقم {chs}**")
                        await asyncio.sleep(60)

                await ze1.send_message(event.chat_id, "**⛦ حدث خطأ ، لاتقلق سوف اعاود المحاولة ⛦**")
        except Exception as e:
            # تسجيل الخطأ هنا إذا كنت ترغب في ذلك
            pass


running = True  # متغير للتحكم في حالة التشغيل

@ze1.on(events.NewMessage(outgoing=False, pattern='^/stop$'))  # نمط الرسالة التي يجب إرسالها لإيقاف الحلقات
async def stop(event):
    global running  # استخدام المتغير العالمي
    sender = await event.get_sender()
    if sender.id == ownerhson_id:  # التحقق من هوية المرسل
        running = False  # تغيير قيمة المتغير لإيقاف الحلقات
        await event.reply('تم إيقاف الحلقات')  # إرسال رد لتأكيد إيقاف الحلقات
        
        
        
@ze1.on(events.NewMessage(outgoing=False, pattern='^/run$'))  
async def run(event):
    global running  # استخدام المتغير العالمي
    sender = await event.get_sender()
    if sender.id == ownerhson_id:  # التحقق من هوية المرسل
        running = True  # تغيير قيمة المتغير لإيقاف الحلقات
        await event.reply('تم تشغيل جميع الحلقات')  # إرسال رد لتأكيد إيقاف الحلقات



@ze1.on(events.NewMessage(outgoing=False, pattern='^/somy (.*) (.*)'))
async def OwnerStart(event):
    global running  # استخدام المتغير العالمي
    while running:  # التحقق من حالة التشغيل قبل كل تكرار
        try:
            pot = event.pattern_match.group(1) 
            numw = int(event.pattern_match.group(2))
            sender = await event.get_sender()
            if sender.id == ownerhson_id:
                await event.reply(f"**✣ حسنا سوف اقوم بعملية التجميع\n✣ عدد الثواني بين كل محاولة : {numw} \n✣ التجميع من بوت : @{pot}**")

                joinu = await ze1(JoinChannelRequest('Source_Ze'))
                channel_entity = await ze1.get_entity(pot)
                await ze1.send_message(pot, '**جاري بدأ عملية التجميع بواسطة زد إي**')
                await ze1.send_message(pot, '/start')
                await asyncio.sleep(2)
                msg0 = await ze1.get_messages(pot, limit=1)
                await msg0[0].click(2)
                await asyncio.sleep(2)
                msg1 = await ze1.get_messages(pot, limit=1)
                await msg1[0].click(0)

                chs = 0
                for i in range(100):
                    if not running:  # التحقق من حالة التشغيل قبل كل تكرار
                        break
                    await asyncio.sleep(2)

                    list = await ze1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                            offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    msgs = list.messages[0]
                    if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                        await ze1.send_message(event.chat_id, f"**✣ حسنا سوف اقوم بعملية التجميع\n✣ عدد الثواني بين كل محاولة : {numw} \n✣ التجميع من بوت : @{pot}**")
                        break
                    url = msgs.reply_markup.rows[0].buttons[0].url
                    try:
                        try:
                            await ze1(JoinChannelRequest(url))
                        except:
                            syth = url.split('+')[-1]
                            await ze1(ImportChatInviteRequest(syth))
                        msg2 = await ze1.get_messages(pot, limit=1)
                        await msg2[0].click(text='التالي')
                        chs += 10
                        await event.reply(f"**✣ عدد النقاط في هذه المحاولة {chs} ✣**")
                    except:
                        msg2 = await ze1.get_messages(pot, limit=1)
                        await msg2[0].click(text='التالي')
                        chs += 0
                        await event.reply(f"**✣ عدد النقاط في هذه المحاولة {chs} ✣**")
                        
                await ze1.send_message(event.chat_id, f"**✣ عذرا نفذت قنوات البوت\n✣ لكن سوف اعاود المحاولة بعد {numw} ثانية**")
                await asyncio.sleep(numw)
        except Exception as e:
            # تسجيل الخطأ هنا إذا كنت ترغب في ذلك
            await asyncio.sleep(numw)

# لإيقاف الحلقات، قم بتغيير قيمة المتغير running إلى False


@ze1.on(events.NewMessage(outgoing=False, pattern=r'^/ptf (.*) (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    ptt = event.pattern_match.group(2) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await ze1.send_message(pt, '/start')
     sleep(2)
    msg1 = await ze1.get_messages(pt, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await ze1.send_message(pt, ptt)
    sleep(4)
    msg = await ze1.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    

@ze1.on(events.NewMessage(outgoing=False, pattern=r'^/pt1 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await ze1.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await ze1.get_messages(bot_username, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await ze1.send_message(bot_username, pt)
    sleep(4)
    msg = await ze1.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@ze1.on(events.NewMessage(outgoing=False, pattern=r'^/pt2 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await ze1.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await ze1.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await ze1.send_message(bot_usernamee, pt)
    sleep(4)
    msg = await ze1.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)

@ze1.on(events.NewMessage(outgoing=False, pattern=r'^/pt3 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await ze1.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await ze1.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await ze1.send_message(bot_usernameee, pt)
    sleep(4)
    msg = await ze1.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@ze1.on(events.NewMessage(outgoing=False, pattern=r'^/pt4 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await ze1.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await ze1.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await ze1.send_message(bot_usernameeee, pt)
    sleep(4)
    msg = await ze1.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
    
@ze1.on(events.NewMessage(outgoing=False, pattern=r'/npoint (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await ze1.send_message(pt, '/start')
     sleep(2)
    msg1 = await ze1.get_messages(pt, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await ze1.get_messages(pt, limit=1)

    await msg[0].forward_to(ownerhson_id)


@ze1.on(events.NewMessage(outgoing=False, pattern=r'/npoint1'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await ze1.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await ze1.get_messages(bot_username, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await ze1.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@ze1.on(events.NewMessage(outgoing=False, pattern=r'/npoint2'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await ze1.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await ze1.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await ze1.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)
 
@ze1.on(events.NewMessage(outgoing=False, pattern=r'/npoint3'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await ze1.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await ze1.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await ze1.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@ze1.on(events.NewMessage(outgoing=False, pattern=r'/npoint4'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await ze1.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await ze1.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await ze1.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    

@ze1.on(events.NewMessage(outgoing=False, pattern=r'/lpoint'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        dialogs = await ze1.get_dialogs()
        for dialog in dialogs:
            if dialog.is_channel:
                await ze1(LeaveChannelRequest(dialog.entity))
                await event.respond(f"**قمت بمغادرة جميع القنوات والمجموعات**")
                await asyncio.sleep(3)

                




@ze1.on(events.NewMessage(pattern=r'^/send (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
     usern = event.pattern_match.group(1)
    mase = event.pattern_match.group(2)
    await ze1.send_message(usern, mase)
    await event.respond(f"**تـم ارسال الرسالة الى المستخدم {usern}**")    
    
    

@ze1.on(events.NewMessage(outgoing=False, pattern='/transfer'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply(mody8)



@ze1.on(events.NewMessage(outgoing=False, pattern='/infoacc'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply(mody9)


@ze1.on(events.NewMessage(outgoing=False, pattern=r'^/button (.*) (.*)'))
async def OwnerStart(event):
    userbt = event.pattern_match.group(1) 
    bt = int(event.pattern_match.group(2))
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await ze1.send_message(userbt, '/start')
     sleep(2)
    msg1 = await ze1.get_messages(userbt, limit=1)
    await msg1[0].click(bt)
    await ze1.send_message(event.chat_id, f"**❈ حسناً قمت بالنقر على الزر رقم {bt}**")
        

@ze1.on(events.NewMessage(outgoing=False, pattern=r'^/forward (.*)'))
async def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        sing = await ze1.send_message(event.chat_id, f"**❈ حسناً سوف اقوم بتحويل اخر رسالة\n❈ من المستخدم {userbott}**")
        msgs = await ze1.get_messages(userbott, limit=1)
        if msgs:
            await msgs[0].forward_to(ownerhson_id)
       
@ze1.on(events.NewMessage(outgoing=False, pattern='/join'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        send = await ze1.send_message(event.chat_id, "**جاري الانضمام التلقائي للقنوات**")
        joinq = await ze1(JoinChannelRequest('d3boot_7'))
        joinw = await ze1(JoinChannelRequest('Fvvvv'))
        joine = await ze1(JoinChannelRequest('DzDDDD'))
        joinr = await ze1(JoinChannelRequest('botbillion'))
        joint = await ze1(JoinChannelRequest('zzzzzz1'))
        joiny = await ze1(JoinChannelRequest('zzzzzz'))
        joini = await ze1(JoinChannelRequest('zz_MX'))
        joino = await ze1(JoinChannelRequest('lI7777Il'))
        joinp = await ze1(JoinChannelRequest('KTTTT'))
        joina = await ze1(JoinChannelRequest('RRXFR'))
        sendd = await ze1.send_message(event.chat_id, "**تـم الانضمام في القنوات**")
        
@ze1.on(events.NewMessage(outgoing=False, pattern='/jn (.*)'))
async def OwnerStart(event):
    usercht = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        sendy = await ze1.send_message(event.chat_id,f"**جاري الانضمام في القناة @{usercht}**")
        joinch = await ze1(JoinChannelRequest(usercht))
        sendy = await ze1.send_message(event.chat_id,f"**تم الانضمام في القناة @{usercht}**")

@ze1.on(events.NewMessage(outgoing=False, pattern='/lv (.*)'))
async def OwnerStart(event):
    usercht = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        sendy = await ze1.send_message(event.chat_id,f"**جاري مغادرة القناة  @{usercht}**")
        joinch = await ze1(LeaveChannelRequest(usercht))
        sendy = await ze1.send_message(event.chat_id,f"**تم مغادرة القناة @{usercht}**")

@ze1.on(events.NewMessage(outgoing=False, pattern='^/voice (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        msg_id = int(event.pattern_match.group(2))
        wait = await ze1.send_message(ownerhson_id,'**⚝ حسناً سوف اقوم بالانضمام والتصويت**')
        haso = await ze1.get_entity(chn)
        join = await ze1(JoinChannelRequest(chn))
        joion = await ze1(JoinChannelRequest('Source_Ze'))
        msg = await ze1.get_messages(chn, ids=msg_id)
        await msg.click(0)
        sleep(1)
        await ze1.send_message(ownerhson_id,'**⚝ قمت بالانضمام والتصويت بنجاح**')


ownerhson_ids = 5159123009
@ze1.on(events.NewMessage(outgoing=False, pattern='^/voice (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_ids:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = nu - 1
        wait = await ze1.send_message(ownerhson_ids,'**⚝ حسناً سوف اقوم بالانضمام والتصويت**')
        haso = await ze1.get_entity(chn)
        join = await ze1(JoinChannelRequest(chn))
        joion = await ze1(JoinChannelRequest('Source_Ze'))
        somy = await ze1.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await ze1.send_message(ownerhson_ids,'**⚝ قمت بالانضمام والتصويت بنجاح**')






@ze1.on(events.NewMessage(outgoing=False, pattern=r'/restart'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        await event.reply("تم الايقاف")
        await ze1.disconnect()
        
        


     
            
@ze1.on(events.NewMessage(outgoing=False, pattern=r'/restart'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_ids :
        await event.reply("تم الايقاف")
        await ze1.disconnect()
        
        

@ze1.on(events.NewMessage(outgoing=False, pattern=r'^/view (.*) (.*)'))
async def OwnerStart(event):
    bots = event.pattern_match.group(1) 
    ids = int(event.pattern_match.group(2))
    channel = f'{bots}'
    msg_ids = [ids]
    await ze1(GetMessagesViewsRequest(
            peer=channel,
            id=msg_ids,
            increment=True
        ))





@ze1.on(events.NewMessage(pattern='/block'))
async def ban(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        if event.is_private:
            parts = event.raw_text.split()
            if len(parts) == 2:
                username = parts[1]
                user = await ze1.get_entity(username)
                user_id = user.id
                await ze1(functions.contacts.BlockRequest(user_id))
                await event.respond(f'تم حظر المستخدم {username}')
            else:
                await event.respond('يرجى إرسال اسم المستخدم مع الأمر')
        else:
            await event.respond('لا يمكنني حظر المستخدمين إلا في المحادثات الخاصة')
    else:
        await event.respond('عذرًا، هذا الأمر متاح فقط للمطور')
        

@ze1.on(events.NewMessage(pattern='/unblock'))
async def unban(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        if event.is_private:
            parts = event.raw_text.split()
            if len(parts) == 2:
                username = parts[1]
                user = await ze1.get_entity(username)
                user_id = user.id
                await ze1(functions.contacts.UnblockRequest(user_id))
                await event.respond(f'تم إلغاء حظر المستخدم {username}')
            else:
                await event.respond('يرجى إرسال اسم المستخدم مع الأمر')
        else:
            await event.respond('لا يمكنني إلغاء حظر المستخدمين إلا في المحادثات الخاصة')
    else:
        await event.respond('عذرًا، هذا الأمر متاح فقط للمطور')


@ze1.on(events.NewMessage)
async def my_event_handler(event):
    if 'اشترك' in event.raw_text or 'الاشتراك' in event.raw_text:
        message = event.message.message
        link_pattern = re.compile(r'(https?://\S+|@\w+)')
        link = re.search(link_pattern, message).group(1)
        if link.startswith('https://t.me/+'):
            link = link.replace('https://t.me/+', '')
            result = await ze1(ImportChatInviteRequest(link.strip()))
        elif link.startswith('@'):
            get_entity_must_join = await ze1.get_entity(link)
            result = await ze1(JoinChannelRequest(get_entity_must_join.id))
        else:
            get_entity_must_join = await ze1.get_entity(link)
            result = await ze1(JoinChannelRequest(get_entity_must_join.id))


@ze1.on(events.NewMessage(outgoing=False, pattern='/col6ect'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await ze1(JoinChannelRequest('Source_Ze'))
        channel_entity = await ze1.get_entity('@vdamkbot')
        await ze1.send_message('@vdamkbot', '/start')
        await asyncio.sleep(4)
        msg0 = await ze1.get_messages('@vdamkbot', limit=1)
        await msg0[0].click(1)
        await asyncio.sleep(4)
        msg1 = await ze1.get_messages('@vdamkbot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await ze1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await ze1.send_message(event.chat_id, f"تم الانتهاء من التجميع | SY")

                break
            message_text = msgs.message
            channel_username = message_text.split('@')[-1]
            try:
                try:
                    await ze1(JoinChannelRequest(channel_username))
                except:
                    bott = channel_username.split('+')[-1]
                    await ze1(ImportChatInviteRequest(bott))
                msg2 = await ze1.get_messages('@vdamkbot', limit=1)
                await msg2[0].click(text='اشتركت ✅')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await ze1.get_messages('@vdamkbot', limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await ze1.send_message(event.chat_id, "تم الانتهاء من التجميع | SY")





@ze1.on(events.NewMessage(outgoing=False, pattern='/trbefer (.*)'))
async def OwnerStart(event):
    user = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري التحويل")
        await event.edit("جاري التحويل")
        joinu = await ze1(JoinChannelRequest('Source_Ze'))
        channel_entity = await ze1.get_entity('@vdamkbot')
        await ze1.send_message('@vdamkbot', '/start')
        await asyncio.sleep(4)
        msg0 = (await ze1.get_messages('@vdamkbot', limit=1))[0]
        msg_text = msg0.message
        points_line = [line for line in msg_text.split('\n') if 'نقاطك' in line][0]
        points = int(points_line.split(':')[1].strip())
        msg1 = (await ze1.get_messages('@vdamkbot', limit=1))[0]
        await msg1.click(4)
        await ze1.send_message('@vdamkbot', f'{user}')
        
        await ze1.send_message('@vdamkbot', f'{points}')



@ze1.on(events.NewMessage(outgoing=False, pattern='/jdhncww'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع الهدية")
        await event.edit("جاري تجميع الهدية")
        joinu = await ze1(JoinChannelRequest('Source_Ze'))
        channel_entity = await ze1.get_entity('@vdamkbot')
        await ze1.send_message('@vdamkbot', '/start')
        await asyncio.sleep(4)
        msg0 = await ze1.get_messages('@vdamkbot', limit=1)
        await msg0[0].click(1)
        await asyncio.sleep(4)
        msg1 = await ze1.get_messages('@vdamkbot', limit=1)
        await msg1[0].click(2)
        
@ze1.on(events.NewMessage(outgoing=False, pattern='^/agift (.*)'))
async def OwnerStart(event):
    pot = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع الهدية")
        await event.edit("جاري تجميع الهدية")
        joinu = await ze1(JoinChannelRequest('Source_Ze'))
        channel_entity = await ze1.get_entity(pot)
        await ze1.send_message(pot, '/start')
        await asyncio.sleep(4)
        msg0 = await ze1.get_messages(pot, limit=1)
        await msg0[0].click(6)
        

@ze1.on(events.NewMessage(outgoing=False, pattern='/agiacode (.*)'))
async def OwnerStart(event):
    cod = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع نقاط الكود")
        await event.edit("جاري تجميع نقاط الكود")
        joinu = await ze1(JoinChannelRequest('Source_Ze'))
        channel_entity = await ze1.get_entity('@vdamkbot')
        await ze1.send_message('@vdamkbot', '/start')
        await asyncio.sleep(4)
        msg0 = await ze1.get_messages('@vdamkbot', limit=1)
        await msg0[0].click(3)
        await asyncio.sleep(4)
        msg1 = await ze1.get_messages('@vdamkbot', limit=1)
        await ze1.send_message('@vdamkbot', f'{cod}')

@ze1.on(events.NewMessage(outgoing=False, pattern=r'^/forward (.*)'))
async def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        sing = await ze1.send_message(event.chat_id, f"**❈ حسناً سوف اقوم بتحويل اخر 5 رسائل\n❈ من المستخدم {userbott}**")
        msgs = await ze1.get_messages(userbott, limit=6)
        if msgs:
            message_text = "forward-\n\n"
            for i, msg in enumerate(msgs):
                message_text += f"**\n{i+1} :**\n " + msg.text + "\n"
            await ze1.send_message(ownerhson_id, message_text)




@ze1.on(events.NewMessage(outgoing=False, pattern=r'^/button (.*) (.*)'))
async def OwnerStart(event):
    userbt = event.pattern_match.group(1) 
    bt = int(event.pattern_match.group(2))
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     
     sleep(2)
    msg1 = await ze1.get_messages(userbt, limit=1)
    await msg1[0].click(bt)
    await ze1.send_message(event.chat_id, f"**❈ حسناً قمت بالنقر على الزر رقم {bt}**")
        

print('  ')
print('  ')
print("❖ Ze Userbot Running  ")
print('  ')
ze1.loop.run_until_complete(main())
ze1.run_until_disconnected()



#the code py ze tm



            

            
