from __future__ import unicode_literals

from textx.metamodel import metamodel_from_file
from custom_classes import *
from tests.run_test import run_all_tests


def run(debug=False):
    my_metamodel = metamodel_from_file('uml_class_diagram.tx',
                                       classes=[Enum, Class, Function, Attribute, Interface,
                                                BasicType, RelationWithoutCardinality, RelationWithCardinality,
                                                Dictionary, List, Cardinality],
                                       autokwd=True)

    run_all_tests(my_metamodel)


if __name__ == '__main__':
    run()
