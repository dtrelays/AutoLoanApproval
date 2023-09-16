import streamlit as st
import pandas as pd

from src.pipeline.predict_pipeline import CustomData,PredictPipeline


df_categorical_var = pd.read_csv('notebook/data/credit_data.csv')

gender = df_categorical_var['Gender'].unique().tolist()

df_state_city = df_categorical_var[['City', 'State']].drop_duplicates()

states = df_state_city['State'].unique().tolist()

df_categorical_var['Occupation'] = df_categorical_var['Occupation'].fillna('Others')

occupation_list = df_categorical_var['Occupation'].unique().tolist()

employment_type = df_categorical_var['Employment Profile'].unique().tolist()


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
    loan_tenure = st.slider("Select Loan Tenure in Years:",1,5)
    no_of_existing_loans = st.slider("Select No of Existing Loans:",0,6)
    
    credit_score = st.slider("Select Your Credit Score:",300,900)
    
    credit_history_length = st.slider("Select Your Credit History in Years:",0,30)
    
    existing_customer =  st.selectbox(f"Are You an Existing Bank Customer?", ['Yes','No'], index=0)

    selected_employment_type =  st.selectbox(f"Select Your Employment Type:", employment_type, index=0)

    selected_occupation =  st.selectbox(f"Select Your Occupation:", occupation_list, index=0)

    # Validation logic
    if loan_amount > bike_price:
        st.error("Error: Loan Amount cannot be greater than Bike Price")
        st.stop()

    # Submit button
    if st.button("Get Score"):
        
        data=CustomData(
            age = age,
            gender = selected_gender,
            income = income,
            credit_score = credit_score,
            credit_history_length = credit_history_length,
            no_of_existing_loans = no_of_existing_loans,
            loan_amount = loan_amount,
            loan_tenure = loan_tenure,
            existing_customer = existing_customer,
            state = selected_state,
            city = selected_city,
            employment_type = selected_employment_type,
            occupation = selected_occupation,
            bike_price = bike_price
        )
        
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        
        #line 104 is giving error, 

        print("Output from Model")        
        print(results)

        # Display the score
        st.write(f"Getting Your Profile Score, {name}")
        st.write(f"Your Score: {results[0]}")
        st.text("If the score is above 75, high chance of loan approval")
        
        st.text("We got your details, our team will reach out to you shortly if you are eligible")




    # Reset button
    if st.button("Reset"):
        # Clear all inputs and selections
        st.experimental_rerun()

    
if __name__=="__main__":
    main()
