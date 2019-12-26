import threading
from yamale import validators
import itertools
import yamale

from yamextavo.utils import YamlFileHelper
from yamextavo.validators.required_reference_validator import RequiredReferenceValidator


class YamaleRequiredReferenceFacade():

    def __init__(self, schema_file):
        validators_list = validators.DefaultValidators
        validators_list[RequiredReferenceValidator.__name__] = RequiredReferenceValidator
        validators_list[RequiredReferenceValidator.tag] = RequiredReferenceValidator
        self.yamale_schema = yamale.make_schema(schema_file, validators=validators_list)

    def validate(self, data_file_path):
        yamale_data = itertools.chain(*map(yamale.make_data, [data_file_path]))
        threading.current_thread().__setattr__("yaml_data_store", YamlFileHelper(data_file_path))
        return yamale.validate(self.yamale_schema, yamale_data) is not None