from model_mommy import mommy
import pytest

from cahiers.models import Cahier, Logement
from cahiers.serializers import CahierSerializer


@pytest.mark.django_db
def test_cahiers_logement_hashids_related_field_is_list_of_logements():
    cahier = mommy.make(Cahier)
    serializer = CahierSerializer(cahier)
    mommy.make(Logement, cahier=cahier)
    mommy.make(Logement, cahier=cahier)
    mommy.make(Logement, cahier=cahier)

    print(serializer.data)
    assert 'logements' in serializer.data.keys()
    assert isinstance(serializer.data['logements'], list)
