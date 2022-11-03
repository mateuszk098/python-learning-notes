'''
Visualization of most popular articles at hacker-news.com with API and Plotly.
'''

import requests
from operator import itemgetter

from plotly.graph_objs import Bar
from plotly import offline


url: str = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"State code: {r.status_code}")

submission_ids = r.json()
submission_dicts: list[dict] = []

for submission_id in submission_ids[:30]:
    # Separate api request for each article.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Dictionary for each article.
    submission_dict = {
        "title": response_dict["title"],
        "hn_link": f"https://news.ycombinator.com/item?id={submission_id}",
        "comments": response_dict.get("descendants", 0)
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter("comments"), reverse=True)


titles: list[str] = []
links: list[str] = []
comments: list[int] = []

for submission_dict in submission_dicts:
    print(f"\nArticle title: {submission_dict['title']}")
    print(f"Link to discussion: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

    titles.append(submission_dict['title'])
    links.append(submission_dict["hn_link"])
    comments.append(submission_dict['comments'])

data = [{
    "type": "bar",
    "x": titles,
    "y": comments,
    "hovertext": links,
    "marker": {
        "color": comments,
        "colorscale": "Viridis",
        "reversescale": True
    },
    "opacity": 0.6
}]

my_layout = {
    "title": "Most popular articles at hacker-news.com",
    "titlefont": {"size": 28},
    "xaxis": {
        "title": "Article Title",
        "titlefont": {"size": 24},
        "tickfont": {"size": 14}
    },
    "yaxis": {
        "title": "Comments",
        "titlefont": {"size": 24},
        "tickfont": {"size": 14}
    }
}

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="hn_articles.html")
