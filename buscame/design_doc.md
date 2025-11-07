# 💻 Design Doc — “Conceptos Clave de la Computación”

## 📘 1. Información General

**Proyecto:** Aplicación interactiva de conceptos de computación  
**Autor:** *Hilario Jiménez*  
**Lenguaje y Tecnologías:**  

- **Python 3.x**  
- **Streamlit** (interfaz interactiva)  
- **Pandas** (manejo de datos tabulares)  
- **Altair** (visualización de datos)  

**Versión:** 1.0  
**Propósito:**  
Crear una aplicación educativa que permita buscar, visualizar y comprender conceptos clave de la computación mediante gráficos y texto explicativo.

---

## 🧠 2. Objetivo del Proyecto

El objetivo principal es desarrollar una **herramienta interactiva** para estudiantes de computación que:

- Muestre definiciones claras de términos técnicos.
- Permita buscar conceptos específicos por nombre.
- Visualice la importancia relativa de cada concepto con gráficos dinámicos.
- Presente una interfaz amigable e intuitiva.

---

## 🧱 3. Arquitectura y Flujo General

### 🔄 Diagrama de Flujo

Inicio
↓
Configurar página (título, icono, layout)
↓
Cargar datos → convertir a DataFrame
↓
Mostrar buscador de conceptos
↓
¿Hay texto en el buscador?
├─ Sí → Filtrar DataFrame con coincidencias
│ ↓
│ Mostrar tabla + gráfico de importancia
│
└─ No → Mostrar mensaje informativo
↓
Mostrar pie de página
↓
Fin


---

## ⚙️ 4. Componentes Principales

| Componente | Descripción | Librería |
|-------------|--------------|-----------|
| `st.set_page_config()` | Configura la apariencia general (título, ícono, diseño) | Streamlit |
| `pd.DataFrame()` | Crea la estructura de datos tabular | Pandas |
| `st.text_input()` | Campo donde el usuario escribe la palabra a buscar | Streamlit |
| `df[df["Palabra"].str.contains(...)]` | Filtra los datos según la búsqueda | Pandas |
| `st.dataframe()` | Muestra los resultados filtrados en formato tabla | Streamlit |
| `alt.Chart()` | Crea el gráfico de barras de importancia | Altair |
| `st.altair_chart()` | Renderiza el gráfico dentro de la app | Streamlit |
| `st.caption()` | Muestra el pie de página con créditos | Streamlit |

---

## 🎨 5. Diseño de Interfaz

- **Encabezado:**  
  Título principal con emoji  para hacerlo más visual y amigable.  
- **Buscador:**  
  Caja de texto con ícono 🔍 e instrucciones.  
- **Resultados:**  
  Tabla interactiva con los conceptos coincidentes.  
- **Visualización:**  
  Gráfico de barras horizontales mostrando la importancia de cada concepto.  
- **Mensajes dinámicos:**  
  - `st.success` → Cuando hay resultados.  
  - `st.warning` → Cuando no hay coincidencias.  
  - `st.info` → Mensaje inicial (sin búsqueda).  
- **Pie de página:**  
  Línea divisoria y créditos del autor.

---

## 📊 6. Datos Utilizados

Los datos se definen como un diccionario dentro del código principal.  
Cada concepto incluye:

- **Palabra:** nombre del concepto.  
- **Importancia:** número (80–99) que indica su relevancia.  
- **Descripción:** definición corta y educativa.


```python
{
  "Palabra": "Inteligencia Artificial",
  "Importancia": 98,
  "Descripción": "Campo que busca que las máquinas imiten la inteligencia humana."
}

🔍 7. Funcionalidad de Búsqueda

El campo de texto st.text_input() permite ingresar una palabra o parte de ella.
El filtrado se realiza con Pandas:

df[df["Palabra"].str.contains(busqueda, case=False, na=False)]

    La búsqueda no distingue mayúsculas/minúsculas.

    Si hay resultados, se muestran en una tabla y un gráfico.

    Si no hay coincidencias, aparece un mensaje de advertencia.

📈 8. Visualización

    Tipo de gráfico: Barras horizontales.

    Ejes:

        X → Nivel de Importancia.

        Y → Nombre del Concepto.

    Color: Azul (#4b9cd3)

    Tooltip: muestra palabra, descripción e importancia.

    Tamaño: 600x300 px aprox.

🚀 9. Posibles Mejoras Futuras

    Cargar los datos desde un archivo CSV o base de datos externa.

    Agregar una opción para ordenar los conceptos por importancia.

    Permitir añadir nuevos términos desde la interfaz.

    Incluir categorías (por ejemplo: IA, redes, hardware, software).

    Añadir un gráfico comparativo general de todos los conceptos.

    Implementar un modo oscuro (dark mode).