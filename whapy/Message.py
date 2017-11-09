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

class Message:
    """Represents a whatsapp message.
    """
    #MessageId is the serialized version of the msg: msg.id._serialized
    def __init__(self, driver, messageId):
        self.__driver = driver
        self.messageId = messageId

    def _parseQuery(self):
        return "return Store.Msg.find('" + self.messageId + "')._value."

    def _parseAction(self):
        return "Store.Msg.find('" + self.messageId + "')._value."

    def get_content(self):
        """Returns the content of the message
        """
        return self.__driver.execute_script(self._parseQuery() + "__x_body")

    def get_author(self):
        """Returns the author (contactId) of the message
        """
        return self.__driver.execute_script(self._parseQuery() + "author")

    def get_from(self):
        """Returns the author (contactId) of the message. If message was sent in a group, the author is the group chat id
        """
        return self.__driver.execute_script(self._parseQuery() + "__x_from")

    def is_group_message(self):
        """Returns True if group message, False otherwise
        """
        return self.__driver.execute_script(self._parseQuery() + "__x_isGroupMsg")

    def is_link(self):
        """Returns True if message is a link, False otherwise
        """
        return self.__driver.execute_script(self._parseQuery() + "__x_isLink")
    
    def is_media(self):
        """Returns True if message is a media, False otherwise
        """
        return self.__driver.execute_script(self._parseQuery() + "__x_isMedia")

    def is_quoted_msg(self):
        """Returns True if message is a quoted message, False otherwise
        """
        if self.__driver.execute_script(self._parseQuery() + "__x_quotedMsg"):
            return True
        else:
            return False
    
    def get_quoted_msg(self):
        """Returns the actually quoted message
        """
        return self.__driver.execute_script(self._parseQuery() + "__x_quotedMsg")

    def get_quoted_participant(self):
        """Returns the author (contact id) of the quoted message 
        """
        return self.__driver.execute_script(self._parseQuery() + "__x_quotedParticipant")
