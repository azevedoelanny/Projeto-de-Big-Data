import dash
import dash_table
import pandas as pd
from dash import html, dcc
from dash.dependencies import Input, Output, State
import base64
import io

# Leia seus dados locais (produtos e marcas)
df_produtos = pd.read_csv('Tabela_de_Produtos_e_Marcas.csv', delimiter=';')

# Inicializa o app Dash
app = dash.Dash(__name__)

# Layout da página com upload de arquivo e tabela interativa
app.layout = html.Div(children=[
    html.H1(children='Classificação ABC de Produtos'),
    
    # Componente de upload de arquivo
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Arraste e solte ou ',
            html.A('selecione um arquivo CSV de estoque')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        multiple=False
    ),
    
    # Tabela para exibir os dados processados
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in ['Produto', 'Marca', 'Categoria', 'Classificação ABC']],
        data=[],  # Inicialmente vazio
        filter_action='native',  # Habilita filtro por coluna
        sort_action='native',    # Habilita ordenação por coluna
        sort_mode='multi',       # Permite ordenar por múltiplas colunas
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'left'},
    ),
])

# Função para processar o arquivo CSV de estoque
def process_csv(contents):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    df_estoque = pd.read_csv(io.StringIO(decoded.decode('utf-8')), delimiter=';')

    # Filtra as saídas
    df_saida = df_estoque[df_estoque['Operação (Entrada/Saída)'] == 'Saída']
    df_agrupado = df_saida.groupby('ID do Produto')['Quantidade'].sum().reset_index()

    # Ordena por quantidade
    df_agrupado = df_agrupado.sort_values(by='Quantidade', ascending=False)
    total_saidas = df_agrupado['Quantidade'].sum()

    # Calcula porcentagem e porcentagem acumulada
    df_agrupado['Porcentagem'] = (df_agrupado['Quantidade'] / total_saidas) * 100
    df_agrupado['Porcentagem Acumulada'] = df_agrupado['Porcentagem'].cumsum()

    # Função para classificar ABC
    def classificar_abc(porcentagem_acumulada):
        if porcentagem_acumulada <= 80:
            return 'A'
        elif porcentagem_acumulada <= 95:
            return 'B'
        else:
            return 'C'

    # Aplica a classificação ABC
    df_agrupado['Classificação ABC'] = df_agrupado['Porcentagem Acumulada'].apply(classificar_abc)

    # Mescla com a tabela de produtos
    df_completo = pd.merge(df_agrupado, df_produtos, left_on='ID do Produto', right_on='ID')

    # Remove as colunas de ID e Quantidade, mantém as necessárias
    df_final = df_completo[['Produto', 'Marca', 'Categoria', 'Classificação ABC']]
    
    return df_final

# Callback para atualizar a tabela com base no arquivo CSV enviado
@app.callback(
    Output('table', 'data'),
    [Input('upload-data', 'contents')],
    [State('upload-data', 'filename')]
)
def update_table(contents, filename):
    if contents is not None:
        df_final = process_csv(contents)
        return df_final.to_dict('records')
    return []

# Executa o servidor
if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0',)
