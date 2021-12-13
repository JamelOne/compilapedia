minuscula = "[a-z|á|à|â|ã|é|è|ê|í|ó|ô|õ|ú|ç|ñ|-]"

automato = {0: {minuscula: 1},
        1: {minuscula: 2},
        2: {minuscula: 2}}
finais = [2]