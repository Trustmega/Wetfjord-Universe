# tmp
# Work with Python 3.6
from typing import List

import discord
import subprocess
import random
import a2s
import asyncio
import os.path
from hansibotConfig import *


address_hl2dm = ("wetfjord.eu", 27020)
address_tf2 = ("wetfjord.eu", 27015)
address_arma3 = ("wetfjord.eu", 2303)

print(discord.__version__)

client = discord.Client()

async def update_now_playing():
    await client.wait_until_ready()
    while not client.is_closed():
        # hl2dm
        players_hl2 = (a2s.players(address_hl2dm))
        player_count_hl2 = len(players_hl2)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
                                                               name="{} players in HL2:DM".format(
                                                                   player_count_hl2)))
        await asyncio.sleep(10)

        # tf2
        players_tf2 = (a2s.players(address_tf2))
        player_count_tf2 = len(players_tf2)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
                                                               name="{} players in TF2".format(player_count_tf2)))
        await asyncio.sleep(10)

        # Arma3
        players_arma3 = (a2s.players(address_arma3))
        player_count_arma3 = len(players_arma3)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
                                                               name="{} players in Arma 3".format(
                                                                   player_count_arma3)))
        await asyncio.sleep(10)

    while not client.is_closed():
        #hl2dm
        players_hl2 = (a2s.players(address_hl2dm))
        player_count_hl2 = len(players_hl2)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
                                                               name="{} players in HL2:DM".format(player_count_hl2)))
        await asyncio.sleep(10)

        #tf2
        players_tf2 = (a2s.players(address_tf2))
        player_count_tf2 = len(players_tf2)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
                                                               name="{} players in TF2".format(player_count_tf2)))
        await asyncio.sleep(10)

        #Arma3
        players_arma3 = (a2s.players(address_arma3))
        player_count_arma3 = len(players_arma3)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
                                                               name="{} players in Arma 3".format(player_count_arma3)))
        await asyncio.sleep(10)


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    #get the channel the message was sent in
    channel = message.channel

    # Everything in this if-statement is for universe-admins and universe-mods only:
    if staff[0] in [y.id for y in message.author.roles] or staff[1] in [y.id for y in message.author.roles]:
        if message.content.startswith('!foradminsonly'):
            msg = '{0.author.mention} is an admin'.format(message)
            await channel.send(msg)
            #await channel.send(message.channel, msg)

        if message.content.startswith('!whitelist add'):
            content = message.content.split()
            msg = 'Whitelisting {}'.format(content[2], message)
            await channel.send(msg)
            whitelistingOutput = subprocess.check_output([whitelistScript, content[2]], stderr=subprocess.STDOUT).decode('utf-8')
            msg = 'Output terminal: {}'.format(whitelistingOutput, message)
            await channel.send(msg)

        if message.content.startswith('!ip'):
            ipOutput = subprocess.check_output([curl, ipsite], stderr=subprocess.STDOUT).decode('utf-8')
            msg = 'Output terminal: {}'.format(ipOutput, message)
            await channel.send(msg)

        if "!HeilHansi" in message.content:
            msg = 'Danke schön {0.author.mention}! https://wetfjord.eu/heilhansi.png '.format(message)
            await channel.send(msg)

        if "!ComradeHansi" in message.content:
            comrade_list = ['Yes comrade?', 'Heil H... Stalin!', 'knock knock who\'s there? COMRADE HANSI!', 'cyka blyat {}'.format(message.author.mention)]
            comrade_item = random.choice(comrade_list)
            msg = '{} https://wetfjord.eu/comradehansi.png '.format(comrade_item, message)
            await channel.send(msg)

    ###### non-admin commands: ######
    if "hansi sucks" in message.content:
        msg = 'You said fucking wut m8?! Fight me bitch'.format(message)
        await channel.send(msg)

    if "!commanderhansi" in message.content:
        commander_list = ['Yes comrade?', 'Well no shit. What\'ve we\'ve got here? A fucking comedian, Private Joker.', 'knock knock who\'s there? COMMANDER HANSI!', 'I bet you\'re the kind of guy that would f-ck a person in the ass and not even have the goddamn common courtesy to give him a reach-around. I\'ll be watching you {}'.format(message.author.mention)]
        commander_item = random.choice(commander_list)
        msg = ' https://wetfjord.eu/commanderhansi.png {}'.format(commander_item, message)
        await channel.send(msg)

###### Specific channels: ######
    ##hl2:dm & tf2##
    if message.channel.id == 237233849820512267:
        if message.content.startswith('!on_hl2'):
            players = (a2s.players(address_hl2dm))
            player_count = len(players)
            players_and_score = ""
            for player in players:
                playtime_minutes = player.duration / 60
                players_and_score += player.name + "\t \t" + str(player.score) + "\t \t" + str(playtime_minutes) + "\n"
            msg = '``` Players online: {} \n Name \t \t Score \t \t Playtime (minutes) \n {} ```'.format(player_count, players_and_score)
            await channel.send(msg)

        if message.content.startswith('!on_tf2'):
            players = (a2s.players(address_tf2))
            player_count = len(players)
            players_and_score = ""
            for player in players:
                playtime_minutes = player.duration / 60
                players_and_score += player.name + "\t \t" + str(player.score) + "\t \t" + str(playtime_minutes) + "\n"
            msg = '``` Players online: {} \n Name \t \t Score \t \t Playtime (minutes) \n {} ```'.format(player_count, players_and_score)
            await channel.send(msg)

    ##Arma3##
    if message.channel.id == 250269739220336642:
        if message.content.startswith('!on'):
            players = (a2s.players(address_arma3))
            game_info = (a2s.info(address_arma3))
            player_count = len(players)
            players_and_score = ""
            for player in players:
                playtime_minutes = player.duration / 60
                players_and_score += player.name + "\t \t" + str(player.score) + "\t \t" + str(playtime_minutes) + "\n"
            msg = '``` Map: {} \n Game: {} \n \n Players online: {} \n Name \t \t Score \t \t Playtime (minutes) \n {} ```'.format( game_info.map_name, game_info.game, player_count, players_and_score)
            await channel.send(msg)

        if message.content.startswith('!restart'):
            if not os.path.exists('/tmp/please_restart_arma3')
                msg = 'Restarting Arma3 server, hold on..'.format(message)
                await channel.send(msg)
                subprocess(['touch', '/tmp/please_restart_arma3'])
                await asyncio.sleep(60)
                subprocess(['rm', '/tmp/please_restart_arma3'])
            else
                msg = 'Restart already in progress, take a chill pill :hansi: '.format(message)
                await channel.send(msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.loop.create_task(update_now_playing())
client.run(TOKEN)