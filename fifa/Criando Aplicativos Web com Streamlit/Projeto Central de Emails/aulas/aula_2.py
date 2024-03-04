import streamlit as st


if not 'pagina_central_email' in st.session_state:
    st.session_state.pagina_central_email = 'home'

def mudar_pagina(nome_pagina):
    st.session_state.pagina_central_email = nome_pagina


# ============== HOME ===================
def home():
    st.markdown('# Central de Emails')

# ============== TEMPLATES ===================
def pag_templates():
    st.markdown('# Templates')


# ============== LISTAS EMAIL ===================
def pag_lista_email():
    st.markdown('# Lista Email')


# ============== CONFIGURACOES ===================
def pag_configuracao():
    st.markdown('# Configurações')


def main():
    st.sidebar.button('Central de Emails', use_container_width=True, on_click=mudar_pagina, args=('home',))
    st.sidebar.button('Templates', use_container_width=True, on_click=mudar_pagina, args=('templates',))
    st.sidebar.button('Lista de Emails', use_container_width=True, on_click=mudar_pagina, args=('lista_emails',))
    st.sidebar.button('Configuração', use_container_width=True, on_click=mudar_pagina, args=('configuracao',))

    if st.session_state.pagina_central_email == 'home':
        home()
    elif st.session_state.pagina_central_email == 'templates':
        pag_templates()
    elif st.session_state.pagina_central_email == 'lista_emails':
        pag_lista_email()
    elif st.session_state.pagina_central_email == 'configuracao':
        pag_configuracao()

main()