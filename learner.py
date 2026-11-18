learner = {}
# # key-value
# ler = {
#  "id" : 1,
#  "name" : "Demo"
# }

while True :
        print("=================Driving School  Mgmt Syst=================")
        print("1. Add Learner")
        print("2. Display All Learner")
        print("3. Search Learner")
        print("4. update Learner")
        print("5. Delete Learner")
        print("6. Exit")

        choice = int(input("Hey user, please enter your choice :::   "))
        
        match choice :
                case 1 :
                    print("================Add Learner Operataion=============")
                
                    lerId = int(input("enter a Learner id ::"))
        
                    if lerId in learner:
                        print("Learner Id is allredy exist")
        
                    else :
                        lerName = input("enter a learner name ::")
                        lerAge =  input("enter a learner Age ::")
                        lerCat = input("enter a learner category ::")
        
                    learner[lerId] = {
                       "lerId" :  lerId,
                       "lerName" : lerName,
                       "lerAge" : lerAge,
                       "lerCat" : lerCat
                    }    
                    
                    print("Learner Data addedd successfully")  


                case 2 :
                    print("================Display All Learner Operataion=============")
                    
                    if len(learner)==0:
                        print("No Learner exist")   
                    else :
                        print("Learner Detials ===========")
                    
                        for lerIdId, lerDtls in learner.items():
                         print("Learner Id ::", lerId)
                         print("Learner Name::", lerDtls["lerName"])
                        print("Learner Age ::", lerDtls["lerAge"])
                        print("Learner Category ::", lerDtls["lerCat"])
                        print("="*20)  # Repeatative operataor
                case 3 :
                    print("================search Learner Operataion=============")
                
                    lerIdId = int(input("enter a learner id ::which learner you want to search ::  "))
                
                    if lerId in learner :
                     print("learner Found")
                
                     print("learner  Details==========")
                
                     print("learner Id ::", lerId)
                     print("learner name ::", learner[lerId]["lerName"])
                     print("learner Age ::", learner[lerId]["lerAge"])
                     print("learner Category ::", learner[lerId]["lerCat"])
                     print("*"*10)  
                    else:
                     print("Learner Id does not exist")



                case 4 :
                    print("================Update learner Operataion=============")
                    
                    id = int(input("enter a ler id- to which learner data you want to update: :"))
                    
                    if id in learner :
                    
                     eName = input("enter updated name of learner::")
                     eAge = input("enter updated age of learner::")
                    
                     learner[lerId]["lerName"] = eName
                     learner[lerId]["lerAge"] = eAge
                    
                     print("learner data is updated successfully")                  
                                     
                     print("learner Id ::", lerId)
                     print("learner name ::", learner[lerId]["lerName"])
                     print("learner name ::", learner[lerId]["lerAge"])
                     print("learner name ::", learner[lerId]["lerCat"])
                     print("*"*10)
                    else:
                       print("Learner Id does not exist")


                case 5 :
                    print("================Delete learner Operataion=============")
                    lerId = int(input("enter a learner id :: which learner you want to delete :: "))

                    if lerId in learner :

                     print("Learner Found")

                     print("Learner Details ==========")

                     print("Learner Id ::", lerId)
                     print("Learner Name ::", learner[lerId]["lerName"])
                     print("Learner Age ::", learner[lerId]["lerAge"])
                     print("Learner Category ::", learner[lerId]["lerCat"])

                     del learner[lerId]

                     print("Learner data deleted successfully")

                    else :
                      print("Learner id does not exist")
                    
                                  
                      pass
                case 6 :     
                 print("================Exit============")
                 print("================Thank you for using our application Operataion=============")
                          
            
                case _:
                  print("================Invalid Choice----============")
                  break
                                                    
                