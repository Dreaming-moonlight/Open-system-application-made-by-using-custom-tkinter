import customtkinter as ctk
import tkinter.messagebox as tkmb
import os
from PIL import Image

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

admin_username = ["admin1", "admin2", "admin3", "admin4"]
admin_password = ["admin"]

print("-------------------------------------------------------------------------------")

print("-------------------------------INSTRUCTIONS------------------------------------")
print("#If you are a admin login here, if you are just a user then double click on enter key")
print("#After registration enter data in the list given in the code in line 13 and 14")
print("#If you are a admin and want to login as a user click the close button on the top right corner of the GUI")

print("-------------------------------------------------------------------------------")

username_admin = input("Enter admin username: ")
userpass_admin = input("Enter admin password: ")

users = ["Tejesh", "Common user"]
password = ['1234', "4321"]

def getFolderPath():
    os.startfile("D:\Tejesh Folder\Tejesh folder\wallpaper\Scenary")


if username_admin in admin_username and userpass_admin in admin_password:

    def admin_review_page():

            new_page = ctk.CTk()
            new_page.title("Logged in as admin")

            new_page.geometry("600x900")

            admin_area_frame = ctk.CTkFrame(master=new_page)
            admin_area_frame.pack(pady=20, padx=40, fill='both', expand=True)

            label_say_admin = ctk.CTkLabel(admin_area_frame, text="ADMIN REVIEWS")
            label_say_admin.pack(pady=20, padx=10)

            write_something = ctk.CTkOptionMenu(admin_area_frame,
                                                values=["Admin1", "Admin2", "Admin3", "Admin4"])
            write_something.pack(pady=20, padx=10)

            scroll_bar = ctk.CTkProgressBar(master=admin_area_frame)
            scroll_bar.pack(pady=20, padx=10)

            scroll_bar.configure(fg_color="black", progress_color="white")
            scroll_bar.set(value=0.5)

            experience_frame = ctk.CTkFrame(master=admin_area_frame)
            experience_frame.pack(pady=20, padx=40, fill='both')

            rating_label = ctk.CTkLabel(experience_frame, text="Rate your experience")
            rating_label.pack(pady=20, padx=10)

            rating_slider = ctk.CTkSlider(experience_frame)
            rating_slider.pack(pady=20, padx=10)

            star_label = ctk.CTkLabel(experience_frame, text="1 star    2 star    3 star    4 star    5 star")
            star_label.pack(pady=20, padx=10)

            frame_admin = ctk.CTkFrame(master=admin_area_frame)
            frame_admin.pack(pady=20, padx=40)

            label_admin = ctk.CTkLabel(frame_admin, text="Hey Admin")
            label_admin.pack(pady=20, padx=10)

            ask_admin = ctk.CTkLabel(frame_admin, text="Want to view some nature images?")
            ask_admin.pack(pady=20, padx=10)

            info = ctk.CTkLabel(frame_admin, text="#Hit exit button to end process correctly")
            info.pack(pady=20, padx=10)

            button = ctk.CTkButton(frame_admin, text="View images", command=getFolderPath)
            button.pack(pady=20, padx=10)

            exit_button = ctk.CTkButton(frame_admin, text="Exit", command=lambda: {exit()})
            exit_button.pack(pady=20, padx=10)

            submit_button = ctk.CTkButton(frame_admin, text="Submit", command=submit)
            submit_button.pack(pady=20, padx=10)

            new_page.mainloop()


    def submit():

        submitted_page = ctk.CTk()

        submitted_page.title("Submitted review")

        submitted_page.geometry('400x400')

        frame7 = ctk.CTkFrame(master=submitted_page)
        frame7.pack(pady=40, padx=20, fill='both', expand=True)

        Label_submitted_page = ctk.CTkLabel(frame7, text="Submitted your review successfully")
        Label_submitted_page.pack(pady=20, padx=10)

        submitted_page.mainloop()


    workspace = ctk.CTk()

    workspace.title("Admin main workspace")

    workspace.geometry('600x700')

    workspace_frame = ctk.CTkFrame(master=workspace)
    workspace_frame.pack(pady=20, padx=40, fill='both', expand=True)

    Image = ctk.CTkImage(dark_image=Image.open("D:\icon.png"))

    button_review = ctk.CTkButton(workspace_frame, text="Found bug?, send review to developer", command=admin_review_page, image=Image)
    button_review.pack(pady=20, padx=10)

    close_btn = ctk.CTkButton(workspace_frame, text="Close workspace", command=lambda:{[exit()]})
    close_btn.pack(pady=20, padx=10)

    workspace.mainloop()


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
                    frame6.pack(pady=20, padx=40)

                    Label = ctk.CTkLabel(frame6, text="Submitted successfully")
                    Label.pack(pady=20, padx=10)

            review_page = ctk.CTkToplevel(reg_page)

            review_page.title("Write review")

            review_page.geometry("500x500")

            frame5 = ctk.CTkFrame(master=review_page)
            frame5.pack(pady=20, padx=40)

            Label_review = ctk.CTkLabel(frame5, text="Write review")
            Label_review.pack(pady=20, padx=10)

            Label_entry = ctk.CTkEntry(frame5, placeholder_text="Write review")
            Label_entry.pack(pady=20, padx=10)

            submit_btn_2 = ctk.CTkButton(review_page, text="Send", command=check)
            submit_btn_2.pack(pady=20, padx=40)

            cancel_button = ctk.CTkButton(review_page, text="Cancel", command=lambda:{exit()})
            cancel_button.pack(pady=20, padx=40)

        reg_page = ctk.CTkToplevel(register_page)

        reg_page.title("Review page")

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
        frame4.pack(pady=20, padx=40)

        label_reg = ctk.CTkLabel(frame4, text="Interested to write a review?")
        label_reg.pack(pady=20, padx=10)

        Review_button = ctk.CTkButton(frame4, text="Write a review", command=write_review)
        Review_button.pack(pady=20, padx=10)

        cancel_button_2 = ctk.CTkButton(frame4, text="Cancel", command=lambda:{exit()})
        cancel_button_2.pack(pady=20, padx=10)


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
    register_label.pack(pady=20, padx=10)

    register_entry = ctk.CTkEntry(frame3, placeholder_text="New Username")
    register_entry.pack(pady=20, padx=10)

    register_password = ctk.CTkEntry(frame3, placeholder_text="Enter new password", show="*")
    register_password.pack(pady=20, padx=10)

    conform_password2 = ctk.CTkEntry(frame3, placeholder_text="Re-Enter password", show="*")
    conform_password2.pack(pady=20, padx=10)

    register_btn = ctk.CTkButton(frame3, text="Register", command=reg)
    register_btn.pack(pady=20, padx=10)

def submit():

    if login_entry.get() in users and password_entry.get() in password and conform_password.get() in password:
        tkmb.showinfo(title="Login granted", message="You are authorized")

        submit_page = ctk.CTkToplevel(window)

        submit_page.title("Authentication")

        submit_page.geometry("500x500")

        frame = ctk.CTkFrame(master=submit_page)
        frame.pack(pady=20, padx=40)

        label_submit_page = ctk.CTkLabel(frame, text="Logged in as user")
        label_submit_page.pack(pady=20, padx=10)

    elif login_entry.get() not in users and password_entry.get() in password and conform_password.get() in password:
        tkmb.showerror("Error", "Login is wrong")

    elif login_entry.get() in users and password_entry.get() not in password and conform_password.get() not in password:
        tkmb.showerror("Error", "Password is wrong")

    elif login_entry.get() in users and password_entry.get() in password and conform_password.get() not in password:
        tkmb.showerror("Error", "Conformation password was entered incorrectly")

    elif login_entry.get() == "" and password_entry.get() == "" and conform_password.get() == "":
        tkmb.showerror("Error", "All details are blank")


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
