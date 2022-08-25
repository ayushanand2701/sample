class person :                                               # class with  anme person
    def __init__(abc,name,surname,emailid,year_of_birth):
        #init-use to pass data to class,its a constr

        abc.name=name                                    #abc is a poim=nter to class
        abc.surname=surname
        abc.emailid=emailid
        abc.year_of_birth=year_of_birth

    def age(abc,current_year,Year_of_birth):
        return current_year-abc.year_of_birth

anuj_var=person("anuj","bhandari","anuj@gmail.com",1994)

#it is variable in which we re passing data

ayush=person("ayush","kumar","ayush@dxc",2000)
print(anuj_var.age(2022))


#it is a vriable


print(anuj_var.name)
print(anuj_var.surname)
print(anuj_var.emailid)
print(anuj_var.year_of_birth)



print(ayush.name)
print(ayush.surname)
print(ayush.emailid)


#conactenate two string ayush with kumar

print(ayush.name+ " " +ayush.surname)
print(type(ayush))


#########################################






