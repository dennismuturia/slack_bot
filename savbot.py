import os
import datetime
import random
import re
from slackclient import SlackClient

#Lets instantiate the slack variable
slack_client = SlackClient(os.environ.get(SLACK_USER_TOKEN))

#This is the bot's user id that is on the slack API. THis value is assigned when the bot starts up
starterbot_id = None

#Constants
RTM_READ_DELAY = 1 #1 second delay when reading the RTM

