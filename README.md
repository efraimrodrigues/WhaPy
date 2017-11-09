[![Documentation Status](https://readthedocs.org/projects/whapy/badge/?version=latest)](http://whapy.readthedocs.io/en/latest/?badge=latest)

Checkout the [documentation][doc].

[doc]: http://whapy.readthedocs.io/
    
## Quick Example
```py
import whapy

whatsapp = whapy.WhaPy(whapy.Browser.firefox)

@whatsapp.event
async def on_message(chat, messages):
    print("New messages arrived: ")
    for i in range(0,len(messages)):
        if not messages[i].isMedia():
            print(messages[i].getContent())
            if messages[i].getContent() == "@who":
                chat.sendMessage("are you?")

@whatsapp.event
async def on_ready():
    print("Let's go!")

whatsapp.run()
```

## Dependencies

- Python 3.4.2+
- `selenium` library
- [a webdriver] (http://selenium-python.readthedocs.io/installation.html#drivers)