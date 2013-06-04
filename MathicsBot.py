import socket
import datetime

# settings
server = "irc.freenode.org"
channel = "#mathics"
botnick = "MathicsBot"
realname = "Mathics Bot"
logname = "mathics.log"

# setup connection
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, 6667))
irc.send("USER {0} {0} {0} :{1}\n".format(botnick, realname))
irc.send("NICK {0}\n".format(botnick))
irc.send("JOIN {0}\n".format(channel))


def privmsg(msg):
    irc.send("PRIVMSG {0} {1}\n".format(channel, msg))


def logline(msg, suffix="\n"):
    with open(logname, "a") as logfile:
        logfile.write(msg + suffix)


buf = ""
while True:
    buf += irc.recv(2048)
    tmp = buf.split("\n")
    buf = tmp.pop()

    for line in tmp:
        line = line.split(" ", 3)

        if line[0] == "PING":
            irc.send("PONG {0}\r\n".format(line[1]))
        elif line[1] == "PRIVMSG":
            usr, msg = line[0][1:], line[3][1:]

            nick = usr.split("!~")[0]
            curtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(logname, "a") as logfile:
                logfile.write("[{0}] {1}: {2}\n".format(curtime, nick, msg))
