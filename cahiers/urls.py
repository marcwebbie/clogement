from rest_framework.routers import SimpleRouter
from cahiers import views


router = SimpleRouter()

router.register(r'cahier', views.CahierViewSet, 'Cahier')
router.register(r'country', views.CountryViewSet, 'Country')
router.register(r'city', views.CityViewSet, 'City')
router.register(r'logement', views.LogementViewSet, 'Logement')

urlpatterns = router.urls
