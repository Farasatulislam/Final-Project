
# Network:1
import streamlit as st

# Network:2
# Header is given
st.header("Hospital Managment System")
st.write('Expert in Medical Services:heartbeat:')

# Network:3
# Navigation bar on top
# Function definitions for different pages
def render_home():
    st.write("Welcome to the Home Page!")

def render_about():
    st.write("Learn more about us here.")

def render_contact():
    st.write("Contact us via email at contact@example.com.")

def render_patient():
    st.write("Patients Records.")

# Initialize session state variables for navigation
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Define a function to handle navigation
def navigate(page):
    st.session_state.page = page


# Layout for the top navigation bar using columns
col1, col2, col3, col4 = st.columns(4)

    # Network:4
# Divider b/w header & body
# Simple HTML to create a colored line
rainbow_html = """
<div style='height: 3px; background: linear-gradient(90deg, rgba(255,0,0,1) 0%, rgba(255,154,0,1) 10%, rgba(208,222,33,1) 20%, rgba(79,220,74,1) 30%, rgba(63,218,216,1) 40%, rgba(47,201,226,1) 50%, rgba(28,127,238,1) 60%, rgba(95,21,242,1) 70%, rgba(186,12,248,1) 80%, rgba(251,7,217,1) 90%, rgba(255,0,0,1) 100%);'>
</div>
"""
st.markdown(rainbow_html, unsafe_allow_html=True)

with col1:
    # Use the button's "on_click" to change the page state
    if st.button("Home"):
        navigate('home')

with col2:
    if st.button("About"):
        navigate('about')

with col3:
    if st.button("Contact"):
        navigate('contact')

with col4:
    if st.button("Patient"):
        navigate('patient')


# Conditional rendering based on the current page
if st.session_state.page == 'home':
    render_home()
    # Network:5
    # image example
    import streamlit as st
    from PIL import Image

    # Load image
    image = Image.open("hms.jpg")

    # Display image
    st.image(image, caption='Example Image', use_column_width=True)

elif st.session_state.page == 'about':
    render_about()
elif st.session_state.page == 'contact':
    render_contact()
elif st.session_state.page == 'patient':
    render_patient()
# Network:
    # Patients entry
    import sqlite3

    # Function to create a database connection
    def create_connection(db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except sqlite3.Error as e:
            st.error(e)
        return conn

    # Function to create a table in the database
    def create_table(conn):
        try:
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS records (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL
                        )''')
        except sqlite3.Error as e:
            st.error(e)

    # Function to insert a record into the database
    def insert_record(conn, name):
        try:
            c = conn.cursor()
            c.execute("INSERT INTO records (name) VALUES (?)", (name,))
            conn.commit()
            st.success(f"Record '{name}' added successfully!")
        except sqlite3.Error as e:
            st.error(e)

    # Function to remove a record from the database
    def remove_record(conn, id):
        try:
            c = conn.cursor()
            c.execute("DELETE FROM records WHERE id=?", (id,))
            conn.commit()
            st.success("Record removed successfully!")
        except sqlite3.Error as e:
            st.error(e)

    # Main function to run the app
    def main():
        st.title(" Patients Record")

        # Create a database connection
        conn = create_connection("example.db")

        if conn is not None:
            create_table(conn)

            # Add record section
            st.header("Add Record")
            new_name = st.text_input("Enter name to add:")
            if st.button("Add"):
                if new_name:
                    insert_record(conn, new_name)
                else:
                    st.warning("Please enter a name.")

            # Remove record section
            st.header("Remove Record")
            record_id = st.text_input("Enter ID of record to remove:")
            if st.button("Remove"):
                if record_id:
                    remove_record(conn, record_id)
                else:
                    st.warning("Please enter the ID of the record.")

            # Display existing records
            st.header("Existing Records")
            c = conn.cursor()
            c.execute("SELECT * FROM records")
            records = c.fetchall()
            for record in records:
                st.write(f"ID: {record[0]}, Name: {record[1]}")

            conn.close()
        else:
            st.error("Error: Unable to create database connection.")

    if __name__ == "__main__":
        main()



#st.header ("abc",divider ='rainbow')

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://banoqabil.pk" target="_blank">Bano Qabil Alkhidmat </a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
