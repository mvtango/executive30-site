import os
import socket


_me=socket.gethostname()
_here=os.path.split(__file__)[0]

from config_events import events

class Config(object):
    DEBUG = False
    TESTING = False
    # DATABASE_PATH = os.path.join(_here,"data","stats.sqlite")
    # STORE=DumpTruck(dbname=DATABASE_PATH)
    HOME=_here
    EVENTS=events
    FREEZER_RELATIVE_URLS=True
    FREEZER_BASE_URL="http://apps2.dpa-newslab.com/"
    FREEZER_DESTINATION="../site/apps"
    FREEZER_REMOVE_EXTRA_FILES=True
    

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
	DEBUG = True
	TESTING = True 

if _me in ('martin-UX21A' , ) :
	Config=DevelopmentConfig
	
