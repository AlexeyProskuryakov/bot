import requests

import properties
__author__ = '4ikist'

class BotEngine(object):
    def __init__(self):
        pass

    def login(self, user_login, user_pass):
        response = requests.get(properties.target_url)
        print response

if __name__ == '__main__':
    bn = BotEngine()
    bn.login(user_login='stack2009@gmail.com', user_pass='sederfes')
