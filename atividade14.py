import streamlit as st

st.title("Calculadora de Saúde Inteligente")
st.markdown("Analise seu estado físico e receba recomendações automáticas de saúde.")

col1, col2, col3 = st.columns(3)

with col1:
    idade = st.number_input("Idade(anos)", value=25, min_value=1, max_value=120)
    sexo = st.selectbox("Sexo", ["Masculino", "Feminino", "Não Binário"], index=0)
with col2:
    peso = st.number_input("Peso(kg)")
    altura = st.number_input("Altura(m)")
with col3:
    nivel_atividade = st.selectbox("Nível de Atividade", ["Sedentário", "Leve", "Moderado", "Ativo"])

if altura > 0:
    altura_m = altura
    imc = peso / (altura_m ** 2)
else:
    imc = 0

if sexo == "Masculino":
    tmb = 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * idade)
elif sexo == "Feminino":
    tmb = 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * idade)
else:  # Não Binário
    tmb_masculino = 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * idade)
    tmb_feminino = 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * idade)
    tmb = (tmb_masculino + tmb_feminino) / 2

fatores = {
    "Sedentário": 1.2,
    "Leve": 1.375,
    "Moderado": 1.55,
    "Ativo": 1.725
}
fator = fatores[nivel_atividade]
gasto_calorico = tmb * fator

if imc < 18.5:
    classificacao_imc = "Abaixo do peso"
    recomendacao = "Você está abaixo do peso. Considere consultar um nutricionista para um plano de ganho de peso saudável."
    st_status = st.warning
elif 18.5 <= imc < 25:
    classificacao_imc = "Peso normal"
    recomendacao = "💡 ✅ Mantenha uma dieta equilibrada e continue com atividade física."
    st_status = st.success
elif 25 <= imc < 30:
    classificacao_imc = "Sobrepeso"
    recomendacao = "Você está com sobrepeso. É um bom momento para focar em uma dieta mais balanceada e aumentar a atividade física."
    st_status = st.warning
else:
    classificacao_imc = "Obesidade"
    recomendacao = "Seu IMC indica obesidade. É altamente recomendável procurar orientação médica e nutricional."
    st_status = st.error

st.divider()
st.subheader("Resultados")

col_res1, col_res2 = st.columns([1, 2])

with col_res1:
    st.metric(label="IMC", value=f"{imc:.2f}")

    if imc < 18.5:
        st.warning(classificacao_imc)
    elif 18.5 <= imc < 25:
        st.success(classificacao_imc)
    elif 25 <= imc < 30:
        st.warning(classificacao_imc)
    else:
        st.error(classificacao_imc)

    st.metric(label="TMB (Kcal/dia)", value=f"{tmb:.0f}")
    st.metric(label="Gasto Calórico Diário", value=f"{gasto_calorico:.0f} kcal")

with col_res2:
  st_status(recomendacao)