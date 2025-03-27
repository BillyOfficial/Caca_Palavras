# Caçador de Palavras

Este é um simples (mas **poderoso**) projeto em Python para encontrar palavras em uma matriz de letras, em todas as direções possíveis: horizontal, vertical e diagonal. **Odeio o Pylint**, mas ele ajudou a manter o código organizado - apesar de ser chato seguir todas as regras dele.

# Estrutura do Projeto em Python

1. **Lista de Letras**
   * [LINHAS_DO_PUZZLE](): Contém as sequências de caracteres (as linhas do caça-palavras).
   * Cada string representa uma linha, que depois transformamos em listas de caracteres.
2. **Função Principal**
   * [buscar_palavra_na_matriz(grade, palavra)]():
     * Recebe a “grade” (a lista de linhas) e a “palavra” a ser procurada.
     * Percorre toda a matriz, comparando cada pedaço de letras com a palavra em questão.
     * Verifica horizontalmente (esquerda->direita e direita->esquerda), verticalmente (cima->baixo e baixo->cima) e nas diagonais (em quatro direções diferentes).
     * Retorna as posições onde a palavra foi encontrada.
3. **Execução do Código**
   * No final, temos um [if__name__==&#34;main&#34;:]() que é o “ponto de entrada”.
   * Ele solicita ao usuário que digite a palavra que deseja procurar (em maiúsculas) e exibe no terminal onde essa palavra aparece na matriz.
4. **Pylint**
   * Para manter o Pylint feliz, foram necessárias várias adaptações, como:
     * Uso de nomes de funções e variáveis em *snake_case*.
     * Quebrar linhas muito longas em vários trechos.
     * Evitar espaçamentos irregulares e outros pontos de estilo.
   * **Confesso que foi inteiramente chato** ficar corrigindo todos os avisos de formatação e nomes de variáveis (principalmente quando passa de 100 caracteres por linha). Mas, no fim, o código ficou bem organizado. Isso me faz exercitar as boas praticas não só nesse projeto, mas tabém nos próximos.

# Como Usar

1. **Clone ou Baixe** este repositório.
2. Abra um terminal na pasta do projeto. (se for Vscode é CTRL + '  e buscar a aba "terminal")
3. Execute o arquivo [cacador_de_palavras.py]() (ou o nome que você deu pra ele):

   ```powershell
   python cacador_de_palavras.py
   ```
4. Digite a palavra que deseja procurar (em maiúsculas).
   Caso você não mude a matriz (letras do campo aonde será caçado), poderá buscar umas dessas palavras, já que eu copiei esse caça-palavras de uma atividade da faculade onde eu não queria perder meu tempo buscando palavras, e pensei em automatizar caso venha maIs dessas kkkk.

   CASOSDEUSO
   CLASSE
   ESTADOS
   ATIVIDADES
   INTERACAO
5. Aguarde o resultado, que mostrará as posições (linha, coluna) e a direção em que a palavra foi encontrada.

Exemplo de saída (caso encontre alguma palavra):

```powershell
[(2, 4, 'horizontal L->R'), (7, 10, 'diagonal TR->BL')]
```

> Isso significa que a palavra foi achada na linha 2, coluna 4 (na horizontal esquerda->direita) e também na linha 7, coluna 10 (diagonal de cima pra direita, descendo pra esquerda).

# Requisitos

* Python 3.10.11
* (Opcional) Pylint caso queira validar o estilo do código.

# Observações

* Se você quiser personalizar o caça-palavras, basta alterar a lista [LINHAS_DO_PUZZLE]() para as letras que desejar.
* Lembre-se que o código está configurado para buscar a palavra exatamente como digitada (maiúsculas).
