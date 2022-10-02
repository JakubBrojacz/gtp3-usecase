import streamlit as st
from model_training_service import Code


pred = Code()

st.set_page_config(layout="wide", page_icon="🎓",
                   page_title="Personal Profile Generator")
st.title("🎓 Personal Profile Generator")

st.write(
    "This app allows you to generate personal profile for your CV based on you experience and supplied keywords."
)
api_key = st.sidebar.text_input("OpenAI API Key:", type="password")


@st.cache
def process_prompt(input):
    return pred.model_prediction(input=input, api_key=api_key)


@st.cache
def get_sample_input():
    with open("sample_input.txt", 'r') as f:
        sample_input = f.read()
    return sample_input


if api_key:
    left, right = st.columns(2)

    left.write("Let us know about your professional experience")
    form = left.form("template_form")

    student = form.text_area(
        "Fill in the data:", value=get_sample_input(), height=200)
    submit = form.form_submit_button("Submit")

    right.write("Result:")

    if submit:
        right.write(process_prompt(student))
