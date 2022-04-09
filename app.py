#import all the necessary libraries
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import FileResponse


def index_page(req):
   return FileResponse("index.html")

# def music_page(req):
#    return FileResponse("music.html")
 
#Line below tells executor to start from here
if __name__ == '__main__':
   with Configurator() as config:
       
       # Create a route called home
       config.add_route('home', '/')
       
       # Bind the view (defined by index_page) to the route named ‘home’
       config.add_view(index_page, route_name='home')
      
      #  # Create a route that handles server HTTP requests at: /music
      #  config.add_route('music', '/music')
       
      #  # Binds the function get_music route and returns music page
      #  config.add_view(music_page, route_name='music')
 
       # Add a static view
       config.add_static_view(name='/', path='./public', cache_max_age=3600)
      
       # Create an app with the configuration specified above       
       app = config.make_wsgi_app()
       
   # start the server on port 6543
   print("Server started on port 6543")
   server = make_server('0.0.0.0', 6543, app) 
   server.serve_forever()