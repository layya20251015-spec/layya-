import streamlit as st 
import  pandas as pd
from sklearn .model_selection import train_test_split
from sklearn.linear_model import linearRegression 

df=pd.read_csv("student_scores.csv")
X=df.iloc[:,:-1].value
Y=df.iloc[:,-1].value
X_train,X_test,Y_train,Y_test=train_test_split( x , y , test_size=0.2,random_state=42)
model = linearRegression()
model.fit(X_train,Y_train)

st.title("exam score prediction model")
st.write("enter the no. of hours you are studied for exam")
hours=st.number_input("hour studied", min_value=0.0,step=0.1)
if st.button("predict score"):
  
  predicted_score=model.predict([[hours]])[0]
  st.success(f"predicted score :{preddicted_score: .2f}")
  st.write("sample training DATA")
  st.dataframe(df)
