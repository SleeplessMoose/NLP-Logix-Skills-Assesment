import requests
import time
def challenge5():
    webpage = "https://www.google.com/"
    start_time = time.time()
    req_page = requests.get(webpage)
    with open("web-download.html", 'wb') as file:
        file.write(req_page.content)
    end_time = time.time()

    total_time = end_time - start_time
    print "Elapsed time: ", total_time, " s"
