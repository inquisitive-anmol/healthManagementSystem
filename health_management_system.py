
########################### Health Management System #########################

def getTime():
    import time
    return time.ctime()


def inputData(c_name):
    def exercise_inpt(c_name):
        while 1:
            try:
                yn_check = input(
                    "press (y) if you want to enter exercise else press (n) : ")

                if yn_check == "y":
                    exrcis_don = input("write exercise : ")
                    print(Efile_format)
                    file_name = input(
                        "Enter the name of the file to save : ")
                    complet_file_name = file_name + "exercise.txt"
                    curr_time = getTime()
                    with open(complet_file_name, "a") as file:
                        file.write(f"{curr_time}: {exrcis_don} \n")

                elif yn_check == "n":
                    print("OK done!!!!!!")
                    break

                else:
                    print(
                        "!! you entered wrong input, Please enter correct key!!!")
            except Exception as e:
                print(f"error {e}")

    def diet_inpt(c_name):
        while 1:
            try:
                yn_check = input(
                    "press (y) if you want to enter Diet else press (n) : ")

                if yn_check == "y":
                    dit_tkn = input("write the Diet : ")
                    print(Dfile_format)
                    file_name = input("Enter the name of the file to save : ")
                    complete_file_name = file_name + "diet.txt"
                    curr_time = getTime()
                    with open(complete_file_name, "a") as file:
                        file.write(f"{curr_time}: {dit_tkn} \n")

                elif yn_check == "n":
                    print("OK done!!!!!!")
                    break
                else:
                    print("!! you entered wrong input, Please enter correct key!!!")
            except Exception as e:
                print(f"error {e}")

    print("What you want to enter about : 1. Exercise or 2. Diet")
    print("Press 1 for Exercise ")
    print("Press 2 for Diet")

    ED_input = input("Enter your choice : ")

    if ED_input == '1':
        exercise_inpt(c_name)
    elif ED_input == '2':
        diet_inpt(c_name)
    else:
        print("!! you entered wrong input, Please enter correct key!!!")


def retriveData(c_name):

    def exrcs_rtv(c_name):
        while 1:
            yn_check = input(
                "press (y) if you want to see Excercise files else press (n) : ")
            if yn_check == 'y':
                day = input("which days Exercise file you want to see : ")
                filName = c_name + day + "exercise.txt"

                try:
                    with open(filName, 'r') as file:
                        print(file.read())
                except Exception as e:
                    print(e)

            elif yn_check == "n":
                print("OK done!!!!!")
                break
            else:
                print("!! you entered wrong input, Please enter correct key!!!")

    def diet_rtv(c_name):
        while 1:
            yn_chek = input(
                "press (y) if you want to see Diet else press (n) : ")

            if yn_chek == "y":
                day = input("which days Diet file you want to see : ")
                filName = c_name + day + "diet.txt"

                try:

                    with open(filName, 'r') as file:
                        print(file.read())
                except Exception as e:
                    print(e)
            elif yn_chek == "n":
                print("OK done!!!!!!")
                break
            else:
                print("!! you entered wrong input, Please enter correct key!!!")

    print("$$$ Showing the data $$$")
    print("What you want to see about : 1. Exercise or 2. Diet")
    print("Press 1 for Exercise ")
    print("Press 2 for Diet")

    edInpt = input("Enter your choice : ")

    if edInpt == '1':
        exrcs_rtv(c_name)
    elif edInpt == '2':
        diet_rtv(c_name)
    else:
        print("!! you entered wrong input, Please enter correct key!!!")


print("!!!!!!!!!!! Welcome !!!!!!!!!!")
Efile_format = "the file formate for saving is client name then day then, eg- rohan1 for day first"
Dfile_format = "the file formate for saving is client name then day, eg- rohan1 for day first"
client_name = input("Enter the name of the client : ")

user_prog_choice = ""
while user_prog_choice != "q":
    try:

        print("What you want to do?")
        print("Input the data or Retrive the Data")
        print("press i to input the data")
        print("press r to retrive the data")
        user_choice = input("Enter your choice : ").lower()

        if user_choice == "i":
            inputData(client_name)

        elif user_choice == "r":
            retriveData(client_name)
        else:
            print("!! you entered wrong input!!")
    except Exception as e:
        print(e)

    user_prog_choice = input("press y to continue or q to quit. :").lower()
