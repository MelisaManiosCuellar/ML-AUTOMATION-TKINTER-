import tkinter
import tkinter.messagebox
import customtkinter
import tkinter as tk
from tkinter import ttk
import os
from tkinter import *


customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Tkinter")
        self.geometry(f"{1366}x{768}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4,sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Elige el modelo en función del tipo de problema", font=customtkinter.CTkFont(size=16, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=5, pady=5)
        self.button_1 = customtkinter.CTkButton(self.sidebar_frame,text="K-Neighbors")
        self.button_1.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
        self.button_2 = customtkinter.CTkButton(self.sidebar_frame,text="K-Means")
        self.button_2.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)
        self.button_3 = customtkinter.CTkButton(self.sidebar_frame,text="Multinomial Naive-Bayes")
        self.button_3.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
        self.button_4 = customtkinter.CTkButton(self.sidebar_frame, text="SVM Classifier")
        self.button_4.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)
        self.button_5 = customtkinter.CTkButton(self.sidebar_frame, text="SVM Regressor")
        self.button_5.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
        self.button_6 = customtkinter.CTkButton(self.sidebar_frame, text="Lasso Regression")
        self.button_6.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)
        self.button_7 = customtkinter.CTkButton(self.sidebar_frame, text="Ridge Regression")
        self.button_7.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        self.button_8 = customtkinter.CTkButton(self.sidebar_frame, text="Linear Regression")
        self.button_8.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)
        self.button_9 = customtkinter.CTkButton(self.sidebar_frame, text="Logistic Regression")
        self.button_9.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.button_10 = customtkinter.CTkButton(self.sidebar_frame, text="MLP Classifier")
        self.button_10.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)
        self.button_11 = customtkinter.CTkButton(self.sidebar_frame, text="DecisionTree Regressor")
        self.button_11.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
        self.button_12 = customtkinter.CTkButton(self.sidebar_frame, text="Best Classifier and Regressor")
        self.button_12.place(relx=0.5, rely=0.65, anchor=tkinter.CENTER)
        self.button_13 = customtkinter.CTkButton(self.sidebar_frame, text="Best Classifier")
        self.button_13.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
        self.button_14 = customtkinter.CTkButton(self.sidebar_frame, text="Best Regressor")
        self.button_14.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)



    
        
      
        # # self.button_14 = customtkinter.CTkButton(self.sidebar_frame, text="Best Classifier")
        # # self.button_14.grid( row=1, column=5, padx=4, pady=(4))
        # # self.button_15 = customtkinter.CTkButton(self.sidebar_frame, text="Best Regressor")
        # # self.button_15.grid( row=2, column=5, padx=4, pady=(4))
    

         
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # # create textbox
        # self.textbox = customtkinter.CTkTextbox(self, width=250)
        # self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

       

        

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(Kmeans):
        print("sidebar_button click")


if __name__ == "__main__":
    app = App()
    app.mainloop()
