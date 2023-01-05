import streamlit
import pandas 

streamlit.title("My test streamlit's display")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.header('🥣 Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('🥑 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🍞 Hard-Boiled Free-Range Egg')

streamlit.header('\N{flexed biceps} Breakfast of Champion Coders \N{flexed biceps}')

## Importing pandas and panda functios
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')



# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# display the table
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.text(fruityvice_normalized)
streamlit.dataframe(fruityvice_normalized)
