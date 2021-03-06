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

def keyProductInteractions_page(req):
   return FileResponse("KeyProductInteractions.html")

def features_page(req):
   return FileResponse("features.html")

# def costs_page(req):
#    return FileResponse("costs.html")

# def  revenue_page(req):
#    return FileResponse("revenue.html")

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

      # Create route that handles server requests at /KeyProductInteractions
      config.add_route('KeyProductInteractions', '/KeyProductInteractions' )
      config.add_view(keyProductInteractions_page, route_name = 'KeyProductInteractions')

      # Create route that handles server requests at /features
      config.add_route('features', '/features' )
      config.add_view(features_page, route_name = 'features')

      # # Create route that handles server requests at /costs
      # config.add_route('costs', '/costs' )
      # config.add_view(costs_page, route_name = 'costs')

      # # Create route that handles server requests at /revenue
      # config.add_route('revenue', '/revenue' )
      # config.add_view(revenue_page, route_name = 'revenue')

       # Add a static view
      config.add_static_view(name='/', path='./public', cache_max_age=3600)
      
       # Create an app with the configuration specified above       
      app = config.make_wsgi_app()
       
   # start the server on port 6543
   print("Server started on port 6543")
   server = make_server('0.0.0.0', 6543, app) 
   server.serve_forever()