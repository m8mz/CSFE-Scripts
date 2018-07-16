import requests, pickle, os, time, hashlib
from getpass import getpass
from bs4 import BeautifulSoup
HOME = os.environ['HOME']

def login():    
    s = requests.session()
    csfepass = getpass("Password: ")
    try:
        with open(HOME + '/passwd/encrypted_pass.txt', 'r') as enc_pass:
            pass_ = enc_pass.readline()
            while hashlib.md5(csfepass.encode('utf8')).hexdigest() != pass_.strip('\n'):
                print("Incorrect Password.")
                csfepass = getpass("Password: ")
            creds = {"oss_user_name": "mhancock-gaillard", "oss_password": csfepass, "oss_login": "Login"}
            url = "https://enduranceoss.com/cs/oss_login.html"
            r = s.post(url, data=creds)
            if r.status_code == 200:
                with open(HOME + '/temp/cookies/csfecookie', 'wb') as f:
                    pickle.dump(s.cookies, f)
    except FileNotFoundError:
        print("Encrypted Pass File Not Found.")


def checkcookie():
    if os.path.isfile(HOME + '/temp/cookies/csfecookie'):
        filetime = os.path.getmtime(HOME + '/temp/cookies/csfecookie')
        timenow = time.time()
        diff = timenow - filetime
        if diff > 28000:
            print("Cookie has expired.. provide password.")
            login()
    else:
        print("No cookie found.. provide password.")
        login()


def sendRequest(link, dataObject):
    with open(HOME + '/temp/cookies/csfecookie', 'rb') as f:
        cookies = pickle.load(f)
        res = requests.post(link, data=dataObject, cookies=cookies)
        htmltext = BeautifulSoup(res.content, 'lxml')
        return htmltext
