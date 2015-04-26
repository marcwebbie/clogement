import pytest
from guardian.shortcuts import assign_perm
from model_mommy import mommy

from accounts.models import Profile
from cahiers.models import Cahier, Logement
from cahiers.serializers import CahierSerializer
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_cahiers_sets_permisions():
    john = User.objects.create(username='john.doe')
    jackie = User.objects.create(username='jackie.brown')
    profile_jackie = mommy.make(Profile, user=jackie)
    cahier_jackie = mommy.make(Cahier, profile=profile_jackie)
    mommy.make(Logement, cahier=cahier_jackie)
    mommy.make(Logement, cahier=cahier_jackie)
    mommy.make(Logement, cahier=cahier_jackie)

    assign_perm('view_cahier', john, cahier_jackie)
    assert john.has_perm('view_cahier', cahier_jackie) is True
