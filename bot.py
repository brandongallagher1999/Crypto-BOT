import discord
from twilio.rest import Client



class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))


    async def on_voice_state_update(random, member, before, after):
        user = member.display_name
        sendText(user, after)

        print(after.channel)


    async def on_message(self, message):
        channel = message.channel

        if message.content == "testing":
            await channel.send("reply!")
        

def open_file(string):
    file = open(string, "r")
    text = file.read()
    file.close()
    return text

def read_phone(arg):
    file = open("phone.txt", "r")
    text = file.read()
    final = text.splitlines()
    file.close()
    return final[arg]

def sendText(user, after):
    if (str(after.channel) != "None"):
        account_sid = open_file("account_sid.txt")
        auth_token = open_file("account_token.txt")
        client1 = Client(account_sid, auth_token)

        string = user + " has joined " + str(after.channel) + " voice channel in your server!"

        message = client1.messages \
        .create(
            body= string,
            from_= read_phone(0),
            to=read_phone(1)
        )

client = MyClient()
client.run(open_file("token.txt"))