import customtkinter as ctk
import tkinter.messagebox as tkmb

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

admin_username = ["admin1", "admin2", "admin3", "admin4"]
admin_password = ["development_process"]

print("#If you are a admin login here, if you are just a user then double enter click")
print("#After registration enter data in the list given in the code in line 13 and 14")

username_admin = input("Enter admin username: ")
userpass_admin = input("Enter admin password: ")

users = ["Tejesh"]
password = ['1234']

if username_admin in admin_username and userpass_admin in admin_password:

    new_page = ctk.CTk()

    new_page.title("Logged in as admin")

    new_page.geometry("500x500")

    frame_admin = ctk.CTkFrame(master=new_page)
    frame_admin.grid(pady=20, padx=40)

    exit_button = ctk.CTkButton(frame_admin, text="Exit", command=lambda:{exit()})
    exit_button.grid(pady=20, padx=10)

    new_page.mainloop()

elif username_admin == "" and userpass_admin == "":
    print("Login screen opening....")

elif username_admin not in admin_username and userpass_admin in admin_password:
    print("Error", "Username is invalid")
    print("Login page will also pop up in case you are a user")
    print("Re-run code if you think you entered username wrong")

elif username_admin in admin_username and userpass_admin not in admin_password:
    print("Error", "Password in entered incorrectly")
    print("Login page will also pop up in case you are a user")
    print("Re-run code if you think you entered password wrong")

elif username_admin not in admin_username and userpass_admin not in admin_password:
    print("Error", "Username is invalid and password in incorrect")
    print("Login page will also pop up in case you are a user")
    print("Re-run code if you think you entered username and password wrong")

print("Check taskbar")

def register():

    def reg():

        def write_review():

            def check():
                if Label_entry.get() == "":
                    tkmb.showerror("Error", "Review is blank")

                else:
                    last_page = ctk.CTkToplevel(review_page)

                    last_page.title("Submitted")

                    last_page.geometry("500x500")

                    frame6 = ctk.CTkFrame(master=last_page)
                    frame6.grid(pady=20, padx=40)

                    Label = ctk.CTkLabel(frame6, text="Submitted successfully")
                    Label.grid(pady=20, padx=10)

            review_page = ctk.CTkToplevel(reg_page)

            review_page.title("Write review")

            review_page.geometry("500x500")

            frame5 = ctk.CTkFrame(master=review_page)
            frame5.grid(pady=20, padx=40)

            Label_review = ctk.CTkLabel(frame5, text="Write review")
            Label_review.grid(pady=20, padx=10)

            Label_entry = ctk.CTkEntry(frame5, placeholder_text="Write review")
            Label_entry.grid(pady=20, padx=10)

            submit_btn_2 = ctk.CTkButton(review_page, text="Send", command=check)
            submit_btn_2.grid(pady=20, padx=40)

            cancel_button = ctk.CTkButton(review_page, text="Cancel", command=lambda:{exit()})
            cancel_button.grid(pady=20, padx=40)

        reg_page = ctk.CTkToplevel(register_page)

        reg_page.title("Registered successfully")

        reg_page.geometry("500x500")

        if register_entry.get() == "" and conform_password2.get() == "" and register_password.get() == "":
            tkmb.showerror("Error", "You have not entered any details")

        elif register_password.get() == "":
            tkmb.showerror("Error", "Please enter password")

        elif conform_password2.get() == "":
            tkmb.showerror("Error", "Please enter conform password")

        elif register_entry.get() == "":
            tkmb.showerror("Error", "Please enter username")

        frame4 = ctk.CTkFrame(master=reg_page)
        frame4.grid(pady=20, padx=40)

        label_reg = ctk.CTkLabel(frame4, text="Interested to write a review?")
        label_reg.grid(pady=20, padx=10)

        Review_button = ctk.CTkButton(frame4, text="Write a review", command=write_review)
        Review_button.grid(pady=20, padx=10)

        cancel_button_2 = ctk.CTkButton(frame4, text="Cancel", command=lambda:{exit()})
        cancel_button_2.grid(pady=20, padx=10)


    register_page = ctk.CTkToplevel(window)

    register_page.title("Register")

    register_page.geometry("500x500")

    frame2 = ctk.CTkFrame(master=register_page)
    frame2.pack(pady=20, padx=40, fill='both', expand=True)

    Label2 = ctk.CTkLabel(register_page, text="REGISTER ACCOUNT")
    Label2.pack(pady=20, padx=10)

    frame3 = ctk.CTkFrame(master=frame2)
    frame3.pack(pady=20, padx=40, fill='both', expand=True)

    register_label = ctk.CTkLabel(frame3, text="REGISTER")
    register_label.grid(pady=20, padx=10)

    register_entry = ctk.CTkEntry(frame3, placeholder_text="New Username")
    register_entry.grid(pady=20, padx=10)

    register_password = ctk.CTkEntry(frame3, placeholder_text="Enter new password", show="*")
    register_password.grid(pady=20, padx=10)

    conform_password2 = ctk.CTkEntry(frame3, placeholder_text="Re-Enter password", show="*")
    conform_password2.grid(pady=20, padx=10)

    register_btn = ctk.CTkButton(frame3, text="Register", command=reg)
    register_btn.grid(pady=20, padx=10)

def submit():
    submit_page = ctk.CTkToplevel(window)

    submit_page.title("Authentication")

    submit_page.geometry("500x500")

    if login_entry.get() == username_admin or users and password_entry.get() == userpass_admin or password and conform_password.get() == userpass_admin or password:
        tkmb.showinfo(title="Login granted", message="You are authorized")
        label_submit_page = ctk.CTkLabel(submit_page, text="LOGGED IN")
        label_submit_page.grid(pady=20, padx=10)

    elif login_entry.get() != username_admin and password_entry.get() == userpass_admin and conform_password.get() == userpass_admin:
        tkmb.showerror("Error", "Login is wrong")

    elif login_entry.get() == username_admin and password_entry.get() != userpass_admin and conform_password.get() != userpass_admin:
        tkmb.showerror("Error", "Password is wrong")

    elif login_entry.get() == username_admin and password_entry.get() == userpass_admin and conform_password.get() != userpass_admin:
        tkmb.showerror("Error", "Conformation password was entered incorrectly")


window = ctk.CTk()
window.geometry('500x500')
window.title("Login")

frame = ctk.CTkFrame(master=window)
frame.pack(pady=20, padx=40, fill='both', expand=True)

Label1 = ctk.CTkLabel(window, text="LOGIN ACCOUNT")
Label1.pack(pady=20, padx=10)

login_entry = ctk.CTkEntry(frame, placeholder_text="Enter username")
login_entry.pack(pady=20, padx=10)

password_entry = ctk.CTkEntry(frame, placeholder_text="Enter password", show="*")
password_entry.pack(pady=20, padx=10)

conform_password = ctk.CTkEntry(frame, placeholder_text="Re-Enter password", show="*")
conform_password.pack(pady=20, padx=10)

Register_button = ctk.CTkButton(frame, text="Don't have an account? Register now!", command=register)
Register_button.pack(pady=20, padx=10)

Submit_button = ctk.CTkButton(frame, text="Submit", command=submit)
Submit_button.pack(pady=20, padx=10)

window.mainloop()