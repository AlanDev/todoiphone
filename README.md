# 📱 iPhone Price Scraper

Un scraper inteligente que extrae precios de iPhones de múltiples tiendas argentinas y los muestra en una interfaz web moderna.

## 🚀 Características

- **Scraping Automático**: Extrae datos de 4 tiendas principales
- **Interfaz Web Moderna**: Diseño responsive con Tailwind CSS
- **Filtros Avanzados**: Búsqueda por modelo, precio, condición y tienda
- **Actualización Automática**: Se actualiza cada 6 horas via GitHub Actions
- **Datos Reales**: Información extraída directamente de los spreadsheets

## 🏪 Tiendas Incluidas

- **VELTRON** - Lista de Precios
- **TECNOSTORE_ARG** 
- **MasStore**
- **iPhoneShop**

## 📊 Datos Extraídos

- Modelo de iPhone
- Capacidad (GB/TB)
- Precio en USD
- Condición (Nuevo/Usado/Reacondicionado)
- Nombre de la tienda

## 🛠️ Instalación Local

### Prerrequisitos
- Python 3.9+
- pip

### Pasos
```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/iphone-scrapper.git
cd iphone-scrapper

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el scraper
python simple_scraper.py

# Servir la página web
npx serve . -p 3000
```

## 🌐 Ver la Página Web

1. **Local**: http://localhost:3000
2. **GitHub Pages**: https://tu-usuario.github.io/todoiphone

## ⚙️ Configuración de Actualización Automática

### GitHub Actions (Recomendado)
El repositorio incluye un sistema completo de actualización automática:

1. **GitHub Actions**: Se ejecuta cada 6 horas y actualiza los datos
2. **GitHub Pages**: Se despliega automáticamente con los nuevos datos
3. **Actualización Automática**: Sin intervención manual necesaria

### Configuración
1. Ve a tu repositorio en GitHub
2. Navega a **Actions** → **Update iPhone Prices Data**
3. El workflow se ejecutará automáticamente cada 6 horas
4. También puedes ejecutarlo manualmente desde la pestaña Actions

### Actualización Manual
```bash
# Ejecutar el scraper
python simple_scraper.py

# Hacer commit y push
git add iphone_prices.csv
git commit -m "Update iPhone prices"
git push
```

## 📁 Estructura del Proyecto

```
iphone-scrapper/
├── .github/workflows/     # GitHub Actions
├── simple_scraper.py      # Scraper principal
├── index.html            # Interfaz web
├── iphone_prices.csv     # Datos extraídos
├── requirements.txt      # Dependencias Python
└── README.md            # Documentación
```

## 🔧 Personalización

### Cambiar Frecuencia de Actualización
Edita `.github/workflows/update-data.yml`:
```yaml
schedule:
  # Cada 6 horas (actual)
  - cron: '0 */6 * * *'
  
  # Cada hora
  - cron: '0 * * * *'
  
  # Diario a las 8 AM
  - cron: '0 8 * * *'
```

### Agregar Nuevas Tiendas
1. Edita `simple_scraper.py`
2. Agrega los datos de la nueva tienda
3. Ejecuta el scraper para actualizar

## 📈 Estadísticas

- **Total de Productos**: 109
- **Tiendas**: 4
- **Frecuencia de Actualización**: Cada 6 horas
- **Formato de Datos**: CSV

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 📞 Soporte

Si tienes problemas o sugerencias:
1. Abre un Issue en GitHub
2. Contacta al desarrollador

---

**Última actualización**: Automática cada 6 horas via GitHub Actions 🤖 