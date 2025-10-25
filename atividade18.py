import streamlit as st

if 'votos' not in st.session_state:
    st.session_state.votos = {
        "Python": 0,
        "JavaScript": 0,
        "JavaOutro": 0 
    }

if 'mostrar_resultados' not in st.session_state:
    st.session_state.mostrar_resultados = True

st.title("Enquete: Qual sua linguagem de programação favorita?")

opcoes = ["Python", "JavaScript", "JavaOutro"]
st.radio("Escolha uma linguagem", options = opcoes, key = 'voto')

if st.button("Votar"):
    voto_atual = st.session_state.voto
    st.success(f"Você votou em {voto_atual}")
    st.session_state.votos[voto_atual] += 1

st.checkbox("Mostrar resultados da enquete", key='mostrar_resultados')

if st.session_state.mostrar_resultados:
    st.subheader("Resultados:")

    votos_atuais = st.session_state.votos

    votos_totais = sum(votos_atuais.values())

    if votos_totais == 0:
        st.write("Ainda não há votos.")
    else:
        for linguagem, contagem in votos_atuais.items():
            
            percentual = (contagem / votos_totais) * 100.0
            
            st.write(f"{linguagem}: {contagem} votos ({percentual:.1f}%)")
            
            st.progress(percentual / 100)