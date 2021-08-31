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
        parse.load('ud_firstvisit=2021-08-17T09:06:25.519466+00:00:1mFv3B:UB4VctGyHbjeA_rcPVcgIVoU3Cs; __udmy_2_v57r=3f441bf0ec9b4bf2b89ffc1eca563eb5; EUCookieMessageShown=true; EUCookieMessageState=initial; _gcl_au=1.1.1093631453.1629191193; blisspoint_fpc=ece09d7c-2d52-4be4-a3d6-3fd107d265fa; __ssid=11e9d947ae89cf02490440d84875593; _rdt_uuid=1629191198124.347bd41f-0739-4468-9d13-a18b0fb84d49; client_id=bd2565cb7b0c313f5e9bae44961e8db2; G_ENABLED_IDPS=google; _pxvid=ac096fcd-033e-11ec-acba-746a6872486d; muxData=mux_viewer_id=574d3188-51ec-43e3-9aef-ef6f6b2457d6&msn=0.4731172036828062&sid=582c23b6-0dd7-4ab1-8d2f-c55b25d2b8a8&sst=1629646574637&sex=1629648074637; intercom-session-sehj53dd=MXpZMU9VRmZlWmZQUHNLckdOMUNudEd6cy9TREVhRGhqQTJvMi9PdStzOVFhcHVKaEI2aS9pMjkrWGJSbXNCOC0tZmxhWmRFWk10NkpxV3V6OUZTUVdoUT09--694b5bd60193e384839c2336fc1a9e4adcba288b; IR_PI=d3e4d6bd-2ed2-3a29-bb67-9e002606d070%7C1629812650646; ki_t=1629191238948%3B1629702602096%3B1629726251348%3B5%3B18; ud_credit_last_seen=None; dj_session_id=ulx6xhtdzhen7tcubp4tx263v73p7f83; access_token=5Axl7JpHyznia9GWTvHQlpngzEtUXYDsuT4nV7XK; ud_user_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im5hbWhhaWhhMDMwOEBnbWFpbC5jb20iLCJncm91cF9pZHMiOltdLCJpZCI6MzMyNTI3MzQsImlzX3N1cGVydXNlciI6ZmFsc2V9.Onk6i_s_I-3B3awZoyqhq4HFAjTdUfUQA3aLTTeBtwY; csrftoken=zlQnbwDw16Pn8HSN9o8BY7GBbcfNzgAIWqqOIQOrInvva3xvnGTiD67QgSwzF10Y; stc111655=env:1629780662%7C20210924045102%7C20210824052107%7C2%7C1014624:20220824045107|uid:1629191195194.372935510.1142955.111655.764040926.2:20220824045107|srchist:1014624%3A1629780662%3A20210924045102:20220824045107|tsa:1629780662026.1511059713.8853574.4855125253184034.:20210824052107; ud_credit_unseen=0; ud_cache_brand=VNen_US; ud_cache_logged_in=1; ud_cache_marketplace_country=VN; ud_cache_release=b185153075ff5f62b34d; ud_cache_version=1; ud_cache_modern_browser=1; ud_cache_price_country=VN; ud_cache_user=33252734; ud_cache_campaign_code=STCKOT82421B; ud_cache_language=en; ud_cache_device=desktop; _ga=GA1.1.992033820.1629191188; _ga_7YMFEFLR6Q=GS1.1.1629948662.33.0.1629948670.52; evi="3@Ygdl5A0jwgk7IIxR-Jc5it82BDl0hasmMJh3AL-tJGAfXUdMyX4-gbD5waL6Z8cWLvNJ3ZB9oyPdzFWMv5DM4Avt1Ui6ch160lumNRYMHlkp-yDSyy9ezZk1fpGwSdTwCYO6quWCKN-ob5XEWxD0z1gWCThHLoQhcV-Sho1rM03tkqw1dwksGAPgw9POeMe9ta4pLDYpEVuAAZzRSvdI-sV0om6EKJziZ0yZLsgyvIY5kxcMC8ixCMxe22G7el0jUGUUZ_rzDI858X4DT7LWuz2O8xGSLEmSgKoOgn-CjPYi5SNz5qEX9r1P5JvFHDsgG8FIe1aKOpMPw7fGKyQf_Gmyh5WMuSrN4kXO_qDpYpEsS1X_BqV2XClCV2lNhDVt36RETmraHNggMLT0ZS9WRF9ag62N4rSZeTu_w3qHlmAGqNuhFeT6eYnwQdtKS-4PO1S8Dt49Ab-LDsOv8qVk9KvZF0jV8zzNlnT3-OXQwuaoVTRrU_pl_g=="; ud_rule_vars="eJx9js2OAiEQhF9lwtWfdMMwzPAskxBoG5esLlmG8WJ8d0k0xnjwVIfK91VdRfXlyJUP7pKWVHOxKvY9hghMU-hDlGGcYiRk8npQHLSlnH8TC9uJ6yxOfqmO8loWfhhcTWeeWzsLCRJ3MO6k6lDZHq00e62MNMMGwALMYts9DTWv9ONq8TEmckvzUfP5knw4PW25HP1fojeo8P_KLQ--fiyi6WCyMFip9xPiaPT7YkylUY-331mNSsGLvYnbHZHNWyA=:1mJ66m:ZzEc78wS3KZwnivXH5KvTiVM6VY"; eventing_session_id=qXXL9qcmS5m8irgkRKAX8Q-1629953654065; seen=1; __cf_bm=cda88cd547d893b799fe529ee6f327fc0aa0ab58-1629951854-1800-Ac0tJjy3X2RLIc43eNUamyz/YQdNsV7f8xhS+X/VCVdFoUM74+eLOjELwlqXCuj+y5oChBNe71xFqF5OvoWdS5U=; __cfruid=562c30e8af19e49e885493cb7e44f103cbba0175-1629951854')
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
            print(self.cookies['access_token'])
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

    def getEnrolledCoursesPerPage(self, uri='https://www.udemy.com/api-2.0/users/me/subscribed-courses?ordering=+enroll_time&fields[course]=@all&page_size=12'):
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
        Enrollment = requests.post('https://www.udemy.com/payment/checkout-submit/', json={"checkout_environment":"Marketplace","checkout_event":"Submit","shopping_info":{"items":[{"discountInfo":{"code":coupon_code},"buyable":{"type":"course","id":id,"context":{}},"price":{"amount":0,"currency":"USD"}}],"is_cart":False},"payment_info":{"method_id":"","payment_vendor":"Free","payment_method":"free-method"},"tax_info":{"tax_rate":0,"billing_location":{"country_code":"VN"},"currency_code":"usd","transaction_items":[{"udemy_txn_item_reference":f"course-{id}","tax_excluded_amount":0,"tax_included_amount":0,"tax_amount":0}],"tax_breakdown_type":"tax_inclusive"}}, cookies=self.cookies, headers={
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
            return dict(id=id, success=True, status_code=200, transaction_id=Enrollment.text)
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
