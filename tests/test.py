import unittest
from tests.mock_data import mock_json
from sniff_json import sniff_json_schema

class TestSniffJson(unittest.TestCase):
    def setUp(self):
        self.json = mock_json
        self.schema = {}
        sniff_json_schema(
            json_data=self.json, schema=self.schema
        )
        self.message = self.schema.get('message')

    def test_attributes_not_in_schema(self):
        self.assertFalse('attributes' in self.schema)

    def test_assert_tag_in_schema(self):
        for key in self.message.get('properties'):
            self.assertIn('tag', self.message['properties'][key])
    
    def test_assert_description_in_schema(self):
        for key in self.message.get('properties'):
            self.assertIn('description', self.message['properties'][key])

    def test_assert_required_is_false(self):
        for key in self.message.get('properties'):
            self.assertFalse(self.message['properties'][key]['required'])

    def test_participant_id_type_is_enum(self):
        self.assertTrue(self.message['properties']['participantIds']['type'], 'enum')

    def test_message_battle_participants_type_is_array(self):
        self.assertTrue(self.message['properties']['battle']['properties']['participants']['type'], 'array')