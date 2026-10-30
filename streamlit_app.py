import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

import requests

# GET data for Pikachu
url = "https://pokeapi.co/api/v2/pokemon/pikachu"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Name: {data['name'].capitalize()}")
    print(f"Height: {data['height']}")
    print(f"Weight: {data['weight']}")
    
    # Extracting abilities from a nested list
    abilities = [item['ability']['name'] for item in data['abilities']]
    st.write(str(abilities))

st.write("Hi this is new edit")
    print(f"Abilities: {abilities}")
