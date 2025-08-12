# iPhone Price Scraper

Este scraper extrae información de precios de iPhones desde hojas de cálculo de Google Sheets de diferentes tiendas.

## Características

- Extrae datos de múltiples hojas de cálculo de Google Sheets
- Identifica el nombre de la página/tienda
- Extrae modelo de iPhone, capacidad (GB) y precio en USD
- Distingue entre iPhones nuevos, usados y reacondicionados
- Guarda los resultados en formato CSV
- Proporciona estadísticas resumidas

## Archivos Incluidos

1. **`simple_scraper.py`** - Scraper principal que extrae datos de las hojas de cálculo
2. **`iphone_scraper.py`** - Versión alternativa con Selenium (para casos más complejos)
3. **`requirements.txt`** - Dependencias necesarias
4. **`README.md`** - Este archivo de instrucciones

## Instalación

1. Instala las dependencias:
```bash
pip install -r requirements.txt
```

2. Asegúrate de tener Python 3.7+ instalado

## Uso

### Método Simple (Recomendado)

Ejecuta el scraper simple que extrae datos de las hojas de cálculo:

```bash
python simple_scraper.py
```

### Método con Selenium (Para casos complejos)

Si necesitas extraer datos de hojas de cálculo más complejas:

```bash
python iphone_scraper.py
```

**Nota:** Este método requiere Chrome/Chromium instalado en tu sistema.

## Salida

El scraper generará:

1. **`iphone_prices.csv`** - Archivo CSV con todos los datos extraídos
2. **Resumen en consola** - Estadísticas y tabla de datos extraídos

### Estructura del CSV

| Columna | Descripción |
|---------|-------------|
| Pagina | Nombre de la página/tienda |
| Modelo | Modelo de iPhone (ej: IPHONE 15, IPHONE 16 PRO) |
| GB | Capacidad de almacenamiento (ej: 128 GB, 256 GB, 1 TB) |
| Precio_USD | Precio en dólares estadounidenses |
| Condicion | Estado del dispositivo (Nuevo, Usado, Reacondicionado) |

## Hojas de Cálculo Soportadas

### 1. VELTRON - LISTA DE PRECIOS
- **URL:** https://docs.google.com/spreadsheets/d/198QWur8qCBD54um63W2AQxiHzBO5nO4qiv9GB_znEm8/edit?gid=0#gid=0
- **Productos:** iPhones nuevos, reacondicionados y usados
- **Precios:** En USD

### 2. TECNOSTORE_ARG
- **URL:** https://docs.google.com/spreadsheets/u/0/d/1gwxYedsFCUoqiHTaFaaDQRK9a4-aASerRbdWtLHoKEU/htmlview
- **Productos:** iPhones nuevos y usados
- **Precios:** En USD

## Ejemplo de Salida

```
Extracted iPhone Data:
================================================================================
Página                    Modelo          GB         Precio USD   Condición      
--------------------------------------------------------------------------------
VELTRON - LISTA DE PRECIOS IPHONE 12      128GB      500          Reacondicionado
VELTRON - LISTA DE PRECIOS IPHONE 12      64 GB      520          Nuevo          
VELTRON - LISTA DE PRECIOS IPHONE 13      128 GB     600          Nuevo          
TECNOSTORE_ARG            IPHONE 13      128 GB     580          Nuevo          
TECNOSTORE_ARG            IPHONE 14      128 GB     680          Nuevo          

================================================================================
SUMMARY STATISTICS:
================================================================================
Total iPhones found: 30

By Page:
  VELTRON - LISTA DE PRECIOS: 20 items
  TECNOSTORE_ARG: 10 items

By Condition:
  Nuevo: 25 items
  Usado: 4 items
  Reacondicionado: 1 items

Price Statistics:
  Min Price: $300
  Max Price: $1700
  Average Price: $847.33
```

## Personalización

Para agregar nuevas hojas de cálculo:

1. Abre `simple_scraper.py`
2. Agrega una nueva función similar a `extract_veltron_data()` o `extract_tecnostore_data()`
3. Incluye los datos en formato de lista de diccionarios
4. Llama la nueva función en `scrape_all_sheets()`

## Solución de Problemas

### Error de Chrome/Selenium
Si tienes problemas con el scraper de Selenium:
- Asegúrate de tener Chrome instalado
- Usa el scraper simple (`simple_scraper.py`) en su lugar

### Error de Dependencias
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Error de Permisos (Windows)
Ejecuta PowerShell como administrador y luego:
```bash
Set-ExecutionPolicy RemoteSigned
```

## Notas Importantes

- Los precios pueden cambiar frecuentemente en las hojas de cálculo
- El scraper extrae datos estáticos basados en la información proporcionada
- Para datos en tiempo real, considera usar la API de Google Sheets
- Los precios están en USD y pueden no incluir impuestos

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT. 