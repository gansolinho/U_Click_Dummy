import streamlit as st

# Konfiguration festlegen
st.set_page_config(
    page_title="After Sales",
    page_icon="📤",
)

# Logo
st.logo('images/logos/Uvex_logo.svg', size='large', icon_image='images/logos/uvex_logo_black.svg')

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