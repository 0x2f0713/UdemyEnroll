import requests
import re
import json
import urllib.parse as parse
from http.cookies import SimpleCookie


class Udemy:
    def __init__(self, email="", password=""):
        self.email = email
        self.password = password
        self.UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3800.0 Safari/537.36 Edg/76.0.167.1"
        self.Courses = []
        parse = SimpleCookie()
        parse.load('__cfduid=dfcecd564c094e953211289b00f2a635f1617102876; __udmy_2_v57r=85471b3677474c7da52529636cdcdb37; ud_firstvisit=2021-03-30T11:14:37.541115+00:00:1lRCKU:2FX_KJ20L-hV-ncH3bzQYrnSp7A; EUCookieMessageShown=true; EUCookieMessageState=initial; ud_credit_last_seen=None; csrftoken=vx9S8X4D3Coy4IEC5OdjsKqg9RdPYrD4cOv93L2q796ScjaaVVZ8O3rnoFdCaKam; access_token=bTuRa3FwXdfG4zZTXtTiAa7zzsYQhnCsB1saJDTt; client_id=bd2565cb7b0c313f5e9bae44961e8db2; ud_user_jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJncm91cF9pZHMiOltdLCJpZCI6MzMyNTI3MzQsImlzX3N1cGVydXNlciI6ZmFsc2UsImVtYWlsIjoibmFtaGFpaGEwMzA4QGdtYWlsLmNvbSJ9.Xz69RyD6Cxk5IEeo4htr5v9INcVvBDvpO0CJaJjj8PI; dj_session_id=bbw6lksm2qe3vv57hota3ur1jszfodrm; ud_cache_modern_browser=1; ud_cache_campaign_code=KEEPLEARNING; ud_cache_user=33252734; ud_cache_brand=VNen_US; ud_credit_unseen=0; ud_cache_logged_in=1; ud_cache_language=en; ud_cache_release=95d85ebba7f2c904a2c6; ud_cache_price_country=VN; ud_cache_version=1; ud_cache_marketplace_country=VN; seen=1; __cf_bm=fe55e05dae2e271aa503daa09a046224eba9cca7-1617807364-1800-AbShbVHdm8u6N3GsF26VOpG29BXbtRK6oec7NLdUqc9NCPCkyhDYKixFrg60296WRIGW69kfZo5+IoKuA64RVdA=; __cfruid=8a318bb11f7bcd2ed58f74fcf1da48e670af4b30-1617807364; __ssid=32e35fd31f9f0a91a5e1cea56c7aed0; ud_cache_device=desktop; eventing_session_id=0IRwq_xaRp6z_QxjRLgXew-1617809231452; evi=SlFJMwINHTwTSVBjXVNCfBNJUGMYQE99HVFdIExYQnUAS1Y8QkAGOUFRETpMUUd+A1EROkwUV3YAXwk3D0BPdAFHHTwTTlcvXQNbY1QZV38ARRljVBlXOhNJGm1MFBRuC0QTeVofWW4CQh11TFgObkdREXBCQAMtE0kceVdWCDEdUVg2TFgObgJBG3lMWA5uR1ERcEJAAy0TSRNxX1IIYBNAGXRYQE83EwUJe19OVzpQURF5X1BHMR1RGXNXWld2SlFdY1RTWW5HEgl7W1pEekxfCXJcUEVuCwgJN0xYRGATBUpjVFpFeAEOB2NcV0x0E0lQYxhAT30dUV0gTFhDeQdLVjxCQBYgQVEROkxRRHQHURE6TBRXdgBfCTcPQE97CEUbPBNOVz5TFwl7FUBGfQJDCXsVQANuC0IHYxgDV3YGSxt5Ex8I; ud_rule_vars="eJx9kMtqwzAQAH_F6No46L2OvkVg5JWciqYRlda9hPx7lJBDSiGnPezODOyFUajHRCnOv7llKtVNRoNYlAXQoBFiMNLIg1UWI8ZFgcNSvnJibmAXz06h0VzTz5b6jIGS7wvPJJdi5GpUfBDCCe3UtAcwkzQfnDvOPdv1qzXXTj3Cb1nYKy0sqFf2Ecay1ZaeBsrffwx65DB03Nh73epJgPlnoLLh50w1rGvGuXUfdl-oOSynpy2fG9UN-288u7LrDeyLWx4=:1lU9cF:UGCEO320Y7K8kKJlFL9TS8Lsalw"')
        self.cookies = {}
        for key, morsel in parse.items():
            self.cookies[key] = morsel.value
        self.Bearer = 'Bearer {access_token}'.format(
            access_token=self.cookies['access_token'])
        try:
            self.csrftoken = self.cookies['csrftoken']
            self.dj_session_id = self.cookies['dj_session_id']
        except KeyError:
            print(self.cookies)
        # if self.login() is True:
        #     print('Logged in!')
        # else:
        #     print('Error when log in!')

    def getCRSFToken(self):
        PopUp = requests.get('https://www.udemy.com/join/login-popup', headers={
            "Accept": "text/html",
            "Sec-Fetch-Mode": "cors",
            "User-Agent": self.UserAgent,
            'upgrade-insecure-requests': '1',
            'sec-fetch-site': 'same-origin',
            'x-requested-with': 'XMLHttpRequest'
        })
        x = re.findall(
            "name=\'csrfmiddlewaretoken\' value=\'(.*)\'", PopUp.text)
        try:
            return {'crsf_form': x[0], 'cookies': requests.utils.dict_from_cookiejar(PopUp.cookies)}
        except Exception:
            print(PopUp.text)

    def login(self):
        data = self.getCRSFToken()
        login = requests.post('https://www.udemy.com/join/login-popup/?display_type=popup&locale=en_US&ref=&response_type=json&xref=', cookies=data['cookies'], data={
            'csrfmiddlewaretoken': data['crsf_form'],
            'locale': "vi_VN",
            'email': self.email,
            'password': self.password,
            'submit':"Log In"
        }, headers={
            'origin': 'https://www.udemy.com',
            'referer': 'https://www.udemy.com/join/login-popup/',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        })
        if login.headers['Content-Type'] == 'application/json':
            self.cookies = requests.utils.dict_from_cookiejar(login.cookies)
            self.Bearer = 'Bearer {access_token}'.format(
                access_token=self.cookies['access_token'])
            self.csrftoken = self.cookies['csrftoken']
            self.dj_session_id = self.cookies['dj_session_id']
            return True
        else:
            return False

    def getEnrolledCourseAmount(self):
        courses = requests.get('https://www.udemy.com/api-2.0/users/me/subscribed-courses', cookies=self.cookies, headers={
            'authorization': self.Bearer,
            'x-udemy-authorization': self.Bearer,
            'user-agent': self.UserAgent,
            'upgrade-insecure-requests': '1'
        })
        CourseList = json.loads(courses.text)
        self.updateCookie(courses.cookies)
        self.EnrolledCourseAmount = CourseList['count']
        return CourseList['count']

    def getEnrolledCoursesPerPage(self, uri='https://www.udemy.com/api-2.0/users/me/subscribed-courses?fields[course]=@all&page_size=12'):
        courses = requests.get(uri, cookies=self.cookies, headers={
            'authorization': self.Bearer,
            'x-udemy-authorization': self.Bearer,
            'user-agent': self.UserAgent,
            'upgrade-insecure-requests': '1'
        })
        CourseList = json.loads(courses.text)['results']
        self.updateCookie(courses.cookies)
        return CourseList

    def writeListCourses(self):
        open('file.txt', "w+").write(json.dumps(self.Courses))

    def getCourseInfo(self, id):
        course = requests.get('https://www.udemy.com/api-2.0/courses/{id}'.format(id=id), cookies=self.cookies, headers={
            'authorization': self.Bearer,
            'x-udemy-authorization': self.Bearer,
            'user-agent': self.UserAgent,
            'upgrade-insecure-requests': '1'
        })
        self.updateCookie(course.cookies)
        return dict(status_code=course.status_code, data=json.loads(course.text))

    def getCourseContent(self, id):
        course = requests.get('https://www.udemy.com/api-2.0/courses/{id}/subscriber-curriculum-items/?page_size=1400&fields[lecture]=title,object_index,is_published,sort_order,created,asset,supplementary_assets,last_watched_second,is_free&fields[quiz]=title,object_index,is_published,sort_order,type&fields[practice]=title,object_index,is_published,sort_order&fields[chapter]=title,object_index,is_published,sort_order&fields[asset]=title,filename,asset_type,external_url,status,time_estimation'.format(id=id), cookies=self.cookies, headers={
            'authorization': self.Bearer,
            'x-udemy-authorization': self.Bearer,
            'user-agent': self.UserAgent,
            'upgrade-insecure-requests': '1'
        })
        self.updateCookie(course.cookies)
        return dict(status_code=course.status_code, data=json.loads(course.text))

    def getCoursePurchaseInfo(self, id, coupon_code=''):
        """ components : purchase,buy_button,discount_expiration,gift_this_course,introduction_asset,deal_badge,redeem_coupon,curriculum,practice_test_bundle,recommendation,instructor_bio,cacheable_deal_badge,cacheable_discount_expiration,cacheable_price_text,cacheable_buy_button,cacheable_purchase_text,cacheable_add_to_cart """
        PurchaseInfo = requests.get('https://www.udemy.com/api-2.0/course-landing-components/{id}/me/?components=redeem_coupon,purchase,buy_button&couponCode={coupon_code}'.format(id=id, coupon_code=coupon_code), cookies=self.cookies, headers={
            'authorization': self.Bearer,
            'x-udemy-authorization': self.Bearer,
            'user-agent': self.UserAgent,
            'upgrade-insecure-requests': '1'
        })
        self.updateCookie(PurchaseInfo.cookies)
        return dict(status_code=PurchaseInfo.status_code, data=json.loads(PurchaseInfo.text))

    def getLecture(self, id, id_lecture):
        lecture = requests.get('https://www.udemy.com/api-2.0/users/me/subscribed-courses/{id}/lectures/{id_lecture}?fields[lecture]=asset,last_watched_second&fields[asset]=asset_type,length,stream_urls,captions,thumbnail_url,thumbnail_sprite,slides,slide_urls,download_urls'.format(id=id, id_lecture=id_lecture), cookies=self.cookies, headers={
            'authorization': self.Bearer,
            'x-udemy-authorization': self.Bearer,
            'user-agent': self.UserAgent,
            'upgrade-insecure-requests': '1'
        })
        self.updateCookie(lecture.cookies)
        return dict(status_code=lecture.status_code, data=json.loads(lecture.text))

    def enrollFreeCourse(self, id):
        Enrollment = requests.get('https://www.udemy.com/course/subscribe/?courseId={id}'.format(id=id), cookies=self.cookies, headers={
            'referer': 'https://www.udemy.com/course/{id}'.format(id=id),
            'user-agent': self.UserAgent,
            'x-csrftoken': self.csrftoken,
            'X-Requested-With': 'XMLHttpRequest',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
        }, allow_redirects=False)
        self.updateCookie(Enrollment.cookies)
        if Enrollment.status_code == 302 and 'location' in Enrollment.headers:
            return dict(id=id, success=True, status_code=Enrollment.status_code, type="Free Course", result_url=Enrollment.headers['location'])
        else:
            return dict(id=id, success=False, status_code=Enrollment.status_code, type="Free Course")

    def enrollPaidCourseWithCoupon(self, id, coupon_code):
        Enrollment = requests.post('https://www.udemy.com/payment/shopping-cart-submit/?DEBUG=True', json={
            "shopping_cart": {
                "items": [
                    {
                        "buyableContext": {
                            "contentLocaleId": None
                        },
                        "discountInfo": {
                            "code": coupon_code
                        },
                        "buyableType": "course",
                        "purchasePrice": {
                            "currency": "USD",
                            "currency_symbol": "$",
                            "price_string": "Free",
                            "amount": 0
                        },
                        "buyableId": id
                    }
                ]
            }
        }, cookies=self.cookies, headers={
            'referer': 'https://www.udemy.com/cart/checkout/express/course/{id}/?discountCode={coupon}'.format(id=id, coupon=coupon_code),
            'user-agent': self.UserAgent,
            'x-csrftoken': self.csrftoken,
            'X-Requested-With': 'XMLHttpRequest',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
        })
        self.updateCookie(Enrollment.cookies)
        if Enrollment.status_code == 200:
            return dict(id=id, success=True, status_code=200, gateway_transaction_id=json.loads(Enrollment.text)['gateway_transaction_id'])
        else:
            return dict(id=id, success=False, status_code=Enrollment.status_code, error=json.loads(Enrollment.text))

    def enrollPaidCourseWithCouponVersion2(self, id, coupon_code):
        Enrollment = requests.post('https://www.udemy.com/payment/checkout-submit/', json={"checkout_environment": "Marketplace","checkout_event":"Submit","shopping_cart":{"items":[{"discountInfo":{"code":coupon_code},"purchasePrice":{"amount":0,"currency":"USD","price_string":"Free","currency_symbol":"$"},"buyableType":"course","buyableId":id,"buyableContext":{}}],"is_cart":False},"payment_info":{"payment_vendor":"Free","payment_method":"free-method"},"tax_info":{"is_tax_enabled":True,"tax_rate":0,"billing_location":{"country_code":"VN","secondary_location_info":None},"currency_code":"usd","transaction_items":[{"tax_amount":0,"tax_included_amount":0,"tax_excluded_amount":0,"udemy_txn_item_reference":f"course-{id}"}],"tax_breakdown_type":"tax_inclusive"}
        }, cookies=self.cookies, headers={
            'accept':'application/json, text/plain, */*',
            'authorization': self.Bearer,
            'content-type':'application/json;charset=UTF-8',
            'origin':'https://www.udemy.com',
            'x-checkout-is-mobile-app':'false',
            'x-checkout-version':'2',
            'referer': f'https://www.udemy.com/cart/checkout/express/course/{id}/?discountCode={coupon_code}',
            'user-agent': self.UserAgent,
            'x-csrftoken': self.csrftoken,
            'X-Requested-With': 'XMLHttpRequest',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'x-udemy-authorization': self.Bearer,
        })
        self.updateCookie(Enrollment.cookies)
        if Enrollment.status_code == 200:
            return dict(id=id, success=True, status_code=200, transaction_id=json.loads(Enrollment.text))
        else:
            return dict(id=id, success=False, status_code=Enrollment.status_code, error=json.loads(Enrollment.text))

    def parseUri(self, url):
        ParseResult = parse.urlparse(url)
        return dict(published_title=ParseResult.path.strip('/'), id=self.getCourseInfo(ParseResult.path.strip('/'))['id'], coupon_code=ParseResult.query.lstrip('couponCode='))

    def updateCookie(self, cookies):
        return self.cookies.update(requests.utils.dict_from_cookiejar(cookies))
# p1 = Udemy('namhaiha0308@gmail.com','qweqwerrr123456789')
# p1.login()
# p1.getEnrolledCourses()
# p1.writeListCourses()
