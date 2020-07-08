import ply.lex as lex
import ply.yacc as yacc

reserved={
   'mas' : 'SU',
   'menos' : 'RE',
   'Sea' : 'ASIGN',
   'sea' : 'ASIGN',
   'igual' : 'EQ',
   'a' : 'EQ2',
   'Mostrar' : 'PR',
   'mostrar' : 'PR',
   'Repetir' : 'RPT',
   'repetir' : 'RPT',
   'veces' : 'V'
}

tokens = [
    'N',
    'ID'
    ]+list(reserved.values())
    
t_SU=r'[Mm]as'
t_RE=r'[Mm]enos'
t_ASIGN = r'[Ss]ea'
t_EQ = r'[Ii]gual'
t_EQ2 = r'a'
t_PR = r'[Mm]ostrar'
t_RPT = r'[Rr]epetir'


def t_N(t):
    r'\-*[0-9]+'
    st = str(t.value)
    num = st.count('-')
    if num == 1 or num == 0:
        t.value = int(t.value)
    elif num % 2 == 0:      #par
        number = st.strip('-')
        t.value = int(number)
    else:                   #impar
        number = st.strip('-')
        t.value = -int(number)
    return t
    
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t
    
t_ignore  = ' \t'

def t_error(t):
    print(":(")
    t.lexer.skip(1)

precedence=(('left', 'SU', 'RE'),)

variables={}

def p_resultado(t):
    'resultado : s'
    

def p_asignacion(t):
    'resultado : ASIGN ID EQ EQ2 s'
    variables[t[2]]=t[5]

def p_expr_num(t):
    's : N'
    t[0]=t[1]
    
def p_expr_id(t):
    's : ID'
    try:
        t[0] = variables[t[1]]
    except LookupError:
        print("Variable indefinida '%s'" % t[1])
        t[0] = 0
    
def p_expr_op(t):
    '''s : s SU s
        | s RE s'''
    if t[2] == 'mas':
        t[0]=t[1]+t[3]
    elif t[2] == 'menos':
        t[0]=t[1]-t[3]

def p_expr_num_neg(t):
    's : RE N'
    t[0] = -t[2]

def p_error(t):
    print(":'(")

def p_PR(t):
    '''s : PR ID 
    | PR s'''
    var_names = list(variables.keys())
    if var_names.count(t[2]) == 1:
        try:
            print(variables[t[2]])
        except LookupError:
            print("Variable indefinida '%s'" % t[2])
            t[0] = 0
    else:
        t[0] = t[2]
        print(t[0])

#def p_repetir(t):
#    's : RPT N V s'
#    
#    for i in range(t[2]):
#        t[0] = t[4]
#        print(t[0])


lexer=lex.lex()
parser=yacc.yacc()
while True:
    try:
        data = input()
    except EOFError:
        break
    parser.parse(data)
