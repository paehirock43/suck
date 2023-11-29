name='Piyawat Panruensan'
age=20
gender=True
sale=25000.50
commission=sale*0.03
interest=['Java','Web Development','IOT','FinTech','Healthy','Sport Car','Dog']
education={'vocational':'Commercial','deploma':'Business Computer','bachelor':'Information System','master':'Information Technology','doctoral':'Information Studies'}
print("*************** Data form Variables ***************")
print("Hello, "+name)
print("You are ",age," years old")
print("Your gender are ",gender)
print("Your sale for this month ",sale,", and get commission : ",commission)
print("Your interest: ",len(interest)," are : ",interest)
interest.append("Fashion")
print("Your interest after update : ",interest)
print("New your interest are ",interest[7])
print("Your education are : ",education)
print("Your bachelor degree is : ",education.get('bachelor'))
print("Good Bye.")
print("***************************************************")