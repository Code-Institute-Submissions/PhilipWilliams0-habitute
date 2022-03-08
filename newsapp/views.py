from django.shortcuts import render
import requests


# Create your views here.
def news_idx(request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key=6e62d2407ee16a925395dba5c53def18&keywords=fashion&countries=gb')
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
