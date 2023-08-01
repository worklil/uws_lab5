"""
Question 2

In a small highland village, everyone has the surname McIntosh, McGregor, McDonald or McKenzie.
Everyone is called Angus, Hamish, Morag or Mhairi
No two people have the same name.
Create a program to compile a list of the inhabitants of the village.
"""

surname = ["McIntosh", "McGregor", "McDonald", "McKenzie"]
name = ["Angus", "Hamish", "Morag", "Mhairi"]
for i in surname:
    for j in name:
        print(j, i)
print("the end")