from rest_framework.routers import SimpleRouter
from cahiers import views


router = SimpleRouter()

router.register(r'cahiers', views.CahierViewSet, 'Cahier')
router.register(r'countries', views.CountryViewSet, 'Country')
router.register(r'cities', views.CityViewSet, 'City')
router.register(r'logements', views.LogementViewSet, 'Logement')

urlpatterns = router.urls
