import time
from datetime import datetime as dt
host_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
websites=["facebook.com","www.facebook.com","filehippo.com","www.filehippo.com"]
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("\nWorking Hours...")
        with open(host_path,"r+") as file:
            content=file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write("\n" + redirect + " " + website)
    else:
        print("\nFun Hours...")
        with open(host_path,"r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
    time.sleep(5)
