invited_names_path = "Input/Names/invited_names.txt"
letter_path = "Output/ReadyToSend/example.txt"
output_directory = "Output/ReadyToSend/letter_for_"
inviter = "Bolaji"
invited_names = []
with open(invited_names_path) as f:
    for invited_name in (f.readlines()):
        invited_name = invited_name.strip("\n")
        invited_names.append(invited_name)

with open(letter_path) as f:
    letter_template = f.readlines()
salutation_name = letter_template[0].split()[1].strip(",")
for invited_name in invited_names:
    with open(f"{output_directory}{invited_name}.txt", mode="w") as f:
        personalised_letter = "\n".join(letter_template)
        personalised_letter = personalised_letter.replace(letter_template[6], inviter)
        invitation_letter = personalised_letter.replace(salutation_name, invited_name)
        f.write(invitation_letter)


