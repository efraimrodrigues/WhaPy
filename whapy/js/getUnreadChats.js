Chats = Store.Chat.models;
UnreadChats = [];

for(var i=0; i<Chats.length; i++)
    if(Chats[i].hasUnread)
        UnreadChats.push(Chats[i].id);
return UnreadChats;