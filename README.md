# compta
it's a light accounting program

# functionality
With this program you can:
- add and remove at each moment a group of person
- manage the purchases of the different groups
- check at any time who owes money to whom and how much

# add
This fonctionality create a txt file with 2 informations:
- the number of persons in the group
- the money you owe to other groups
*When you run the program, write 'add' and press enter.*
After that, you have to write the name of the new group and the the number of persons in the group separate by a comma.

# remove
This feature removes the name from the list of groups but keeps the file of the same name.
*When you run the program, write 'rm' and press enter.*
After that, write the name of the group you want to delete.

# buy
This feature allows you to manage the purchases of different groups and thus adjust their account.
*When you run the program, write 'buy' and press enter.*
After that, the fonction takes 2 arguments:
- the name of the person who bought something
- the value of the purchase

# account
This fonction displays the numbers of persons in each group and the amount of his 'debt'.
*When you run the program, write 'cpt' and press enter.*

# important
- If **group.txt** is empty, the program start at the menu "add".
- To exit the program, type 'q' when you are in the main menu.
