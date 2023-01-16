from rest_framework import routers

api_routers = routers.DefaultRouter()

# views
from apps.customers import views as customer_views
from apps.products import views as product_views
from  apps.plans import views as plan_view
from apps.aports import views as aport_views

# register routers
api_routers.register('customers', customer_views.ClienteView)
api_routers.register('products', product_views.ProdutoView)
api_routers.register('plans', plan_view.ContratacaoPlanoView)
api_routers.register('aports', aport_views.AporteExtraView)
api_routers.register('rescues', aport_views.ResgateView)
