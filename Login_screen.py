'''import bibliothek'''
import customtkinter as ctk


'''set theme'''
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


'''Initialize the main screen settings'''
root = ctk.CTk()
root.geometry('350x197')  # screen size
root.title("Provisionamento")  # screen title
root.iconbitmap('Prov/img/rikka.ico')  #screen icon
root.eval('tk::PlaceWindow . center')  # make window center
root.resizable(False,False)  # make window not resizable


'''Username entry section'''

# Show Username entry css
user = ctk.CTkEntry(root,
                    placeholder_text='Username',
                    corner_radius=25,
                    fg_color='#ffffff',
                    text_color='#000000',
                    width=200                    
                    )
# Place the username entry
user.pack_configure(pady=20
                    )

'''Password entry section'''

# Show Password entry css
password = ctk.CTkEntry(root,
                        placeholder_text='Password',
                        corner_radius=25,
                        fg_color='#ffffff',
                        text_color='#000000',
                        width=200,
                        show='*'  # hide the password character
                        )
# Place the password entry
password.pack_configure(pady=5,
                        side='top'
                        )

'''Login handler'''
def logon():
    if user.get() == 'admin' and password.get() == 'admin':
        return True
    else:
        return False


'''Login button section'''

# Show login name on screen CSS
login = ctk.CTkButton(root,
                     text='Login',
                     fg_color='#48ff2f',
                     corner_radius=50,
                     text_color='black',
                     width=70,
                     height=30,
                     font=('arial',15),
                     command=logon
                    )
# Place the login
login.pack_configure(pady=20,
                     side='bottom'
                     )

if __name__ == "__main__":
    root.mainloop()
