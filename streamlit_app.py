
import streamlit

streamlit.title("My Parents New health Diner")

streamlit.header("Breakfast Menu")

streamlit.text("🥣Omega 3 & Blueberry Oatmeal")

streamlit.text("Kale, Spinach & Rocket Smoothie")

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fuit_list)
