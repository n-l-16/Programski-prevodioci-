import unittest

from textx import TextXSyntaxError

from custom_exceptions.exceptions import *
from semantic_check import check_diagram_semantic
from visualization import visualize_class_diagram
from custom_classes import *

testing_files = {
    0: "correct_file.md",
    1: "semantic_check_relation_failed1.md",
    2: "semantic_check_relation_failed2.md",  # reflexive
    3: "semantic_check_relation_failed3.md",  # class_doesnt_exist
    4: "semantic_check_interface_type_failed1.md",  # atribut nije public
    5: "semantic_check_interface_type_failed2.md",  # funkcija nije public
    6: "semantic_check_custom_type_failed.md",  # ne postoji clasa koja je navedena kao tim promenljive
    7: "semantic_check_relation_failed4.md",  # from i to klase iste, a veza nije reflexive association
    8: "semantic_check_class_already_defined.md",
    9: "semantic_check_attribute_already_declared.md",
    10: "semantic_check_function_already_declared.md",
    11: "semantic_check_param_already_declared.md",
    12: "semantic_check_enum_value_already_declared.md",
    13: "syntax_check_failed1.md",
    14: "syntax_check_failed2.md",
    15: "syntax_check_failed3.md",
    16: "correct_file2.md"
}


def clear_collections():
    classes.clear()
    interfaces.clear()
    enums.clear()


def run_test(test_file, my_metamodel):
    my_model = my_metamodel.model_from_file('./tests/' + test_file)


def run_all_tests(my_metamodel):
    tests = Tests(my_metamodel)
    tests.run_all()



class Tests(unittest.TestCase):

    def __init__(self, my_metamodel):
        self.my_metamodel = my_metamodel
        self.my_metamodel.register_model_processor(check_diagram_semantic)
        super().__init__()

    def run_all(self):
        self.test0()
        self.test13()
        self.test14()
        self.test15()
        self.test1()
        self.test2()
        self.test3()
        self.test4()
        self.test5()
        self.test6()
        self.test7()
        self.test8()
        self.test9()
        self.test10()
        self.test11()
        self.test12()
        self.test16()

    def test0(self):
        try:
            run_test(testing_files[0], self.my_metamodel)
            print(color.GREEN + "Syntax and semantic passed. File is correct" + color.END_GREEN)
            visualize_class_diagram()
            clear_collections()
        except Exception as e:
            print(color.RED, "Test failed: no expected exception but get \n", e, color.END_RED)
            clear_collections()

    def test1(self):
        try:
            self.assertRaises(ParamAlreadyDeclared, run_test, testing_files[10], self.my_metamodel)
            clear_collections()
            print(color.GREEN + "Semantic check: ParamAlreadyDeclared TEST PASSED" + color.END_GREEN)
        except Exception as e:
            print(color.RED, "Test failed: expected exception ParamAlreadyDeclared but get \n", e, color.END_RED)
            clear_collections()

    def test2(self):
        try:
            self.assertRaises(AttributeAlreadyDeclared, run_test, testing_files[9], self.my_metamodel)
            clear_collections()
            print(color.GREEN + "Semantic check: AttributeAlreadyDeclared TEST PASSED" + color.END_GREEN)
        except Exception as e:
            print(color.RED, "Test failed: expected exception AttributeAlreadyDeclared but get \n", e, color.END_RED)
            clear_collections()

    def test3(self):
        try:
            self.assertRaises(FunctionAlreadyDeclared, run_test, testing_files[10], self.my_metamodel)
            clear_collections()
            print(color.GREEN + "Semantic check: FunctionAlreadyDeclared TEST PASSED" + color.END_GREEN)
        except Exception as e:
            print(color.RED, "Test failed: expected exception FunctionAlreadyDeclared but get \n", e, color.END_RED)
            clear_collections()

    def test4(self):
        try:
            self.assertRaises(EnumValueAlreadyDeclared, run_test, testing_files[12], self.my_metamodel)
            clear_collections()
            print(color.GREEN + "Semantic check: EnumValueAlreadyDeclared TEST PASSED" + color.END_GREEN)
        except Exception as e:
            print(color.RED, "Test failed: expected exception EnumValueAlreadyDeclared but get \n", e, color.END_RED)
            clear_collections()

    def test5(self):
        try:
            self.assertRaises(ElementAlreadyDeclared, run_test, testing_files[8], self.my_metamodel)
            clear_collections()
            print(color.GREEN + "Semantic check: ElementAlreadyDeclared TEST PASSED" + color.END_GREEN)
        except Exception as e:
            print(color.RED, "Test failed: expected exception ElementAlreadyDeclared but get \n", e, color.END_RED)
            clear_collections()

    def test6(self):
        try:
            self.assertRaises(TypeDoesNotExists, run_test, testing_files[6], self.my_metamodel)
            clear_collections()
            print(color.GREEN + "Semantic check: TypeDoesNotExists TEST PASSED" + color.END_GREEN)
        except Exception as e:
            print(color.RED, "Test failed: expected exception TypeDoesNotExists but get \n", e, color.END_RED)
            clear_collections()

    def test7(self):
        try:
            self.assertRaises(InterfaceAttributeException, run_test, testing_files[4], self.my_metamodel)
            clear_collections()
            print(color.GREEN + "Semantic check: InterfaceAttributeException TEST PASSED" + color.END_GREEN)
        except Exception as e:
            print(color.RED, "Test failed: expected exception InterfaceAttributeException but get \n", e, color.END_RED)
            clear_collections()

    def test8(self):
        try:
            self.assertRaises(InterfaceFunctionException, run_test, testing_files[5], self.my_metamodel)
            clear_collections()
            print(color.GREEN + "Semantic check: InterfaceFunctionException TEST PASSED" + color.END_GREEN)
        except Exception as e:
            print(color.RED, "Test failed: expected exception InterfaceFunctionException but get \n", e, color.END_RED)
            clear_collections()

    def test9(self):
        try:
            self.assertRaises(ReflexiveTypeError, run_test, testing_files[2], self.my_metamodel)
            clear_collections()
            print(color.GREEN + "Semantic check: ReflexiveTypeError TEST PASSED" + color.END_GREEN)
        except Exception as e:
            print(color.RED, "Test failed: expected exception ReflexiveTypeError but get \n", e, color.END_RED)
            clear_collections()

    def test10(self):
        try:
            self.assertRaises(SameClassNameInRelationError, run_test, testing_files[7], self.my_metamodel)
            clear_collections()
            print(color.GREEN + "Semantic check: SameClassNameInRelationError TEST PASSED" + color.END_GREEN)
        except Exception as e:
            print(color.RED, "Test failed: expected exception SameClassNameInRelationError but get \n", e, color.END_RED)
            clear_collections()

    def test11(self):
        try:
            self.assertRaises(RealizationRelationClassError, run_test, testing_files[1], self.my_metamodel)
            clear_collections()
            print(color.GREEN + "Semantic check: RealizationRelationClassError TEST PASSED" + color.END_GREEN)
        except Exception as e:
            print(color.RED, "Test failed: expected exception RealizationRelationClassError but get \n", e, color.END_RED)
            clear_collections()

    def test12(self):
        try:
            self.assertRaises(TypeDoesNotExists, run_test, testing_files[3], self.my_metamodel)
            clear_collections()
            print(color.GREEN + "Semantic check: TypeDoesNotExists TEST PASSED" + color.END_GREEN)
        except Exception as e:
            print(color.RED, "Test failed: expected exception TypeDoesNotExists but get \n", e, color.END_RED)
            clear_collections()

    def test13(self):
        try:
            self.assertRaises(TextXSyntaxError, run_test, testing_files[13], self.my_metamodel)
            clear_collections()
            print(color.GREEN + "Syntax error detection TEST PASSED" + color.END_GREEN)
        except Exception as e:
            print(color.RED, "Test failed: expected exception TextXSyntaxError but get \n", e, color.END_RED)
            clear_collections()

    def test14(self):
        try:
            self.assertRaises(TextXSyntaxError, run_test, testing_files[14], self.my_metamodel)
            clear_collections()
            print(color.GREEN + "Syntax error detection TEST PASSED" + color.END_GREEN)
        except Exception as e:
            print(color.RED, "Test failed: expected exception TextXSyntaxError but get \n", e, color.END_RED)
            clear_collections()

    def test15(self):
        try:
            self.assertRaises(TextXSyntaxError, run_test, testing_files[15], self.my_metamodel)
            clear_collections()
            print(color.GREEN + "Syntax error detection TEST PASSED" + color.END_GREEN)
        except Exception as e:
            print(color.RED, "Test failed: expected exception TextXSyntaxError but get \n", e, color.END_RED)
            clear_collections()

    def test16(self):
        try:
            run_test(testing_files[16], self.my_metamodel)
            print(color.GREEN + "Syntax and semantic passed. File is correct" + color.END_GREEN)
            visualize_class_diagram()
            clear_collections()
        except Exception as e:
            print(color.RED, "Test failed: no expected exception but get \n", e, color.END_RED)
            clear_collections()
