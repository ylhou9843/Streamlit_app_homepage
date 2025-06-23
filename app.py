import streamlit as st

def main():

    st.set_page_config(page_title="MyCAF App Home")

    # Set the title of the homepage
    st.title("Welcome to MyCAF Apps")

    # Add a description
    st.write("Choose the app you want to explore:")

    st.link_button("Go to PDF Converter", "https://appapppdf2text-luxva4cpqg43dzjgrvbqvm.streamlit.app")
    st.link_button("Go to PIC Converter", "https://appapppic2text-vt37ckbzbrzc6vfc69fscc.streamlit.app")
    st.link_button("Go to Address Validator", "https://appaddrvalid-ilrcbsvbfneyxynvxmybvw.streamlit.app/")



# Call the main function to run the app
if __name__ == "__main__":
    main()
