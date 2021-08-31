from Udemy import Udemy
import requests
Session = Udemy('namhaiha0308@gmail.com','qweqwerrr123456789')
newfile = open("Enrolled.txt","w")
amount = Session.getEnrolledCourseAmount() // 100 + 2
start = 4
end = 3
for i in range(start,start + 1):
    data = Session.getEnrolledCoursesPerPage("https://www.udemy.com/api-2.0/users/me/subscribed-courses?ordering=+enroll_time&page_size=100&page={page}&fields=@min".format(page = i))
    print(i)
    for y in data:
        newfile.write(y['published_title']+"\n")
        #print(y['published_title'])
