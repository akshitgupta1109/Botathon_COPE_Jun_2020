from firebase import firebase

firebase = firebase.FirebaseApplication('https://newagent-8f431.firebaseio.com/', None)

data =  { 
			"Day" : "26th June 2020",
			"DoctorAddress" : "3505 Progress Ln, Saint Cloud, FL-34769",
			"DoctorContact" : "239-200-7990",
			"DoctorHospital" : "Govt Hospital Saint Cloud",
			"DoctorName" : "LAKHINDER BHATIA",
			"Slot" : "Slot1 : 10am-11am, Slot2: 3pm-4pm"	
		}
				
result = firebase.post('/Data8/',data)  