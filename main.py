from colored import fg
import requests
import os
os.system("title Kyoto Token Checker - Akiko#4200")
color = fg("red_3a")
working = open("hits.txt","w")

print(fg("44") + "██╗  ██╗██╗   ██╗ ██████╗ ████████╗ ██████╗ ")
print(fg("45") + "██║ ██╔╝╚██╗ ██╔╝██╔═══██╗╚══██╔══╝██╔═══██╗")
print(fg("46") + "█████╔╝  ╚████╔╝ ██║   ██║   ██║   ██║   ██║")
print(fg("47") + "██╔═██╗   ╚██╔╝  ██║   ██║   ██║   ██║   ██║")
print(fg("48") + "██║  ██╗   ██║   ╚██████╔╝   ██║   ╚██████╔╝")
print(fg("49") + "╚═╝  ╚═╝   ╚═╝    ╚═════╝    ╚═╝    ╚═════╝ ")
print("""


""")
input("Press ENTER to start...")
print("""


""")
with open("tokens.txt") as lines:
    for line in lines:
        token = line.strip("\n")
        headers = {'Content-Type': 'application/json', 'authorization': token}
        url = "https://discordapp.com/api/v6/users/@me/library"
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            print("[+] " + token)
            working.write(token + "\n")
        else:
            print("[-] "  + token)
print("""

""")
input("Results saved in hits.txt")
