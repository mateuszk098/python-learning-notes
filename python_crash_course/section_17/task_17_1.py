'''
Visualization of python's most stars repositories on GitHub, with API and Plotly.
'''

import requests

from plotly.graph_objs import Bar
from plotly import offline

url: str = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers: dict[str, str] = {"Accept": "application/vnd.github.v3+json"}

r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

response_dict: dict = r.json()
repo_dicts: dict = response_dict["items"]

repo_stars: list[int] = []
labels: list[str] = []
repo_links: list[str] = []

for repo_dict in repo_dicts:
    owner: str = repo_dict["owner"]["login"]
    description: str = repo_dict["description"]
    label: str = f"{owner}<br />{description}"
    labels.append(label)

    repo_name = repo_dict["name"]
    repo_url: str = repo_dict["html_url"]
    repo_link: str = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    repo_stars.append(repo_dict["stargazers_count"])

data = [{
    "type": "bar",
    "x": repo_links,
    "y": repo_stars,
    "hovertext": labels,
    "marker": {
        "color": "rgb(60, 100, 150)",
        "line": {"width": 1.5, "color": "rgb(25, 25, 25)"}
    },
    "opacity": 0.6
}]

my_layout = {
    "title": "Most stars Python's projects at GitHub.",
    "titlefont": {"size": 28},
    "xaxis": {
        "title": "Repository",
        "titlefont": {"size": 24},
        "tickfont": {"size": 14}
    },
    "yaxis": {
        "title": "Stars",
        "titlefont": {"size": 24},
        "tickfont": {"size": 14}
    }
}

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="python_repos.html")
