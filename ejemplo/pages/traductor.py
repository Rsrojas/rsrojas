import streamlit as st
from translate import Translator

trad= Translator(
    from_lang= "english",
    to_lang="spanish")
st.title("Traductor de idiomas")
st.write("Este es un traductor de idiomas que puede traducir texto de inglés a español. Puedes escribir el texto que deseas traducir en")
txt=st.text_area("Escribe aca tu texto a traducir, maximo 500 caracters")
resultado=trad.translate(txt)
traduccion=st.text_area("Texto Traducido",resultado)
