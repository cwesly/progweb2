import streamlit as st
import pandas as pd
import requests

st.title("Consulta de Clima - API Open-Meteo")
st.text("Digite o nome de uma cidade para ver o clima atual e previsão para os próximos dias")
st.text("Nome da cidade:")

# Input para o nome da cidade
cidade = st.text_input("Digite o nome da cidade:")

st.button("Buscar Clima")

if cidade:
    # API de geocoding para obter latitude e longitude
    geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={cidade}"
    geocoding_response = requests.get(geocoding_url)
    geocoding_data = geocoding_response.json()

    if 'results' in geocoding_data and geocoding_data['results']:
        # Pegar a primeira correspondência
        lat = geocoding_data['results'][0]['latitude']
        lon = geocoding_data['results'][0]['longitude']
        st.write(f"Coordenadas para {cidade}: Latitude {lat}, Longitude {lon}")

        # API de previsão do tempo
        forecast_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=America%2FBahia"
        forecast_response = requests.get(forecast_url)
        forecast_data = forecast_response.json()

        if 'daily' in forecast_data:
            daily = forecast_data['daily']
            dates = daily['time']
            temp_max = daily['temperature_2m_max']
            temp_min = daily['temperature_2m_min']
            precipitation = daily['precipitation_sum']

            # Exibir dados em uma tabela
            st.subheader("Previsão Diária")
            data = {
                "Data": dates,
                "Temp. Máx. (°C)": temp_max,
                "Temp. Mín. (°C)": temp_min,
                "Precipitação (mm)": precipitation
            }
            st.table(data)

            # Gráfico para temperaturas
            st.subheader("Gráfico de Temperaturas")
            df = pd.DataFrame(data)
            st.line_chart(df.set_index("Data")[["Temp. Máx. (°C)", "Temp. Mín. (°C)"]])
        else:
            st.error("Erro ao obter dados de previsão.")
    else:
        st.error("Cidade não encontrada.")
