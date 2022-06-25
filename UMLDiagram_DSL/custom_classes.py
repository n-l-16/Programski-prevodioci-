import enum
from custom_exceptions.exceptions import *


def cname(o):
    return o.__class__.__name__

classes = {}
interfaces = {}
enums = {}
current_class_attributes = []
current_class_functions = []
current_class_relations = []
basic_types = ["int", "float", "string", "bool", "Date"]


class RelationType(enum.Enum):
    DIRECTED_ASSOCIATION = "DIRECTED_ASSOCIATION"
    REFLEXIVE_ASSOCIATION = 'REFLEXIVE ASSOCIATION'
    ASSOCIATION = 'ASSOCIATION'
    AGGREGATION = 'AGGREGATION'
    COMPOSITION = 'COMPOSITION'
    INHERITANCE = 'INHERITANCE'
    REALIZATION = 'REALIZATION'


class color:
    BOLD = '\033[1m'
    BOLD_END = '\033[0m'
    ITALIC = "\x1B[3m"
    ITALIC_END = "\x1B[0m"
    TITLE = '\033[36m'
    TITLE_END = '\033[0m'
    GREEN = '\033[92m'
    END_GREEN = '\033[0m'
    RED = '\033[91m'
    END_RED = '\033[0m'
    YELLOW = '\033[93m'
    END_YELLOW = '\033[0m'


def element_name_check(name):
    if name not in classes.keys() and name not in interfaces.keys() and name not in enums.keys():
        return True
    return False


class Interface:
    def __init__(self, **kwargs):
        interface_name = kwargs.pop("name")
        if element_name_check(interface_name):
            self.name = interface_name
            self.attributes = kwargs.pop("attributes")
            self.methods = kwargs.pop("methods")
            self.relations = kwargs.pop("relations")
            interfaces[interface_name] = self
            self.clear_list()
        else:
            raise ElementAlreadyDeclared(interface_name)

    def clear_list(self):
        current_class_functions.clear()
        current_class_attributes.clear()

class Class:

    def __init__(self, **kwargs):
        class_name = kwargs.pop("name")
        if element_name_check(class_name):
            self.attributes = kwargs.pop("attributes")
            self.functions = kwargs.pop("functions")
            self.relations = kwargs.pop("relations")
            self.abstract = kwargs.pop("abstract")
            self.name = class_name
            classes[class_name] = self
            self.clear_list()
        else:
            raise ElementAlreadyDeclared(class_name)


    def clear_list(self):
        current_class_functions.clear()
        current_class_attributes.clear()


class Enum:
    def __init__(self, **kwargs):
        enum_name = kwargs.pop("name")
        if element_name_check(enum_name):
            self.enum_name = enum_name
            self.values = []
            self.set_values(kwargs.pop("values"))
            enums[enum_name] = self
            self.clear_list()
        else:
            raise ElementAlreadyDeclared(enum_name)


    def set_values(self, enum_values):
        for value in enum_values:
            if value not in self.values:
                self.values.append(value)
            else:
                raise EnumValueAlreadyDeclared(value)

    def clear_list(self):
        current_class_functions.clear()
        current_class_attributes.clear()



class Attribute:
    def __init__(self, **kwargs):
        attribute_name = kwargs.pop("name")
        if attribute_name not in current_class_attributes:
            self.name = attribute_name
            self.scope = kwargs.pop("scope")
            self.type = kwargs.pop("type")
            current_class_attributes.append(attribute_name)
        else:
            raise AttributeAlreadyDeclared(attribute_name)


class Function:
    def __init__(self, **kwargs):
        function_name = kwargs.pop("name")
        return_type = kwargs.pop("return_type")
        params = kwargs.pop("params")
        number_of_params = len(params)
        self.function_signature = function_name + "|" + str(return_type) + "|" + str(number_of_params)
        if self.function_signature not in current_class_functions:
            self.name = function_name
            self.no_params = kwargs.pop("no_params")
            self.scope = kwargs.pop("scope")
            self.return_type = return_type
            self.set_params(params)
            current_class_functions.append(self.function_signature)
        else:
            raise FunctionAlreadyDeclared(self.function_signature)

    def set_params(self, list_of_params):
        if self.no_params and len(list_of_params) > 0:
            print(color.YELLOW + "Warning: function contains sign for no params but params are declared. "
                  "Params will be checked and saved" + color.END_YELLOW)
        params_name = []
        self.params = []
        for i in range(len(list_of_params)):
            param = list_of_params[i]
            if param.name not in params_name:
                params_name.append(param.name)
                self.params.append(param)
            else:
                raise ParamAlreadyDeclared(param.name)



class RelationWithoutCardinality:
    def __init__(self, **kwargs):
        self.type = kwargs.pop("type")
        self.to = kwargs.pop("to")


class RelationWithCardinality:
    def __init__(self, **kwargs):
        self.type = kwargs.pop("type")
        self.to = kwargs.pop("to")
        self.cardinality = kwargs.pop("cardinality")


class Cardinality:
    def __init__(self, **kwargs):
        self.from_side_cardinality = kwargs.pop("from_side_cardinality")
        self.to_side_cardinality = kwargs.pop("to_side_cardinality")


class BasicType:
    def __init__(self, basic_type):
        self.type = basic_type


class List:
    def __init__(self, **kwargs):
        self.object_type = kwargs.pop("object_type")

    def __str__(self):
        return "List<" + str(self.object_type) + ">"


class Dictionary:
    def __init__(self, **kwargs):
        self.key_type = kwargs.pop("key_type")
        self.value_type = kwargs.pop("value_type")

    def __str__(self):
        return "Dictionary<" + str(self.key_type) + "," + str(self.value_type) + ">"
