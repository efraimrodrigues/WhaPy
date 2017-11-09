import whapy

whatsapp = whapy.WhaPy(whapy.Browser.firefox)

@whatsapp.event
async def on_message(chat, messages):
    print("New messages arrived: ")
    for i in range(0,len(messages)):
        if not messages[i].is_media():
            print(messages[i].get_content())
            if messages[i].get_content() == "@who":
                chat.send_message("are you?")

@whatsapp.event
async def on_ready():
    print("Let's go!")

whatsapp.run()