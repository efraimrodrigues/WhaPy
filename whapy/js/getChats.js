Chats = Store.Chat.models;
ChatsId = [];

for(var i=0; i<Chats.length; i++)
    ChatsId.push(Chats[i].id);
return ChatsId;