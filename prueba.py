# It's a class that creates a window with a list of radio buttons that when clicked, displays the
# calories and price of the dessert.
from customtkinter import *
class App(CTk):
    def __init__(self):
        """
        The function creates a window with a title, geometry, and a list of desserts with their calories
        and price.
        """
        super().__init__()
        self.title("Desserts, Calories, and $_$")
        self.geometry("400x300")
 
        # A list having desserts, their calories, and their price.
        self.D = [
            ("Doughnuts", "300, 0.99"),
            ("Pumpkin Pie", "243, 5.24"),
            ("Fudge", "411, 14"),
            ("Brownies", "466, 8.47"),
            ("Cheesecake", "321, 13"),
        ]
 
        # A customtkinter string variable to store calories and price of the selected dessert
        self.selected = StringVar()
        for dessert, calories in self.D:
            # It's creating radio buttons that when clicked, will display the calories and price
            # of the dessert.
            self.rb = CTkRadioButton(self, text=dessert, variable=self.selected, value=calories, command=self.show_calories)
            # Display the buttons with a padding(spacing) of 10 pixels
            self.rb.pack(pady=10)
 
        # Create an empty label to display the calories later
        self.show = CTkLabel(self, text="")
        self.show.pack()
 
 
    def show_calories(self):
        """
        It takes the dessert(radio button) selected, splits its calorie and price into a list, and then displays the first
        item in the list (the calories) and the second item in the list (the price) in a label
        """
        # Remove the previous display of the calories and price ($) (if any)
        self.show.pack_forget()
        # split calories and price($) into two
        temp = self.selected.get().split(", ")
        # Create a label to display the calories and price ($)
        self.show = CTkLabel(self, text=f"I have {temp[0]} calories! And you would need ${temp[1]} to have me!")
        # Display the label with a padding of 10 pixels
        self.show.pack(pady=10)
         
 
if __name__ == "__main__":
    app = App()
    app.mainloop()