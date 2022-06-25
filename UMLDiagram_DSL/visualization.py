from semantic_check import cname
from custom_classes import classes, interfaces, enums, Dictionary, List, RelationWithCardinality, \
    RelationWithoutCardinality, color
    
horizontal_line_length = 60
padding_space = 25
padding_space_enum = 20

scope_symbols = {
    "private": "-",
    "public": "+",
    "protected": "#",
    "package": "~"
}

relation_symbols = {
    "DIRECTED ASSOCIATION" : "⎯⎯⎯⎯▶",
    'REFLEXIVE ASSOCIATION': "⎯⎯⎯⎯↺",
    'ASSOCIATION' : "⎯⎯⎯⎯⎯",
    'AGGREGATION': "◇⎯⎯⎯⎯⎯",
     'COMPOSITION': "◆⎯⎯⎯⎯⎯",
    'INHERITANCE': "⎯⎯⎯⎯⎯▷",
    'REALIZATION' : "----▷"
}

cardinality_symbols = {
    "one or more" : "1..*",
    "zero or more" : "0..*",
    "zero or one" : "0..1",
    "one to one" : "1"
}



def visualize_type(type):
    if cname(type) == Dictionary.__name__:
        return  "Dictionary<" + type.key_type + ", " + type.value_type + ">"
    elif cname(type) == List.__name__:
        return type.object_type + "[0..*]"
    else:
        return type


def visualize_class_name(class_element):
    if class_element.abstract:
        print(padding_space * " ", color.ITALIC  + color.BOLD + class_element.name + color.BOLD_END + color.ITALIC_END )
    else:
        print(padding_space * " ", color.BOLD + class_element.name + color.BOLD_END)


def visualize_class_attribute(attribute):
    print(" " + scope_symbols[attribute.scope] + " " + attribute.name + ": " + visualize_type(attribute.type))


def visualize_class_function(function):
    function_params = "("
    for i in range(len(function.params)):
        param = function.params[i]
        function_params += visualize_type(param.type) + " " + param.name + ", "
    if len(function_params) > 1:
        function_params = function_params[0 : len(function_params) - 2]
    function_params += ")"
    print(" " + scope_symbols[function.scope] + " " + function.name + function_params + ": " + visualize_type(function.return_type))


def visualize_relations_with_cardinality(relation):
    print(" " + cardinality_symbols[relation.cardinality.from_side_cardinality]
          + " " + relation_symbols[relation.type] + " "
          + cardinality_symbols[relation.cardinality.to_side_cardinality]
             + " " + relation.to)



def visualize_relations_without_cardinality(relation):
    print(" " + relation_symbols[relation.type] + " " +
         relation.to)


def visualize_relations(relation):
    if cname(relation) == RelationWithCardinality.__name__:
        visualize_relations_with_cardinality(relation)
    if cname(relation) == RelationWithoutCardinality.__name__:
        visualize_relations_without_cardinality(relation)


def visualize_class(class_element):
    print(horizontal_line_length * "_")
    visualize_class_name(class_element)
    print(horizontal_line_length * "-")
    for attribute in class_element.attributes:
        visualize_class_attribute(attribute)
    print(horizontal_line_length * "-")
    for i in range(len(class_element.functions)):
        visualize_class_function(class_element.functions[i])
    print(horizontal_line_length * "-")
    for i in range(len(class_element.relations)):
        visualize_relations(class_element.relations[i])
    print(horizontal_line_length * "_")
    print()


def visualize_interface_name(interface_name):
    print(padding_space * " " + color.ITALIC  + color.BOLD + "I" + interface_name + color.BOLD_END + color.ITALIC_END )


def visualize_interface(interface_element):
    print(horizontal_line_length * "_")
    print(padding_space_enum * " ", "<<interface>>")
    visualize_interface_name(interface_element.name)
    print(horizontal_line_length * "-")
    for attribute in interface_element.attributes:
        visualize_class_attribute(attribute)
    print(horizontal_line_length * "-")
    for method in interface_element.methods:
        visualize_class_function(method)
    print(horizontal_line_length * "-")
    for relation in interface_element.relations:
        visualize_relations(relation)

    print(horizontal_line_length * "_")
    print()


def visualize_enum(enum_element):
    print(horizontal_line_length * "_")
    print(padding_space_enum * " ", "<<enumaeration>>")
    print(padding_space * " ", color.BOLD + enum_element.name + color.BOLD_END)
    print(horizontal_line_length * "-")
    for value in enum_element.values:
        print(value)
    print(horizontal_line_length * "_")
    print()


def visualize_class_diagram():
    print( color.TITLE + "ENUMERATIONS" + color.TITLE_END)
    for enum_name in enums:
        visualize_enum(enums[enum_name])

    print( color.TITLE + "INTERFACES" + color.TITLE_END)
    for interface_name in interfaces:
        visualize_interface(interfaces[interface_name])

    print(color.TITLE + "CLASSES" + color.TITLE_END)
    for class_name in classes:
        visualize_class(classes[class_name])

