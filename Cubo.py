from enum import Enum
class Type(Enum):
     INT = 1
     FLOAT = 2
     DEGREE = 3
     BOOL = 4
     RAD = 5
     ERROR = -1

class Operation(Enum):
     PLUS = 1
     MINUS = 2
     MULTIPLY = 3
     DIVIDE = 4
     GREATER = 5
     GREATEREQUAL = 6
     LESS = 7
     LESSEQUAL = 8
     ASIGN = 9
     EQUAL = 10
     NOTEQUAL = 11
     AND = 12
     OR = 13
     MOD = 14

charToEnum = {
    "+" : Operation.PLUS,
    "-" : Operation.MINUS,
    "*" : Operation.MULTIPLY,
    "/" : Operation.DIVIDE,
    ">" : Operation.GREATER,
    ">=" : Operation.GREATEREQUAL,
    "<" : Operation.LESS,
    "<=" : Operation.LESSEQUAL,
    "=" : Operation.ASIGN,
    "==" : Operation.EQUAL,
    "!=" : Operation.NOTEQUAL,
    "&&" : Operation.AND,
    "||" : Operation.OR,
    "%" : Operation.MOD,
    "int" : Type.INT,
    "float" : Type.FLOAT,
    "RAD" : Type.RAD,
    "bool" : Type.BOOL,
    "DEGREE" : Type.DEGREE,
    "err" : Type.ERROR
}
def getCubeType(typ1,typ2,act):
    return cubo[charToEnum[typ1]][charToEnum[typ2]][charToEnum[act]]

cubo = {
# int operacion tipo
    Type.INT: {
    #int operacion int
      Type.INT: {
        Operation.PLUS:"int",
        Operation.MINUS:"int",
        Operation.MULTIPLY:"int",
        Operation.DIVIDE:"int",
        Operation.GREATER:"bool",
        Operation.GREATEREQUAL:"bool",
        Operation.LESSEQUAL:"bool",
        Operation.LESS:"bool",
        Operation.ASIGN:"int",
        Operation.EQUAL:"bool",
        Operation.NOTEQUAL:"bool",
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:"int"
        },
    #int operacion float
      Type.FLOAT: {
        Operation.PLUS:"float",
        Operation.MINUS:"float",
        Operation.MULTIPLY:"float",
        Operation.DIVIDE:"float",
        Operation.GREATER:"bool",
        Operation.GREATEREQUAL:"bool",
        Operation.LESSEQUAL:"bool",
        Operation.LESS:"bool",
        Operation.ASIGN:"int",
        Operation.EQUAL:"bool",
        Operation.NOTEQUAL:"bool",
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:"float"
        },
    #int operacion DEGREE
      Type.DEGREE: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
    #int operacion bool
      Type.BOOL: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
    #int operacion rad
      Type.RAD: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
      },
#float operacion tipo
    Type.FLOAT:{
    #float operacion int
      Type.INT: {
        Operation.PLUS:"float",
        Operation.MINUS:"float",
        Operation.MULTIPLY:"float",
        Operation.DIVIDE:"float",
        Operation.GREATER:"bool",
        Operation.GREATEREQUAL:"bool",
        Operation.LESSEQUAL:"bool",
        Operation.LESS:"bool",
        Operation.ASIGN:"float",
        Operation.EQUAL: "bool",
        Operation.NOTEQUAL:"bool",
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
    #float operacion float
      Type.FLOAT: {
        Operation.PLUS:"float",
        Operation.MINUS:"float",
        Operation.MULTIPLY:"float",
        Operation.DIVIDE:"float",
        Operation.GREATER:"bool",
        Operation.GREATEREQUAL:"bool",
        Operation.LESSEQUAL:"bool",
        Operation.LESS:"bool",
        Operation.ASIGN:"float",
        Operation.EQUAL: "bool",
        Operation.NOTEQUAL:"bool",
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
    #float operacion DEGREE
      Type.DEGREE: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
    #float operacion bool
      Type.BOOL: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
    #float operacion RAD
      Type.RAD: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
      },
#DEGREEE operacion tipo
    Type.DEGREEE:{
    #DEGREE operacion int
      Type.INT: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
    #DEGREE operacion float
      Type.FLOAT: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
    #DEGREE operacion DEGREE
      Type.DEGREEE: {
        Operation.PLUS:"DEGREEE",
        Operation.MINUS:"DEGREEE",
        Operation.MULTIPLY:"DEGREEE",
        Operation.DIVIDE:"DEGREEE",
        Operation.GREATER:"bool",
        Operation.GREATEREQUAL:"bool",
        Operation.LESSEQUAL:"bool",
        Operation.LESS:"bool",
        Operation.ASIGN:"DEGREEE",
        Operation.EQUAL: "bool",
        Operation.NOTEQUAL:"bool",
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
    #DEGREE operacion Bool
      Type.BOOL: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
    #DEGREE operacion RAD
      Type.RAD: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
      },
#bool operacion tipo
    Type.BOOL:{
    #bool operacion int
      Type.INT: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
    #bool operacion float
      Type.FLOAT: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
    #bool operacion DEGREE
      Type.DEGREE: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
    #bool operacion bool
      Type.BOOL: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:"bool",
        Operation.EQUAL:"bool",
        Operation.NOTEQUAL:"bool",
        Operation.AND:"bool",
        Operation.OR:"bool",
        Operation.MOD:Type.ERROR
        },
    #bool operacion RAD
      Type.RAD: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
      },
#RAD operacion tipo
    Type.RAD:{
    #RAD operacion int
      Type.INT: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
    #RAD operacion float
      Type.FLOAT: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
    #RAD operacion DEGREE
      Type.DEGREEE: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
    #array operacion bool
      Type.BOOL: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
    #RAD operacion RAD
      Type.ARRAY: {
        Operation.PLUS:"RAD",
        Operation.MINUS:"RAD",
        Operation.MULTIPLY:"RAD",
        Operation.DIVIDE:"RAD",
        Operation.GREATER:"bool",
        Operation.GREATEREQUAL:"bool",
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:"RAD",
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
      },
}