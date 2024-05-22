#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6501548699:AAEIsN52Q4ZZagVFO8HTO1XCKjuVON-qhpQ")
    API_ID = int(os.environ.get("API_ID", "11657097"))
    API_HASH = os.environ.get("API_HASH", "7198384c0cc8cb877e4731d14e2dd7b8")
    AUTH_USERS = "1085174050"

