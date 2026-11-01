contacts={}
while True:
   print("Contact Management \n")
   print("1- Add a contact")
   print("2- View a contact")
   print("4- Exit")
   choice = input("\nPlease choose a number from 1-4: ")
   
   #Add contact
   if choice == "1"" 
     contact_id = input("Enter the contact ID: ")
     contact_name = input("Please type a name: ")
     contact_phone = int(input("Please type a phone number: ")
     contacts["ID"] = contact_id
     contacts["name"] = contact_name
     contacts["phone"] = contact_phone
     print(f"\n \n {contact_name} was added successfully... \n \n")
     
     #view contact
     elif choice == "2":
          print(contacts)
     
     #Edit Contact
     elif choice == "3": 
          id_to_edit = input("Please enter and ID to edit:  ")
          if  id_to_edit in contacts["ID"]:
              new_name = input("Enter  a new name: ")
              new_phone = int(input("Enter a new phone: "))
              contacts["name"] = new_name
              contacts["phone"] = new_phone
              print("\n Success...")
           else:
              print(f"Sorry, {id_to_edit} was not found ...")   
      #Exit
      elif chlice =="4": 
           pritn("Exiting ...")
           break
           
       #Invalid 
       else:
          print("Invalid Choice!") 
