import streamlit as st

def mad_libs_story(adjective, noun, verb):
    return f"Once upon a time, there was a {adjective} {noun} that loved to {verb}."

def main():
    st.title("Mad Libs Game")
    
    # User inputs
    adjective = st.text_input("Enter an adjective:")
    noun = st.text_input("Enter a noun:")
    verb = st.text_input("Enter a verb:")
    
    if st.button("Generate Story"):
        if adjective and noun and verb:
            story = mad_libs_story(adjective, noun, verb)
            st.write(story)
        else:
            st.write("Please fill in all fields.")

    # Provide Google Colab URL
    st.write("You can also run this project in [Google Colab](https://colab.research.google.com/).")

if __name__ == "__main__":
    main()
