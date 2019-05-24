from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from django.urls import re_path

import chat.routing
from tailf.consumers import TailfConsumer

# application = ProtocolTypeRouter({
#     'websocket':
#         URLRouter([
#             chat.routing.websocket_urlpatterns,
#             re_path(r"^ws/tailf/(?P<id>\d+)/$", TailfConsumer)
#         ])
# })


url_patterns =  chat.routing.websocket_urlpatterns + [re_path(r"^ws/tailf/(?P<id>\d+)/$", TailfConsumer)]
application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            url_patterns
        )
    ),
})