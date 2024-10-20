import streamlit as st
import time


def read_mind() -> None:
  """
  This function reads mind.. :)
  """

  st.title("Mind Reader")
  st.header("Let's read your mind... :bulb:")

  submitted = False
  num_inp = None
  fav_dish_inp = None
  with st.form("mind_reader_form"):
    num = st.number_input("Think of a number between 1-100...", max_value=100, step=1)
    if 1 <= num <= 100:
      fav_dish = st.text_input("What's your favorite dish? :yum:")

    submitted = st.form_submit_button("Go")
    if submitted and num and fav_dish:
      num_inp = num
      fav_dish_inp = fav_dish
  
  if num_inp and fav_dish_inp:
    action(num_inp, fav_dish_inp)

def action(num: int, fav_dish: str) -> None:
  """
  Processes the inputs.
  """
  sleep_time = 1.5
  with st.empty():
    # msg = st.toast("Making connections with your mind...")
    st.info("Making connections with your mind...")
    time.sleep(sleep_time)
    # msg.toast("Analysing your thoughts...")
    st.info("Analysing your thoughts...")
    time.sleep(sleep_time)
    # msg.toast("Almost there...")
    st.info("Almost there...")
    time.sleep(sleep_time)
    # msg.toast("Okay! I am ready now...")
    st.info("Okay! I am ready now...")
    time.sleep(sleep_time)

    st.info(f"You were thinking about the number {num} and your favorite dish is {fav_dish}... :sunglasses:")

  st.balloons()


if __name__ == "__main__":
  read_mind()
