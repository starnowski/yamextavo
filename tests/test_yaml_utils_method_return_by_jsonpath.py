import unittest
from yaml import load
from yamextavo.validators import YamlFileHelper
import os
from os import path


class TestYamlFileHelper(unittest.TestCase):

    test_file = path.join(os.path.dirname(__file__), "yaml_utils/data.yaml")
    tested = YamlFileHelper(test_file)

    def test_should_return_correct_value_for_existed_main_root_node(self):
        # given
        with open(self.test_file, "r") as f:
            yaml_data = load(f)
            self.assertTrue("organization" in yaml_data, "Yaml should contains property \"organization\"")
            self.assertEqual(yaml_data.get("organization"), "Community", "Yaml should contains property \"organization\" with value \"Community\"")

        # when
        result = self.tested.return_first_value_by_jsonpath("organization")

        # then
        self.assertEqual(result, "Community" , "YamlFileHelper object should return value \"Community\" for \"organization\" node!")

    def test_should_return_none_value_for_non_existed_main_root_node(self):
        # given
        with open(self.test_file, "r") as f:
            yaml_data = load(f)
            self.assertFalse("company" in yaml_data, "Yaml should not contains property \"organization\"")

        # when
        result = self.tested.return_first_value_by_jsonpath("company")

        # then
        self.assertIsNone(result, "YamlFileHelper object should return None value for node \"company\"!")
