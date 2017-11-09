.. currentmodule:: whapy

API Reference
===============

WhaPy
-------

.. autoclass:: WhaPy
    :members:

Event Reference
---------------

This page outlines the different types of events listened by :class:`WhaPy`.

This is an example of how to register an event: ::

    from WhaPy import WhaPy

    @asyncio.coroutine
    async def on_message(chat, messages):
        for i in range(0,len(messages)):
        if not messages[i].isMedia():
            print(messages[i].getContent())
            if messages[i].getContent() == "@who":
                chat.sendMessage("are you?")

.. warning::

    All the events must be a |corourl|_. If they aren't, then you might get unexpected
    errors. In order to turn a function into a coroutine they must either be decorated
    with ``@asyncio.coroutine`` or in Python 3.5+ be defined using the ``async def``
    declaration.

    The following two functions are examples of coroutine functions: ::

        async def on_ready():
            pass

        @asyncio.coroutine
        def on_ready():
            pass

.. function:: on_ready()

    Called after scanning QR Code and Whatsapp page is ready. Chats and messages are filled up.

.. function:: on_message(chat, messages)

    Called each time unread messages are detected. 

    :param chat: A :class:`Chat` of the chat which fired the event.
    :param messages: An array of :class:`Message`.


Enumeration
-------------

The API provides a enumeration for browser selection.

All enumerations are subclasses of `enum`_.

.. _enum: https://docs.python.org/3/library/enum.html

.. class:: Browser

    Specifies the browser application will execute on.

    .. note::
        Drivers are required to interface with the chosen browser. Make sure it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin.

        Drivers' information and download links: http://selenium-python.readthedocs.io/installation.html#drivers

    .. attribute:: chrome

        Google Chrome browser.
    .. attribute:: edge

        Microsoft Edge.
    .. attribute:: firefox

        Mozilla Firefox.
    .. attribute:: safari

        Safari browser.

Data Classes
--------------

Classes that represent chats and messages in whatsapp web.

Chat
~~~~~

.. autoclass:: Chat()
    :members:

Message
~~~~~~~

.. autoclass:: Message()
    :members: