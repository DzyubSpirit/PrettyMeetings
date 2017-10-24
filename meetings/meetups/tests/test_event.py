from .base import BaseApiTestCase

from ..models import Event
from ..serializers import EventSerializer


class EventTestCase(BaseApiTestCase):
    def create_events(self):
        Event.objects.create(
            author=self.authenticated_user,
            place='test1',
            description='test1',
        )
        Event.objects.create(
            author=self.authenticated_user,
            place='test2',
            description='test2',
        )
        Event.objects.create(
            author=self.not_authenticated_user,
            place='test3',
            description='test3',
        )

    def setUp(self):
        super(EventTestCase, self).setUp()
        self.create_events()

    def test_events_list_GET_return_200_status_code(self):
        response = self.client.get('/api/v1/events/')
        self.assertEqual(response.status_code, 200)

    def test_events_list_return_correct_filter(self):
        response = self.client.get('/api/v1/events/')
        expected_events = Event.objects.filter(author=self.authenticated_user)
        serializer = EventSerializer(expected_events, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(expected_events.count(), 2)

    def test_events_detail(self):
        event = Event.objects.filter(author=self.authenticated_user).first()
        response = self.client.get('/api/v1/events/{}/'.format(event.id))
        serializer = EventSerializer(event)
        self.assertEqual(response.data, serializer.data)

    def test_events_POST(self):
        # todo: remove user from post
        data = {
            "author": str(self.authenticated_user.id),
            "place": "test",
            "description": "test"
        }

        url = '/api/v1/events/'

        events_quantity_before_post = Event.objects.count()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)

        events_quantity_after_post = Event.objects.count()
        self.assertEqual(events_quantity_after_post, events_quantity_before_post + 1)
