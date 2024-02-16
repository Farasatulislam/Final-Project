import streamlit as st

import datetime
x=datetime.datetime.now()
st.write(x.strftime('%d-%b-%Y'))

 # image example
import streamlit as st
from PIL import Image

# Title
st.title("Hospital Management System")
st.write('Expert in Medical Services')

# Load image
image = Image.open("hms.jpg")

# Display image
st.image(image, caption='Example Image', use_column_width=True)


st.write('A hospital management system was introduced with the cause of helping hospitals speed up their processes.')
st.write('What is Hospital Management System (HMS):')
st.write('The hospital management system is a computer system that helps manage the information related to healthcare and aids in the job completion of healthcare providers effectively. They manage the data related to all departments of healthcare such as,')
st.write('Clinical Management\n,Financial Management\n,Laboratory Management\n,Operation theater Management\n,Materials Management\n,Nursing Management\n,Pharmaceutical Management')
