from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession
import json

# Define the required scopes
scopes = [
  "https://www.googleapis.com/auth/userinfo.email",
  "https://www.googleapis.com/auth/firebase.database"
]

# Authenticate a credential with the service account
credentials = service_account.Credentials.from_service_account_file(r"C:\Users\nm17839\Documents\Automation Anywhere Files\Automation Anywhere\My Docs\Pythonkey.json", scopes=scopes)

# Use the credentials object to authenticate a Requests session.
authed_session = AuthorizedSession(credentials)
name = authed_session.get("https://newagent-8f431.firebaseio.com/Data1/Name.json", verify=False)
patient_name = name.json()
age = authed_session.get("https://newagent-8f431.firebaseio.com/Data2/Age.json", verify=False)
patient_age = age.json()
gender = authed_session.get("https://newagent-8f431.firebaseio.com/Data3/Gender.json", verify=False)
patient_gender = gender.json()
pincode = authed_session.get("https://newagent-8f431.firebaseio.com/Data4/Zip.json", verify=False)
patient_pincode = pincode.json()
q1 = authed_session.get("https://newagent-8f431.firebaseio.com/Data5/Q1.json", verify=False)
patient_q1 = q1.json()
q2 = authed_session.get("https://newagent-8f431.firebaseio.com/Data6/Q2.json", verify=False)
patient_q2 = q2.json()
q3 = authed_session.get("https://newagent-8f431.firebaseio.com/Data7/Q3.json", verify=False)
patient_q3 = q3.json()
risk_category = authed_session.get("https://newagent-8f431.firebaseio.com/Data9/risk_category.json", verify=False)
patient_risk_category = risk_category.json()
recommendation = authed_session.get("https://newagent-8f431.firebaseio.com/Data10/recommendation.json", verify=False)
patient_recommendation = recommendation.json()
slots_booked = authed_session.get("https://newagent-8f431.firebaseio.com/Data11/slots_booked.json", verify=False)
patient_slots_booked = slots_booked.json()

patientData = {
    "name":patient_name,
    "age":patient_age,
    "gender":patient_gender,
    "pincode":patient_pincode,
    "q1":patient_q1,
    "q2":patient_q2,
    "q3":patient_q3,
    "risk_category":patient_risk_category,
    "recommendation":patient_recommendation,
    "slot_booked": patient_slots_booked
}

dfObj = pd.DataFrame(list(patientData.items()), columns=['Inputs','Values'])
dfObj.to_csv(r'C:\Users\nm17839\Documents\Automation Anywhere Files\Automation Anywhere\My Docs\PatientData.csv',index=False)


