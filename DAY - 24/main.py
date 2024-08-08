with open("./DAY - 24/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./DAY - 24/Input/Letters/starting_letter.txt") as letters_file:
    letters_contents = letters_file.read()
    for name in names:
        striped_name = name.strip()
        new_lettter = letters_contents.replace("[name]", striped_name)
        with open(f"./DAY - 24/Output/ReadyToSend/letter_for_{striped_name}.txt", "w") as completed_letter:
            new = completed_letter.write(new_lettter)