class Citizen:
   def _init_(self,name,age,dob,id_number):
       self.citizen_name = name
       self.citizen_age = age
       self.citizen_dob = dob
       self.citizen_id = id_number
       
   def add_citizen(self):
       print("Name:"+self.citizen_name)
       print("Age:"+self.citizen_dob)
       print("Date of birth:"+self.citizen_dob)
       print("Citizen Id:"+self.citizen_id)
       print("Citizen Added")
        
citizen1 = Citizen("Peter",8,"19th October 2012","0198")
citizen1.add_citizen()

citizen2 = Citizen("Sarthaki",11,"11th April 2011","0199")
citizen2.add_citizen()