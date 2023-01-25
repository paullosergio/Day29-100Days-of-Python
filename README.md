Skip to content
Search or jump to…
Pulls
Issues
Codespaces
Marketplace
Explore
 
@paullosergio 
priyanka-111-droid
/
100daysofcode
Public
Fork your own copy of priyanka-111-droid/100daysofcode
Code
Issues
Pull requests
Actions
Projects
Security
Insights
100daysofcode/Day029/password-manager-start/README.md
@priyanka-111-droid
priyanka-111-droid added
Latest commit 5b6e7ec on Jul 19, 2021
 History
 1 contributor
57 lines (28 sloc)  2.55 KB

# Password Manager using Tkinter

Logo is given already.

Tkdocs for canvas [here](https://tkdocs.com/tutorial/canvas.html)


## UI setup section

1.In user interface section,create canvas widget with title Password Manager,width and height of 200px and padding 20 px from all edges.Logo is in center of canvas.

2.Use grid() and **columnspan** to complete user interface(add labels and entry for website,email/username,password) and buttons for generate password and add password and remove password.

3.Now when we run code,we can bring cursor to website entry using focus method

4.Add starting value to email entry so that when you run program,it is already filled with email you use the most.(Hint:use [insert()](https://tkdocs.com/tutorial/widgets.html#entry))


## Save password section


5.Create text file called data.txt.In Save Password section of main.py file,accept user input for website,email and password and save all these answers in data.txt file.

6.**Standard dialogs** are pop-ups tkinter can generate.See [here](https://docs.python.org/3/library/tkinter.messagebox.html)

eg.message boxes to show errors,ask yes/no question etc.

Use  a dialog box to display error in case user leaves any of the entry fields empty and another dialog box that asks user click ok to confirm their entered website and password else click cancel if they need to edit something.

7.In case user enters same website and same email,we have displayed message saying password already saved.

## Password Generator section

8.We have edited password generator code made in Day5 so that we don't have to type anything from console.
We have copy pasted day5.py code.

* Now convert 3 for loops into 3 list comprehensions 

* Use join() method to convert password list into string

These make code more pythonic.

9.Now use insert() to display randomly generated password in password entry field.

10.Use [pyperclip](https://pypi.org/project/pyperclip/) to copy password directly to clipboard.Now we can directly use ctrl+v to paste password in our website.
