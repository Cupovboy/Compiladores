import ply.lex as lex
import ply.yacc as yacc
import sys
from cuadruplos import *

valido = True;

#Stacks ---------------------------------------------------------------------------------

saltos = []																
tipos =[]
variables = []
operadores =[]
cuadruplos =[]

# Variable encargada de contar los cuadruplos 
tempCont = 1
tempSaltos = 0

reserved = {
	  'MAIN' : 'PR_main',
	  'IF' : 'PR_if' ,
	  'ELSE' : 'PR_else',
	  'TRUE' : 'PR_true',
	  'FALSE' : 'PR_false',
	  'AND' : 'PR_and',
	  'OR' : 'PR_or',
	  'INT' : 'PR_int',
	  'FLOAT' : 'PR_float',
	  'BOOL' : 'PR_bool',
	  'VOID' : 'PR_void',
	  'SIN' : 'PR_sin',
	  'COS' : 'PR_cos',
	  'TAN' : 'PR_tan',
	  'COTANGENT' : 'PR_cotengent',
	  'GRAPH' : 'PR_graph',
	  'SECANT' : 'PR_secant',
	  'COSSECAT' : 'PR_cossecat',
	  'READ' : 'PR_read',
	  'DISPLAY': 'PR_display',
	  'NORMALIZAR': 'PR_normalizar',
	  'MAPMAT': 'PR_mapmat',
	  'SENINV': 'PR_seninv',
	  'COSINV': 'PR_cosinv',
	  'TANINV': 'PR_taninv',
	  'DEGREE': 'PR_degree',
	  'RAD': 'PR_rad',
	  'prog':'PR_Program',
	  'var':'PR_var',
	  'globalVar':'PR_globalVar',
	  'WHILE': 'PR_while',
	  'write': 'PR_Write',
	  'Fun':'PR_fun'

}
 

tokens = [
	'Token_SUMA', 'Token_Resta', 'TOKEN_MULTI','TOKEN_DIVID', 'TOKEN_POW',
	'TOKEN_COMPARA','TOKEN_ASIGNA',  'TOKEN_MENOR', 'TOKEN_MAYOR','TOKEN_MENOR_IG', 'TOKEN_MAYOR_IG',
	'TOKEN_NO_IGUAL',
	'Token_Parent_Abierto', 'Token_Parent_Cerrado', 'Token_Corchete_Abierto', 'Token_Corchete_Cerrado', 
	'Token_Llave_Abierta', 'Token_Llave_Cerrado',
	'Token_Single_Dig', 'Token_Entero', 'Token_Float', 'ID', 
	'Token_Coma', 'Token_Punto_Coma',
	'Token_And' , 'Token_Or'

]


#tokens
t_Token_SUMA = r'\+'
t_Token_Resta = r'\-'
t_TOKEN_MULTI= r'\*'
t_TOKEN_DIVID = r'\/'
t_TOKEN_POW = r'\^'
t_TOKEN_COMPARA = r'\=\='
t_TOKEN_ASIGNA = r'\='
t_TOKEN_MENOR = r'\<'
t_TOKEN_MAYOR = r'\>'
t_TOKEN_MENOR_IG = r'\<\='
t_TOKEN_MAYOR_IG = r'\>\='
t_TOKEN_NO_IGUAL = r'\!\='
t_Token_Parent_Abierto = r'\('
t_Token_Parent_Cerrado= r'\)'
t_Token_Llave_Abierta = r'\{'
t_Token_Llave_Cerrado = r'\}'
t_Token_Corchete_Abierto = r'\['
t_Token_Corchete_Cerrado= r'\]'
t_Token_Single_Dig = r'[0-9]'
t_Token_Entero = r'[0-9]+'
t_Token_Float = r'[0-9]+\.[0-9]+'
t_Token_Coma = r'\,'
t_Token_Punto_Coma =  r';'
t_Token_And =  r'\&\&'
t_Token_Or =  r'\|\|'




tokens = tokens + list(reserved.values())

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t

# Caracteres ignorados
t_ignore = ' \t\n'

def t_error(t):
	

    global valido
    valido = False
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)



# Construye el lexer
lex.lex()

def p_progama(p):
	'prog : PR_Program Token_Llave_Abierta globalVar BlockFun  MainBlock Token_Llave_Cerrado'
 

def p_tipo(p):
	'''tipo : PR_int
			| PR_float
			| PR_bool 
			| PR_void
			| PR_rad
			| PR_degree 
			'''


# Variable rules ---------------------------------------------------------------------------
def p_globalVar(p):
      '''globalVar : PR_globalVar tipo decVar Token_Punto_Coma globalVar
				   | empty
      '''
      print ('holi')

def p_var(p):
   'var : PR_var tipo decVar Token_Punto_Coma'

def p_decVar(p):
    '''decVar : varNom decVar2
    		'''

def p_decVar2(p):
	'''decVar2 : Token_Coma decVar
			   | empty
	'''
     

def p_varNom(p):
	 '''varNom : ID arr1
	 	arr1 : Token_Corchete_Abierto Token_Entero Token_Corchete_Cerrado arr2
	 	     | empty
	 	arr2 : Token_Corchete_Abierto Token_Entero Token_Corchete_Cerrado
	 	     | empty
		       '''

# Function Rules -----------------------------------------------------------------------------


def p_BlockFun(p):
	''' BlockFun : fun BlockFun
	              | empty
	              '''

def p_fun(p):
	'fun : PR_fun tipo ID Token_Parent_Abierto params Token_Parent_Cerrado funBlock' 

def p_params(p):
	'''params : tipo ID
	        | tipo ID Token_Coma params
			| empty'''


def p_funBlock(p):
   'funBlock : Token_Llave_Abierta bloque Token_Llave_Cerrado'


def p_funCall(p):
   'funCall : ID Token_Parent_Abierto paramsCall Token_Parent_Cerrado '

def p_funCallVoid(p):
   'funCallVoid : ID Token_Parent_Abierto paramsCall Token_Parent_Cerrado Token_Punto_Coma'

def p_paramsCall(p):
	'''paramsCall : SuperExp
	        | SuperExp Token_Coma paramsCall
			| empty'''


# main rule -------------------------------------------------------------------------------------

def p_mainBlock(p):
	'MainBlock : PR_main Token_Llave_Abierta bloque Token_Llave_Cerrado'



def p_empty(p):
    'empty :'
    pass

def p_error(p):
    global valido
    valido = False
    print("Error de sintaxis en '%s'" % p.value)
   
# Block --------------------------------------------------------------------------------------------
def p_block(p):
	'''bloque : statements bloque
	       |  empty '''

def p_statments(p):
	'''statements : var 
	              | funCallVoid
	              | Conditions
	              | ciclos
	              | asigna
	              | read 
	              | write
	              | GRAPH
	              | map
	              | NORMALIZAR'''


#Expresiones ---------------------------------------------------------------------------------------

def p_SuperExp(p):
	'''SuperExp : Exp 
	            | Exp  PR_and CuadruploOpp SuperExp CuadruplosCreaANDOR
	            | Exp  PR_or CuadruploOpp  SuperExp CuadruplosCreaANDOR
	            | Exp  Token_And CuadruploOpp SuperExp CuadruplosCreaANDOR
	            | Exp  Token_Or CuadruploOpp SuperExp CuadruplosCreaANDOR  '''
def p_Exp(p):
	'''Exp : miniExp 
	        | miniExp  TOKEN_MAYOR CuadruploOpp miniExp CuadruplosCreaCompara 
	        | miniExp TOKEN_MENOR CuadruploOpp miniExp CuadruplosCreaCompara
	        | miniExp  TOKEN_MAYOR_IG CuadruploOpp miniExp CuadruplosCreaCompara
	        | miniExp  TOKEN_MENOR_IG CuadruploOpp miniExp CuadruplosCreaCompara
	        | miniExp  TOKEN_COMPARA CuadruploOpp miniExp CuadruplosCreaCompara
	        | miniExp  TOKEN_NO_IGUAL CuadruploOpp miniExp CuadruplosCreaCompara'''

def p_miniExp(p):
	'''miniExp : microExp CuadruplosCrea 
	           | microExp CuadruplosCrea Token_SUMA CuadruploOpp miniExp
	           | microExp CuadruplosCrea Token_Resta CuadruploOpp miniExp'''



def p_microExp(p):
	'''microExp : minimicroExp CuadruplosCreaMult 
	           | minimicroExp  CuadruplosCreaMult TOKEN_MULTI CuadruploOpp microExp
	           |  minimicroExp CuadruplosCreaMult  TOKEN_DIVID CuadruploOpp microExp'''

def p_minimicroExp(p):
	'''minimicroExp : conjunto CuadruplosCreaPow
	           | conjunto CuadruplosCreaPow  TOKEN_POW CuadruploOpp minimicroExp '''

def p_conjunto(p):
	'''conjunto : ID CuadruploMiniExp
	           | ID Token_Corchete_Abierto miniExp Token_Corchete_Cerrado
	           | ID Token_Corchete_Abierto miniExp Token_Corchete_Cerrado Token_Corchete_Abierto miniExp Token_Corchete_Cerrado
	           | Token_Entero  CuadruploMiniExp
	           | Token_Float CuadruploMiniExp
	           | PR_true CuadruploMiniExp
	           | PR_false CuadruploMiniExp
	           | funCall 
	           | llamada
	           | Token_Parent_Abierto CuadruploOpp SuperExp Token_Parent_Cerrado CuadruploOppPop'''

def p_CuadruploMiniExp(p):
	"CuadruploMiniExp : empty"
	variables.append(p[-1])

def p_CuadruploOpp(p):
	"CuadruploOpp : empty"
	operadores.append(p[-1])

def p_CuadruploOppPop(p):
	"CuadruploOppPop : empty"
	operadores.pop()

def p_CuadruploCrea(p):
	'CuadruplosCrea : empty'
	if len(operadores)> 0:
		global tempCont
		if operadores[len(operadores)-1] == '+' or operadores[len(operadores)-1] == '-' :
			varTemp= "t" + str(tempCont)
			derecho = variables.pop()
			izquierdo = variables.pop()
			cuadruplos.append(cuadruplo(len(cuadruplos), operadores.pop(), izquierdo, derecho , varTemp))
			variables.append(varTemp)
			tempCont = tempCont + 1

def p_CuadruploCreaMult(p):
	'CuadruplosCreaMult : empty'
	if len(operadores) > 0:
		global tempCont
		if operadores[len(operadores)-1] == '*' or operadores[len(operadores)-1] == '/' :
			varTemp= "t" + str(tempCont)
			derecho = variables.pop()
			izquierdo =variables.pop()
			cuadruplos.append(cuadruplo(len(cuadruplos), operadores.pop(), izquierdo, derecho , varTemp))
			variables.append(varTemp)
			tempCont = tempCont + 1

def p_CuadruploCreaPow(p):
	'CuadruplosCreaPow : empty'
	if len(operadores)> 0:
		global tempCont
		if operadores[len(operadores)-1] == '^' :
			varTemp= "t" + str(tempCont)
			derecho = variables.pop()
			izquierdo =variables.pop()
			cuadruplos.append(cuadruplo(len(cuadruplos), operadores.pop(), izquierdo, derecho , varTemp))
			variables.append(varTemp)
			tempCont = tempCont + 1

def p_CuadruploCreaCompara(p):
	'CuadruplosCreaCompara : empty'
	if len(operadores)> 0:
		global tempCont
		if operadores[len(operadores)-1] == '<' or operadores[len(operadores)-1] == '>' or operadores[len(operadores)-1] == '!=' or operadores[len(operadores)-1] == '==' or operadores[len(operadores)-1] == '<=' or operadores[len(operadores)-1] == '>=':
			varTemp= "t" + str(tempCont)
			derecho = variables.pop()
			izquierdo = variables.pop()
			cuadruplos.append(cuadruplo(len(cuadruplos), operadores.pop(), izquierdo, derecho , varTemp))
			variables.append(varTemp)
			tempCont = tempCont + 1

			
def p_CuadruploCreaANDOR(p):
	'CuadruplosCreaANDOR : empty'
	if len(operadores)> 0:
		global tempCont
		if operadores[len(operadores)-1] == '||' or operadores[len(operadores)-1] == '&&' or operadores[len(operadores)-1] == 'OR' or operadores[len(operadores)-1] == 'AND' :
			varTemp= "t" + str(tempCont)
			derecho = variables.pop()
			izquierdo = variables.pop()
			cuadruplos.append(cuadruplo(len(cuadruplos), operadores.pop(), izquierdo, derecho , varTemp))
			variables.append(varTemp)
			tempCont = tempCont + 1




#Conditions------------------------------------------------------------------------------------------

def p_condition(p):
	'Conditions : PR_if Token_Parent_Abierto  CuadruploSaltosINI SuperExp Token_Parent_Cerrado CuadruploCon Token_Llave_Abierta bloque CuadruploConEnd Token_Llave_Cerrado PR_else Token_Llave_Abierta bloque Token_Llave_Cerrado CuadruplosFinal'

def p_CuadruploCon(p):
	'CuadruploCon : empty'
	global tempSaltos
	if len(variables)> 0:
        		# PILA JUMP 
		saltos.append(len(cuadruplos))
		cuadruplos.append(cuadruplo(len(cuadruplos), 'GOTOF', variables.pop(), None ,None ))

		
def p_CuadruploConEnd(p):
	'CuadruploConEnd : empty'
	global tempSaltos
	tempSaltos = saltos.pop()
	cuadruplos[tempSaltos].var3 = len(cuadruplos)+1
	cuadruplos.append(cuadruplo(len(cuadruplos), 'GOTO', None, None ,None))
	saltos.append(len(cuadruplos))

def p_CuadruplosFinal(p):
	'CuadruplosFinal : empty'
	cuadruplos[saltos.pop()-1].var3 = len(cuadruplos)

#Ciclos-----------------------------------------------------------------------------------------------

def p_ciclos(p):
	'ciclos : PR_while Token_Parent_Abierto  CuadruploSaltosINI SuperExp Token_Parent_Cerrado CuadruploCiclos Token_Llave_Abierta bloque Token_Llave_Cerrado CuadruploCiclosEnd '

def p_CuadruploSaltosINI(p) :
	'CuadruploSaltosINI : empty'
	saltos.append(len(cuadruplos))


def p_CuadruploCiclos(p):
	'CuadruploCiclos  : empty'
	if len(variables)> 0:
	   saltos.append(len(cuadruplos))		         
	   cuadruplos.append(cuadruplo(len(cuadruplos), 'GOTOF', variables.pop(), None ,None ))

def p_CuadruploCiclosEnd(p):
	'CuadruploCiclosEnd : empty'
	global tempSaltos
	tempSaltos = saltos.pop()
	cuadruplos[tempSaltos].var3 = len(cuadruplos)+1
	cuadruplos.append(cuadruplo(len(cuadruplos), 'GOTO', None, None ,saltos.pop()))

	



#asignasiones--------------------------------------------------------------------------------------------

def p_asignaciones(p):
    '''asigna : ID CuadruploMiniExp TOKEN_ASIGNA CuadruploOpp SuperExp CuadruplosAsigna  Token_Punto_Coma
      | ID Token_Corchete_Abierto miniExp Token_Corchete_Cerrado TOKEN_ASIGNA  CuadruploOpp SuperExp CuadruplosAsigna  Token_Punto_Coma
      | ID Token_Corchete_Abierto miniExp Token_Corchete_Cerrado Token_Corchete_Abierto miniExp Token_Corchete_Cerrado TOKEN_ASIGNA CuadruploOpp SuperExp CuadruplosAsigna Token_Punto_Coma '''

def p_CuadruploAsigna(p):
	'CuadruplosAsigna : empty'
	if len(operadores)> 0:
		if operadores[len(operadores)-1] == '=' :
			cuadruplos.append(cuadruplo(len(cuadruplos), operadores.pop(),variables.pop(), None , variables.pop()))





#Premade Funtions -----------------------------------------------------------------------------------------

def p_llamada(p):
	''' llamada : sin
	            | cos
	            | tan
	            | COTANGENT
	            | COSECANT
	            | SECANT
	            | sininv
	            | cosinv
	            | taninv '''

def p_sin(p):
	'sin : PR_sin Token_Parent_Abierto SuperExp Token_Parent_Cerrado'

def p_cos(p):
	'cos : PR_cos Token_Parent_Abierto SuperExp Token_Parent_Cerrado'

def p_tan(p):
    'tan : PR_tan Token_Parent_Abierto SuperExp Token_Parent_Cerrado'

def p_cotan(p):
	'COTANGENT : PR_cotengent Token_Parent_Abierto SuperExp Token_Parent_Cerrado'

def p_cosecant(p):
	'COSECANT : PR_cossecat Token_Parent_Abierto SuperExp Token_Parent_Cerrado'


def p_secant(p):
	'SECANT : PR_secant Token_Parent_Abierto SuperExp Token_Parent_Cerrado'

def p_sininv(p):
	'sininv : PR_seninv Token_Parent_Abierto SuperExp Token_Parent_Cerrado'

def p_cosinv(p):
	'cosinv : PR_cosinv Token_Parent_Abierto SuperExp Token_Parent_Cerrado'

def p_taninv(p):
	'taninv : PR_taninv Token_Parent_Abierto SuperExp Token_Parent_Cerrado'

def p_write(p):
	'''write : PR_Write Token_Parent_Abierto ID Token_Parent_Cerrado Token_Punto_Coma
	           | PR_Write Token_Parent_Abierto ID  Token_Corchete_Abierto SuperExp Token_Corchete_Cerrado Token_Parent_Cerrado Token_Punto_Coma
	           | PR_Write Token_Parent_Abierto ID Token_Corchete_Abierto miniExp Token_Corchete_Cerrado Token_Corchete_Abierto miniExp Token_Corchete_Cerrado Token_Parent_Cerrado Token_Punto_Coma'''

def p_read(p):
    'read : PR_read Token_Parent_Abierto SuperExp Token_Parent_Cerrado Token_Punto_Coma'

def p_graf(p):
   	'GRAPH : PR_graph Token_Parent_Abierto SuperExp Token_Parent_Cerrado Token_Punto_Coma'

def p_NORM(p):
   	'NORMALIZAR : PR_normalizar Token_Parent_Abierto SuperExp Token_Parent_Cerrado Token_Punto_Coma'

def p_map (p):
   	'map : PR_mapmat Token_Parent_Abierto SuperExp Token_Parent_Cerrado Token_Punto_Coma'




parser = yacc.yacc(start ='prog')



archivo = sys.argv[1]
f = open(archivo, 'r')
s = f.read()
parser.parse(s)

for i in range(0,len(cuadruplos)):
   print (cuadruplos[i].ind, cuadruplos[i].estatuto,   cuadruplos[i].var1,   cuadruplos[i].var2,   cuadruplos[i].var3 )

#for i in range(0,len(saltos)):
 #  print (saltos[i])




if valido == True:
    print("Archivo valido")
    sys.exit()
else: 
    print("Archivo no valido")
    sys.exit()