import streamlit as st

st.set_page_config(page_title="Legal Vino Tinto", layout="wide")

st.title("Asistente Legal Vino Tinto")
st.write("Bienvenido a tu asistente legal especializado en Derecho Ecuatoriano.")

consulta = st.text_area("Escribe tu consulta legal aquí:")

if st.button("Consultar"):
    if consulta.strip() == "":
        st.warning("Por favor, escribe una consulta.")
    else:
        # Aquí irá la lógica futura de la IA legal
        st.success("Respuesta automática: (Aquí se generará la respuesta legal con IA).")
