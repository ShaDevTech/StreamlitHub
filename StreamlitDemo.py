# import core package
import streamlit as st

# import image library
from PIL import Image

# create a global variable to store user creds
user_cred = {
    "user" : "user",
    "admin" : "admin",
    "test" : "test"
}

def sign_in():
    # user a container to hold page content
    with st.container():
        # add a title
        st.title("Sign In")

        # ask for username and password
        username = st.text_input("Username")
        password = st.text_input("Password", type = 'password')

        if st.button("Log In"):
            # check if username and password are in the system
            if username in user_cred and password == user_cred[username]:
                st.session_state['username'] = username
                st.success(f" You have logged in successfully {username}")
                home()
            else:
                st.error("Invalid username or password")

def home():
    # use container to hold page content
    with st.container():

        # add pages
        menu = ['Sign In', 'Home','Projects','About']

        # buttons specs
        menu_items = [
            (1,1,1), # sign in button
            (1,1,1), # home button
            (1,1,1), # projects button
            (1,1,1) , # about button
        ]

        menu_selected = []

        for i, choice in enumerate(menu):
            col1, _, col2 = st.sidebar.columns(menu_items[i])
            which_menu_selected = st.sidebar.button(choice)
            menu_selected.append(which_menu_selected)

        # create a sign out button
        if st.sidebar.button("Sign Out"):
            st.session_state.pop("username")
            # take user to sign in page
            sign_in()

        # create a button to go back to home page
        if 'page' in st.session_state:
            if st.session_state['page'] == 'about':
                if st.button("Back to HOME page"):
                    st.session_state.pop('page', None)
                    home()
            if st.session_state['page'] == 'projects':
                if st.button("Back to HOME page"):
                    st.session_state.pop('page', None)
                    home()


        # assign actions to buttons
        if menu_selected[0]:
            sign_in()
        elif menu_selected[1]:
            st.title("Home Page")
            st.write("Welcome " + st.session_state['username'])
        elif menu_selected[2]:
            projects()
        elif menu_selected[3]:
            about()

def projects():
    # create container
    with st.container():
        # add a back button
        if st.button("Back to HOME page"):
            home()
        st.title("Projects Status")

        tab1, tab2 = st.tabs(['Case Studies','Leaders Outlook'])
        with tab1:
            case_studies()
        with tab2:
            leaders_outlook()

def case_studies():

    with st.container():
        image_path = Image.open("C:\\Users\\SHARM\\Downloads\\What-is-a-Business-Case-Study-and-How-to-Write-with-Examples-min.png")
        st.image(image_path)
def leaders_outlook():
    with st.container():
        image_path = Image.open("C:\\Users\\SHARM\\Downloads\\colinpowell1.jpg")
        st.image(image_path)




def about():
    # create container
    with st.container():
        # add a back button
        if st.button("Back to HOME page"):
            home()

        # write title of the page
        st.title("About")

        # add an image with bio
        col1,col2 = st.columns([4,2])
        with col1:
            image_path = Image.open("C:\\Users\\SHARM\Pictures\\Screenshots\\Screenshot 2023-03-25 181211.png")
            st.image(image_path, use_column_width=True)
        with col2:
            st.write("Hi, This is Deepak")


def main():
    # set page configuration
    st.set_page_config(page_title ="My streamlit App Login and mutiple pages")

    # initialize session state
    session_state = st.session_state

    # if user has logged in past , take them to home page otherwise ask them to sign in
    if 'username' not in st.session_state:
        sign_in()
    else:
        home()

if __name__ =='__main__':
    main()