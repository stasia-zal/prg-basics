import re
def f(vname):
    pattern=r'^[A-Za-z_]{1}[A-Za-z0-9_]{,5}$'
    if re.fullmatch(pattern,vname):
        return True
    return False




if __name__=='__main__':
    print(f('aBC'))
    print(f('_ab_c'))
    print(f('abcdef'))
    print(f('8abc'))
    print(f('no_book'))