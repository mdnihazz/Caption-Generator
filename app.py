import streamlit as st 
from dill import dump, load
from PIL import Image
st.subheader('Hello User 👋')
st.write('Do you Want to know what your image is all about.....')
st.write('Then check me out')
st.subheader('I am......')
st.title('Image Captioner 📸💬🔡')
st.header('So, What do I do?')
st.write("I will examine your *picture* very carefully 🔎, then tell *YOU* what's there in it")
st.write('Pretty Cool right!!😎')
st.subheader('So, What you have to do?')
st.write('Not so Much.....')
st.write("Just give me an image🖼️ and see how cool I am😎.....")

uploaded_file = st.file_uploader('Show me the Image',type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
model = load(open('model.pkl','rb'))

feature_extractor = load(open('feature_extractor.pkl','rb'))

tokenizer = load(open('tokenizer.pkl','rb'))

device = load(open('device.pkl','rb'))


gen_caption = load(open('gen_caption.pkl','rb'))

caption_0 = load(open('caption_0.pkl','rb'))

caption_1 = load(open('caption_1.pkl','rb'))

caption_2 = load(open('caption_2.pkl','rb'))

image = uploaded_file

result_placeholder = st.empty()

if uploaded_file is not None:
    
    tab1, tab2, tab3 = st.tabs(["Caption1", "Caption2", "Caption3"])

    with tab1:
        st.subheader('My AI brain says🤔 ...')
        with st.spinner('It is a Picture of'):
                caption_fn = caption_0
                result = caption_fn(image)
                st.subheader(result)
                
                
    with tab2:
        st.subheader('My AI brain says🤔 ...')
        with st.spinner('It is a Picture of'):
                caption_fn_1 = caption_1
                result_1 = caption_fn_1(image)
                st.subheader(result_1)
                
                
    with tab3:
        st.subheader('My AI brain says🤔 ...')
        with st.spinner('It is a Picture of'):
                caption_fn_2 = caption_2
                result_2 = caption_fn_2(image)
                st.subheader(result_2)

