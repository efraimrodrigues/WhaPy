Chats = Store.Chat.models;

for(var i=0; i<Chats.length; i++)
    if(Chats[i].hasUnread)
        return true;
return false;