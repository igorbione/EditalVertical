import streamlit as st
import pandas as pd
import re

# Inicializar o DataFrame na sessão
if 'df' not in st.session_state:
    st.session_state['df'] = pd.DataFrame(columns=[
        'Disciplina', 'Item', 'Estudo 1', 'Estudo 2', 'Revisado', 'Questões Feitas', '% Acerto'
    ])

st.title('📚 EditalVertical - Transforme seu edital em um plano de estudos')

# Entrada de dados
disciplina = st.text_input('Nome da disciplina (ex: Direito Admnistrativo):')
texto = st.text_area('Cole aqui os tópicos do edital:')

def parse_edital(texto, disciplina):
    linhas = texto.split('\n')
    dados = []

    for linha in linhas:
        # Captura itens numerados tipo 1, 1.1, 1.2 etc
        if re.match(r'^\d+(\.\d+)*\s', linha.strip()):
            dados.append({
                'Disciplina': disciplina,
                'Item': linha.strip(),
                'Estudo 1': '',
                'Estudo 2': '',
                'Revisado': '',
                'Questões Feitas': '',
                '% Acerto': ''
            })
    return pd.DataFrame(dados)

if st.button('Adicionar disciplina ao plano'):
    if disciplina and texto:
        novo_df = parse_edital(texto, disciplina)
        st.session_state['df'] = pd.concat([st.session_state['df'], novo_df], ignore_index=True)
        st.success(f'Disciplina "{disciplina}" adicionada!')
    else:
        st.warning('Preencha o nome da disciplina e o texto do edital.')

# Visualizar o DataFrame atual
st.write('📄 Plano atual:')
st.dataframe(st.session_state['df'], use_container_width=True)

# Botão de exportação
if st.button('Exportar para Excel'):
    st.session_state['df'].to_excel('Plano_de_Estudos.xlsx', index=False)
    with open('Plano_de_Estudos.xlsx', 'rb') as f:
        st.download_button('📥 Baixar Plano_de_Estudos.xlsx', f, file_name='Plano_de_Estudos.xlsx')
