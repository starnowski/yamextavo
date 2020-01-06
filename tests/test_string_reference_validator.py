import unittest
import os
from os import path
import yaml
from yamextavo import YamaleRequiredReferenceFacade


class TestRequiredReferenceValidator(unittest.TestCase):

    schema_file = path.join(os.path.dirname(__file__), "string_reference_validator/schemas/1/schema.yml")

    def test_should_return_validation_error_for_invalid_schema_where_child_element_has_invalid_content_and_primary_node_not_exists(self):
        # given
        tested = YamaleRequiredReferenceFacade(self.schema_file)
        test_file = path.join(os.path.dirname(__file__), "string_reference_validator/schemas/1/invalid_content_validation_message/nonexistent_parent_invalid_child.yml")
        with open(test_file, "r") as f:
            yaml_data = yaml.full_load(f)
            self.assertTrue("dependent_node2" in yaml_data, "Yaml should contains property \"dependent_node2\"")
            self.assertEqual("xxx", yaml_data.get("dependent_node2"), "The element \"dependent_node2\" should have value \"xxx\"")
            self.assertFalse("primary_node2" in yaml_data, "Yaml should not contains property \"dependent_node2\"")

        try:
            # when
            tested.validate(test_file)
            self.fail("Expected ValueError")

        except ValueError:
            # then
            pass

    def test_should_return_validation_error_for_invalid_schema_where_child_element_has_invalid_content_and_primary_node_is_empty(self):
        # given
        tested = YamaleRequiredReferenceFacade(self.schema_file)
        test_file = path.join(os.path.dirname(__file__), "string_reference_validator/schemas/1/invalid_content_validation_message/empty_parent_invalid_child.yml")
        with open(test_file, "r") as f:
            yaml_data = yaml.full_load(f)
            self.assertTrue("dependent_node2" in yaml_data, "Yaml should contains property \"dependent_node2\"")
            self.assertEqual("xxx", yaml_data.get("dependent_node2"), "The element \"dependent_node2\" should have value \"xxx\"")
            self.assertTrue("primary_node2" in yaml_data, "Yaml should contains property \"primary_node2\"")
            self.assertEqual(None, yaml_data.get("primary_node2"), "The element \"primary_node2\" should have value \"None\"")

        try:
            # when
            tested.validate(test_file)
            self.fail("Expected ValueError")

        except ValueError:
            # then
            pass

    def test_should_return_validation_error_for_invalid_schema_where_child_element_is_required_but_not_exists(self):
        # given
        tested = YamaleRequiredReferenceFacade(self.schema_file)
        test_file = path.join(os.path.dirname(__file__), "string_reference_validator/schemas/1/invalid_content_required_message/non_empty_primary_node.yml")
        with open(test_file, "r") as f:
            yaml_data = yaml.full_load(f)
            self.assertFalse("dependent_node2" in yaml_data, "Yaml should not contains property \"dependent_node2\"")
            self.assertTrue("primary_node2" in yaml_data, "Yaml should contains property \"primary_node2\"")
            self.assertEqual("parent", yaml_data.get("primary_node2"), "The element \"primary_node2\" should have value \"parent\"")

        try:
            # when
            tested.validate(test_file)
            self.fail("Expected ValueError")

        except ValueError:
            # then
            pass


if __name__ == '__main__':
    unittest.main()