# Compilapedia

# Desenvolvedores

André Siqueira Ramos de Lima  
Fabio Augusto Ramanho  
Victor Daisuke Dano  

# Conceitos:
Ao ler um texto, o compilador busca nele um padrão de frase descritiva baseado nos padrões encontrados em textos biográficos do Wikipedia sobre personagens da história e do presente.   
Uma varredura na base de dados do Wikipedia seria capaz de listar correlações entre personagens através da combinação de adjetivos, sejam ele sobre ocupações, como: juízes, filósofos, ídolos; ou sobre origens, como: romanos, americanos, europeus.  A diferenciação entre os verbos também traz a possibilidade de diferenciar entidades do passado e do presente.


# Analisador Léxico:

O analisador léxico recebe como entrada um frase inserida pelo usuário na interface.   
Em seguida, são removidos todos os conteúdos que estão presentes entre parênteses e colchetes.  
A frase é então transformada em uma lista de palavras, separadas por espaço (incluindo vírgulas e pontos finais como palavras da lista).  
Cada palavra é submetida ao reconhecimento pelos autômatos do sistema, sendo eles, na respectiva ordem de prioridade: Nome, Artigo, Verbo, Separador, Final e Adjetivo.  
Ao ser reconhecida, uma palavra é transformada em um token, que será inserida em uma nova lista de tokens, que será a saída do analisador léxico.  

# Analisador Sintático:

Com a lista de tokens recebida do analisador léxico, é feita uma concatenação de tokens iguais adjacentes (Para casos de Nomes e Adjetivos compostos).  
Feito o tratamento, a lista de tokens é submetida a uma analise sintática no autômato Geral, assim, será verificado se os tokens formam uma composição aceita pela linguagem.   

# Requisitos de execução:

Primeiramente, é preciso apresentar o Python 3 instalado na máquina local.  
Também deve ser instalado o pacote tkinter (aplicação de interface gráfica) use o seguinte comando: 

Windows (Com pip instalado):

pip install tk

Linux:

sudo apt install python3-tk

# Exemplo 1:

![Alt text](imagens/Cortella.png?raw=true "Title")

Início do Processamento - Texto Original: Caio Júlio César (em latim: Caius ou Gaius Iulius Caesar) foi um patrício, líder militar e político romano.  

Início do Analisador Léxico:  
"Caio" : NOME  
"Júlio" : NOME  
"César" : NOME  
"foi" : VERBO  
"um" : ARTIGO  
"patrício" : ADJETIVO  
"," : SEPARADOR  
"líder" : ADJETIVO  
"militar" : ADJETIVO  
"e" : SEPARADOR  
"político" : ADJETIVO  
"romano" : ADJETIVO  
"." : FINAL  

Início do Analisador Sintático:  
{'tipo': 'NOME', 'conteudo': 'Caio Júlio César'}  
{'tipo': 'VERBO', 'conteudo': 'foi'}  
{'tipo': 'ARTIGO', 'conteudo': 'um'}  
{'tipo': 'ADJETIVO', 'conteudo': 'patrício'}  
{'tipo': 'SEPARADOR', 'conteudo': ','}  
{'tipo': 'ADJETIVO', 'conteudo': 'líder militar'}  
{'tipo': 'SEPARADOR', 'conteudo': 'e'}  
{'tipo': 'ADJETIVO', 'conteudo': 'político romano'}  
{'tipo': 'FINAL', 'conteudo': '.'}  
A cadeia é uma cadeia válida!  

# Exemplo 2:

![Alt text](imagens/Cortella.png?raw=true "Title")

Início do Processamento - Texto Original: Mario Sergio Cortella (Londrina, 5 de março de 1954) é um filósofo, escritor, educador, palestrante e professor universitário brasileiro.  

Início do Analisador Léxico:  
"Mario" : NOME  
"Sergio" : NOME  
"Cortella" : NOME  
"é" : VERBO  
"um" : ARTIGO  
"filósofo" : ADJETIVO  
"," : SEPARADOR  
"escritor" : ADJETIVO  
"," : SEPARADOR  
"educador" : ADJETIVO  
"," : SEPARADOR  
"palestrante" : ADJETIVO  
"e" : SEPARADOR  
"professor" : ADJETIVO  
"universitário" : ADJETIVO  
"brasileiro" : ADJETIVO  
"." : FINAL  

Início do Analisador Sintático:  
{'tipo': 'NOME', 'conteudo': 'Mario Sergio Cortella'}  
{'tipo': 'VERBO', 'conteudo': 'é'}  
{'tipo': 'ARTIGO', 'conteudo': 'um'}  
{'tipo': 'ADJETIVO', 'conteudo': 'filósofo'}  
{'tipo': 'SEPARADOR', 'conteudo': ','}  
{'tipo': 'ADJETIVO', 'conteudo': 'escritor'}  
{'tipo': 'SEPARADOR', 'conteudo': ','}  
{'tipo': 'ADJETIVO', 'conteudo': 'educador'}  
{'tipo': 'SEPARADOR', 'conteudo': ','}  
{'tipo': 'ADJETIVO', 'conteudo': 'palestrante'}  
{'tipo': 'SEPARADOR', 'conteudo': 'e'}  
{'tipo': 'ADJETIVO', 'conteudo': 'professor universitário brasileiro'}  
{'tipo': 'FINAL', 'conteudo': '.'}  
A cadeia é uma cadeia válida!  

# Exemplo 3:

![Alt text](imagens/Marco.png?raw=true "Title")

Início do Processamento - Texto Original: Marco Túlio Cícero (em latim: Marcus Tullius Cicero,romaniz.: Kikeron; 106 – 43 a.C.) foi um advogado, político, escritor, orador e filósofo da gens Túlia da República Romana eleito cônsul.  

Início do Analisador Léxico:    
"Marco" : NOME  
"Túlio" : NOME  
"Cícero" : NOME  
"foi" : VERBO  
"um" : ARTIGO  
"advogado" : ADJETIVO  
"," : SEPARADOR  
"político" : ADJETIVO  
"," : SEPARADOR  
"escritor" : ADJETIVO  
"," : SEPARADOR  
"orador" : ADJETIVO  
"e" : SEPARADOR  
"filósofo" : ADJETIVO  
"da" : ADJETIVO  
"gens" : ADJETIVO  
"Túlia" : NOME  
"da" : ADJETIVO  
"República" : NOME  
"Romana" : NOME  
"eleito" : ADJETIVO  
"cônsul" : ADJETIVO  
"." : FINAL  

Início do Analisador Sintático:  
{'tipo': 'NOME', 'conteudo': 'Marco Túlio Cícero'}  
{'tipo': 'VERBO', 'conteudo': 'foi'}  
{'tipo': 'ARTIGO', 'conteudo': 'um'}  
{'tipo': 'ADJETIVO', 'conteudo': 'advogado'}  
{'tipo': 'SEPARADOR', 'conteudo': ','}  
{'tipo': 'ADJETIVO', 'conteudo': 'político'}  
{'tipo': 'SEPARADOR', 'conteudo': ','}  
{'tipo': 'ADJETIVO', 'conteudo': 'escritor'}  
{'tipo': 'SEPARADOR', 'conteudo': ','}  
{'tipo': 'ADJETIVO', 'conteudo': 'orador'}  
{'tipo': 'SEPARADOR', 'conteudo': 'e'}  
{'tipo': 'ADJETIVO', 'conteudo': 'filósofo da gens'}  
{'tipo': 'NOME', 'conteudo': 'Túlia'}  
{'tipo': 'ADJETIVO', 'conteudo': 'da'}  
{'tipo': 'NOME', 'conteudo': 'República Romana'}  
{'tipo': 'ADJETIVO', 'conteudo': 'eleito cônsul'}  
{'tipo': 'FINAL', 'conteudo': '.'}  
A cadeia não é uma cadeia válida!  