import os
import tkinter.filedialog


def createtemplate():

    chosenname = input("Name your new template: ")

    with open(chosenname + '.txt', 'w') as file:
        file.write('Write your email template here...')

    os.startfile(chosenname + '.txt')
    file.close()

listoffiles = []

def listfiles():
    for x in os.listdir():
        if x.endswith(".txt"):
            # Prints only text file present in My Folder
            print(x)
            listoffiles.append(x)
            print(listoffiles)



# Open a file dialog
filename = tkinter.filedialog.askopenfilename()

# Do something with the filename
print(filename)

choice = str(input("What shall it be?"))

if "new" in choice or "1" in choice:
    print("You picked new.")
elif "email" or "2" in choice:
    pass

def gatherinfo():
    proj_name = input("What is the project site?   ")
    contact = input("Who is the contact?   ")
    return proj_name, contact

proj_name, contact = gatherinfo()
print (proj_name, contact)