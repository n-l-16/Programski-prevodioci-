diagram begin

Enum UserType: (
has values : ADMIN , CLIENT , ADMIN
)

Class Address: (
has attributes : city type of string and scope is public , state type of string and scope is public , street type of string and scope is public
has functions : getAddress with no parameters function scope is public and return type is  string            
has relations :
)

Class Client : (
has attributes : category type of string and scope is private , point type of int and scope is private , earning type of dictionary of int - string pairs and scope is private
has functions : setCategory with parameters category type of string , points type of int function scope is public and return type is void ,
getEarning with no parameters function scope is protected and return type is dictionary of int - string pairs  
has relations : INHERITANCE to User
)

Interface Offer : (
has attributes : services type of list of string objects and scope is public , price type of float and scope is public
has methods: getServices with no parameters function scope is public and return type is void ,
calculatePrice with parameters persons type of int , days type of int function scope is public and return type is float
has relations:

)

Abstract Class User : (
has attributes : firstName type of string and scope is private , lastName type of string and scope is private , userType type of UserType and scope is public
has functions: getName with no parameters  function scope is public and return type is string ,
getLastName with no parameters  function scope is public and return type is string ,
setAge with parameters age type of int function scope is public and return type is void
has relations : ASSOCIATION to Offer with cardinality zero or more on "from" side and zero or one on "to" side ,
DIRECTED ASSOCIATION to Address with cardinality zero or more on "from" side and zero or one on "to" side
)



diagram end
