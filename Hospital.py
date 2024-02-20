import streamlit as st

import datetime
x=datetime.datetime.now()
st.write(x.strftime('%d-%b-%Y'))

import streamlit as st

# Define functions for each page
def page_home():
    st.title("Home Page")
    st.write("Welcome to the Home Page!")

def page_about():
    st.title("About Page")
    st.write("Welcome to the About Page!")

def page_contact():
    st.title("Contact Page")
    st.write("Welcome to the Contact Page!")

# Define a function to display navigation
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", options=["Home", "About", "Contact"])

    if page == "Home":
        page_home()

        # Title
        st.title("Hospital Management System")
        st.write('Expert in Medical Services')
        
        # Load image
        image = Image.open("hms.jpg")
        
        # Display image
        st.image(image, caption='Example Image', use_column_width=True)
    elif page == "About":
        page_about()
    elif page == "Contact":
        page_contact()

# Run the main function to start the app
if __name__ == "__main__":
    main()
 

st.write('A hospital management system was introduced with the cause of helping hospitals speed up their processes.')
st.write('What is Hospital Management System (HMS):')
st.write('The hospital management system is a computer system that helps manage the information related to healthcare and aids in the job completion of healthcare providers effectively. They manage the data related to all departments of healthcare such as,')
st.write('Clinical Management\n,Financial Management\n,Laboratory Management\n,Operation theater Management\n,Materials Management\n,Nursing Management\n,Pharmaceutical Management')
