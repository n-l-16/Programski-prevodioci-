from custom_classes import *
from custom_exceptions.exceptions import *


def dictionary_semantic_check(dictionary):
    type_semantic_check(dictionary.key_type)
    type_semantic_check(dictionary.value_type)


def type_semantic_check(type):
    if cname(type) == Dictionary.__name__:
        dictionary_semantic_check(type)
    elif cname(type) == List.__name__:
        type_semantic_check(type.object_type)
    elif type not in basic_types :
        if type not in classes.keys() and type not in interfaces.keys() and type not in enums.keys():
            raise TypeDoesNotExists(type)

def attributes_semantic_check(attributes, parent):
    for attribute in attributes:
        if cname(parent) == Interface.__name__ and attribute.scope != "public":
            raise InterfaceAttributeException(attribute.name)

        type_semantic_check(attribute.type)


def function_semantic_check(function, parent):
    if cname(parent) == Interface.__name__ and function.scope != "public":
        raise InterfaceFunctionException(function.name)
    if cname(function.return_type) == Dictionary.__name__:
        dictionary_semantic_check(function.return_type)
    elif cname(function.return_type) == List.__name__:
        type_semantic_check(function.return_type.object_type)
    elif function.return_type != "void":
        type_semantic_check(function.return_type)
    for param in function.params:
            type_semantic_check(param.type)


def relation_semantic_check(relation, class_element):
    if relation.to not in classes.keys() and relation.to not in interfaces.keys():
        raise TypeDoesNotExists(relation.to)
    if relation.type == RelationType.REFLEXIVE_ASSOCIATION.value:
        if relation.to != class_element.name:
            raise ReflexiveTypeError()
    else:
        if relation.to == class_element.name:
            raise SameClassNameInRelationError(relation.type)
        if relation.type == RelationType.REALIZATION.value:
            if relation.to not in interfaces.keys():
                raise RealizationRelationClassError()
        elif relation.type == RelationType.INHERITANCE.value and relation.to in interfaces.keys():
            if class_element.name not in interfaces.keys():
                raise InheritanceRelationInterfaceError()


def class_semantic_check(class_element):
    attributes_semantic_check(class_element.attributes, class_element)
    for function in class_element.functions:
        function_semantic_check(function, class_element)
    for relation in class_element.relations:
        relation_semantic_check(relation, class_element)


def interface_semantic_check(interface_element):
    attributes_semantic_check(interface_element.attributes, interface_element)
    for method in interface_element.methods:
        function_semantic_check(method, interface_element)
    for relation in interface_element.relations:
        relation_semantic_check(relation, interface_element)


def check_diagram_semantic(metamodel, model):
    for element in metamodel.elements:
        if cname(element) == 'Class':
            class_semantic_check(element)
        elif cname(element) == 'Interface':
            interface_semantic_check(element)

