import random
import urllib.request


def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)


download_web_image("http://s29281.pcdn.co/wp-content/uploads/2018/12/Tipstomaintaininteriorpaints.jpg")

