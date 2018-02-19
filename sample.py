import whapy

wap = whapy.WhaPy(whapy.Browser.chrome,False)

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