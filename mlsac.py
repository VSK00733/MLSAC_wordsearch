import streamlit as st
from PIL import Image
st.set_page_config(page_title="WORD SEARCH")
st.header("WORD SEARCH")
st.write('''Hello there! Welcome to this word search!
The rules are pretty simple. The following word search has 10 words related to MLSAC,
technology and related things. One word in particular hints to a BIG THING coming up.
You have to guess what that word is. If you are correct, you will get selected 
under the Early Bird Offer and will get a sneak-peak of the BIG THING coming up!
Sounds exciting, doesn't it? So let's begin!!''')
image=Image.open("mlsac.jpg")
st.image(image,caption="Word search")
p=0
while p==0:
    x=st.text_input("Enter the word you think is the correct answer!")
    if x=="HTTPS" or x=="https" or x=="Https":
        st.write('''Congratulations! You guessed it right!
        So, as promised, here is the sneak-peak!
        ''')
        st.balloons()
    elif x=="":
        pass
    else:
        st.write('''Oh, incorrect answer.... No problemo! Stay tuned to our instagram for 
        further updates!''')
    p=1
