maiuscula = "[A-Z|Á|À|Â|Ã|É|È|Ê|Í|Ó|Ô|Õ|Ú|Ç|Ñ|-]"
minuscula = "[a-z|á|à|â|ã|é|è|ê|í|ó|ô|õ|ú|ç|ñ|-]"

automato = {0: {maiuscula: 1},
        1: {maiuscula: 1, minuscula: 1, '\.': 2, ' ': 0},
        2: {' ': 0}}
finais = [1,2]