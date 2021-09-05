import os
q = "curl https://catfact.ninja/fact"
w = "curl https://api.coindesk.com/v1/bpi/currentprice.json"
e = "curl https://www.boredapi.com/api/activity"
print("1. animal facts\n2. real time bitcoin price\n3. bored\n4. predict gender with name\n5. programmed_joke\n6. Random user name, email, address etc\n7. name of all universities in a country\n8. more information about pincode of any nation\n")
a = str(input("input the no. to use api : "))
if a == "1":
	os.system(q)
elif a == "2":
	os.system(w)
elif a == "3":
	os.system(e)
elif a == "4":
	t = str(input("input name."))
	r = "curl https://api.genderize.io?name="+t
	os.system(r)
elif a == "5":
	os.system("curl https://official-joke-api.appspot.com/random_joke")
elif a == "6":
	os.system("curl https://randomuser.me/api/")
elif a == "7":
	country = str(input("input country name in format of 'United States'='United+States' : "))
	os.system("curl http://universities.hipolabs.com/search?country="+country)
elif a == "8":
	country1 = str(input("input country name in format 'us', 'in', etc : "))
	pincode = str(input("input pincode : "))
	os.system("curl https://api.zippopotam.us/"+country1+"/"+pincode)
else:
	print("input correct number.")