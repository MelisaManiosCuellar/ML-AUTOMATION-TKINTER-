import customtkinter
from PIL import Image, ImageTk
    
window = customtkinter.CTk()


my_image = customtkinter.CTkImage(light_image=Image.open("datos.png"),
                                  dark_image=Image.open("datos.png"),
                                  size=(768, 768))

button = customtkinter.CTkButton(master=window, image=my_image)
button.pack()

window.mainloop()