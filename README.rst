[![Documentation Status](https://readthedocs.org/projects/whapy/badge/?version=latest)](http://whapy.readthedocs.io/en/latest/?badge=latest)

Checkout the [documentation][doc].

[doc]: http://whapy.readthedocs.io/
    
## Quick Example
```py
import whapy

wap = whapy.WhaPy(whapy.Browser.firefox, True)

@wap.event
async def on_message(chat, messages):
    print("New messages arrived: ")
    for i in range(0,len(messages)):
        if not messages[i].is_media():
            print(messages[i].get_content())
            if messages[i].get_content() == "@who":
                chat.send_message("are you?")

@wap.event
async def on_ready():
    print("Logged in as " + wap.get_me())

wap.run()
```

## Dependencies

- Python 3.4.2+
- `selenium` library
- `a webdriver` (http://selenium-python.readthedocs.io/installation.html#drivers)