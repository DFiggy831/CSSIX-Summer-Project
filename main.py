import webapp2
import jinja2
from google.appengine.api import urlfetch
import json 
import os
import urllib
the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
class MainPage(webapp2.RequestHandler):
    def post(self):
        user_search = self.request.get('search')
        key = 'dd7ea6984amshefbca95228569eep19d405jsndeeed831f044'
        
        params = {
            'platform': 'pc'
        }
        formatted_params = urllib.urlencode(params)
        
        user_search = urllib.quote(user_search)
        
        endpoint = 'https://chicken-coop.p.rapidapi.com/games/' + user_search
        
        api_url = endpoint + '?' + formatted_params
        
        
        headers = {'X-RapidAPI-Key': key}
        
        response = urlfetch.fetch(
            url = endpoint,
            method = urlfetch.GET,
            headers = headers
        )   
        
        games_json = json.loads(response.content)
        
        game = games_json["result"]
        
        variable_dict = {
            "title": game["title"],
            "image": game["image"],
            "description": game["description"],
            "developer": game["developer"],
            "rating": game["rating"],
            "genre": game["genre"],
            "score": game["score"],
            "release_date": game["releaseDate"],
            "publisher": game["publisher"],
            }
        print("onfondvodnoid")
        test_template = the_jinja_env.get_template('game_page/game_page.html')
        self.response.write(test_template.render(variable_dict))
        
class HomePage(webapp2.RequestHandler):
    def get(self):
        test_template = the_jinja_env.get_template('home/home.html')
        self.response.write(test_template.render())
class ReviewPage(webapp2.RequestHandler):
    def get(self):
        test_template = the_jinja_env.get_template('review_page/review_page.html')
        self.response.write(test_template.render())
class TopPicks(webapp2.RequestHandler):
    def get(self):
        test_template = the_jinja_env.get_template('toppicks/top_picks.html')
        self.response.write(test_template.render())
class NewsPage(webapp2.RequestHandler):
    def get(self):
        test_template = the_jinja_env.get_template('news_page/news_page.html')
        self.response.write(test_template.render())

app = webapp2.WSGIApplication([
    ('/search_game', MainPage),
    ('/', HomePage),
    ('/reviews', ReviewPage),
    ('/news', NewsPage),
    ('/toppicks', TopPicks),
], debug=True)