class person:
    def age(self,current_age,year_of_birth):
        return current_age-year_of_birth

    def email_id(self,email_id):
        print("email id to print",email_id)
    def ask_name(self):
        name=input("Tell me your name")
        return name
    def ask_dob(self):
        dob=input("tell me ur dob")
        return dob

sudh=person()
hitesh=person()
anuj=person()


hitesh.email_id("ayushanand@gmail.com")
print(hitesh.ask_name())
print(hitesh.ask_dob())
