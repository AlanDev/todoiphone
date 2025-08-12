import streamlit as st
import pandas as pd
from simple_scraper import SimpleiPhoneScraper

st.title("📱 iPhone Price Scraper")

if st.button("Extraer Datos"):
    with st.spinner("Extrayendo datos..."):
        scraper = SimpleiPhoneScraper()
        scraper.scrape_all_sheets()
        
        if scraper.results:
            df = pd.DataFrame(scraper.results)
            st.success(f"¡Datos extraídos! {len(df)} iPhones encontrados")
            
            # Mostrar tabla
            st.dataframe(df)
            
            # Mostrar estadísticas
            st.subheader("📊 Estadísticas")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Total iPhones", len(df))
            
            with col2:
                st.metric("Precio Promedio", f"${df['Precio_USD'].astype(float).mean():.0f}")
            
            with col3:
                st.metric("Precio Mínimo", f"${df['Precio_USD'].astype(float).min()}")
            
            # Gráfico de precios por tienda
            st.subheader("Precios por Tienda")
            st.bar_chart(df.groupby('Pagina')['Precio_USD'].mean())
        else:
            st.error("No se pudieron extraer datos")

# Mostrar datos guardados si existen
if st.sidebar.checkbox("Mostrar datos guardados"):
    try:
        df_saved = pd.read_csv('iphone_prices.csv')
        st.subheader("Datos Guardados")
        st.dataframe(df_saved)
    except:
        st.info("No hay datos guardados")