import pandas as pd
import streamlit as st
import pyperclip
import openpyxl

#git add -A
#git status
#git commit -m "Terceiro commit de teste"
#git push origin main

# Carregar o arquivo Excel
df = pd.read_excel("LPAW_BASE_COD.xlsx", engine='openpyxl')
df.rename(columns={df.columns[8]: 'OBS'}, inplace=True)
df = df[["Máquina" ,"Cod Grupo PcFactory" ,
         "Desc Cod Grupo PcFactory" , "Cod Mot PcFactory",
         "Desc Mot Grupo PcFactory",
          "Status" , "Copiar PcFactory" , 
          "Auxiliar" , "OBS"]]

# Separamos as máquinas
df_maquinas = df["Máquina"].dropna().unique()

# Criar o aplicativo Streamlit
st.set_page_config(page_title="LPAW Sistemas de Paradas", layout="wide")

# Criar uma aba lateral
st.sidebar.header("Filtros para a parada.")

# Criar uma lista
setores = df_maquinas.tolist()

# Adicionar a caixa de seleção para escolher
setor_selecionado = st.sidebar.selectbox('Máquinas:', setores)

# Filtramos o DataFrame baseado na máquina selecionada
df_filtrado = df[df['Máquina'] == setor_selecionado]

# Verificar se existem dados filtrados para a máquina
if not df_filtrado.empty:
    # Selecionar o status pai disponivel apos o primeiro filtro
    df_status = df_filtrado['Status'].dropna().unique()
    status_pai = df_status.tolist()

    # Adicionar a caixa de seleção para escolher o status
    status_selecionado = st.sidebar.selectbox('Status:', status_pai)

    # Filtramos o DataFrame com base no setor e status selecionados
    df_filtro_final = df_filtrado[df_filtrado['Status'] == status_selecionado] 
    st.dataframe(df_filtro_final, height=600)    

# Criacao da parada
    # Juntamos os select box para formar a parada
    df_filtro_aux = df_filtro_final['Copiar PcFactory'].dropna().unique()
    opcoes_paradas = [''] + list(df_filtro_aux) 
    parada_selecionada = st.sidebar.selectbox('Selecione:', [""] + list(df_filtro_final['Copiar PcFactory']))
    filtro_1 = df_filtro_final[df_filtro_final['Copiar PcFactory'] == parada_selecionada]
# Auxilio
    # Criamos um codigo unico para o auxilio    
    df_filtro_aux = df_filtro_final['Auxiliar'].dropna().unique()
    opcoes_aux = [''] + list(df_filtro_aux)    
    aux_selecionado = st.sidebar.selectbox('Selecione:', opcoes_aux)
     

    # Exibir a coluna 'Status'
    if not filtro_1.empty:
        mensagem = f'<p style="font-size: 20px; font-weight: bold;">{parada_selecionada} {aux_selecionado}</p>'
        st.markdown(mensagem, unsafe_allow_html=True)

        mensagem_copia = f"{parada_selecionada} {aux_selecionado}"

        if st.sidebar.button('Copiar parada'):
            pyperclip.copy(mensagem_copia)
            st.success("Parada copiada com sucesso!")

else:
    st.write(f"Não há dados disponíveis para a máquina '{setor_selecionado}'.")

