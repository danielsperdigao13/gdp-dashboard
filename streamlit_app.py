import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import time

# Função para pegar o preço do Bitcoin
def get_bitcoin_price():
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': 'bitcoin',
        'vs_currencies': 'usd'
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data['bitcoin']['usd']

# Função principal do app
def main():
    st.title("Bitcoin Price Monitor")
    
    # Criação de espaço para o preço do bitcoin
    bitcoin_price = st.empty()

    # Gráfico de evolução do preço ao longo do tempo
    price_history = []

    while True:
        price = get_bitcoin_price()
        price_history.append(price)
        bitcoin_price.markdown(f"### Preço Atual do Bitcoin: ${price}")
        
        # Atualiza gráfico de preços
        if len(price_history) > 1:
            df = pd.DataFrame(price_history, columns=['Preço'])
            df['Tempo'] = pd.date_range(start='now', periods=len(df), freq='S')
            fig = px.line(df, x='Tempo', y='Preço', title='Evolução do Preço')
            st.plotly_chart(fig)
        
        # Espera 10 segundos antes de atualizar
        time.sleep(10)

if __name__ == "__main__":
    main()
