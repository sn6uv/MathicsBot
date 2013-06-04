import socket

server = "irc.freenode.org"
channel = "#mathics"
botnick = "MathicsBot"
realname = "Mathics Bot"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

irc.connect((server, 6667))
irc.send("USER {0} {0} {0} :{1}\n".format(botnick, realname))
irc.send("NICK {0}\n".format(botnick))
irc.send("JOIN {0}\n".format(channel))

while True:
    text = irc.recv(2048)
    print text
