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
        parse.load('__cfduid=da6b138a2e0274d9d86d5dc5542b693fa1597692772; ud_cache_modern_browser=1; ud_cache_language=en; __udmy_2_v57r=4ff0c854b92543e7bbc716a780a7e8ba; ud_cache_marketplace_country=VN; ud_firstvisit=2020-08-17T19:32:55.421087+00:00:1k7ksJ:J76YnjQvE-2gc9wq32SIgPuxWbo; ud_cache_version=1; ud_cache_price_country=VN; EUCookieMessageShown=true; EUCookieMessageState=initial; __ssid=183b9e0d2ba7fd81cd6ef2050907b17; ud_credit_last_seen=None; ud_cache_logged_in=1; csrftoken=X2V4H95OsvDZAUkG2gNZtBG5msfh9g1RfFa0AojFNN9czMzxtg35QLIRRKAg78tT; client_id=bd2565cb7b0c313f5e9bae44961e8db2; access_token=bTuRa3FwXdfG4zZTXtTiAa7zzsYQhnCsB1saJDTt; dj_session_id=yjq3q7y188s14wgv2o0sx656ekdmd8d6; ud_cache_user=33252734; quality_general=720; caption=en; intercom-session-sehj53dd=eHJpRW1yWCtvbTlrVkVWOFU5T01HckVtbXlLSHF2V1pWYmVBSG0zUyt5YnZXaXNSaExCQ0dod01NalBnVTNyNS0tN1FMZEY4VVZHUC9iSDdiaHM2WDJLZz09--449a086d60eebb7120df2a539d68bf17023ec826; muxData=mux_viewer_id=6afc2c40-1fbc-47e5-b89d-595a024f0697&msn=0.7929344385681227&sid=ff8a70b8-a404-4942-bff2-27944eea0363&sst=1597696440120&sex=1597698893491; ud_cache_release=7f4ed8d139af2e6ee688; ud_cache_device=desktop; seen=1; __cfruid=9458b0560f9c904ca6f238b24838af9b7a0e49f6-1597736524; ud_credit_unseen=0; ud_cache_brand=VNen_US; ud_cache_campaign_code=SKILLUPSALE; ud_rule_vars="eJyFj01uwyAQha9isW0TDRgbzFksoYEMCUpaVBhnE-XuRUoiVe2i26f3vZ-bYKxHYjr4a26ZS3U6JYh20mFRkx7JhBCNnNFYQEM2oIulnDMJN4jbKlKujR-sPyDT2vVVKFCwA7uTZpCLG5Wbpr2Wo9bjG4ADWMV7d12wo5W-Nmr_wdbOC8g_MJctnjxXTClH38pWI_kr1ozh8kzLn43rFvuzH1zszkbP2Zw_fjfbAYzTs4M-W6lZmlfzXdy_ASz_W-U=:1k7wJp:sQFZSmNKzZXuOzljmeCCUggCzGY"; ud_user_jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJncm91cF9pZHMiOltdLCJpc19zdXBlcnVzZXIiOmZhbHNlLCJlbWFpbCI6Im5hbWhhaWhhMDMwOEBnbWFpbC5jb20iLCJpZCI6MzMyNTI3MzR9.TNAV-nT_IZYFjIfuQqdXguzyVKXHfGGbpGSy3sUsUHI; evi="SlFeMhlATzcTQRN2XEBPNxMFSmNUVUd/BV8JN0xYRDFMXwkyGxJXdkpRGXlZUld2SlFdIExYQn4DSwdjGEBPfUwOB2MNFgVuCwgJc1ZSRW4LCAk3D0BPewFFH21MFFd2AA4HY1xWTH4TSVBjGANXdgdAH3FCQANuC0FWPEJABjsTSVBjXFpNfhNJUGMYA1d2BkEedUJAA24LQlZtTFBAdQlRETpMFBRuC0Ued1ZOVzoTSRo8QkBHeghDCXsVQAMtE0kddlZSWW5HURF5E05XfglGHWNUGVc6UFERdl9bQ2ATBQl7XB9ZbgNBEnlMWA5uRxIJe1taR3wdUV1jVFMIYBNBHnZWQE83EwVKY1RUQH8BXwk3TFhEMUxfCScLQE83E0ETdVxATzcTBUpjVFVEegdfCTdMWEQxTF8JMQ8bV3ZKURl3WVBXdkpRXSBMWEN7AkUHYxhAT31MDgdjDQ4FPBNJUGNcWkB0E0lQYxgDV3YGQRtxQkADbgtCVjxCQAAoXRpfJExYDm4DSxhzTFgObkcSCXtZU0F4HVFdY1RTCDFM"; eventing_session_id=0NIe6BsASAC52cByQzLOcA-1597738566836; ')
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
        Enrollment = requests.post('https://www.udemy.com/payment/checkout-submit/', json={"checkout_event":"Submit","shopping_cart":{"items":[{"discountInfo":{"code":coupon_code},"purchasePrice":{"amount":0,"currency":"USD","price_string":"Free","currency_symbol":"$"},"buyableType":"course","buyableId":id,"buyableContext":{}}],"is_cart":False},"payment_info":{"payment_vendor":"Free","payment_method":"free-method"},"tax_info":{"is_tax_enabled":True,"tax_rate":0,"billing_location":{"country_code":"VN","secondary_location_info":None},"currency_code":"usd","transaction_items":[{"tax_amount":0,"tax_included_amount":0,"tax_excluded_amount":0,"udemy_txn_item_reference":f"course-{id}"}],"tax_breakdown_type":"tax_inclusive"}
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
            return dict(id=id, success=True, status_code=200, transaction_id=json.loads(Enrollment.text)['data']['transaction_id'])
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
