import requests
import re
import json
import urllib.parse as parse
from http.cookies import SimpleCookie


class Udemy:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3800.0 Safari/537.36 Edg/76.0.167.1"
        self.Courses = []
        parse = SimpleCookie()
        parse.load('__cfduid=d1a96af197869b04489c4fb5698d415921566837072; ud_cache_version=1; ud_cache_device=None; __udmy_2_v57r=0227efd3c2ad4a5d8a91a34ff2da980d; ud_firstvisit=2019-08-26T16:31:12.843499+00:00:1i2Htg:vzLX-iOKyXHlb62he1ZYNogwxks; ud_cache_price_country=VN; ud_cache_marketplace_country=VN; ud_cache_language=en; ud_cache_brand=::VN:en_US; EUCookieMessageShown=true; EUCookieMessageState=initial; ud_cache_release=2fbe2f5f8fcbaff1881961e25696491631f7e3a3; seen=1; eventing_session_id=b0453f0ca454445cb92ef24c48184223; _pxhd=8f4c955dcba5b7fef827f239df1ded881bae985f3ad7fed6a408468e0e62c69c:837ccd40-c8de-11e9-a0b0-59e67ff1cda2; client_id=bd2565cb7b0c313f5e9bae44961e8db2; dj_session_id=btjqpqm09rpcarz3r6f2j56zagkyugmi; csrftoken=ARrdukM20imoMYU0pmU4stTx68ZXonUO9312GEOnGgSXalYCxaxMYUN34W5kjVIl; ud_credit_unseen=0; access_token=npRfMMVtNjTsYrauoMZX430KftH9bBD88FtBgeNF; ud_credit_last_seen=None; ud_cache_user=33252734; ud_cache_logged_in=1; ud_cache_campaign_code=MORETHANACOURSE; evi="SlFHKAYSV3ZKURlzXVBXdkpRXWNUU1luRxIJe1tURnxMDgdjHRVXdkpRGXNaUld2SlFdY1RTWW5HEgl7W1RAfExfCXNdUU1uCwgJN0xYRGATBUpjVFdMfwkOB2NcU0B8E0lQYxhAT30dUV0gTFhAeANFVm1MUEd/AVEROkwUV3YAXwk3D0BPeQdBGTxCQEd+BUsJexVAA24LQhttTBQUbgtGHXZeH1luA0ESeUxYDm5HURFwQkADLRNJHnlfWghgE0EYclpATzcTBQl7X05XOlBREXRXUEcxTA4="; ud_rule_vars="eJyFy0EKwjAQQNGryGy1Mpm0aZKzBMrQmUhQKKbRTendLYhrt5__Nmhcb9pUpndZS1tqRKJRs9iZWHoexHMwbPucSTh4lDgvy70oxBNsCXKpa_vaSbhpOnoCQhM69B25k3HRmmjo6u3gzHhGjIgJLsf14INWfb50_Yt9GND98A77B9bQNRw=:1i2dLO:gmDCgBAOiFlqElmioEr-42odcj4"; useragent=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzc2LjAuMzgwOS4xMDAgU2FmYXJpLzUzNy4zNg%3D%3D; ')
        self.cookies = {}
        for key, morsel in parse.items():
            self.cookies[key] = morsel.value
        self.Bearer = 'Bearer {access_token}'.format(
            access_token=self.cookies['access_token'])
        self.csrftoken = self.cookies['csrftoken']
        self.dj_session_id = self.cookies['dj_session_id']
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
            'password': self.password
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

    def parseUri(self, url):
        ParseResult = parse.urlparse(url)
        return dict(published_title=ParseResult.path.strip('/'), id=self.getCourseInfo(ParseResult.path.strip('/'))['id'], coupon_code=ParseResult.query.lstrip('couponCode='))

    def updateCookie(self, cookies):
        return self.cookies.update(requests.utils.dict_from_cookiejar(cookies))
# p1 = Udemy('namhaiha0308@gmail.com','qweqwerrr123456789')
# p1.login()
# p1.getEnrolledCourses()
# p1.writeListCourses()
