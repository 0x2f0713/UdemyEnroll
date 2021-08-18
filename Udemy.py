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
        parse.load('ud_firstvisit=2021-08-17T09:06:25.519466+00:00:1mFv3B:UB4VctGyHbjeA_rcPVcgIVoU3Cs; __udmy_2_v57r=3f441bf0ec9b4bf2b89ffc1eca563eb5; EUCookieMessageShown=true; EUCookieMessageState=initial; _gcl_au=1.1.1093631453.1629191193; blisspoint_fpc=ece09d7c-2d52-4be4-a3d6-3fd107d265fa; __ssid=11e9d947ae89cf02490440d84875593; _rdt_uuid=1629191198124.347bd41f-0739-4468-9d13-a18b0fb84d49; dj_session_id=1m7jsdqsevfslke2ipcznhdu9mte4w8x; ud_credit_last_seen=None; ud_user_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MzMyNTI3MzQsImdyb3VwX2lkcyI6W10sImlzX3N1cGVydXNlciI6ZmFsc2UsImVtYWlsIjoibmFtaGFpaGEwMzA4QGdtYWlsLmNvbSJ9.YKhuPXqbc3Odge15tMxQw56fl8XCPCu8nOM-kpjNSz4; access_token=MYeEeGSu7ytfdMclznI8lfNYNKRhdfhxc0N6XnVj; client_id=bd2565cb7b0c313f5e9bae44961e8db2; csrftoken=L0ssYgZzzIsEZty6R7s9f4neBw1s7AOpaC7FkQpXt5Y9mTKkbFoReID3erLII3EK; stc111655=tsa:1629191195194.1181633872.632246.5289537832286677.4:20210817093713|env:1%7C20210917090635%7C20210817093713%7C2%7C1014624:20220817090713|uid:1629191195194.372935510.1142955.111655.764040926.2:20220817090713|srchist:1014624%3A1%3A20210917090635:20220817090713; IR_PI=d3e4d6bd-2ed2-3a29-bb67-9e002606d070%7C1629277633669; ki_t=1629191238948%3B1629191238948%3B1629191238948%3B1%3B1; seen=1; __cfruid=535eccb6cc26ae227b9da0143eff26575dab8ce5-1629300882; ud_credit_unseen=0; ud_cache_user=33252734; ud_cache_campaign_code=LV2LRNCP80921B; ud_cache_modern_browser=1; ud_cache_version=1; ud_cache_marketplace_country=VN; ud_cache_price_country=VN; ud_cache_release=4231c926ee89175c1d60; ud_cache_brand=VNen_US; ud_cache_language=en; ud_cache_logged_in=1; ud_cache_device=desktop; _gid=GA1.2.1372064011.1629300891; _ga_7YMFEFLR6Q=GS1.1.1629300892.9.1.1629301113.55; _ga=GA1.2.992033820.1629191188; __cf_bm=83565057ed5460e67bd78a1823a815f010ab799e-1629302128-1800-AXhQWj1R3gnScAOYvMhF5q3PdFz/sgyRwljRiUqVl11MrVaWiL8Uu8za5jtA1zazS300ZYYL0IgGrySBaz1NWiLmCdLRbR4TEUzktiocVLpxy7M4CuNufCSZ1tUre5CIacYK0FczMN+owusXptUylurfHQeXt8kB0ajFJidw3ej+; evi="3@SKjARn-d1abVObNioN5IZhTKTPyFlhz-6uAT4tNs_rOCgG03vssnAQnPOODMctwM_4ivmdoy6p8cha5Mk1F6msMYrp-VYeaSdN18iVk4gD2mbTO5gj9-GsPMBgwCczaviFjW3RWak2InMlRBeY99oSa9rDTgRIdg_qBvCzMA9juC_-M7p_IyPCvYXKme5LbPUBB5MFgxuJZewoi5TIdNFBe2nKr0jXB7xaicD9aWToZAbqauCVhBhn1JAqiR_yFkSaasXKyhJlTrpQkHDi3CbxiJ_WCL8mnejg6K-dm3l8PDogOgN233CAQjgP5LPU3JyIT4guelFKj9VJf_dtF63kC1u7FhStrq9JpTp0Zz6UqQ5gG5ckU42AsQ3zhqTjdOD1qt0770l_V7dBAteoVsZ1v24Yq7gdcJaEWBG9y3-nKgXnt4Aq3fRzF-TPwejqu21MKIrNvGKKJW7t6ZnwlPs8kX4Hv1baOpWKm6xV19Op7Qc6spqkMKqg=="; ud_rule_vars="eJyFjkFuwyAQRa9isW0dzYCxMWexhGAypKhpUDDOJvLdayXupllkNYuv997cRfXlxJWP7pbmVHOxKnYdhghMY-hClMGMMRIyed0rDtpSzt-JhW3EfRJnP1dX-Lrwdo--8rQNk5AgsQXT4tDAaKG3Uh9GRDPoDwALMInPZodrXujL1eJjTOTmvBRid_Ml-XDebbmc_CXRE4qpbNTj2zdBjUrBa5C2xMy7oaaf_wbToLbKWCUPsh_6Af8Mq1h_ARVtWyc=:1mGNub:vkZMbvzM56YCcJzAls5CiBIbkjg"; eventing_session_id=zpxo1gY2SXu1pFYEbynYvQ-1629303929383')
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
