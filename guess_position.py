import requests
import json
import sys
from operator import itemgetter
from collections import OrderedDict
from bs4 import BeautifulSoup, SoupStrainer

from requests.exceptions import ConnectionError

def get_page(page):
    try:
        request = requests.get(page)
    except ConnectionError:
        print "Could not fetch page. Are you connected to the internet?"
        sys.exit(1)
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

def print_teams_around(scores, team):
    pos = scores.keys().index(team)
    ahead = scores.keys()[pos-1]
    ahead_points = scores[ahead]
    behind = scores.keys()[pos+1]
    behind_points = scores[behind]
    print "Team %s is ahead with %s points" % (ahead, ahead_points)
    print "Team %s is behind with %s points" % (behind, behind_points)

def print_team_position(scores, team):
    pos = scores.keys().index(team)
    if pos == -1:
        print "Invalid team"
        return
    print "%s is probably ranked %s out of %s teams with %s points" % (team, pos + 1, len(scores), scores[team])
    print_teams_around(scores, team)

def write_teams(scores):
    fout = open("scoreboard.txt", "w")
    scoreboard = ""
    for x in range(len(scores)):
        team = scores.keys()[x]
        score = scores[team]
        if score > 0:
            scoreboard += "%s. %s - %s\n" % (x + 1, team.encode("ascii", "ignore"), score)
    fout.write(scoreboard)
    fout.close()

URL = "https://hsf.csaw.engineering.nyu.edu/solves/"
teams = get_teams()
scores = {}
for team in teams:
    print "Parsing %s" % team
    number = teams[team].split("/")[-1]
    scores[team] = get_score(get_solves(get_page(URL + number)))

scores = OrderedDict(sorted(scores.items(), key=itemgetter(1), reverse=True))
write_teams(scores)

print_team_position(scores, "in/s/ane")
