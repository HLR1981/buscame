import streamlit as st
import pandas as pd
import altair as alt

# Configuración de la página
st.set_page_config(page_title="Computación 💻", layout="centered", page_icon="💡")

st.title("💻 Conceptos Clave de la Computación")

# Datos: palabras, ponderación y descripción
data = {
    "Palabra": [
        "Programación", "Algoritmo", "Inteligencia Artificial", "Base de Datos",
        "Redes", "Ciberseguridad", "Hardware", "Software", "Computación en la Nube",
        "Machine Learning", "Blockchain", "Sistemas Operativos", "Big Data",
        "Realidad Virtual", "Computación Cuántica"
    ],
    "Importancia": [95, 90, 98, 88, 85, 92, 80, 84, 89, 97, 91, 83, 86, 82, 99],
    "Descripción": [
        "Proceso de crear programas mediante lenguajes de programación.",
        "Conjunto de pasos lógicos para resolver un problema.",
        "Campo que busca que las máquinas imiten la inteligencia humana.",
        "Colección estructurada de información que puede consultarse fácilmente.",
        "Conjunto de dispositivos conectados para compartir recursos y datos.",
        "Protege sistemas y datos contra accesos o ataques no autorizados.",
        "Parte física de una computadora: CPU, RAM, discos, etc.",
        "Parte lógica de una computadora: programas y aplicaciones.",
        "Uso de servidores remotos para almacenar y procesar datos en línea.",
        "Subcampo de la IA que permite a las máquinas aprender de datos.",
        "Tecnología que garantiza transacciones seguras y descentralizadas.",
        "Programa que gestiona los recursos y procesos de una computadora.",
        "Análisis de grandes volúmenes de datos para obtener información útil.",
        "Tecnología que crea entornos digitales inmersivos.",
        "Rama avanzada que usa principios cuánticos para procesar información."
    ]
}

# Convertimos a DataFrame
df = pd.DataFrame(data)

# --- Buscador ---
st.subheader("🔍 Buscador de conceptos")
busqueda = st.text_input("Escribe una palabra o parte de ella para buscar:", "")

if busqueda:
    resultados = df[df["Palabra"].str.contains(busqueda, case=False, na=False)]
    if not resultados.empty:
        st.success(f"Se encontraron {len(resultados)} coincidencias:")
        st.dataframe(resultados)

        # --- Gráfico filtrado ---
        st.subheader("📊 Nivel de importancia del concepto buscado")
        chart = (
            alt.Chart(resultados)
            .mark_bar(color="#4b9cd3")
            .encode(
                x=alt.X("Importancia:Q", title="Nivel de Importancia"),
                y=alt.Y("Palabra:N", sort="-x", title="Concepto"),
                tooltip=["Palabra", "Descripción", "Importancia"]
            )
            .properties(width=600, height=300)
        )
        st.altair_chart(chart, use_container_width=True)
    else:
        st.warning("No se encontraron coincidencias con esa palabra.")
else:
    st.info("Escribe algo para comenzar la búsqueda. 👆")

# Pie de página
st.markdown("---")
st.caption("Aplicación desarrollada en Streamlit — Tema: Computación 💻")
