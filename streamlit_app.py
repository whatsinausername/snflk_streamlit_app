import streamlit
import pandas 
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("My test streamlit's display")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.header('🥣 Breakfast Menu')

## Importing pandas and panda functios
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# display the table
streamlit.dataframe(fruits_to_show)

# create the repeatbale code block
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
  
###############
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
 
except URLError as e:
  streamlit.error()

streamlit.stop()



my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT* from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

fruit_add = streamlit.text_input('What fruit would you like to add')
streamlit.write('Thanks for adding', fruit_add)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")
