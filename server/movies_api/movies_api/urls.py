from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from movies.views import *


urlpatterns = [
    # JWT
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

    path('admin/', admin.site.urls),
    path('api/movies', MoviesListCreate.as_view()),
    path('api/movies/<uuid:movie_id>', MovieRetrieveUpdateDestroy.as_view()),
    path('api/movies/<uuid:movie_id>/vote', VoteCreate.as_view()),
    path('api/auth/', include('rest_framework.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

# rogulik
# {
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MjU2ODg5NSwiaWF0IjoxNjc2NTIwODk1LCJqdGkiOiI4YjY1ZjJhN2Y0NzQ0ODcyODQzYTk5YjczMjY0ODUyYyIsInVzZXJfaWQiOjF9._dVjEBMHrgja9Q2d8FmqOe-e5i24POG0_ul6RAWZcsE",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc5NTQ0ODk1LCJpYXQiOjE2NzY1MjA4OTUsImp0aSI6Ijk3NmJkMDFkN2ZjNjQxYjJiYzVmZTlmYTI3MGEwZWE3IiwidXNlcl9pZCI6MX0.lKFIc_MWrH-zsn7v1qeX2bXuMUihA1UIggxDjw-zSVo"
# }

# abobaladno
# {
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MzAwMTcyMCwiaWF0IjoxNjc2OTUzNzIwLCJqdGkiOiJmZDY5ZWY5ZmUzMjE0MTMyOTA3YTU3MWRhNDgxMzI5MyIsInVzZXJfaWQiOjJ9._Ey2X2aDbOaSH6SwQqpz-df61PkZQ1dvDbXwIoi3g4Q",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc5OTc3NzIwLCJpYXQiOjE2NzY5NTM3MjAsImp0aSI6IjMyZWI4ZmY0MWQ0ODRmYjY5Y2MwNDUxMjU5N2E5MWRhIiwidXNlcl9pZCI6Mn0.zTu4JSueQlvnI8hb8pq85IxdLt6ckRflIFRQK75k9rw"
# }
