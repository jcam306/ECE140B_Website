#import all the necessary libraries
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import FileResponse


def index_page(req):
   return FileResponse("index.html")

def product_page(req):
   return FileResponse("product.html")

def kvp_page(req):
   return FileResponse("kvp.html")

def mockUI_page(req):
   return FileResponse("mockUI.html")

def designLaws_page(req):
   return FileResponse("designLaws.html")
 
#Line below tells executor to start from here
if __name__ == '__main__':
   with Configurator() as config:
       
       # Create a route called home
      config.add_route('home', '/')      
       # Bind the view (defined by index_page) to the route named ‘home’
      config.add_view(index_page, route_name='home')
      
      #  Create a route that handles server HTTP requests at: /product
      config.add_route('product', '/product')       
      #  Binds the function get_music route and returns product page
      config.add_view(product_page, route_name='product')

      # Create route that handles server requests at /kvp
      config.add_route('kvp', '/kvp' )
      config.add_view(kvp_page, route_name = 'kvp')
 
       # Create route that handles server requests at /mockUI
      config.add_route('mockUI', '/mockUI' )
      config.add_view(mockUI_page, route_name = 'mockUI')

      # Create route that handles server requests at /designLaws
      config.add_route('designLaws', '/designLaws' )
      config.add_view(designLaws_page, route_name = 'designLaws')
      
       # Add a static view
      config.add_static_view(name='/', path='./public', cache_max_age=3600)
      
       # Create an app with the configuration specified above       
      app = config.make_wsgi_app()
       
   # start the server on port 6543
   print("Server started on port 6543")
   server = make_server('0.0.0.0', 6543, app) 
   server.serve_forever()