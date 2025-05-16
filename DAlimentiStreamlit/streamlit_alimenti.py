import streamlit as st
import pandas as pd
st.title("Diario Alimentare")

df_csv= pd.read_csv(r"./DAlimentiStreamlit/diarioalimenti.csv")
select_alimento=st.selectbox("Scegli l'alimento\n", df_csv["alimento"].unique())

qt= st.number_input("Inserisci la quantità di CHO\n", min_value=0.0, step=0.0)

if st.button("Esegui Calcolo"):
    if select_alimento and qt > 0:
        dati = df_csv[df_csv["alimento"] == select_alimento].iloc[0]

        calc_cho= (qt * dati["cho"]) / (dati["peso"])
        calc_kcal= (qt * dati["kcal"]) / (dati["peso"])
        calc_fibre= (qt * dati["fibre"]) / (dati["peso"])
        calc_proteine= (qt * dati["proteine"]) / (dati["peso"])

        df_result= pd.DataFrame({
            "CHO" : [calc_cho],
            "KCAL" : [calc_kcal],
            "FIBRE" : [calc_fibre],
            "PROTEINE" : [calc_proteine] 
        })

        st.dataframe(df_result.style.format("{:.2f}"))
    else:
        st.write("error")
else:
    st.write("\n")
