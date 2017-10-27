from .base import BaseApiTestCase

from ..models import EventUser
from ..serializers import EventUserSerializer


class SuggestionsTestCase(BaseApiTestCase):
    def setUp(self):
        super(SuggestionsTestCase, self).setUp()

    def test_all(self):
        pass
        # must take event argument and return all guests
        # only author can send post to create new suggestions
