
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
PLACEHOLDER = "[name]"
with open("/Users/junwoo-kwon/python_course/Mail Merge Project Start/Input/Names/invited_names.txt") as names:
    name_list = names.readlines()
    for i in range(len(name_list)):
        new_name = name_list[i].replace("\n", "")
        name_list[i] = new_name
print(name_list)
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in name_list:
        new_letter = letter_contents.replace(PLACEHOLDER, name)
        print(new_letter)
        with open(f"./Output/ReadyToSend/letter_for_{name}", mode="a") as ready_letter:
            ready_letter.write(new_letter)



#     name_list = []
#     for i in range(1,9):
#         name = names.readlines(i)
#         print(name)
#         name_list.append(name)
# print(name_list)
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp