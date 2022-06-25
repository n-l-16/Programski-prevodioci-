diagram begin

Enum UserType: (
has values : ADMIN , CLIENT
)

Class Address: (
has attributes : city type of string and scope is public , state type of string and scope is public , street type of string and scope is public
has functions : getAddress with no parameters function scope is public and return type is  string            
has relations :
)

Interface Client : (
has attributes : category type of string and scope is public , point type of int and scope is public , earning type of dictionary of int - string pairs and scope is public
has methods : setCategory with parameters category type of string , points type of int function scope is public and return type is void ,
               getEarning with no parameters category type of string function scope is public and return type is dictionary of int - string pairs  
has relations : INHERITANCE to User     
)

Abstract Class Offer : (
has attributes : services type of list of string objects and scope is public , price type of float and scope is public
has functions: getServices with no parameters function scope is public and return type is void ,
calculatePrice with parameters persons type of int , days type of int function scope is public and return type is float
has relations:

)

Interface User : (
has attributes : firstName type of string and scope is public , lastName type of string and scope is public , userType type of UserType and scope is public
has methods: getName with no parameters  function scope is public and return type is string ,
            getLastName with no parameters  function scope is public and return type is string 
has relations : ASSOCIATION to Offer with cardinality zero or more on "from" side and zero or one on "to" side 

)



diagram end
