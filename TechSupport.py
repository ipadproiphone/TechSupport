"We've caught you hackers!"
'''
Logging in. BEGINNGING
'''
import time
import random
import os





logins = {"saira rao":"80pinata","shiv govindan":"password","nita rao":"password","michael mchenry":"password","suman govindan":"password","rajan":"govindan","regina jackson":"password","katie debord":"password","jaikar rao":"password","patty specht":"password","alex govindan":"password","1234":"1234","lila govindan":"password"}

for i in range(0,101):
  percentloading = str(i)
  print("Loading %" + percentloading)
  time.sleep(0.08)
  os.system("clear")

print("Loaded Successfully!")


def welcomeMessage():
  print("Welcome to APT tech support. Please log in if you have a membership. Please visit https://forms.gle/1PFqDWHHjZ8vZNdq9 to register. Email allpowertechhelp@gmail.com with any other questions. ")
welcomeMessage()




usernameprompt = input("Please type your username. If you are on a mobile device, you may have to click anywhere on this page. (Please type here at that tiny white spot). ")


passwordprompt = input("Please type your password. (Please type here at that tiny white spot) ")

if usernameprompt == "admin" and passwordprompt == "08092010":
  print("Hi dar, to print all logins, hit al")
  x = input()
  if x == "al":
    print(logins)
elif usernameprompt not in logins:
  print("Username does not exist. Hit the 'run again' button and try again. ")

elif logins[usernameprompt] != passwordprompt:
  print("Incorrect Password, hit run again to try again")
else:


  print("Welcome to APT Tech support %s!" % usernameprompt)





  print("Type your problem with 3 keyword for example 'phone, not ,ringing' that would help you if phone isn't ringing.* \n *Hit enter after each word.")
  keyword1 = input("Type in your first keyword(all lowercase), ")
  keyword2 = input("Type in your second keyword(all lowercase), ")
  keyword3 = input("Type in your third keyword(all lowercase), ")
  brand = input("What brand is your phone(all lowercase(for example:apple, samsung))")

  IOS13NotRingingBug = ['phone','not','ringing','iphone']
  carplayoniphonesenotconnecting = ["carplay","phone","iphone","se"]












  #Below check IOS 13 phone not ringing bug.



  if brand == "samsung":
    print("Email allpowertechhelp@gmail.com with your question. Our page doesn't support Samsung support yet. ")
  elif brand == "apple":
    appleDevice = input("What device do you need service with? (ex: iphone or ipad or macbook) (type all lowercase no spaces) ")
    if appleDevice == "iphone":
      if keyword1 in IOS13NotRingingBug or  keyword2 in IOS13NotRingingBug or keyword3 in IOS13NotRingingBug:
        checkIfTrue = input("Your phone isn't ringing is that right?(answer yes or no(all lowercase)). ")
      if checkIfTrue == 'no':
        
        followup0 = input("Is the following true?: There's a problem with your iPhone. Type yes or no(all lowercase): ")
        
      elif checkIfTrue == 'yes':
        
        print("Go to settings > sound and haptics(NOT in general) > ringtone. Make sure ringtone is set to something. Have someone call you!")
        followup = input("Did that work?(Type yes or no all lowercase). ")
        followup1 = ''
        if followup == 'no':
          print("Ok, that didn't work. On the side of your iPhone next to the volume button, there is a tiny little button, toggle the button to the opposite, Have someonecall you!")
          followup1 = input("Did that work?(Type yes or no all lowercase). ")
        no = str("no")

        if followup1 == no:
            print('Email allpowertech@gmail.com with your question. ')
        


        elif followup1 == 'yes':
            print('Thank you for coming to APT')

        elif followup == "yes":
          print('Thank you for coming to APT')
        
  else:
    print("Email allpowertechhelp@gmail.com with your question or hit the 'run again' button with different keywords.")
