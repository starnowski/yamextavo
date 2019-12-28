import threading
from yamale.validators import Validator, Any
from yamextavo.utils import YamlFileHelper


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
        ct = threading.current_thread() #TODO Move to extractYamlDataStore method
        if not hasattr(ct, 'yaml_data_store'):  #TODO Move to extractYamlDataStore method
            pass #TODO return Validation error  #TODO Move to extractYamlDataStore method
        yaml_data_store = threading.current_thread().__getattribute__("yaml_data_store")    #TODO Move to extractYamlDataStore method
        if yaml_data_store is not None and  isinstance(yaml_data_store, YamlFileHelper) :   #TODO Move to extractYamlDataStore method
            if yaml_data_store.contains_jsonpath(self.jsonpath):    #TODO Move to retrieveJsonNode method
                yaml_document = yaml_data_store.return_first_value_by_jsonpath(self.jsonpath)   #TODO Move to retrieveJsonNode method
                if yaml_document is not None and yaml_document.strip() != "":   #TODO  Move to checkIfPropertyIsRequired method
                    required = True
        return not required
