import streamlit as st
import pandas as pd
from simple_scraper import SimpleiPhoneScraper

st.set_page_config(
    page_title="📱 iPhone Price Scraper - CEBRA",
    page_icon="📱",
    layout="wide"
)

st.title("📱 iPhone Price Scraper - CEBRA")
st.markdown("### Comparador de precios de iPhones en Argentina")

# Sidebar for filters
st.sidebar.header("🔍 Filtros")

# Extract data button
if st.button("🔄 Extraer Datos Actualizados", type="primary"):
    with st.spinner("Extrayendo datos de todas las tiendas..."):
        scraper = SimpleiPhoneScraper()
        scraper.scrape_all_sheets()
        
        if scraper.results:
            df = pd.DataFrame(scraper.results)
            df.to_csv('iphone_prices.csv', index=False)
            st.success(f"¡Datos extraídos exitosamente! {len(df)} iPhones encontrados")
        else:
            st.error("No se pudieron extraer datos")

# Load and display data
try:
    df = pd.read_csv('iphone_prices.csv')
    
    # Filters
    stores = ['Todos'] + list(df['Pagina'].unique())
    selected_store = st.sidebar.selectbox("Tienda", stores)
    
    conditions = ['Todas'] + list(df['Condicion'].unique())
    selected_condition = st.sidebar.selectbox("Condición", conditions)
    
    models = ['Todos'] + sorted(list(df['Modelo'].unique()))
    selected_model = st.sidebar.selectbox("Modelo", models)
    
    # Apply filters
    filtered_df = df.copy()
    if selected_store != 'Todos':
        filtered_df = filtered_df[filtered_df['Pagina'] == selected_store]
    if selected_condition != 'Todas':
        filtered_df = filtered_df[filtered_df['Condicion'] == selected_condition]
    if selected_model != 'Todos':
        filtered_df = filtered_df[filtered_df['Modelo'] == selected_model]
    
    # Main content
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📱 Total iPhones", len(filtered_df))
    
    with col2:
        avg_price = filtered_df['Precio_USD'].astype(float).mean()
        st.metric("💰 Precio Promedio", f"${avg_price:.0f} USD")
    
    with col3:
        min_price = filtered_df['Precio_USD'].astype(float).min()
        st.metric("💵 Precio Mínimo", f"${min_price} USD")
    
    with col4:
        max_price = filtered_df['Precio_USD'].astype(float).max()
        st.metric("💸 Precio Máximo", f"${max_price} USD")
    
    # CEBRA specific section
    st.subheader("🏪 CEBRA PHONE - Precios Destacados")
    cebra_df = df[df['Pagina'] == 'CEBRA PHONE'].copy()
    if not cebra_df.empty:
        cebra_df['Precio_USD'] = cebra_df['Precio_USD'].astype(float)
        cebra_df = cebra_df.sort_values('Precio_USD')
        
        # Show CEBRA data in a nice format
        for _, row in cebra_df.head(10).iterrows():
            col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
            with col1:
                st.write(f"**{row['Modelo']} {row['GB']}**")
            with col2:
                st.write(f"${row['Precio_USD']} USD")
            with col3:
                st.write(row['Condicion'])
            with col4:
                if row['Condicion'] == 'Nuevo':
                    st.success("🆕")
                elif row['Condicion'] == 'Usado':
                    st.warning("📱")
                else:
                    st.info("🔄")
    
    # Data table
    st.subheader("📊 Tabla Completa de Precios")
    
    # Add price comparison
    if len(filtered_df) > 1:
        st.write("💡 **Consejo:** Usa los filtros de la barra lateral para comparar precios específicos")
    
    # Display the filtered dataframe
    st.dataframe(
        filtered_df.sort_values('Precio_USD'),
        use_container_width=True,
        hide_index=True
    )
    
    # Charts
    if len(filtered_df) > 0:
        st.subheader("📈 Análisis de Precios")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Precios por Tienda**")
            store_prices = filtered_df.groupby('Pagina')['Precio_USD'].mean().sort_values(ascending=False)
            st.bar_chart(store_prices)
        
        with col2:
            st.write("**Precios por Condición**")
            condition_prices = filtered_df.groupby('Condicion')['Precio_USD'].mean().sort_values(ascending=False)
            st.bar_chart(condition_prices)
    
    # Download button
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="📥 Descargar datos filtrados (CSV)",
        data=csv,
        file_name=f'iphone_prices_{selected_store}_{selected_condition}_{selected_model}.csv',
        mime='text/csv'
    )

except FileNotFoundError:
    st.info("📋 No hay datos disponibles. Haz clic en 'Extraer Datos Actualizados' para comenzar.")
except Exception as e:
    st.error(f"Error al cargar los datos: {e}")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>📱 iPhone Price Scraper - Comparador de precios en Argentina</p>
    <p>Incluye datos de: VELTRON, TECNOSTORE, MASSTORE, IPHONESHOP y <strong>CEBRA PHONE</strong></p>
</div>
""", unsafe_allow_html=True)