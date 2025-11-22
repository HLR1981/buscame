"""
=========================================================
                PRESENTACIÓN DEL PROYECTO
=========================================================

Nombre del estudiante: Hilario Jimenez Victoriano
Matrícula: 22760839
Profesor: Guillermo Alejandro Chávez Sánchez
Materia: Programación Lógica
Fecha: Noviembre 2025

Nombre del proyecto:
"Analizador de conceptos de computación con Streamlit"

Descripción:
Este programa permite buscar conceptos clave relacionados
con el tema de la computación y analizar textos para detectar
palabras asociadas. Utiliza Streamlit para generar una interfaz
interactiva, Pandas para organizar los datos y Altair para
construir gráficos que muestran la importancia de cada concepto.
El analizador identifica coincidencias con las palabras definidas
y presenta resultados visuales claros y fáciles de interpretar.

=========================================================
"""

import streamlit as st
import pandas as pd
import altair as alt
import re

# ===============================
# CONFIGURACIÓN DE LA PÁGINA
# ===============================
st.set_page_config(
    page_title="Conceptos de Computación",
    page_icon="💻",
    layout="wide"
)

st.title("💻 Conceptos Clave de la Computación")
st.caption("Aplicación interactiva desarrollada con Streamlit — Datos cargados desde archivo CSV")

# ===============================
# CARGA DE DATOS EXTERNOS
# ===============================
@st.cache_data
def cargar_datos():
    df = pd.read_csv("conceptos.csv")
    return df

df = cargar_datos()

# ===============================
# SIDEBAR
# ===============================
st.sidebar.title("Opciones")
vista = st.sidebar.radio(
    "Selecciona vista:",
    ["Buscador", "Análisis de texto", "Listado completo"]
)

st.sidebar.info("Los datos provienen del archivo **conceptos.csv**")

# ===============================
# VISTA 1: BUSCADOR
# ===============================
if vista == "Buscador":
    st.subheader("🔍 Buscador de conceptos")
    busqueda = st.text_input("Escribe algo para buscar:", "")

    if busqueda:
        resultados = df[df["Palabra"].str.contains(busqueda, case=False, na=False)]

        if not resultados.empty:
            st.success(f"{len(resultados)} resultados encontrados")

            for _, row in resultados.iterrows():
                with st.container(border=True):
                    st.markdown(f"## {row['Palabra']}")
                    col1, col2 = st.columns([1, 3])
                    with col1:
                        st.image(row["Imagen"], width=120)
                    with col2:
                        st.write(row["Descripción"])
                        st.progress(row["Importancia"] / 100)

            st.subheader("📊 Importancia de conceptos encontrados")
            chart = alt.Chart(resultados).mark_bar().encode(
                x="Importancia:Q",
                y=alt.Y("Palabra:N", sort="-x"),
                tooltip=["Palabra", "Importancia"]
            ).properties(height=300)

            st.altair_chart(chart, use_container_width=True)

        else:
            st.warning("No se encontraron coincidencias.")

# ===============================
# VISTA 2: ANÁLISIS DE TEXTO
# ===============================
elif vista == "Análisis de texto":
    st.subheader("📝 Análisis de texto automático")

    texto_usuario = st.text_area("Escribe o pega tu texto:", height=200)

    if st.button("Analizar"):
        if texto_usuario.strip():
            texto_limpio = texto_usuario.lower()

            coincidencias = []
            for palabra in df["Palabra"]:
                palabra_limpia = re.sub(r"[^a-zA-Záéíóúüñ ]", "", palabra.lower())
                if re.search(r"\b" + palabra_limpia + r"\b", texto_limpio):
                    coincidencias.append(palabra)

            if coincidencias:
                st.success(f"Encontré {len(coincidencias)} conceptos.")
                st.write(", ".join(coincidencias))

                chart = alt.Chart(df[df["Palabra"].isin(coincidencias)]).mark_bar().encode(
                    x="Importancia:Q",
                    y=alt.Y("Palabra:N", sort="-x"),
                    tooltip=["Palabra", "Importancia"]
                )
                st.altair_chart(chart, use_container_width=True)

            else:
                st.warning("No encontré conceptos en tu texto.")

        else:
            st.error("El texto está vacío.")

# ===============================
# VISTA 3: LISTADO COMPLETO
# ===============================
else:
    st.subheader("📚 Lista completa de conceptos")

    for _, row in df.iterrows():
        with st.expander(f"{row['Palabra']} — ({row['Importancia']}%)"):
            col1, col2 = st.columns([1, 4])
            with col1:
                st.image(row["Imagen"], width=100)
            with col2:
                st.write(row["Descripción"])


