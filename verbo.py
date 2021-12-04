import re

def aceitaVerbo(string):
    if re.match("^(é|era|foi)$", string):
        return True
    else:
        return False

x = aceitaVerbo('foi')
print(x)