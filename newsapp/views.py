import os
from django.shortcuts import render
from dotenv import load_dotenv
import requests

load_dotenv()
# environment variables
MEDIASTACK_KEY = os.environ.get("MEDIASTACK_KEY")


# Create your views here.
def news_idx(request):
    r = requests.get(
        f'http://api.mediastack.com/v1/news?access_key={MEDIASTACK_KEY}&\
        keywords=fashion&countries=gb')
    res = r.json()
    data = res['data']
    title = []
    description = []
    image = []
    url = []
    published_at = []
    for i in data:
        title.append(i['title'])
        description.append(i['description'])
        image.append(i['image'])
        url.append(i['url'])
        published_at.append(i['published_at'])
    news = zip(title, description, image, url, published_at)
    return render(request, 'newsapp/news_idx.html', {'news': news})
