from read_csv import get_names, get_emails

names=get_names()
original_names=[name.strip(' ') for name in names]

emails=get_emails()
original_emails=[email.strip(' ') for email in emails]

print(original_names)
print(original_emails)
print("Please provide your name and email")
count=0
while count<3:
    user_name=input("Please enter your name(Names are case sensitive): ")
    user_email=input("Please enter your email: ")
    if user_name in original_names and user_email in original_emails:
        print(f"\n Hello {user_name} \n")
        with open('welcome_note.txt','r') as f:
                print(f.read())
                user_input=input("Do you want to get in?[YES/NO]: ").upper()
                if user_input=='YES':
                    with open('game_instruction.txt','r') as g:
                        print(g.read())
                        while True:
                            try:
                                choice=input("Press P to play: ").upper()
                                if choice=='P':
                                    print("you are in")
                                else:
                                    raise ValueError("You Entered the wrong choice")
                                break
    
                            except ValueError as e:
                                print(e)

                else:
                    print("Bye")
                    
        break
    else:
        print("It doesnt match our records. Please try again")
        print(2 - count, "attempts left")
        count+=1




                 
         
  


