# SPDX-License-Identifier: MIT
# Copyright (c) 2015-2025 Andrii Andrushchyshyn

import os
import tempfile
import platform
import json
import BigWorld
import Keys

from external_strings_utils import unicode_from_utf8
from . import __version__

DEFAULT_CONFIG = {
	"version": 1,
	"channels": [
		{
			"displayName": "netradio.by/wot",
			"stream_url": "http://sv.netradio.by:8061/128",
			"ext_url": "https://netradio.by/wot",
			"tags_url": "http://sv.netradio.by:81/broad.xml"
		}
	]
}

DEFAULT_BINDINGS = {
	'previosChannel': [Keys.KEY_PGDN],
	'nextChannel': [Keys.KEY_PGUP],
	'toggleRadio': [Keys.KEY_F9],
	'volumeDown': [Keys.KEY_F11],
	'volumeUp': [Keys.KEY_F12]
}

DEFAULT_SETTINGS = {
	'saveVolume': True,
	'lastVolume': 0.5,
	'saveChannel': True,
	'lastChannel': 0,
	'muteOnVoip': False,
	'autoPlay': False,
	'showBattleTips': True,
	'muteOnMinimize': True,
	'keyBindings': DEFAULT_BINDINGS
}

DEFAULT_CACHE = {}

CLIENT_ROOT_PATH = '.' if os.path.isfile('./paths.xml') else '..'
CONFIGS_PATH = '{}/mods/configs/NetRadio/'.format(CLIENT_ROOT_PATH)

def _load_config_url():
	try:
		with open(CONFIGS_PATH + 'NetRadio.json', 'r') as f:
			config = json.load(f)
			config_url = config['config_url']
			print("[NetRadio] Config founded, URL: {}".format(config_url))
			return config_url
	except:
		print("[NetRadio] Config not founded. Path: {}".format(CONFIGS_PATH + 'NetRadio.json'))
		return None

class CONFIG:
	SAVE_SETTINGS = True
	SAVE_CACHE = True
	CONFIG_URL = _load_config_url()
	EXPIRE_TIME = 24

class PLAYER_STATUS:
	INITED = 'inited'
	ERROR = 'error'
	PLAYING = 'playing'
	STOPPED = 'stopped'

class PLAYER_COMMANDS:
	INIT = 'init'
	ADD_CHANNELS = 'add_channels'
	PLAY = 'play_channel'
	STOP = 'stop'
	VOLUME = 'volume'
	TEST = 'test'
	EXIT = 'exit'

class BUTTON_STATES:
	NORMAL = 'normal'
	SELECTED = 'selected'
	NORMAL_DISABLED = NORMAL + 'disabled'
	SELECTED_DISABLED = SELECTED + 'disabled'

class HOTKEYS_COMMANDS:
	START_ACCEPT = 'startAccept'
	STOP_ACCEPT = 'stopAccept'
	DEFAULT = 'default'
	CLEAN = 'clean'

BROADCAST_INTERVAL = 300
TAGS_UPDATE_INTERVAL = 20
VOLUME_STEP = 0.1
VOLUME_STEP_LOW = 0.05
VOLUME_STEP_VERY_LOW = 0.02

USER_AGENT = 'NetRadio-RadioPlayer/' + __version__

LOBBY_WINDOW_UI = 'NetRadioLobby'
BATTLE_INJECTOR_UI = 'NetRadioBattleInjector'
BATTLE_COMPONENT_UI = 'NetRadioBattle'

LANGUAGE_FILES = 'mods/me.poliroid.netradio/text'
LANGUAGE_DEFAULT = 'en'
LANGUAGE_FALLBACK = ('en', 'ru', 'ua', )

SETTINGS_FILE = os.path.normpath(os.path.join(CONFIGS_PATH, 'setting.dat'))
CACHE_FILE = os.path.normpath(os.path.join(CONFIGS_PATH, 'cache.dat'))
CONFIG_CACHE_FILE = os.path.normpath(os.path.join(CONFIGS_PATH, 'config.dat'))

TEMP_DATA_FOLDER = os.path.normpath(os.path.join(tempfile.gettempdir(), 'world_of_tanks', 'netradio'))
TEMP_DATA_FOLDER_VFS = 'mods/me.poliroid.netradio/temp'

CONSOLE_PLAYER = os.path.normpath(os.path.join(TEMP_DATA_FOLDER, 'win64', 'net_radio_player.exe'))
MAX_RESTART_ATTEMPS = 10

# (r, g, b) color to AS3 Flash RGBHEX(uint)
DEFAULT_BATTLE_MESSAGE_COLOR = 116 << 16 | 199 << 8 | 48
DEFAULT_BATTLE_MESSAGE_LIFETIME = 6000

SETTINGS_VERSION = 1

UI_VOLUME_MULTIPLIYER = 10.0