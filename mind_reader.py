import streamlit as st
import time


def read_mind() -> None:
  """
  This function reads mind.. :)
  """

  st.title("Mind Reader")
  st.header("Let's read your mind... :bulb:")

  with st.form("mind_reader_form"):
    
    fav_dish = None
    st.write("Think of a number between 1-100 and I will read your thoughts...")
    num = st.number_input("Think of a number between 1-100...", min_value=1, max_value=100, step=1)
    if num:
      fav_dish = st.text_input("What's your favorite dish? :yum:")

    submitted = st.form_submit_button("Go")
    if submitted and num and fav_dish:
        action(num, fav_dish)

def action(num: int, fav_dish: str) -> None:
  """
  Processes the inputs.
  """
  msg = st.toast("Making connections with your mind...")
  time.sleep(1)
  msg.toast("Analysing your thoughts...")
  time.sleep(1)
  msg.toast("Almost there...")
  time.sleep(1)
  msg.toast("Analysing your thoughts...")
  time.sleep(1)
  msg.toast("Okay! I am ready now...")
  time.sleep(1)

  msg.toast(f"You were thinking about the number: {num} and your favorite dish is: {fav_dish}... :sunglasses:")

  st.balloons()


if __name == "__main__":
  read_mind()
