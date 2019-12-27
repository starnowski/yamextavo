import yaml
import jsonpath_rw_ext as jp


class YamlFileHelper:

    def __init__(self, filepath):
        with open(filepath, "r") as f:
            yaml_file = yaml.load(f)
            self.json_data=yaml_file
        pass

    def contains_jsonpath(self, jsonpath):
        return jp.match(jsonpath, self.json_data)

    def return_first_value_by_jsonpath(self, jsonpath):
        for v in jp.match(jsonpath, self.json_data):
            return v
        return None