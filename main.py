nt1 = 'A'
rule1, rule2 = "aA", 'aB'
nt2 = 'B'
rule3, rule4 = 'bB', 'c'

lookahead = 0
keyw = 'ac'



def error():
    print('bib bib, you lose. Could not generate the given string with this grammar.')
    exit()
def match(in1):
    global lookahead
    if keyw[lookahead] == in1:
        lookahead += 1
    else:
        error()

def A(in1):
    global lookahead
    try:
        if lookahead == len(in1):
            error()
        if in1[lookahead] in 'a':
            match('a')
            if lookahead == len(in1):
                error()
            if in1[lookahead] in 'a':
                A(in1)
                return
            elif in1[lookahead] in 'bc':
                B(in1)
                return
            else: error()
        else:
            error()
    except():
        error()


def B(in1):
    try:
        global lookahead
        if lookahead == len(in1):
            error()
        if in1[lookahead] in 'b':
            match('b')
            B(in1)
            return
        elif in1[lookahead] in 'c':
            match('c')
            if lookahead != len(in1):
                error()
            print('Mission accomplished, soldier! The given string can be perfectly generated using this grammar.')

            exit()
        else:
            error()
    except():
        error()


if __name__ == '__main__':
    A(keyw)











