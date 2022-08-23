import requests
from twocaptcha import TwoCaptcha
import string
import secrets


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0"}
solver = TwoCaptcha('6d2047f498b2f9d6dd6d823a876411dd')
url = "https://discord.com/api/v9/auth/register"


def generate_user_password() -> str:
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for _ in range(10))
    return password


email = input("Enter your Email:")
username = input("Enter your username:")
password = generate_user_password()
birth_date = input("Enter your birthdate,format like this 'YYYY-MM-DD':")


object = {
    'captcha_key': 'null',
    'consent': True,
    'date_of_birth': birth_date,
    'email': email,
    'fingerprint': '1011358247548104714.7WgVhFFWHb8igscmAR7zVGww3zk',
    'gift_code_sku_id': 'null',
    'invite': 'null',
    'password': password,
    'username': username

}


def get_url(url,object,headers):
    return requests.post(url, json=object, headers=headers).json()



def main():
    get_captcha = get_url(url,object,headers)
    catcha_solved_code = solver.hcaptcha(sitekey=get_captcha["captcha_sitekey"],url=url)
    object["captcha_key"] = catcha_solved_code["code"]
    responce_with_token = get_url(url,object,headers)
    print(f"Your token is {responce_with_token['token']}")


if __name__ == "__main__":
    main()
