from datetime import datetime as dt
import time

host='/etc/hosts'
websites = ["www.instagram.com","instagram.com", "youtube.com","www.youtube.com"]
redirect = '127.0.0.1'


'
def block(hour1:int,hour2:int):
    while True:
        if dt(dt.now().year, dt.now().month, dt.now().day, hour1) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, hour2 ):
            # open and read host file (r+ allows reading and writing)
            with open(host,'r+') as file:
                # content within host file
                # host file will contain websites that local host cannot gather information from
                content = file.read()
                for website in websites:
                    # check list of websites to see if website is in the list redirected list (redirected url in front of website url)
                    # if website url is in host folder, do nothing
                    # if website url is not in host folder, add it
                    if website in content:
                        # do nothing; website in host folder (to be blocked)
                        pass
                    else:
                        # if website url is not in folder, write the website url to folder
                        file.write(redirect + " " + website + "\n")
        # time allotted to access url information
        else:
            with open(host, 'r+') as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in websites):
                        file.write(line)
                file.truncate()
    time.sleep(5)
