"""
The MIT License (MIT)

Copyright (c) 2017-2017 Efraim Rodrigues

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""


#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import os
import asyncio

from .Chat import Chat
from .Message import Message
from .Enums import Browser

class WhaPy:
    """Represents the current whatsapp session.

    This class is intended to give a python interface to interact with whatsapp web.
    """
    def __init__(self,browser,loop=None):
        try:
            self.script_path = os.path.dirname(os.path.abspath(__file__))
        except NameError:
            self.script_path = os.getcwd()

        self.loop = asyncio.get_event_loop()

        if browser == Browser.chrome:
            self._driver = webdriver.Chrome()
        elif browser == Browser.firefox:
            self._driver = webdriver.Firefox()
        elif browser == Browser.safari:
            self._driver = webdriver.Safari()
        elif browser == Browser.edge:
            self._driver = webdriver.Edge()
        else:
            raise ValueError('Unknown browser parameter.')

        self._driver.get("https://web.whatsapp.com/")

        #Waits until QR Code is scan
        while self._driver.find_elements_by_class_name("_2EZ_m"):
            self._driver.save_screenshot("qrcode.png")
            print("Scan QR Code!",end='')
            print('\r',end='')
        
        #Wait until chats are loaded
        element = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "chat"))
        )

    def event(self, coro):
        """A decorator that registers an event to listen to.

        Example
        ---------

        Using the basic :meth:`event` decorator: ::

            @whatsapp.event
            @asyncio.coroutine
            def on_message(chat, messages):
                print('Received a message!')
        """

        if not asyncio.iscoroutinefunction(coro):
            raise ClientException('event registered must be a coroutine function')

        setattr(self, coro.__name__, coro)
        return coro

    @asyncio.coroutine
    def start(self):
        if hasattr(self, "on_ready"):
            yield from getattr(self, "on_ready")()

        while True:
            has_unread = False
            try:
                has_unread = self.has_unread()
            except:
                pass

            if has_unread:
                yield from self._parse_message()

    def run(self):
        """Starts listening to events
        """
        try:
            self.loop.run_until_complete(self.start())
        finally:
            self.loop.close()

    #Parse message will get the first occurrency of a unread message, will return a Chat object and author's id
    @asyncio.coroutine
    def _parse_message(self):
        unread_chat = Chat(self._driver, self.get_unread_chats()[0])
        
        #It turns out chats are load with only one message and then more messages are loaded, so make it wait
        if unread_chat.count_unread() >= unread_chat.count_loaded_msgs():
            pass
        else:
            unread_messages = unread_chat.get_last_n_messages(unread_chat.count_unread())

            #This will process the chat as so it won't get here again because of the same messages
            unread_chat.mark_seen()

            yield from getattr(self, "on_message")(unread_chat, unread_messages)

    def has_unread(self):
        """Returns True whenever there are unread messages
        """
        script = open(os.path.join(self.script_path, "js/hasUnread.js"), "r").read()
        return self._driver.execute_script(script)

    def get_unread_chats(self):
        """Returns an array of unread chats' id
        """
        script = open(os.path.join(self.script_path, "js/getUnreadChats.js"), "r").read()
        return self._driver.execute_script(script)

    def get_chats_id(self):
        """Returns an array of all chats' id. Use instantiateChat to have access to :class:`Chat` methods
        """
        script = open(os.path.join(self.script_path, "js/getChats.js"), "r").read()
        return self._driver.execute_script(script)

    def instantiate_chat(self,chatId):
        """Returns a :class:`Chat` class

        :param chatId: Chat identification
        """
        return Chat(self._driver, chatId)

    #Set bot's status
    def set_status(self, status):
        """Sets bot status
        :param status: A string containing the new status
        """
        self._driver.execute_script("Store.Status.setMyStatus(" + status + ")")
        
    #Leaves a group
    def leave_group(self, chatId):
        """Leaves a group
        :param chatId: Chat identification
        """
        self._driver.execute_script("Store.Wap.leaveGroup(" + chatId + ")")