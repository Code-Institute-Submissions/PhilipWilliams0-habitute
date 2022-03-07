from django.shortcuts import render
import requests


# Create your views here.
def news_idx(request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key=6e62d2407ee16a925395dba5c53def18&keywords=fashion&countries=us,gb')
    res = r.json()
    data = res['data']
    title = []
    description = []
    image = []
    url = []
    for i in data:
        title.append(i['title'])
        description.append(i['description'])
        image.append(i['image'])
        url.append(i['url'])
    news = zip(title, description, image, url)
    return render(request, 'newsapp/news_idx.html', {'news': news})
