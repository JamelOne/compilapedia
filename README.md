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

# Exemplos:




