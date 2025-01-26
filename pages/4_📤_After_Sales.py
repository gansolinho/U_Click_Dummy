import streamlit as st

# Konfiguration festlegen
st.set_page_config(
    page_title="After Sales",
    page_icon="📤",
)

# Logo
st.logo('https://drive.google.com/file/d/1hC30Wa2Shvi10T3yem47BW_0umoO0T_Q/view?usp=drive_link', size='large', icon_image='https://drive.google.com/file/d/1IWrUNlSQzwpZla-3ycj9drekRTIb9pfM/view?usp=drive_link')

# Page-Überschrift
st.write("# After Sales 📤")

# Tabs aufmachen
tab1, tab2, tab3 = st.tabs(["Service", "🔒 Second-Hand", "🔒 Reparatur"])

# Tab 1: Service
with tab1:
    # Überschrift: Reklamation
    st.write("#### Reklamation")

    # Überschrift: Freischaltung erweiterte Garantie
    st.write("#### Freischaltung erweiterte Garantie")

# Tab 2: Second-Hand
with tab2:
    # Überschrift: Eingabe Daten zum Weiterverkauf
    st.write("#### Daten zum Weiterverkauf")

# Tab 3: Reparatur
with tab3:
    st.write("#### Informationen zu durchgeführten Reparaturen")
