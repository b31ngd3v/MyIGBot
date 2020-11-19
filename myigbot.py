import requests
import os
from datetime import datetime
import json
from bs4 import BeautifulSoup as bs
import time
import random
import numpy

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class MyIGBot:
    def __init__(self, username, password, use_cookie = True):
        self.username = username
        self.password = password
        self.use_cookie = use_cookie

        self.path = os.getcwd()

        if use_cookie == False or os.path.exists(self.path+f'//cookie_{self.username}.bot') == False:
            link = 'https://www.instagram.com/accounts/login/'
            login_url = 'https://www.instagram.com/accounts/login/ajax/'

            time_now = int(datetime.now().timestamp())
            response = requests.get(link)
            csrf = response.cookies['csrftoken']

            payload = {
                'username': self.username,
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time_now}:{self.password}',
                'queryParams': {},
                'optIntoOneTap': 'false'
            }

            login_header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": "https://www.instagram.com/accounts/login/",
                "x-csrftoken": csrf
            }

            login_response = requests.post(login_url, data=payload, headers=login_header)
            json_data = json.loads(login_response.text)

            cookies = login_response.cookies
            cookie_jar = cookies.get_dict()
            self.csrf_token = cookie_jar['csrftoken']

            try:
                if json_data["authenticated"]:
                    pass
                else:
                    print(bcolors.FAIL+"[✗] Login Failed!"+bcolors.ENDC, login_response.text)
                    quit()
            except KeyError:
                try:
                    if json_data["two_factor_required"]:
                        self.ig_nrcb = cookie_jar['ig_nrcb']
                        self.ig_did = cookie_jar['ig_did']
                        self.mid = cookie_jar['mid']

                        otp = input(bcolors.OKBLUE+'[!] Two Factor Auth. Detected! Enter Code Here: '+bcolors.ENDC)
                        twofactor_url = 'https://www.instagram.com/accounts/login/ajax/two_factor/'
                        twofactor_payload = {
                            'username': self.username,
                            'verificationCode': otp,
                            'identifier': json_data["two_factor_info"]["two_factor_identifier"],
                            'queryParams': {}
                        }

                        twofactor_header = {
                            "accept": "*/*",
                            "accept-encoding": "gzip, deflate, br",
                            "accept-language": "en-US,en;q=0.9",
                            "content-type": "application/x-www-form-urlencoded",
                            "cookie": 'ig_did='+self.ig_did+'; ig_nrcb='+self.ig_nrcb+'; csrftoken='+self.csrf_token+'; mid='+self.mid,
                            "origin": "https://www.instagram.com",
                            "referer": "https://www.instagram.com/accounts/login/two_factor?next=%2F",
                            "sec-fetch-dest": "empty",
                            "sec-fetch-mode": "cors",
                            "sec-fetch-site": "same-origin",
                            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                            "x-csrftoken": self.csrf_token,
                            "x-ig-app-id": "936619743392459",
                            "x-ig-www-claim": "0",
                            "x-instagram-ajax": "00c4537694a4",
                            "x-requested-with": "XMLHttpRequest"
                        }

                        login_response = requests.post(twofactor_url, data=twofactor_payload, headers=twofactor_header)
                        try:
                            if login_response.headers['Set-Cookie'] != 0:
                                pass
                        except:
                            try:
                                if json_data["message"]=="checkpoint_required":
                                    self.ig_nrcb = cookie_jar['ig_nrcb']
                                    self.ig_did = cookie_jar['ig_did']
                                    self.mid = cookie_jar['mid']
                                    url='https://www.instagram.com'+json_data['checkpoint_url']
                                    header = {
                                        "accept": "*/*",
                                        "accept-encoding": "gzip, deflate, br",
                                        "accept-language": "en-US,en;q=0.9",
                                        "content-type": "application/x-www-form-urlencoded",
                                        "cookie": 'ig_did='+self.ig_did+'; ig_nrcb='+self.ig_nrcb+'; csrftoken='+self.csrf_token+'; mid='+self.mid,
                                        "origin": "https://www.instagram.com",
                                        "referer": 'https://instagram.com'+json_data['checkpoint_url'],
                                        "sec-fetch-dest": "empty",
                                        "sec-fetch-mode": "cors",
                                        "sec-fetch-site": "same-origin",
                                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                                        "x-csrftoken": self.csrf_token,
                                        "x-ig-app-id": "936619743392459",
                                        "x-ig-www-claim": "0",
                                        "x-instagram-ajax": "e8e20d8ba618",
                                        "x-requested-with": "XMLHttpRequest"
                                    }
                                    code=input(bcolors.OKBLUE+json.loads(requests.post(url, headers=header, data={'choice': '1'}).text)['extraData']['content'][1]['text']+' > '+bcolors.ENDC)
                                    if json.loads(requests.post(url, headers=header, data={'security_code': code}).text)['type']=='CHALLENGE_REDIRECTION':
                                        login_response = requests.post(login_url, data=payload, headers=login_header)
                                    else:
                                        print(bcolors.FAIL+'[✗] Login Failed!'+bcolors.ENDC)
                                        quit()
                            except:
                                print(bcolors.FAIL+'[✗] Login Failed!'+bcolors.ENDC)
                                quit()

                except KeyError:
                    try:
                        if json_data["message"]=="checkpoint_required":
                            self.ig_nrcb = cookie_jar['ig_nrcb']
                            self.ig_did = cookie_jar['ig_did']
                            self.mid = cookie_jar['mid']
                            url='https://www.instagram.com'+json_data['checkpoint_url']
                            header = {
                                "accept": "*/*",
                                "accept-encoding": "gzip, deflate, br",
                                "accept-language": "en-US,en;q=0.9",
                                "content-type": "application/x-www-form-urlencoded",
                                "cookie": 'ig_did='+self.ig_did+'; ig_nrcb='+self.ig_nrcb+'; csrftoken='+self.csrf_token+'; mid='+self.mid,
                                "origin": "https://www.instagram.com",
                                "referer": 'https://instagram.com'+json_data['checkpoint_url'],
                                "sec-fetch-dest": "empty",
                                "sec-fetch-mode": "cors",
                                "sec-fetch-site": "same-origin",
                                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                                "x-csrftoken": self.csrf_token,
                                "x-ig-app-id": "936619743392459",
                                "x-ig-www-claim": "0",
                                "x-instagram-ajax": "e8e20d8ba618",
                                "x-requested-with": "XMLHttpRequest"
                            }
                            code=input(bcolors.OKBLUE+json.loads(requests.post(url, headers=header, data={'choice': '1'}).text)['extraData']['content'][1]['text']+' > '+bcolors.ENDC)
                            if json.loads(requests.post(url, headers=header, data={'security_code': code}).text)['type']=='CHALLENGE_REDIRECTION':
                                login_response = requests.post(login_url, data=payload, headers=login_header)
                            else:
                                print(bcolors.FAIL+'[✗] Login Failed!'+bcolors.ENDC)
                                quit()
                    except:
                        print(bcolors.FAIL+'[✗] Login Failed!'+bcolors.ENDC)
                        quit()

            self.sessionid = login_response.headers['Set-Cookie'].split('sessionid=')[1].split(';')[0]                
            self.cookie = "sessionid=" + self.sessionid + "; csrftoken=" + self.csrf_token + ";"
            create_cookie = open(self.path+f'//cookie_{self.username}.bot', 'w+', encoding='utf-8')
            create_cookie.write(self.cookie)
            create_cookie.close()
            self.session = requests.session()
            cookie_obj = requests.cookies.create_cookie(
                    name='sessionid', secure=True, value=self.sessionid)
            self.session.cookies.set_cookie(cookie_obj)

        elif os.path.exists(self.path+f'//cookie_{self.username}.bot'):
            try:
                read_cookie = open(self.path+f'//cookie_{self.username}.bot', 'r', encoding='utf-8')
                self.cookie = read_cookie.read()
                read_cookie.close()
                homelink = 'https://www.instagram.com/op/'
                self.session = requests.session()
                self.sessionid = self.cookie.split('=')[1].split(';')[0]
                self.csrf_token = self.cookie.split('=')[2].replace(';', '')
                cookie_obj = requests.cookies.create_cookie(
                    name='sessionid', secure=True, value=self.sessionid)
                self.session.cookies.set_cookie(cookie_obj)
                login_response = self.session.get(homelink)
                time.sleep(1)
                soup = bs(login_response.text, 'html.parser')
                soup.find("strong", {"class": "-cx-PRIVATE-NavBar__username -cx-PRIVATE-NavBar__username__"}).get_text()
            except AttributeError:
                print(bcolors.FAIL+"[✗] Login Failed! Cookie file is corupted!"+bcolors.ENDC)
                os.remove(self.path+f'//cookie_{self.username}.bot')
                print(bcolors.WARNING+"[-] Deleted Corupted Cookie File! Try Again!"+bcolors.ENDC)
                quit()
            

    def already_liked(self, url):
        resp = self.session.get(url)
        time.sleep(1)
        soup = bs(resp.text, 'html.parser')
        scripts = soup.find_all('script')
        data_script = str(scripts[15])
        time.sleep(1)
        try:
            shortcode = url.split('/p/')[1].replace('/', '')
            data_script = data_script.replace(
                f'''<script type="text/javascript">window.__additionalDataLoaded('/p/{shortcode}/',''', '')
        except:
            shortcode = url.split('/tv/')[1].replace('/', '')
            data_script = data_script.replace(
                f'''<script type="text/javascript">window.__additionalDataLoaded('/tv/{shortcode}/',''', '')
        data_object = data_script.replace(");</script>", '')
        data_json = json.loads(data_object)
        liked = data_json["graphql"]["shortcode_media"]["viewer_has_liked"]
        
        return bool(liked)

    def like(self, url):
        try:
            if self.already_liked(url) == False:
                resp = self.session.get(url)
                time.sleep(1)
                soup = bs(resp.text, 'html.parser')
                scripts = soup.find_all('script')
                data_script = str(scripts[15])
                time.sleep(1)
                try:
                    shortcode = url.split('/p/')[1].replace('/', '')
                    data_script = data_script.replace(
                        f'''<script type="text/javascript">window.__additionalDataLoaded('/p/{shortcode}/',''', '')
                except:
                    shortcode = url.split('/tv/')[1].replace('/', '')
                    data_script = data_script.replace(
                        f'''<script type="text/javascript">window.__additionalDataLoaded('/tv/{shortcode}/',''', '')
                data_object = data_script.replace(");</script>", '')
                data_json = json.loads(data_object)
                id_post = data_json["graphql"]["shortcode_media"]["id"]
                
                url_post = f"https://www.instagram.com/web/likes/{id_post}/like/"

                headers = {
                    "accept": "*/*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                    "content-length": "0",
                    "content-type": "application/x-www-form-urlencoded",
                    "cookie": self.cookie,
                    "origin": "https://www.instagram.com",
                    "referer": url,
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                    "x-csrftoken": self.csrf_token,
                    "x-ig-app-id": "936619743392459",
                    "x-ig-www-claim": "hmac.AR3dC7naiVtTKkwrEY0hwTO9zj4kLxfvf4Srvp3wFyoZFqSx",
                    "x-instagram-ajax": "d3d3aea32e75",
                    "x-requested-with": "XMLHttpRequest"
                }
                response = requests.request("POST", url_post, headers=headers)

                if response.status_code != 200:
                    return bcolors.FAIL+'[✗] Unable to Like Post! url: '+bcolors.ENDC+url
            else:
                return bcolors.OKCYAN+'[i] Post Already Liked! url: '+bcolors.ENDC+url
        except:
            return bcolors.FAIL+'[✗] Unable to Like Post! url: '+bcolors.ENDC+url
            

        return bcolors.OKGREEN+"[✓] Liked Post Successfully! url: "+bcolors.ENDC+url

    def unlike(self, url):
        try:
            if self.already_liked(url) == True:
                resp = self.session.get(url)
                time.sleep(1)
                soup = bs(resp.text, 'html.parser')
                scripts = soup.find_all('script')
                data_script = str(scripts[15])
                time.sleep(1)
                try:
                    shortcode = url.split('/p/')[1].replace('/', '')
                    data_script = data_script.replace(
                        f'''<script type="text/javascript">window.__additionalDataLoaded('/p/{shortcode}/',''', '')
                except:
                    shortcode = url.split('/tv/')[1].replace('/', '')
                    data_script = data_script.replace(
                        f'''<script type="text/javascript">window.__additionalDataLoaded('/tv/{shortcode}/',''', '')
                data_object = data_script.replace(");</script>", '')
                data_json = json.loads(data_object)
                id_post = data_json["graphql"]["shortcode_media"]["id"]
                
                url_post = f"https://www.instagram.com/web/likes/{id_post}/unlike/"

                headers = {
                    "accept": "*/*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                    "content-length": "0",
                    "content-type": "application/x-www-form-urlencoded",
                    "cookie": self.cookie,
                    "origin": "https://www.instagram.com",
                    "referer": url,
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                    "x-csrftoken": self.csrf_token,
                    "x-ig-app-id": "936619743392459",
                    "x-ig-www-claim": "hmac.AR3dC7naiVtTKkwrEY0hwTO9zj4kLxfvf4Srvp3wFyoZFqSx",
                    "x-instagram-ajax": "d3d3aea32e75",
                    "x-requested-with": "XMLHttpRequest"
                }
                response = requests.request("POST", url_post, headers=headers)

                if response.status_code != 200:
                    return bcolors.FAIL+'[✗] Unable to Unlike Post! url: '+bcolors.ENDC+url
            else:
                return bcolors.OKCYAN+'[i] Post Already Unliked! url: '+bcolors.ENDC+url
                
        except:
            return bcolors.FAIL+'[✗] Unable to Unlike Post! url: '+bcolors.ENDC+url
            

        return bcolors.OKGREEN+"[✓] Unliked Post Successfully! url: "+bcolors.ENDC+url

    def like_recent(self, username):  
        resp = self.session.get('https://www.instagram.com/'+username+'/')
        time.sleep(1)
        soup = bs(resp.text, 'html.parser')
        scripts = soup.find_all('script')
        try:
            data_script = str(scripts[4])
            time.sleep(1)
            data_script = data_script.replace(
                '''<script type="text/javascript">window._sharedData = ''', '')
            data_object = data_script.replace(";</script>", '')
            data_json = json.loads(data_object)
        except:
            data_script = str(scripts[3])
            time.sleep(1)
            data_script = data_script.replace(
                '''<script type="text/javascript">window._sharedData = ''', '')
            data_object = data_script.replace(";</script>", '')
            data_json = json.loads(data_object)
        try:
            shortcode = data_json["entry_data"]["ProfilePage"][0]["graphql"]['user']["edge_owner_to_timeline_media"]["edges"][0]["node"]["shortcode"]
            self.like('https://www.instagram.com/p/'+shortcode+'/')
        except IndexError:
            return bcolors.FAIL+'[✗] No Post Found! username: '+bcolors.ENDC+username
        except KeyError:
            return bcolors.FAIL+'[✗] Invalid username! username: '+bcolors.ENDC+username

    def comment(self, url, comment_text):
        try:
            resp = self.session.get(url)
            time.sleep(1)
            soup = bs(resp.text, 'html.parser')
            scripts = soup.find_all('script')
            data_script = str(scripts[15])
            time.sleep(1)
            try:
                shortcode = url.split('/p/')[1].replace('/', '')
                data_script = data_script.replace(
                    f'''<script type="text/javascript">window.__additionalDataLoaded('/p/{shortcode}/',''', '')
            except:
                shortcode = url.split('/tv/')[1].replace('/', '')
                data_script = data_script.replace(
                    f'''<script type="text/javascript">window.__additionalDataLoaded('/tv/{shortcode}/',''', '')
            data_object = data_script.replace(");</script>", '')
            data_json = json.loads(data_object)
            id_post = data_json["graphql"]["shortcode_media"]["id"]

            url_post = f"https://www.instagram.com/web/comments/{id_post}/add/"

            headers = {
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "content-length": "39",
                "content-type": "application/x-www-form-urlencoded",
                "cookie": self.cookie,
                "origin": "https://www.instagram.com",
                "referer": url,
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                "x-csrftoken": self.csrf_token,
                "x-ig-app-id": "936619743392459",
                "x-ig-www-claim": "hmac.AR3dC7naiVtTKkwrEY0hwTO9zj4kLxfvf4Srvp3wFyoZFvZV",
                "x-instagram-ajax": "d3d3aea32e75",
                "x-requested-with": "XMLHttpRequest"
            }

            response = requests.request("POST", url_post, headers=headers, data=f"comment_text={comment_text}&replied_to_comment_id=".encode('utf-8'))
                
            if response.status_code != 200:
                return bcolors.FAIL+'[✗] Unable to Comment on The Post! url: '+bcolors.ENDC+url
        except:
            return bcolors.FAIL+'[✗] Unable to Comment on The Post! url: '+bcolors.ENDC+url

        return bcolors.OKGREEN+"[✓] Commented on The Post Successfully! url: "+bcolors.ENDC+url

    def comment_recent(self, username, comment_text):  
        resp = self.session.get('https://www.instagram.com/'+username+'/')
        time.sleep(1)
        soup = bs(resp.text, 'html.parser')
        scripts = soup.find_all('script')
        try:
            data_script = str(scripts[4])
            time.sleep(1)
            data_script = data_script.replace(
                '''<script type="text/javascript">window._sharedData = ''', '')
            data_object = data_script.replace(";</script>", '')
            data_json = json.loads(data_object)
        except:
            data_script = str(scripts[3])
            time.sleep(1)
            data_script = data_script.replace(
                '''<script type="text/javascript">window._sharedData = ''', '')
            data_object = data_script.replace(";</script>", '')
            data_json = json.loads(data_object)
        try:
            shortcode = data_json["entry_data"]["ProfilePage"][0]["graphql"]['user']["edge_owner_to_timeline_media"]["edges"][0]["node"]["shortcode"]
            self.comment('https://www.instagram.com/p/'+shortcode+'/', comment_text)
        except IndexError:
            return bcolors.FAIL+'[✗] No Post Found! username: '+bcolors.ENDC+username
        except KeyError:
            return bcolors.FAIL+'[✗] Invalid username! username: '+bcolors.ENDC+username

    def already_followed(self, username):
        resp = self.session.get('https://www.instagram.com/'+username+'/')
        time.sleep(1)
        soup = bs(resp.text, 'html.parser')
        scripts = soup.find_all('script')
        try:
            data_script = str(scripts[4])
            time.sleep(1)
            data_script = data_script.replace(
                '''<script type="text/javascript">window._sharedData = ''', '')
            data_object = data_script.replace(";</script>", '')
            data_json = json.loads(data_object)
        except:
            data_script = str(scripts[3])
            time.sleep(1)
            data_script = data_script.replace(
                '''<script type="text/javascript">window._sharedData = ''', '')
            data_object = data_script.replace(";</script>", '')
            data_json = json.loads(data_object)
        followed = data_json["entry_data"]["ProfilePage"][0]["graphql"]['user']['followed_by_viewer']
        return bool(followed)

    def follow(self, username):
        try:
            if self.already_followed(username) == False:
                resp = self.session.get('https://www.instagram.com/'+username+'/')
                time.sleep(1)
                soup = bs(resp.text, 'html.parser')
                scripts = soup.find_all('script')
                try:
                    data_script = str(scripts[4])
                    time.sleep(1)
                    data_script = data_script.replace(
                        '''<script type="text/javascript">window._sharedData = ''', '')
                    data_object = data_script.replace(";</script>", '')
                    data_json = json.loads(data_object)
                except:
                    data_script = str(scripts[3])
                    time.sleep(1)
                    data_script = data_script.replace(
                        '''<script type="text/javascript">window._sharedData = ''', '')
                    data_object = data_script.replace(";</script>", '')
                    data_json = json.loads(data_object)
                id_page = data_json["entry_data"]["ProfilePage"][0]["graphql"]['user']['id']

                url_page = f"https://www.instagram.com/web/friendships/{id_page}/follow/"

                headers = {
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-length': '0',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': self.cookie,
                    "origin": "https://www.instagram.com",
                    "referer": f"https://www.instagram.com/{username}/",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                    "x-csrftoken": self.csrf_token,
                    "x-ig-app-id": "936619743392459",
                    "x-ig-www-claim": "hmac.AR3dC7naiVtTKkwrEY0hwTO9zj4kLxfvf4Srvp3wFyoZFvZV",
                    "x-instagram-ajax": "d3d3aea32e75",
                    "x-requested-with": "XMLHttpRequest"
                }

                response = requests.request("POST", url_page, headers=headers)
                if response.status_code == 200:
                    return bcolors.OKGREEN+"[✓] Followed User Successfully! username: "+bcolors.ENDC+username
                else:
                    return bcolors.FAIL+'[✗] Unable to Follow User! username: '+bcolors.ENDC+username
            else:
                return bcolors.OKCYAN+'[i] User Already Followed! username: '+bcolors.ENDC+username
                
        except KeyError:
            return bcolors.FAIL+'[✗] Invalid username! username: '+bcolors.ENDC+username

    def unfollow(self, username):
        try:
            if self.already_followed(username) == True:
                resp = self.session.get('https://www.instagram.com/'+username+'/')
                time.sleep(1)
                soup = bs(resp.text, 'html.parser')
                scripts = soup.find_all('script')
                try:
                    data_script = str(scripts[4])
                    time.sleep(1)
                    data_script = data_script.replace(
                        '''<script type="text/javascript">window._sharedData = ''', '')
                    data_object = data_script.replace(";</script>", '')
                    data_json = json.loads(data_object)
                except:
                    data_script = str(scripts[3])
                    time.sleep(1)
                    data_script = data_script.replace(
                        '''<script type="text/javascript">window._sharedData = ''', '')
                    data_object = data_script.replace(";</script>", '')
                    data_json = json.loads(data_object)
                id_page = data_json["entry_data"]["ProfilePage"][0]["graphql"]['user']['id']

                url_page = f"https://www.instagram.com/web/friendships/{id_page}/unfollow/"

                headers = {
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-length': '0',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': self.cookie,
                    "origin": "https://www.instagram.com",
                    "referer": f"https://www.instagram.com/{username}/",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                    "x-csrftoken": self.csrf_token,
                    "x-ig-app-id": "936619743392459",
                    "x-ig-www-claim": "hmac.AR3dC7naiVtTKkwrEY0hwTO9zj4kLxfvf4Srvp3wFyoZFvZV",
                    "x-instagram-ajax": "d3d3aea32e75",
                    "x-requested-with": "XMLHttpRequest"
                }

                response = requests.request("POST", url_page, headers=headers)
                if response.status_code == 200:
                    return bcolors.OKGREEN+"[✓] Unfollowed User Successfully! username: "+bcolors.ENDC+username
                else:
                    return bcolors.FAIL+'[✗] Unable to Unfollow User! username: '+bcolors.ENDC+username
            else:
                return bcolors.OKCYAN+'[i] User Already Unfollowed! username: '+bcolors.ENDC+username
        except KeyError:
            return bcolors.FAIL+'[✗] Invalid username! username: '+bcolors.ENDC+username

    def story_view(self, username):
        try:
            resp = self.session.get('https://www.instagram.com/'+username+'/')
            time.sleep(1)
            soup = bs(resp.text, 'html.parser')
            scripts = soup.find_all('script')
            try:
                data_script = str(scripts[4])
                time.sleep(1)
                data_script = data_script.replace(
                    '''<script type="text/javascript">window._sharedData = ''', '')
                data_object = data_script.replace(";</script>", '')
                data_json = json.loads(data_object)
            except:
                try:
                    data_script = str(scripts[3])
                    time.sleep(1)
                    data_script = data_script.replace(
                        '''<script type="text/javascript">window._sharedData = ''', '')
                    data_object = data_script.replace(";</script>", '')
                    data_json = json.loads(data_object)
                except:
                    return bcolors.FAIL+'[✗] Invalid Username!'+bcolors.ENDC
            page_id = data_json["entry_data"]["ProfilePage"][0]["graphql"]['user']['id']
            surl = f'https://www.instagram.com/graphql/query/?query_hash=c9c56db64beb4c9dea2d17740d0259d9&variables=%7B%22reel_ids%22%3A%5B%22{page_id}%22%5D%2C%22tag_names%22%3A%5B%5D%2C%22location_ids%22%3A%5B%5D%2C%22highlight_reel_ids%22%3A%5B%5D%2C%22precomposed_overlay%22%3Afalse%2C%22show_story_viewer_list%22%3Atrue%2C%22story_viewer_fetch_count%22%3A50%2C%22story_viewer_cursor%22%3A%22%22%2C%22stories_video_dash_manifest%22%3Afalse%7D'
            resp = self.session.get(surl)
            time.sleep(1)
            soup = bs(resp.text, 'html.parser')        
            data_json = json.loads(str(soup))
            story_count =  len(data_json["data"]["reels_media"][0]["items"])

            for i in range(0, story_count):
                id_story = data_json["data"]["reels_media"][0]["items"][i]['id']
                taken_at_timestamp = data_json["data"]["reels_media"][0]["items"][i]['taken_at_timestamp']
                stories_page = f"https://www.instagram.com/stories/reel/seen"

                headers = {
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-length': '127',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': self.cookie,
                    "origin": "https://www.instagram.com",
                    "referer": f"https://www.instagram.com/stories/{username}/{id_story}/",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                    "x-csrftoken": self.csrf_token,
                    "x-ig-app-id": "936619743392459",
                    "x-ig-www-claim": "hmac.AR3dC7naiVtTKkwrEY0hwTO9zj4kLxfvf4Srvp3wFyoZFvZV",
                    "x-instagram-ajax": "d3d3aea32e75",
                    "x-requested-with": "XMLHttpRequest"
                }

                data = {
                    'reelMediaId': id_story,
                    'reelMediaOwnerId': page_id,
                    'reelId': page_id,
                    'reelMediaTakenAt': taken_at_timestamp,
                    'viewSeenAt': taken_at_timestamp
                }

                requests.request("POST", stories_page, headers=headers, data=data)

        except IndexError:
            return bcolors.OKCYAN+'[i] No Story Found! username: '+bcolors.ENDC+username
            
        except KeyError:
            return bcolors.FAIL+'[✗] Invalid username! username: '+bcolors.ENDC+username
            
        return bcolors.OKGREEN+"[✓] Story View Sent! username: "+bcolors.ENDC+username


    def upload_post(self, photo, caption=''):
        micro_time = int(datetime.now().timestamp())

        headers = {
            "content-type": "image / jpg",
            "content-length": "1",
            "X-Entity-Name": f"fb_uploader_{micro_time}",
            "Offset": "0",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
            "x-entity-length": "1",
            "X-Instagram-Rupload-Params": f'{{"media_type": 1, "upload_id": {micro_time}, "upload_media_height": 1080, "upload_media_width": 1080}}',
            "x-csrftoken": self.csrf_token,
            "x-ig-app-id": "1217981644879628",
            "cookie": self.cookie
        }

        upload_response = requests.post(f'https://www.instagram.com/rupload_igphoto/fb_uploader_{micro_time}',
                                        data=open(photo, "rb"), headers=headers)

        json_data = json.loads(upload_response.text)
        upload_id = json_data['upload_id']

        if json_data["status"] == "ok":
            url = "https://www.instagram.com/create/configure/"

            payload = 'upload_id=' + upload_id + '&caption=' + caption + '&usertags=&custom_accessibility_caption=&retry_timeout='
            headers = {
                'authority': 'www.instagram.com',
                'x-ig-www-claim': 'hmac.AR2-43UfYbG2ZZLxh-BQ8N0rqGa-hESkcmxat2RqMAXejXE3',
                'x-instagram-ajax': 'adb961e446b7-hot',
                'content-type': 'application/x-www-form-urlencoded',
                'accept': '*/*',
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
                'x-csrftoken': self.csrf_token,
                'x-ig-app-id': '1217981644879628',
                'origin': 'https://www.instagram.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.instagram.com/create/details/',
                'accept-language': 'en-US,en;q=0.9,fa-IR;q=0.8,fa;q=0.7',
                'cookie': self.cookie
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            json_data = json.loads(response.text)

            if json_data["status"] == "ok":
                return bcolors.OKGREEN+"[✓] Post Shared Successfully!"+bcolors.ENDC

        else:
            return bcolors.FAIL+'[✗] Failed!'+bcolors.ENDC+json_data

    def upload_story(self, photo):
        micro_time = int(datetime.now().timestamp())

        headers = {
            "content-type": "image / jpg",
            "content-length": "1",
            "X-Entity-Name": f"fb_uploader_{micro_time}",
            "Offset": "0",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
            "x-entity-length": "1",
            "X-Instagram-Rupload-Params": f'{{"media_type": 1, "upload_id": {micro_time}, "upload_media_height": 1080, "upload_media_width": 1080}}',
            "x-csrftoken": self.csrf_token,
            "x-ig-app-id": "1217981644879628",
            "cookie": self.cookie
        }

        upload_response = requests.post(f'https://www.instagram.com/rupload_igphoto/fb_uploader_{micro_time}',
                                        data=open(photo, "rb"), headers=headers)

        json_data = json.loads(upload_response.text)
        upload_id = json_data['upload_id']

        if json_data["status"] == "ok":
            url = "https://www.instagram.com/create/configure_to_story/"

            payload = 'upload_id=' + upload_id + '&caption=&usertags=&custom_accessibility_caption=&retry_timeout='
            headers = {
                'authority': 'www.instagram.com',
                'x-ig-www-claim': 'hmac.AR2-43UfYbG2ZZLxh-BQ8N0rqGa-hESkcmxat2RqMAXejXE3',
                'x-instagram-ajax': 'adb961e446b7-hot',
                'content-type': 'application/x-www-form-urlencoded',
                'accept': '*/*',
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
                'x-csrftoken': self.csrf_token,
                'x-ig-app-id': '1217981644879628',
                'origin': 'https://www.instagram.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.instagram.com/create/details/',
                'accept-language': 'en-US,en;q=0.9,fa-IR;q=0.8,fa;q=0.7',
                'cookie': self.cookie
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            json_data = json.loads(response.text)

            if json_data["status"] == "ok":
                return bcolors.OKGREEN+"[✓] Story Shared Successfully!"+bcolors.ENDC

        else:
            return bcolors.FAIL+'[✗] Failed!'+bcolors.ENDC+json_data
