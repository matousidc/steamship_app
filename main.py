from steamship import Steamship
import streamlit as st


st.set_page_config(
    page_title="Ericsson motivator",
    page_icon="🧊",
    initial_sidebar_state="auto",
    menu_items={
        # 'Get Help': 'https://www.extremelycoolapp.com/help',
        # 'Report a bug': "https://www.extremelycoolapp.com/bug",
        "About": "Made by https://github.com/matousidc!"
    },
)
st.title("Your personal Ericsson motivator to get you through loads")


def generate():
    name = "bob"
    trait = "autistic"
    # Invoke the method
    resp = pkg.invoke("generate", name=name, trait=trait)
    print(resp)


def generate_motivation(prompt):
    resp2 = pkg.invoke("generate_ericsson", _prompt=prompt)
    print(resp2)
    st.write(str(resp2))
    # st.markdown(str(resp2))
    # st.text_area(label='Response', value=resp2, height=150, label_visibility='collapsed')


# api_key="AB14DB2B-15A2-44B2-BB20-A351F8B7B1B5"
# Load the package instance stub.
pkg = Steamship.use("ericsson_motivator", instance_handle="ericsson_motivator-6if")

st.markdown("### What is bothering you today?")
text = st.text_input("# What is bothering you today?", label_visibility='collapsed')
st.markdown("### Response")
if text:
    generate_motivation(text)

