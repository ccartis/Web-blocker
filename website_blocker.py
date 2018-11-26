import time
from datetime import datetime as dt

host_temp=r"C:\Users\noblegas\Desktop\Mega_python_projects\application_3_build_a_website_blocker\hosts.txt"
host_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","dub119.mail.live.com","www.dub119.mail.live.com"]

while True:
    if  dt(dt.now().year,dt.now().month,dt.now().day,19)<dt.now()< dt(dt.now().year,dt.now().month,dt.now().day,20):
        print("Working hours...")
        with open(host_path,'r+') as file:
            content=file.read()
            # print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+"   "+website+"\n")

    else:
        with open(host_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()

        print("Fun hours..")

    time.sleep(4)
