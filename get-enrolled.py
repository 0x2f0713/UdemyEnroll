from Udemy import Udemy
import requests
Session = Udemy('namhaiha0308@gmail.com','qweqwerrr123456789')
newfile = open("Enrolled.txt","a+")
amount = Session.getEnrolledCourseAmount() // 100 + 2
for i in range(1,amount):
    data = Session.getEnrolledCoursesPerPage("https://www.udemy.com/api-2.0/users/me/subscribed-courses?page_size=100&page={page}&fields=@min".format(page = i))
    print(i)
    for y in data:
        newfile.write(y['published_title']+"\n")
        #print(y['published_title'])
