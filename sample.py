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