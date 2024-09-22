
# Análise ABC de Produtos

Este projeto é uma aplicação web construída com Dash que permite realizar a **classificação ABC de produtos** com base nos dados de vendas. Ele processa arquivos CSV e gera uma tabela interativa com a classificação ABC, facilitando a análise diretamente no navegador.

## Funcionalidades

- Upload de arquivo CSV contendo os dados de estoque (saídas de produtos).
- Processamento e cálculo da classificação ABC dos produtos com base nas quantidades vendidas.
- Exibição dos resultados em uma tabela interativa, com opções de filtro e ordenação.

## Pré-requisitos

- Python 3.7 ou superior
- Todas as bibliotecas necessárias estão listadas no arquivo `requirements.txt`.

## Instalação

Siga as etapas abaixo para configurar e executar o projeto localmente.

### Clonar o repositório

```bash
git clone <url-do-repositorio>
cd <pasta-do-projeto>
```

### Criar e ativar um ambiente virtual (opcional, mas recomendado)

```bash
# Criar um ambiente virtual
python -m venv venv

# Ativar o ambiente virtual (Windows)
venv\Scripts\activate

# Ativar o ambiente virtual (Linux/Mac)
source venv/bin/activate
```

### Instalar as dependências

Execute o seguinte comando para instalar todas as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

## Executando o projeto

Após instalar as dependências, você pode iniciar a aplicação com o seguinte comando:

```bash
python <nome_do_arquivo_principal>.py
```

Substitua `<nome_do_arquivo_principal>` pelo nome do arquivo Python principal do projeto.

### Acessar o aplicativo

Após iniciar o servidor, você poderá acessar o aplicativo no seu navegador web no seguinte endereço:

```
http://localhost:8050
```

## Como utilizar a aplicação

1. **Carregue os dados de estoque:** No topo da página, você encontrará um botão de upload. Arraste e solte ou selecione um arquivo CSV contendo as informações de estoque. O arquivo deve conter as seguintes colunas:
   - `ID do Produto`
   - `Transação`
   - `Operação (Entrada/Saída)`
   - `Data de Entrada`
   - `Data de Saída`
   - `Quantidade`
   - `Data de Validade`
   
   Certifique-se de que os dados no CSV correspondam às saídas de produtos.

2. **Veja os resultados:** Após o upload, os dados serão processados e exibidos em uma tabela interativa que mostrará:
   - O nome do produto
   - A marca
   - A categoria
   - A classificação ABC (A, B ou C)

## Estrutura do arquivo CSV

O arquivo CSV de estoque deve ter um formato como o abaixo:

| ID do Produto | Transação | Operação (Entrada/Saída) | Data de Entrada | Data de Saída | Quantidade | Data de Validade |
|---------------|-----------|--------------------------|-----------------|--------------|------------|------------------|
| 123           | TX001     | Saída                    | 01/01/2024      | 05/01/2024   | 50         | 01/01/2025       |
| 456           | TX002     | Saída                    | 10/01/2024      | 12/01/2024   | 20         | 01/01/2025       |
| 789           | TX003     | Entrada                  | 15/01/2024      | -            | 10         | 01/02/2025       |

A aplicação só processa as linhas com `Operação = Saída` para calcular a classificação ABC.