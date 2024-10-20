import streamlit as st
import time


def read_mind() -> None:
  """
  This function reads mind.. :)
  """

  st.title("Mind Reader :crystal_ball:")
  st.header("Let's read your mind... :bulb:")
  
  with st.form("mind_reader_form"):
    fav_dish = None
    num = st.number_input("Think of a number between 1-100...", max_value=100, step=1)
    if 1 <= num <= 100:
      fav_dish = st.text_input("What's your favorite dish? :yum:")

    submitted = st.form_submit_button("Go")
  if submitted and num and fav_dish:
    action(num, fav_dish)
  

def action(num: int, fav_dish: str) -> None:
  """
  Processes the inputs.
  """
  sleep_time = 1.5
  with st.empty():
    st.info("Making connections with your mind...")
    time.sleep(sleep_time)
    
    st.info("Analysing your thoughts...")
    time.sleep(sleep_time)
    
    st.info("Almost there...")
    time.sleep(sleep_time)
    
    st.info("Okay! I am ready now...")
    time.sleep(sleep_time)

    st.info(f"You were thinking about the number {num} and your favorite dish is {fav_dish}... :sunglasses:")

  st.balloons()
  with open("query_count.txt", "r+") as file:
    count = file.read()
    if not count:
      count = 0
      st.write(f"first time: {count}")
    else:
      st.write(f"next time: {count}")
      count = int(count)
    file.write(str(count + 1))


if __name__ == "__main__":
  read_mind()
