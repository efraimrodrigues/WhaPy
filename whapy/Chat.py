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

from .Message import Message

class Chat:
    """Represents a whatsapp chat and allows chat management.
    """
    #Driver will allow methods to manage chats; Chat is a selenium element
    def __init__(self, driver, chatId):
        self.__driver = driver
        self.chatId = chatId

    def _parseQuery(self):
        return "return Store.Chat.find('" + self.chatId + "')._value."

    def _parseAction(self):
        return "Store.Chat.find('" + self.chatId + "')._value."

    #Sends a message to the chat
    def send_message(self, message):
        """Sends a message to this chat

        :param message: A str to be sent to this chat
        """
        self.__driver.execute_script(self._parseAction() + "sendMessage('" + message + "')")

    #Returns the title of the chat
    def get_title(self):
        """Returns the title of the chat
        """
        return self.__driver.execute_script(self._parseQuery() + "title()")

    #Returns the number of unread messages
    def count_unread(self):
        """Returns the number of unread messages in this chat
        """
        return self.__driver.execute_script(self._parseQuery() + "unreadCount")

    #Returns the number of loaded messages
    def count_loaded_msgs(self):
        """Returns the number of loaded messages in this chat
        """
        return self.__driver.execute_script(self._parseQuery() + "msgs.length")

    #Returns the last N messages
    def get_last_n_messages(self, number):
        """Returns the last N messages

        :param number: int referring to the number of messages to retrieved
        """
        messages = []

        for i in range(1,number+1)[::-1]:
            query = self._parseQuery() + "msgs.models[" + str(int(self.count_loaded_msgs()) - i) + "].id._serialized"
            messageId = self.__driver.execute_script(query)
            messages.append(Message(self.__driver, messageId))

        return messages

    #Loads earlier msgs. This is useful to make some statistic about the chat. Loaded messages are stored in session
    #To get loaded messaegs use Chat.getLastNMessages(Chat.countLoadedMsgs())
    def load_earlier_msgs(self):
        """Not all chat's messages are loaded at once. They're loaded in batches, so this will ask for more messages.
        This will not return anything, but allow more messages to be retrieved
        """
        self.__driver.execute_script(self._parseAction() + "loadEarlierMsgs()")

    #Returns true if the chat has been viewed
    def viewed(self):
        """Returns true if the chat has been viewed
        """
        return self.__driver.execute_script(self._parseQuery() + "viewed")

    #Pins or unpins a chat according to the parameter
    def set_pin(self,boolean):
        """Pins or unpins a chat according to the parameter

        :param boolean: True for pinning and False otherwise
        """
        if type(boolean) == type(True):
            self.__driver.execute_script(self._parseAction() + "setPin(" + boolean + ")")
        else:
            raise ValueError('boolean parameter invalid type, give me a boolean.')

    #Returns true if the chat is a group
    def is_group(self):
        """Returns true if the chat is a group
        """
        return self.__driver.execute_script(self._parseQuery() + "isGroup")

    #Mark the chat as seen
    def mark_seen(self):
        """Mark the chat as seen
        """
        self.__driver.execute_script(self._parseAction() + "markSeen()")

    #Mark the chat as unseen
    def mark_unseen(self):
        """Mark the chat as unseen
        """
        self.__driver.execute_script(self._parseAction() + "markUnseen()")

    #Returns true is the chat is muted
    def is_mute(self):
        """Returns true is the chat is muted
        """
        return self.__driver.execute_script(self._parseQuery() + "mute.__x_isMuted")

    #Mute the chat for a certain time
    def mute(self,time):
        """Mute the chat for a certain time

        :param time: Time for keeping chat muted
        """
        self.__driver.execute_script(self._parseAction() + "mute.mute(" + time + ")")

    #Unmutes the chat
    def unmute(self):
        """Unmutes the chat
        """
        self.__driver.execute_script(self._parseAction() + "mute.unmute()")

    #Sends the specified contact to the chat
    def send_contact(self, contactId):
        """Sends the specified contact to the chat

        :param contactId: Contact identification to be sent
        """
        self.__driver.execute_script(self._parseAction() + "sendContact(Store.Contact.find(" + contactId + ")._value)")

    #Deletes messages but doesn't leave group
    def delete(self):
        """Deletes messages but doesn't leave group
        """
        self.__driver.execute_script(self._parseAction() + "delete()")

    #This will tag chat as spam. User will leave and delete chat. All messages will be deleted
    def report_spam(self):
        """This will tag chat as spam. User will leave and delete chat. All messages will be deleted
        """
        self.__driver.execute_script(self._parseAction() + "sendContact(Store.Contact.find(" + contactId + ")._value)")
    
    