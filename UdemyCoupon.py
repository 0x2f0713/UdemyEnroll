import requests
import re
import json
import urllib.parse as parse
import time
import random
import sys
from Udemy import Udemy


class UdemyCoupon:
    def __init__(self):
        file = open('Enroll.txt', 'r+')
        self.CoursesCollection = file.readlines()
        self.session = Udemy('namhaiha0308@gmail.com', 'qweqwerrr123456789')
        self.Cookies = self.session.cookies

    def UpdateCookie(self, cookies):
        return self.Cookies.update(requests.utils.dict_from_cookiejar(cookies))

    def Pausing(self):
        for x in range(1, random.randint(10, 20)):
            sys.stdout.write("\rPausing: %s" % str(x))
            sys.stdout.flush()
            time.sleep(1)
        print()
    def Enroll(self, url):
        Parse = parse.urlparse(url)
        published_title = Parse[2].strip('/')
        if len(Parse[4]) is not 0 and 'couponCode' in Parse[4]:
            Coupon = parse.parse_qs(Parse[4])['couponCode'][0]
            haveCoupon = True
        else:
            Coupon = ''
            haveCoupon = False
        if published_title+'\n' not in self.CoursesCollection:
            x = requests.get('https://www.udemy.com/api-2.0/courses/{published_title}/'.format(published_title=published_title), cookies=self.Cookies, headers={
                'authorization': self.session.Bearer,
                'x-udemy-authorization': self.session.Bearer,
                'user-agent': self.session.UserAgent,
                'upgrade-insecure-requests': '1'
            })
            CourseInfo = json.loads(x.text)
            self.UpdateCookie(x.cookies)
            if 'id' in CourseInfo:
                y = requests.get('https://www.udemy.com/api-2.0/course-landing-components/{id}/me/?components=buy_button,discount_expiration,gift_this_course,introduction_asset,purchase,deal_badge,redeem_coupon'.format(id=CourseInfo["id"]), params={
                    'components': 'buy_button,discount_expiration,gift_this_course,introduction_asset,purchase,deal_badge,redeem_coupon',
                    'couponCode': Coupon
                }, cookies=self.Cookies, headers={
                    'authorization': self.session.Bearer,
                    'x-udemy-authorization': self.session.Bearer,
                    'user-agent': self.session.UserAgent,
                    'upgrade-insecure-requests': '1'
                })
                self.UpdateCookie(y.cookies)
                Price = json.loads(y.text)
                if Price['purchase']['data']['pricing_result']['price']['amount'] == 0.0:
                    if haveCoupon:
                        Enroll = requests.get('https://www.udemy.com/course/subscribe/?courseId={id}'.format(id=CourseInfo['id']), cookies=self.Cookies, headers={
                            'referer': url,
                            'user-agent': self.session.UserAgent,
                            'x-csrftoken': self.session.csrftoken,
                            'X-Requested-With': 'XMLHttpRequest',
                            'sec-fetch-mode': 'navigate',
                            'sec-fetch-site': 'same-origin',
                            'sec-fetch-user': '?1',
                            'upgrade-insecure-requests': '1',
                        }, allow_redirects=False)
                        self.UpdateCookie(Enroll.cookies)
                        if Enroll.status_code == 302 and 'location' in Enroll.headers:
                            print('Free courses {} enroll success'.format(
                                published_title))
                        else:
                            Enroll = requests.post('https://www.udemy.com/payment/shopping-cart-submit/?DEBUG=True', json={
                                "shopping_cart": {
                                    "items": [
                                        {
                                            "buyableContext": {
                                                "contentLocaleId": None
                                            },
                                            "discountInfo": {
                                                "code": Coupon
                                            },
                                            "buyableType": "course",
                                            "purchasePrice": {
                                                "currency": "USD",
                                                "currency_symbol": "$",
                                                "price_string": "Free",
                                                "amount": 0
                                            },
                                            "buyableId": CourseInfo['id']
                                        }
                                    ]
                                }
                            }, cookies=self.Cookies, headers={
                                'referer': 'https://www.udemy.com/cart/checkout/express/course/{id}/?discountCode={coupon}'.format(id=CourseInfo['id'], coupon=Coupon),
                                'user-agent': self.session.UserAgent,
                                'x-csrftoken': self.session.csrftoken,
                                'X-Requested-With': 'XMLHttpRequest',
                                'sec-fetch-mode': 'navigate',
                                'sec-fetch-site': 'same-origin',
                                'sec-fetch-user': '?1',
                                'upgrade-insecure-requests': '1',
                            })
                            self.UpdateCookie(Enroll.cookies)
                            print(Enroll.text)
                    else:
                        Enroll = requests.get('https://www.udemy.com/course/subscribe/?courseId={id}'.format(id=CourseInfo['id']), cookies=self.Cookies, headers={
                            'referer': url,
                            'user-agent': self.session.UserAgent,
                            'x-csrftoken': self.session.csrftoken,
                            'X-Requested-With': 'XMLHttpRequest',
                            'sec-fetch-mode': 'navigate',
                            'sec-fetch-site': 'same-origin',
                            'sec-fetch-user': '?1',
                            'upgrade-insecure-requests': '1',
                        }, allow_redirects=False)
                        self.UpdateCookie(Enroll.cookies)
                        if Enroll.status_code == 302 and 'location' in Enroll.headers:
                            print(Enroll.headers['location'])
                            print('Free courses {} enroll success'.format(
                                published_title))
                        else:
                            print('Blocked')
                            print(Enroll.text)
                            exit()
                    open('Enroll.txt', 'a').write(published_title+'\n')
                    self.CoursesCollection.append(published_title+'\n')
                    print(Enroll.text)
                    print(url)
                    return True
            else:
                print(CourseInfo)
                print(url)
                open('id.txt', 'a').writelines(published_title+"\n")
                return False
        else:
            print('Inserted: '+url)
            return False

    def discudemy(self):
        i = 1
        try:
            while True:
                HTML = requests.get(
                    'https://www.discudemy.com/all/{number}'.format(number=i), allow_redirects=True)
                print(i)
                URLS = re.findall(
                    r'<a class="card-header" href="((http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[discudemy]*\.[a-z]{2,5}?(\/.*)?)">', HTML.text)
                if len(URLS) == 0:
                    break
                else:
                    i = i+1
                for x in range(0, 15):
                    endpoint = URLS[x][2].strip('/').split('/')
                    if endpoint[0] == 'giveaway':
                        continue
                    info = requests.get(
                        'https://www.discudemy.com/go/{published_title}'.format(published_title=endpoint[1])).text
                    url = re.search(
                        r'(https):\/\/(www\.udemy)([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', info)
                    if self.Enroll(url[0].replace('/course/', '/')):
                        self.Pausing()
        except Exception as e:
            print(str(e))

    def udemycoupon_learnviral_com(self):
        i = 0
        while True:
            HTML = requests.get(
                'https://udemycoupon.learnviral.com/coupon-category/free100-discount/page/{number}'.format(number=i), allow_redirects=True)
            print(i)
            URLS = re.findall(
                r'(https://www\.udemy\.com.*)(" id)', HTML.text)
            if len(URLS) == 0:
                break
            else:
                i = i+1
            for x in URLS:
                if self.Enroll(x[0].replace('/course/', '/')):
                    self.Pausing()

    def real_discount(self):
        i = 0
        while True:
            HTML = requests.get(
                'https://www.real.discount/new/page/{number}'.format(number=i), allow_redirects=True)
            print(i)
            URLS = re.findall(
                r'(https:\/\/www\.real\.discount\/offer\/[\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])', HTML.text)
            if len(URLS) == 0:
                break
            else:
                i = i+1
            for x in URLS:
                info = requests.get(x).text
                url = re.search(
                    r'(https):\/\/(www\.udemy)([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', info)
                if url is not None:
                    if self.Enroll(url[0].replace('/course/', '/')):
                        self.Pausing()

    def freebiesglobal_com(self):
        i = 1
        while True:
            HTML = requests.get(
                'https://freebiesglobal.com/dealstore/udemy/page/{number}'.format(number=i), allow_redirects=True)
            print(i)
            URLS = re.findall(
                r'<a class="img-centered-flex rh-flex-center-align rh-flex-justify-center" href="(https:\/\/freebiesglobal\.com\/[\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])', HTML.text)
            if len(URLS) == 0:
                break
            else:
                i = i+1
            for x in URLS:
                info = requests.get(x).text
                url = re.search(
                    r'(https):\/\/(www\.udemy)([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', info)
                if url is not None:
                    if self.Enroll(url[0].replace('/course/', '/')):
                        self.Pausing()
p1 = UdemyCoupon()
num = int(input("Enter number :"))
if num == 1:
    p1.discudemy()
if num == 2:
    p1.udemycoupon_learnviral_com()
if num == 3:
    p1.real_discount()
if num == 4:
    p1.freebiesglobal_com()
