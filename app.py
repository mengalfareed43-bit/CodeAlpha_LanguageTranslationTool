import streamlit as st
from googletrans import Translator, LANGUAGES

# Page configuration
st.set_page_config(page_title="CodeAlpha - Language Translation Tool", page_icon="🌐", layout="centered")

translator = Translator()

# App Header
st.title("🌐 CodeAlpha AI Internship")
st.subheader("Task 1: Language Translation Tool")
st.write("Enter text below, select the source and target languages, and get instant translation!")

# Input text box
text_to_translate = st.text_area("Enter Text to Translate:", placeholder="Yahan apna text likhein...")

# Language selection dictionaries
language_names = {name.capitalize(): code for code, name in LANGUAGES.items()}
sorted_languages = sorted(language_names.keys())

col1, col2 = st.columns(2)

with col1:
    src_lang_name = st.selectbox("Source Language", sorted_languages, index=sorted_languages.index('English'))

with col2:
    dest_lang_name = st.selectbox("Target Language", sorted_languages, index=sorted_languages.index('Urdu'))

src_code = language_names[src_lang_name]
dest_code = language_names[dest_lang_name]

# Translate Button
if st.button("Translate Now", type="primary"):
    if text_to_translate.strip() != "":
        try:
            # Performing translation
            translation = translator.translate(text_to_translate, src=src_code, dest=dest_code)
            
            st.success("Translation Successful!")
            st.markdown("### Translated Text:")
            st.info(translation.text)
            
        except Exception as e:
            st.error(f"Error aa gaya: {e}")
    else:
        st.warning("Pehle kuch text toh enter karein!")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>Developed with ❤️ for CodeAlpha Internship</p>", unsafe_allow_html=True)
