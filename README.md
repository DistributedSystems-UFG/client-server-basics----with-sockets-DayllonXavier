# ClientServerBasics

O servidor consiste de serviços relativos a operações de números primos.
Cada serviço é solicitado por meio de uma mensagem no formato 
* \<identificador\> \<valor\>

O \<identificador\> explicita o tipo de operação que será realizado sobre o parâmetro \<valor\>.
Os serviços disponíveis são:

* CHECK \<valor\> -\> Retorna 1 se o \<valor\> é um número primo e 0 caso contrário.
* POS \<valor\> -\> Se \<valor\> é um número primo, será retornado a posição de \<valor\> na lista de números primos, indexados de 1 (número 2 é o primeiro da lista). Caso \<valor\> não seja um número primo, será retornado a posição na lista de primos do menor número primo maior que \<valor\>.
* NEXT \<valor\> -\> Retorna o menor número primo maior que \<valor\>.
* PREV \<valor\> -\> Retorna o maior número primo menor que \<valor\>.
* PRIME \<valor\> -\> Retorna \<valor\>-ésimo número primo da lista de números primos.

### Implementação do servidor.

A primeira ação do código do servidor ao ser inicializado é a computação dos números primos no intervalo de 2 à \<MAXVALUE\>. Esse último valor representa uma constante especificada no código server.py.
A partir disso, os primos são computados por meio do algoritmo Crivo de Eratóstenes. Ao final da computação, tem-se uma lista de todos os primos encontrados denominada "primes". Após a computação dos primos, o server é de fato inicializado e espera por uma conexão.

### Implementação do cliente.

O cliente primeiramente se conecta ao servidor e espera a leitura de uma "query" do teclado. Essa "query" é então encaminhada para ser processada pelo servidor. Caso essa "query" seja o texto "EXIT", a conexão entre o cliente e o servidor é encerrada e o programa finalizado.

### Vídeo de apresentação

O link para a apresentação do projeto está disponível aqui: https://youtu.be/zf8ITDOUbeQ