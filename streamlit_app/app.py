import streamlit as st
import pandas as pd
import joblib


# CONFIGURACION PAGINA


st.set_page_config(page_title="Bank Marketing App", layout="centered")

col1, col2 = st.columns([4,1], vertical_alignment="center")

with col1:
    st.title("BankPredict")
    st.write("Introduce los datos del cliente para predecir si contratará el depósito")

with col2:
    st.image("streamlit_app/logoBank.png", width=140)

# CARGAR MODELO


model = joblib.load("random_forest_model.pkl")


# LISTA COLUMNAS EXACTAS MODELO

columns = ['age', 'campaign', 'pdays', 'previous', 'emp.var.rate',
'cons.price.idx', 'cons.conf.idx', 'euribor3m', 'nr.employed',
'job_admin.', 'job_blue-collar', 'job_entrepreneur', 'job_housemaid',
'job_management', 'job_retired', 'job_self-employed', 'job_services',
'job_student', 'job_technician', 'job_unemployed', 'job_unknown',
'marital_divorced', 'marital_married', 'marital_single',
'marital_unknown', 'education_basic.4y', 'education_basic.6y',
'education_basic.9y', 'education_high.school', 'education_illiterate',
'education_professional.course', 'education_university.degree',
'education_unknown', 'default_no', 'default_unknown', 'default_yes',
'housing_no', 'housing_unknown', 'housing_yes', 'loan_no',
'loan_unknown', 'loan_yes', 'contact_cellular', 'contact_telephone',
'month_apr', 'month_aug', 'month_dec', 'month_jul', 'month_jun',
'month_mar', 'month_may', 'month_nov', 'month_oct', 'month_sep',
'day_of_week_fri', 'day_of_week_mon', 'day_of_week_thu',
'day_of_week_tue', 'day_of_week_wed', 'poutcome_failure',
'poutcome_nonexistent', 'poutcome_success']


# INPUTS USUARIO

st.header("Datos Macroeconómicos")

euribor = st.number_input(
    "Euribor 3 meses",
    value=0.0,
    format="%.3f"
)

nr_employed = st.number_input(
    "Número empleados",
    value=5000
)

emp_var_rate = st.number_input(
    "Emp var rate",
    value=0.0,
    format="%.2f"
)


st.header("Datos Cliente")

age = st.number_input(
    "Edad",
    min_value=18,
    max_value=100,
    value=40
)

campaign = st.number_input(
    "Número contactos campaña",
    min_value=0,
    value=3
)

previous = st.number_input(
    "Número contactos previos",
    min_value=0,
    value=0
)


#  DATAFRAME COMPLETO

input_dict = dict.fromkeys(columns, 0)

input_dict['poutcome_nonexistent'] = 1
input_dict['contact_cellular'] = 1
input_dict['month_may'] = 1
input_dict['day_of_week_mon'] = 1

input_dict['age'] = age
input_dict['campaign'] = campaign
input_dict['previous'] = previous

# valor fijo correcto para evitar preguntar al usuario
input_dict['pdays'] = 999

input_dict['euribor3m'] = euribor
input_dict['nr.employed'] = nr_employed
input_dict['emp.var.rate'] = emp_var_rate

input_df = pd.DataFrame([input_dict])


# PREDICCION


if st.button("Predecir"):

    prediction = model.predict(input_df)

    if prediction[0] == 1:

        st.success("Cliente probable YES")

    else:

        st.error("Cliente probable NO")