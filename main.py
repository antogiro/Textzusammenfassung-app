import streamlit as st
from transformers import pipeline

summarizer = pipeline(task='summarization', model='t5-small', tokenizer='t5-small')


def main():
    st.title("Text Zusammenfassungs-App")

    # Eingabefeld für Benutzertext
    user_input = st.text_area("Geben Sie Ihren Text ein:")

    if st.button("Zusammenfassen"):
        if user_input:
            # Zusammenfassung generieren
            summary = summarizer(user_input, max_length=100, min_length=30, do_sample=False)
            st.success(summary[0]['summary_text'])
        else:
            st.warning("Bitte geben Sie einen Text ein, den Sie zusammenfassen möchten.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

