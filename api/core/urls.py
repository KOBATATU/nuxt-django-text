
from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path
# from app.urls import router as app_router
from app.views import PredictAPIView

urlpatterns = [
    url(r"^admin/",admin.site.urls),
    path("api/predict/",PredictAPIView.as_view())
    # url(r"^api/predic",include(app_router.urls))

]
