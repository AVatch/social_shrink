# -*- coding: utf-8 -*-
"""Create an application instance."""
from flask.helpers import get_debug_flag

from socialShrink.app import create_app
from socialShrink.settings import DevConfig, ProdConfig

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


CONFIG = DevConfig if get_debug_flag() else ProdConfig

app = create_app(CONFIG)
