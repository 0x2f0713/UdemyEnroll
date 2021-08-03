#!/usr/bin/python3
from Udemy import Udemy
import requests
import threading
import queue
import re
import sys
import urllib.parse as parse
import random
import time
import sys
from Crypto.Cipher import AES
import codecs


CoursesQueue = queue.Queue(maxsize=0)
User = Udemy("namhaiha0308@gmail.com", "qweqwerrr123456789")

def getInfinityFreeCookie(): 
    getRawData_request = requests.post("https://mess.0x2f0713.cf/api/enroll_udemy/logs",verify=False)
    print(getRawData_request.text)
    x = re.findall("[a-f0-9]{32}", getRawData_request.text)
    if x:
        for index_x,i in enumerate(x):
            x[index_x] = codecs.decode(i,"hex")
        iv = x[1]
        ct = x[2]
        cipher = AES.new(x[0], AES.MODE_CBC, iv)
        res = cipher.decrypt(ct).hex()
        print(res)
        return res
    else:
        print("No need cookie")
        return "b9cb98eab7325b9bac3a43cda928a72b"


class EnrollThreading(threading.Thread):
    def __init__(self, queue, user):
        threading.Thread.__init__(self)
        self.queue = queue
        self.Udemy = user
        self.begin = 1
        self.end = 10

    def writeProgress(self):
        sys.stdout.write(
            "\rFound: {size} {noun}".format(
                size=self.queue.qsize(),
                noun="course" if self.queue.qsize() < 2 else "courses",
            )
        )
        sys.stdout.flush()

    def addCourse(self, url):
        ParseResult = parse.urlparse(url)

        coupon_code = ParseResult.query.lstrip("couponCode=")
        published_title = ParseResult.path.strip("/")

        CourseInfo = self.Udemy.getCourseInfo(published_title)

        if CourseInfo["status_code"] == 200:
            data = CourseInfo["data"]
            id = data["id"]
            title = data["title"]
            PurchaseInfo = self.Udemy.getCoursePurchaseInfo(id, coupon_code)["data"]
            if PurchaseInfo["purchase"]["data"]["purchase_date"] is None:
                if (
                    data["is_paid"]
                    and PurchaseInfo["purchase"]["data"]["pricing_result"]["price"][
                        "amount"
                    ]
                    == 0
                ):
                    self.queue.put(
                        dict(
                            published_title=published_title,
                            title=title,
                            id=id,
                            coupon_code=coupon_code,
                        )
                    )
                elif not data["is_paid"]:
                    self.queue.put(
                        dict(
                            published_title=published_title,
                            title=title,
                            id=id,
                            coupon_code="",
                        )
                    )


class discudemy(EnrollThreading):
    def __init__(self, queue, user):
        EnrollThreading.__init__(self, queue, user)

    def run(self):
        def scanPage(self, i):
            try:
                HTML = requests.get(
                    "https://www.discudemy.com/all/{number}".format(number=i),
                    allow_redirects=True,
                )
                # print("%s: %i" % (self.name, i))
                URLS = re.findall(
                    r'<a class="card-header" href="((http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[discudemy]*\.[a-z]{2,5}?(\/.*)?)">',
                    HTML.text,
                )
                if len(URLS) == 0:
                    print("discudemy error")
                else:
                    for x in range(0, 15):
                        endpoint = URLS[x][2].strip("/").split("/")
                        if endpoint[0] == "giveaway":
                            continue
                        info = requests.get(
                            "https://www.discudemy.com/go/{published_title}".format(
                                published_title=endpoint[1]
                            )
                        ).text
                        url = re.search(
                            r"(https):\/\/(www\.udemy)([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?",
                            info,
                        )[0].replace("/course/", "/")
                        self.addCourse(url)
                        self.writeProgress()
            except:
                sys.exit(1)

        for i in range(self.begin, self.end):
            t_page = threading.Thread(target=scanPage, args=(self, i,))
            t_page.start()
            t_page.join()


class udemycoupon_learnviral_com(EnrollThreading):
    def __init__(self, queue, user):
        EnrollThreading.__init__(self, queue, user)

    def run(self):
        def scanPage(self, i):
            try:
                HTML = requests.get(
                    "https://udemycoupon.learnviral.com/coupon-category/free100-discount/page/{number}".format(
                        number=i
                    ),
                    allow_redirects=True,
                    headers={
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3800.0 Safari/537.36 Edg/76.0.167.1"
                    },
                )
                URLS = re.findall(r'(https://www\.udemy\.com.*)(" id)', HTML.text)
                if len(URLS) == 0:
                    print("udemycoupon.learnviral.com error")
                for url in URLS:
                    self.addCourse(url[0].replace("/course/", "/"))
                    self.writeProgress()
            except:
                sys.exit(1)

        for i in range(self.begin - 1, self.end):
            t_page = threading.Thread(target=scanPage, args=(self, i,))
            t_page.start()
            t_page.join()


class freebiesglobal_com(EnrollThreading):
    def __init__(self, queue, user):
        EnrollThreading.__init__(self, queue, user)

    def run(self):
        def scanPage(self, i):
            try:
                HTML = requests.get(
                    "https://freebiesglobal.com/dealstore/udemy/page/{number}".format(
                        number=i
                    ),
                    allow_redirects=True,
                )
                # print("%s: %i" % (self.name, i))
                URLS = re.findall(
                    r'<a class="img-centered-flex rh-flex-center-align rh-flex-justify-center" href="(https:\/\/freebiesglobal\.com\/[\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])',
                    HTML.text,
                )
                if len(URLS) == 0:
                    print(HTML)
                    print("freebiesglobal_com error")
                for x in URLS:
                    info = requests.get(x).text
                    url = re.search(
                        r"(https):\/\/(www\.udemy)([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?",
                        info,
                    )
                    if url is not None:
                        url = url[0].replace("/course/", "/")
                        self.addCourse(url)
                        self.writeProgress()
            except:
                sys.exit(1)

        for i in range(self.begin, self.end):
            t_page = threading.Thread(target=scanPage, args=(self, i,))
            t_page.start()
            t_page.join()

res_cookie = getInfinityFreeCookie()
Thread_Discudemy = discudemy(CoursesQueue, User)
Thread_Discudemy.start()
Thread_udemycoupon_learnviral_com = udemycoupon_learnviral_com(CoursesQueue, User)
Thread_udemycoupon_learnviral_com.start()
Thread_freebiesglobal_com = freebiesglobal_com(CoursesQueue, User)
Thread_freebiesglobal_com.start()

Thread_Discudemy.join()
Thread_udemycoupon_learnviral_com.join()
Thread_freebiesglobal_com.join()
print("Scanning done!")


while not CoursesQueue.empty():
    Course = CoursesQueue.get()
    print(Course["id"], Course["coupon_code"])
    if (
        User.getCoursePurchaseInfo(Course["id"])["data"]["purchase"]["data"][
            "purchase_date"
        ]
        is None
    ):
        if Course["coupon_code"] == "":
            Enrollment = User.enrollFreeCourse(Course["id"])
        else:
            Enrollment = User.enrollPaidCourseWithCouponVersion2(
                Course["id"], Course["coupon_code"]
            )
        if Enrollment["success"]:
            print(
                f"Enrolled: {Course['title']}. ID: {Course['id']}. Task left: {CoursesQueue.qsize()}"
            )
            LogRequest = requests.post(
                "https://mess.0x2f0713.cf/api/enroll_udemy/logs",
                verify=False,
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.53",
                    "upgrade-insecure-requests": "1",
                    "Cookie":"__test="+res_cookie
                },
                json={
                    "course_id": Course["id"],
                    "course_long_id": Course["published_title"],
                    "course_name": Course["title"],
                    "free": Course["coupon_code"] == "",
                },
            )
        else:
            print(Enrollment)
        for x in range(1, random.randint(10, 20)):
            sys.stdout.write("\rPausing: %s" % str(x))
            sys.stdout.flush()
            time.sleep(1)
        print()
    else:
        print(
            f"The '{Course['title']}' has been already enrolled. ID: {Course['id']}. Task left: {CoursesQueue.qsize()}"
        )
