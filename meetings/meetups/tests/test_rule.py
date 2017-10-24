from .base import BaseApiTestCase

from ..models import Rule
from ..serializers import RuleSerializer


class RulesTestCase(BaseApiTestCase):

    def create_rules(self):
        Rule.objects.create(
            start_time="2017-10-12T01:00:00+0000",
            end_time="2017-10-14T01:00:00+0000",
            period="day",
            category="CAN",
            user=self.authenticated_user,
        )
        Rule.objects.create(
            start_time="2017-10-12T01:00:00+0000",
            end_time="2017-10-14T01:00:00+0000",
            period="day",
            category="CAN",
            user=self.authenticated_user,
        )
        Rule.objects.create(
            start_time="2017-10-12T01:00:00+0000",
            end_time="2017-10-14T01:00:00+0000",
            period="day",
            category="CAN",
            user=self.not_authenticated_user,
        )

    def setUp(self):
        super(RulesTestCase, self).setUp()
        self.create_rules()

    def test_rules_list_GET_return_200_status_code(self):
        response = self.client.get('/api/v1/rules/')
        self.assertEqual(response.status_code, 200)

    def test_rules_list_return_correct_filter(self):
        response = self.client.get('/api/v1/rules/')
        expected_rules = Rule.objects.filter(user=self.authenticated_user)
        serializer = RuleSerializer(expected_rules, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(expected_rules.count(), 2)

    def test_rules_detail(self):
        rule = Rule.objects.filter(user=self.authenticated_user).first()
        response = self.client.get('/api/v1/rules/{}/'.format(rule.id))
        serializer = RuleSerializer(rule)
        self.assertEqual(response.data, serializer.data)

    def test_rules_POST(self):
        # todo: remove user from post
        data = {
            "start_time": "2017-10-12T01:00:00+0000",
            "end_time": "2017-10-14T01:00:00+0000",
            "period": "day",
            "category": "CAN",
            "user": str(self.authenticated_user.id),
        }
        url = '/api/v1/rules/'

        rules_quantity_before_post = Rule.objects.count()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)

        rules_quantity_after_post = Rule.objects.count()
        self.assertEqual(rules_quantity_after_post, rules_quantity_before_post + 1)
