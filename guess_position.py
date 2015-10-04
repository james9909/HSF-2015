import requests
import json
from operator import itemgetter
from collections import OrderedDict
from bs4 import BeautifulSoup, SoupStrainer

def get_page(page):
    request = requests.get(page)
    return request.text

def get_solves(data):
    return json.loads(data)["solves"]

def get_score(solved):
    score = 0
    for problem in solved:
        score += problem["value"]
    return score

def get_teams():
    html = get_page("https://hsf.csaw.engineering.nyu.edu/teams")
    soup = BeautifulSoup(html, "lxml")
    teams = {}
    for team in soup.findAll("a", attrs={"target": ""}):
        if "team/" in team["href"]:
            teams[team.text] = team["href"]
    return teams

def get_team_position(scores, team):
    return scores.keys().index(team) + 1

URL = "https://hsf.csaw.engineering.nyu.edu/solves/"
teams = get_teams()
scores = {}
for team in teams:
    print "Parsing %s" % team
    number = teams[team].split("/")[-1]
    scores[team] = get_score(get_solves(get_page(URL + number)))

scores = OrderedDict(sorted(scores.items(), key=itemgetter(1), reverse=True))

print get_team_position(scores, "in/s/ane")
