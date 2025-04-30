# tkinterProject1
Built using CIS 112 concepts

## LeverApp

My very first tkinter App to create a GUI!
Inspired by the Emperor's New Groover, users can input their names, and be asked to pull the lever!

## Greeting Assignment

### Objective
The objective of this assignment is to create a 
simple greeting application using Python's Tkinter library. 
The application should allow users to input their name, 
select their preferred language for the greeting, 
and display a personalized greeting message.

### Requirements:

1. Create a GUI application using Tkinter that includes the following components:
   - Label prompting the user to enter their name.
   - Entry widget for users to input their name.
   - Label prompting the user to select their preferred language.
   - Combobox (dropdown menu) for users to select their preferred language from a list of options (e.g., English, French, Spanish).
   - Button labeled "Greet Me" that, when clicked, generates a personalized greeting message based on the user's input.

2. Implement functionality to display a greeting message based on the user's input:
   - When the "Greet Me" button is clicked, the application should generate a greeting message that includes the user's name and is displayed in the selected language.

3. Apply styling and formatting to the GUI components to enhance the visual appeal of the application:
   - Use appropriate font styles, sizes, and colors for labels, entry widgets, combobox, button, and greeting message.

### Scoring Rubric:

1. GUI Components (3 points):
   - Label prompting the user to enter their name.
   - Entry widget for name input.
   - Label prompting the user to select their preferred language.
   - Combobox for language selection.
   - "Greet Me" button.

2. Functionality (4 points):
   - Application generates a personalized greeting message.
   - Greeting message includes the user's name.
   - Greeting message is displayed in the selected language.
   - Proper handling of edge cases (e.g., empty name input).

3. Styling and Formatting (3 points):
   - Use of appropriate font styles, sizes, and colors for GUI components.
   - Consistent alignment and spacing of components.
   - Overall visual appeal and user-friendliness of the application.


*Note: Bonus points may be awarded for implementing additional features or enhancements beyond the basic requirements.*

## Weather App

This was the first app I used grid() and tk.PhotoImage for. At the moment of this commit, only the front-end and hard-coded examples have been made. By the end though, this app will call an API to get current weather in different locations. 


## Ordering Kiosk

### Objective
Your task is to develop an ordering kiosk application using the Tkinter library in Python. The application should allow customers to enter their name, choose whether to add a drink to their order, select an entree from the provided options, and display their order details upon submission. Utilizing a theme for the application is optional but will earn extra credit.

### Requirements:

1. Create an `OrderingKiosk` class that represents the application.
2. The application should have the following features:
- Entry widget for customers to enter their name. 
- Checkbutton to allow customers to choose whether to add a drink to their order
- Combobox with options for entrees (e.g., Pizza, Burger, Salad)
- Button to submit the order  
- Label to display the order details upon submission.
3. Display the order details, including the customer's name, drink choice (if selected), and selected entree, upon clicking the submit button.
4. Implement proper error handling to display a message if the customer's name is not provided or if no entree is selected upon submission.

### Scoring Rubric:

1. Class Structure (2 points):
  - Properly define the `OrderingKiosk` class with all necessary methods and attributes.
2. Widget Functionality (4 points):
  - Entry widget captures customer name.
  - Checkbutton allows customers to choose whether to add a drink to their order.
  - Combobox provides options for selecting an entree.
  - Button triggers the submission of the order and displays order details.
3. Error Handling (2 points):
  - Proper error message is displayed if the customer's name is not provided upon submission.
  - Proper error message is displayed if no entree is selected upon submission.
4. Code Quality (2 points):
  - Code is well-structured, organized, and easy to understand.
  - Proper use of Tkinter widgets and methods.
  - Comments are included to explain the purpose of major code sections.
5. Extra Credit (2 point):
  - Utilization of a theme for the application interface.