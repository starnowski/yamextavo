import threading
from yamale.validators import Validator, Any
import itertools
import yamale
from yamale import validators

from yamextavo.yaml_utils import YamlFileHelper


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

class RequiredReferenceValidator(Any):
    tag = 'ref_req'

    def __init__(self, *args, **kwargs):
        self.validators = [val for val in args if isinstance(val, Validator)]
        self.is_required = False
        self.jsonpath = args[0]
        super(RequiredReferenceValidator, self).__init__(*args, **kwargs)

    def _is_valid(self, value):
        return True

    @property
    def is_optional(self):
        required = False
        ct = threading.current_thread()
        if not hasattr(ct, 'yaml_data_store'):
            pass #TODO return Validation error
        yaml_data_store = threading.current_thread().__getattribute__("yaml_data_store")
        if yaml_data_store is not None and  isinstance(yaml_data_store, YamlFileHelper) :
            if yaml_data_store.contains_jsonpath(self.jsonpath):
                yaml_document = yaml_data_store.return_first_value_by_jsonpath(self.jsonpath)
                if yaml_document is not None and yaml_document.strip() != "":
                    required = True
        return not required
