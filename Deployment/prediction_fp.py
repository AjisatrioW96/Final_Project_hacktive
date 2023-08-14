import streamlit as st
import pandas as pd
import numpy as np
import pickle
import tensorflow as tf
from PIL import Image

#model inferencing

with open ('pipeline.pkl' , 'rb') as file_10:
    pipeline = pickle.load(file_10)

model_functional_final = tf.keras.models.load_model('model_functional_final.h5')
model_functional_final.load_weights('best_model_weights.h5')



def run(): 
    st.write('#   ')
    background_color_3 = "#a66827"
    st.markdown(
                f"""
                <div style="background-color: {background_color_3}; padding: 10px; border-radius: 5px;">
                    <p><strong>This model prediction still needs to be improved in order to enhance its accuracy and reliability. While it provides valuable insights and predictions, it is essential to use the results with caution.</strong></p>
                </div>
                """,
                unsafe_allow_html=True
            )
    st.markdown('')
    with st.form('key=Form Prediction Churn Customer'):
        st.write ('### Fill out the Following:')

        gender_options = { 
            'Female': 'F', 'Male': 'M'
            }
        education_options = { 
            'High School': 'High School','Graduate': 'Graduate','Uneducated': 'Uneducated','Unknown': 'Unknown',
            'College': 'College','Post-Graduate': 'Post-Graduate','Doctorate': 'Doctorate'
            }
        marital_options = { 
            'Married': 'Married','Single': 'Single',
            'Unknown': 'Unknown','Divorced': 'Divorced'
            }
        income_options = { 
            '$60K - $80K': '$60K - $80K','Less than $40K': 'Less than $40K',
            '$80K - $120K': '$80K - $120K','$40K - $60K': '$40K - $60K','$120K +': '$120K +','Unknown': 'Unknown' 
            }
        card_options = { 
            'Blue': 'Blue','Gold': 'Gold','Silver': 'Silver','Platinum': 'Platinum'
            }


        Name = st.text_input('Tuliskan nama customer', 'Sarah')

        gender = st.selectbox('Apa Gender Customer yang anda cari ?', list(gender_options.keys()), index=0)
        gender_value = gender_options[gender]

        education = st.selectbox('Apa tingkat pendidikan Customer yang anda cari ?', list(education_options.keys()), index=0)
        education_value = education_options[education]

        marital_status = st.selectbox('Apa status pernikahan pelanggan yang anda cari ?', list(marital_options.keys()), index=0)
        marital_status_value = marital_options[marital_status]

        income_category = st.selectbox('Masuk dalam kategori pendapatan manakah pelanggan yang anda cari ?', list(income_options.keys()), index=0)
        income_category_value = income_options[income_category]

        card_category = st.selectbox('Apa jenis kartu yang digunakan oleh pelanggan yang anda cari ?', list(card_options.keys()), index=0)
        card_category_value = card_options[card_category]


        customer_age = st.slider("Berapa usia pelanggan?", min_value=18, max_value=100, value=30)
        dependent_count = st.number_input("Berapa jumlah dependen pelanggan?", min_value=0, max_value=5, value=1)
        months_on_book = st.slider("Berapa bulan pelanggan telah menjadi nasabah?", min_value=13, max_value=56, value=30)
        total_relationship_count = st.slider("Berapa total produk yang dipegang oleh pelanggan?", min_value=1, max_value=6, value=3)
        months_inactive_12_mon = st.slider("Berapa bulan tidak aktif dalam 12 bulan terakhir?", min_value=0, max_value=6, value=2)
        contacts_count_12_mon = st.slider("Berapa jumlah kontak dalam 12 bulan terakhir?", min_value=0, max_value=6, value=3)
        credit_limit = st.number_input("Berapa limit kredit di kartu kredit?", min_value=1000, max_value=50000, value=10000)
        total_revolving_bal = st.number_input("Berapa total saldo berputar di kartu kredit?", min_value=0, max_value=3000, value=1000)
        avg_open_to_buy = st.number_input("Berapa rata-rata kredit yang tersedia untuk pembelian?", min_value=0, max_value=50000, value=15000)
        total_amt_chng_q4_q1 = st.slider("Berapa perubahan jumlah transaksi (Q4 dibandingkan Q1)?", min_value=0, max_value=5, value=4)
        total_trans_amt = st.number_input("Berapa jumlah total transaksi dalam 12 bulan terakhir?", min_value=0, max_value=20000, value=5000)
        total_trans_ct = st.slider("Berapa jumlah total transaksi dalam 12 bulan terakhir?", min_value=0, max_value=200, value=50)
        total_ct_change_q4_q1 = st.slider("Berapa perubahan jumlah transaksi (Q4 dibandingkan Q1)?", min_value=0, max_value=5, value=2)
        avg_utilization_ratio = st.slider("Berapa rata-rata rasio pemanfaatan kartu?", min_value=0.0, max_value=1.0, value=0.5)

        submitted = st.form_submit_button('Predict')

        data_inf = {
                    'Customer_Age' : customer_age,
                    'Gender' : gender_value,
                    'Dependent_count' : dependent_count,
                    'Education_Level' : education_value,
                    'Marital_Status' :marital_status_value,
                    'Income_Category' : income_category_value,
                    'Card_Category' : card_category_value,
                    'Months_on_book' : months_on_book,
                    'Total_Relationship_Count' : total_relationship_count,
                    'Months_Inactive_12_mon' : months_inactive_12_mon,
                    'Contacts_Count_12_mon' : contacts_count_12_mon,
                    'Credit_Limit' : credit_limit,
                    'Total_Revolving_Bal' : total_revolving_bal,
                    'Avg_Open_To_Buy' : avg_open_to_buy,
                    'Total_Amt_Chng_Q4_Q1' : total_amt_chng_q4_q1,
                    'Total_Trans_Amt' : total_trans_amt,
                    'Total_Trans_Ct' : total_trans_amt,
                    'Total_Ct_Chng_Q4_Q1' : total_ct_change_q4_q1,
                    'Avg_Utilization_Ratio' : avg_utilization_ratio
                    }
        data_inf = pd.DataFrame([data_inf])



    if submitted: 
        #splitting data
        data_inf_transform = pipeline.transform(data_inf)
        y_pred_inf = model_functional_final.predict(data_inf_transform)
        background_color_1 = "#e63946"
        background_color_2 = "#3d85c6" 
        background_color_4 = "#70e000"
        
        if y_pred_inf == 1:
            st.write(f'###### Halo, berdasarkan dari model yang diberikan Customer dengan nama {Name} mempunyai : ')
            st.markdown(
                f"""
                <div style="background-color: {background_color_1}; padding: 10px; border-radius: 5px; ">
                    <p><strong>EXPECTED TO CHURN</strong></p>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.markdown('')
            st.markdown(
                f"""
                <div style="background-color: {background_color_2}; padding: 10px; border-radius: 5px;">
                    <p>The training file used for this prediction contains data for churn customers from Bank . The goal is to predict whether a customer is likely to churn. The dataset consists of approximately 10127 records with 21 features. The data serves as the training set for a machine learning model, which utilizes an Artificial Neural Network (ANN) with the architecture of Functional API. The model has achieved an precision about 0.84  in predicting whether a customer is likely to churn or not. However, it's important to acknowledge that even though the model exhibits a good precision , it may not be entirely flawless. There could be room for improvement and potential challenges to consider in its performance and predictions."</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.markdown('')
        else:
            st.write(f'###### Halo, berdasarkan dari model yang diberikan Customer dengan nama {Name} mempunyai : ')
            st.markdown(
                f"""
                <div style="background-color: {background_color_4}; padding: 10px; border-radius: 5px;">
                    <p><strong>LOW RISK OF CHURN</strong></p>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.markdown('')
            st.markdown(
                f"""
                <div style="background-color: {background_color_2}; padding: 10px; border-radius: 5px;">
                    <p>The training file used for this prediction contains data for churn customers from Bank . The goal is to predict whether a customer is likely to churn. The dataset consists of approximately 10127 records with 21 features. The data serves as the training set for a machine learning model, which utilizes an Artificial Neural Network (ANN) with the architecture of Functional API. The model has achieved an precision about 0.84  in predicting whether a customer is likely to churn or not. However, it's important to acknowledge that even though the model exhibits a good precision , it may not be entirely flawless. There could be room for improvement and potential challenges to consider in its performance and predictions."</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.markdown('')

    with st.expander("Click to see model explanation"):
        image = Image.open('feature_importance.png')
        st.image(image, caption='feature_importance')
        st.write(" From the results of the model's SHAP plot, it is evident that the most influential features in generating predictions are Total_trans_ct, Total_trans_Amt, and Total_revolving_bal. On the other hand, features with less impact include dependent count and education level. The 'Total_trans_ct' feature signifies the count of transactions performed by customers, reflecting their level of activity in using their credit cards. 'Total_trans_Amt' represents the total amount of money spent by customers in credit card transactions. Lastly, 'Total_revolving_bal' pertains to the overall unpaid balance from the previous month's bill.")



if __name__ == '__main__':
    run()





