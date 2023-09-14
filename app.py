import streamlit as st
import pandas as pd


df_categorical_var = pd.read_csv('notebook/data/credit_data.csv')

gender = df_categorical_var['Gender'].unique().tolist()

df_state_city = df_categorical_var[['City', 'State']].drop_duplicates()

states = df_state_city['State'].unique().tolist()

df_categorical_var['Occupation'] = df_categorical_var['Occupation'].fillna('Others')

occupation_list = df_categorical_var['Occupation'].unique().tolist()


def main():

     
    # Title
    st.title("2W Loan Mela")

    # Set a background color
    
    html_temp = """
    <div style="background-color:#f0f0f0;padding:10px">
    <h2 style="color:black;text-align:center;"> 2W Loan Approval Scoring App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    

    # Input fields 
    st.header("Fill the below Form to get your 2W Loan Score")
    
    # Dropdowns
    dropdown_states = states
     
    name = st.text_input("Enter Your Name:","Type Here")
    contact_number = st.text_input("Enter Your Mobile No:","Type Here")
        
    selected_gender =  st.selectbox(f"Select Gender:", gender, index=0)

    age = st.number_input("Enter Your Age",18,75)
    
    selected_state = st.selectbox(f"Select State:", dropdown_states, index=0)

    city_list = df_state_city[df_state_city['State'] == selected_state]['City'].unique().tolist()

    selected_city =  st.selectbox(f"Select City:", city_list, index=0)
 
    income = st.slider("Select Your Income",15000,300000)
    bike_price = st.number_input("Enter Two Wheeler On Road Price",0,350000)
    loan_amount = st.number_input("Enter Loan Amount Required",20000,300000)
    
    existing_customer =  st.selectbox(f"Are You an Existing Bank Customer?", ['Yes','No'], index=0)
    
    selected_occupation =  st.selectbox(f"Select Your Occupation:", occupation_list, index=0)

    # Submit button
    if st.button("Get Score"):
        # Perform actions here based on user input
        st.write("Getting Your Profile Score, "+name)
        st.text("If the score is above 75, high chance of loan approval")

    # Reset button
    if st.button("Reset"):
        # Clear all inputs and selections
        st.experimental_rerun()

    # Footer
    st.text("We got your details, our team will reach out to you shortly if you are eligible")

if __name__=="__main__":
    main()
