from flask import Flask
from mapi.api.movies.views import movie_blueprint

app = Flask(__name__)
app.register_blueprint(movie_blueprint, url_prefix='/movies')

if __name__=='__main__':
  app.run()