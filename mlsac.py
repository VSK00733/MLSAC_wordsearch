import streamlit as st
from PIL import Image
st.set_page_config(page_title="WORD SEARCH")
st.header("WORD SEARCH")
st.write('''Hello there! Welcome to this word search!
The rules are pretty simple. The following word search has 10 words related to MLSAC,
technology and related things. One word in particular hints to a BIG THING coming up.
You have to guess what that word is. If you are correct, you will get a sneak-peak of the BIG THING coming up!
Sounds exciting, doesn't it? So let's begin!!''')
image=Image.open("mlsac.jpg")
st.image(image,caption="Word search")
p=0

z = st.empty()  #for single element container

while p==0:
    x=z.text_input("Enter the word you think is the correct answer!")
    if x.lower()=="https":
        z.write('''Congratulations! You guessed it right!
        \n
        ''')
        st.balloons()
        st.write(f'''
        <a href="https://bit.ly/MLSAC_Surprise">
        <button style="border:none; background:#0093f4; color:white; width:215px; height:40px; border-radius:24px; font-weight:600; box-shadow:inset 0 0 12px #01010e;">
            Click here for the Surprise!
        </button>
        </a>
        ''',
        unsafe_allow_html=True
        )
    elif x=="":
        pass
    else:
        z.write('''Oh, incorrect answer.... No problemo! Stay tuned to our instagram for 
        further updates!''')
    p=1
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
body {color: white; background-color: blue;}
</style>


"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
