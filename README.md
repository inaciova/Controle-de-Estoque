# Sistema de Gerenciamento de Estoque  

Este projeto implementa um sistema de gerenciamento de estoque, com o objetivo de otimizar a administração de materiais. O sistema permite carregar dados de um arquivo CSV, atualizar quantidades de itens, listar estoques, salva as alterações em um novo arquivo CSV e verificar alertas de itens com quantidade baixa.

## Funcionalidades

- **Carregamento de Estoque**: Carrega dados de um arquivo CSV para o sistema.
- **Atualização de Estoque**: Permite a atualização das quantidades de itens em estoque.
- **Listagem de Itens**: Exibe todos os itens disponíveis no estoque.
- **Verificação de Estoque Baixo**: Alerta sobre itens que estão abaixo do estoque mínimo.
- **Salvar Estoque**: Salva as alterações em um novo arquivo CSV.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para desenvolver o sistema.
- **Pandas**: Biblioteca utilizada para manipulação de dados.
- **Tkinter**: Biblioteca utilizada para a construção da interface gráfica.

## Pré-requisitos

- Python 3.x instalado em sua máquina.
- Bibliotecas necessárias:
  - pandas

Para instalar o `pandas`, execute o seguinte comando: No terminal ou prompt de comando

pip install pandas

## Como Executar o Programa

### 1. Copie o código do arquivo python desse repositório:
estoque.py

### 2. Crie o arquivo Python: 

Crie um arquivo chamado estoque.py e cole o código copiado do arquivo desse repositório.

### 3. Execute o arquivo:

python estoque.py

### 4. Criar um Atalho no Desktop
Se você estiver usando Windows, pode criar um atalho no desktop para facilitar a execução do programa. Aqui está como fazer isso:
1. Criar um Arquivo Batch (.bat):
Abra o Bloco de Notas.
Cole o seguinte código, substituindo o caminho pelo diretório onde está o seu arquivo estoque.py:

@echo off <br/>
cd "C:\caminho\para\o\diretorio" <br/>
python estoque.py <br/>
pause

Salve o arquivo com a extensão .bat, por exemplo, iniciar_estoque.bat.
Clique com o botão direito no arquivo .bat que você criou e selecione "Criar atalho".
Arraste o atalho para a área de trabalho.
Agora, você pode dar um duplo clique no atalho para iniciar o programa rapidamente.


### 4. Uso do Programa:

Ao iniciar, selecione um arquivo CSV para carregar o estoque.
Insira as quantidades desejadas para cada item e clique em "Atualizar Estoque de Todos os Itens".
Clique em "Listar Itens em Estoque" para visualizar todos os itens disponíveis.
Use o botão "Salvar Estoque" para salvar as alterações em um novo arquivo CSV.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.
## Licença
Este projeto está licenciado sob a MIT License.



