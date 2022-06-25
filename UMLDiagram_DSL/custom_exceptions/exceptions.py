
class AttributeAlreadyDeclared(Exception):
    def __init__(self, name):
        self.message = "Semantic error -> AttributeAlreadyDeclared: Attribute with name ", name, " " \
                       "already defined for same class"
        super().__init__(self.message)


class FunctionAlreadyDeclared(Exception):
    def __init__(self, function_signature):
        self.message = "Semantic error-> FunctionAlreadyDeclared: Function with signature ", function_signature, \
                       " already declared in same class"
        super().__init__(self.message)


class ParamAlreadyDeclared(Exception):
    def __init__(self, param_name):
        self.message = "Semantic error -> ParamAlreadyDeclared: Param ", param_name, \
                       " already declared in same function"
        super().__init__(self.message)



class ElementAlreadyDeclared(Exception):
    def __init__(self, name):
        self.message = "Semantic error -> ElementAlreadyDeclared: Element ", name, \
                       " has already been declared as class or interface or enum"
        super().__init__(self.message)



class TypeDoesNotExists(Exception):
    def __init__(self, type_name):
        self.message = "Semantic error -> TypeDoesNotExists: Type ", type_name, " does not exits"
        super().__init__(self.message)



class InterfaceAttributeException(Exception):
    def __init__(self, attribute_name):
        self.message = "Semantic error -> InterfaceAttributeException: Interface attribute ", attribute_name, \
                       " has to be public"
        super().__init__(self.message)



class InterfaceFunctionException(Exception):
    def __init__(self, function_name):
        self.message = "Semantic error -> InterfaceFunctionException: Interface function ", function_name, \
                       " has to be public"
        super().__init__(self.message)



class ReflexiveTypeError(Exception):
    def __init__(self):
        self.message = "Semantic error -> ReflexiveTypeError:  Relation type REFLEXIVE_ASSOCIATION " \
                       "requires that the 'to' attribute and 'from' attribute be the same"
        super().__init__(self.message)



class SameClassNameInRelationError(Exception):
    def __init__(self, relation_type):
        self.message = "Semantic error -> SameClassNameInRelationError: relation type ", relation_type, \
                       " cannot be reflexive"
        super().__init__(self.message)



class RealizationRelationClassError(Exception):
    def __init__(self):
        self.message = "Semantic error -> RealizationRelationClassError: Relation type REALIZATION requires that the " \
                       "'to' attribute be an interface"
        super().__init__(self.message)



class InheritanceRelationInterfaceError(Exception):
    def __init__(self):
        self.message = "Semantic error -> InheritanceRelationInterfaceError: relation type INHERITANCE from " \
                       "interface requires that the 'to' attribute be an interface"
        super().__init__(self.message)



class EnumValueAlreadyDeclared(Exception):
    def __init__(self, enum_value):
        self.message = "Semantic error -> EnumValueAlreadyDeclared: Enum value ", enum_value, \
                       " already declared in same enum"
        super().__init__(self.message)
