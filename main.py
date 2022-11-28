from requests     import Session
from time         import time
from urllib.parse import unquote, quote
from base64       import b64decode, b64encode
from re           import findall
from PIL          import Image
from io           import BytesIO
from time         import sleep

base_url     = "https://azubis.live/v1.0.php"
base_headers = {
    "host": "azubis.live",
    "connection": "keep-alive",
    "sec-ch-ua": "\"Opera\";v=\"93\", \"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"107\"",
    "accept": "*/*",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "x-requested-with": "XMLHttpRequest",
    "sec-ch-ua-mobile": "?0",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0",
    "sec-ch-ua-platform": "\"Windows\"",
    "origin": "https://azubis.live",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://azubis.live/",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8"
}
_link = input("tiktok link: ")

def __send_views(__session__, __key__, link):
    # link       = "https://www.tiktok.com/@fefepixart/video/7106016809131805958"
    payload    = f"{__key__}=ttfreev&l={b64encode(link.encode()).decode()}"

    # print(payload)
    __signer__ = __session__.post("http://127.0.0.1:3000/sign", 
        params = {
            "data" : quote(payload),
            "input": quote(link),
            "timestamp": int(time())
    })

    __signed__   = __signer__.json()["__data__"]
    resp         = __session__.post('https://azubis.live/v1.0.php', 
                                    headers = base_headers, data = __signed__)

    __response__ = b64decode(unquote(resp.json()['ecvfl']).encode()).decode()
    # print(__response__)
    if "Success" in __response__:
        print("sent likes !!")
    else:
        if "time is expired" in __response__:
            timer = findall(r"ime =([0-9 ]{0,3});", __response__)[0]
            print("sleeping for %s seconds" % timer)
            sleep(int(timer))
            __send_views(__session__, __key__, link)
        
        else:
            print(__response__)
        print(__response__)
    
    __send_views(__session__, __key__, link)

    print(__session__.cookies.get_dict())


with Session() as __session__:

    __signer__ = __session__.post("http://127.0.0.1:3000/init")

    res = __session__.post(base_url, 
                                headers = base_headers, data = __signer__.json()["__data__"])
    
    __response__ = b64decode(unquote(res.json()['ecvfl']).encode("utf-8")).decode("utf-8")

    cap_key = findall(r"je\(\\'([A-Za-z0-9]{7,8})=cap", __response__)[0]
    print(cap_key)

    __captcha__ = __session__.get(f"https://azubis.live/captcha.php?ts={int(time())}").content

    img = Image.open(BytesIO(__captcha__))
    img.show()

    __cap_answer__ = input("captcha: ")

    payload = cap_key + '=capc&result=' + __cap_answer__

    __signer__ = __session__.post("http://127.0.0.1:3000/sign", 
        params = {
            "data" : quote(payload),
            "input": __cap_answer__,
            "timestamp": int(time())
    })

    __signed__ = __signer__.json()["__data__"]
    resp       = __session__.post('https://azubis.live/v1.0.php', headers=base_headers, data=payload)
    
    __response__ = b64decode(unquote(resp.json()['ecvfl']).encode()).decode()
    views_key = findall(r"ndje\(\\'([A-Za-z0-9]{7,8})+=ttf", __response__)[0]
    
    __send_views(__session__, views_key, _link)