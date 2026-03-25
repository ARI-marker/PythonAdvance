import streamlit as st

# def main():
#     st.title("Hello world")
#
#     st.button("Click me")
#
#
#
# if __name__ == "__main__":
#     main()

if st.button("Click me"):
    st.write("Button clicked")

st.checkbox("Check me")


if st.checkbox("check to show some text"):
    st.write("some text")


user_input = st.text_input("Enter text" , "Sample text")

st.write("You enterd: " , user_input)

age = st.number_input("Enter age: " , min_value=0 , max_value=100)

st.write(f"Your age is: {age}")

message = st.text_area("Enter a message")

choice = st.radio("Pick one", ["1" , "2" , "3"])

st.write(f"Your choice is : {choice}")

if st.button("Success"):
    st.success("Operation was succesful")



try:
    1/0
except Exception as e:
    st.exception(e)