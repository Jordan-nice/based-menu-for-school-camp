from tkinter import*
from random import*
from tkinter import ttk
import sqlite3
from tkinter import messagebox





class CampProgram:
   
   def __init__ (self, parent): 
      self.root = root
      self.root.configure(background='blue')
      self.Welcome = Frame(parent)
      self.Welcome.grid(row=0, column=0)
      self.title_label = Label(self.Welcome, text = "Welcome to the School Camp Menu  program", bg = "blue", fg = "white", width = 80, padx = 90, pady = 20, font = ("Time", '14', "bold italic"))
      self.title_label.grid(columnspan = 4)
      self.NextButton = ttk.Button(self.Welcome, text = 'Next', command = self.homepage)
      self.NextButton.grid(row=8, column=2)
      self.introduction = Label(self.Welcome, text = '''Hello, this is a based-menu planning programme, you can choose 
      differnt kinds of foods from the list to create your own menu for the 
      school camp.
      ''') 
      
      
          
      
      self.introduction.grid(row = 3, column =1)
      self.introduction1 = Label(self.Welcome, text = 'Please input your name and school while continue the process.')
      self.introduction1.grid(row = 4, column =1)
      self.username = Label(self.Welcome, text = 'username:')
      self.username.grid(row = 5, column= 1)
      self.password = Label(self.Welcome, text = 'password:')
      self.password.grid(row = 6, column = 1)
      self.username_entry = Entry(self.Welcome, width = 20)
      self.username_entry.grid(row =5, column = 2)
      self.password_entry = Entry(self.Welcome, width= 20, show = "*")
      self.password_entry.grid(row = 6, column =2)
      self.register = ttk.Button(self.Welcome, text = "register", command = self.register_form)
      self.register.grid(row = 8, column =3)
      self.Homepage = Frame(parent)
      
      
     #self.Homepage.grid(row =0, column = 0)      
      self.title_label_1 = Label(self.Homepage, text = "homepage", bg = "blue", fg = "white", width = 80, padx = 90, pady = 20, font = ("Time", '14', "bold italic"))
      self.title_label_1.grid(columnspan = 10)
      
      menu_list = Label(self.Homepage, text = "choose ingradients to make up your menu:")
      menu_list.grid(row = 1, column =0 )
      
      
      self.var1 = IntVar()
      Checkbutton(self.Homepage, text="Pizza", variable=self.var1, command = self.disable).grid(row=2, column = 0, sticky = W)

       
       
      self.var2 = IntVar()
      Checkbutton(self.Homepage, text="BBQ pork Bun", variable=self.var2, command = self.disable1).grid(row=3, column = 0, sticky = W)
       
       
      self.var3 = IntVar()
      Checkbutton(self.Homepage, text="Chicken Fry", variable=self.var3, command = self.disable2).grid(row=4, column = 0, sticky = W)
       
       
      self.var4 = IntVar()
      Checkbutton(self.Homepage, text="Spring Roll", variable=self.var4, command = self.disable3).grid(row=5, column = 0, sticky = W)
       
      self.var5 = IntVar()
      Checkbutton(self.Homepage, text=" Fish Fried Rice  ", variable=self.var5, command = self.disable4).grid(row=6, column = 0, sticky = W)   

      self.var6 = IntVar()
      Checkbutton(self.Homepage, text=" Hotpot  ", variable=self.var6, command = self.disable5).grid(row=7, column = 0, sticky = W) 
      
      self.var7 = IntVar()
      Checkbutton(self.Homepage, text=" Noodle  ", variable=self.var7, command = self.disable6).grid(row=8, column = 0, sticky = W) 
      
      self.var8 = IntVar()
      Checkbutton(self.Homepage, text=" Sushi  ", variable=self.var8, command = self.disable7).grid(row=9, column = 0, sticky = W) 
      
      self.var9 = IntVar()
      Checkbutton(self.Homepage, text=" Paella ", variable=self.var9, command = self.disable8).grid(row=10, column = 0, sticky = W)       
      
      self.var10 = IntVar()
      Checkbutton(self.Homepage, text=" Kimchi  ", variable=self.var10, command = self.disable9).grid(row=11, column = 0, sticky = W)     
      
      self.var11 = IntVar()
      Checkbutton(self.Homepage, text=" Fries Salmon fish  ", variable=self.var11, command = self.disable10).grid(row=12, column = 0, sticky = W)
      
      self.var12 = IntVar()
      Checkbutton(self.Homepage, text=" Cheeseburger with fries  ", variable=self.var12, command = self.disable11).grid(row=13, column = 0, sticky = W)      
      
     
   
   #login system
   def homepage(self):
      self.database()
      self.lbl_result1 = Label(self.Welcome, text="", font=('arial', 10))
      self.lbl_result1.grid(row=10, columnspan=2, column = 2)         
      if self.username_entry.get() == "" or self.password_entry.get() == "":
         self.lbl_result1.config(text="Please complete the request for enter the information!", fg="orange")
      else:
         cursor.execute("SELECT * FROM `member` WHERE `username` = ? and `password` = ?", (self.username_entry.get(), self.password_entry.get()))
         if cursor.fetchone() is not None:
            self.Welcome.grid_remove()
            self.Homepage.grid()
         else:
            self.lbl_result1.config(text="Invalid Username or password", fg="red")
                      
         
         
   
   
         
   # store the user information to the database
   def register_form(self):
     
      self.RegisterFrame = Toplevel(root)
      self.RegisterFrame.grid()
      self.USERNAME = StringVar()
      self.PASSWORD = StringVar()      
      lbl_username = Label(self.RegisterFrame, text="Username:", font=('arial', 18), bd=18)
      lbl_username.grid(row=1)
      lbl_password = Label(self.RegisterFrame, text="Password:", font=('arial', 18), bd=18)
      lbl_password.grid(row=2)
      self.lbl_result2 = Label(self.RegisterFrame, text="", font=('arial', 18))
      self.lbl_result2.grid(row=5, columnspan=2)      
      username1 = Entry(self.RegisterFrame, font=('arial', 20), textvariable=self.USERNAME, width=15)
      username1.grid(row=1, column=1)
      password1 = Entry(self.RegisterFrame, font=('arial', 20), textvariable=self.PASSWORD, width=15, show="*")
      password1.grid(row=2, column=1)
         
      btn_login = Button(self.RegisterFrame, text="Register", font=('arial', 18), width=35, command=self.Register)
      btn_login.grid(row=6, columnspan=2, pady=20)
   
   
   def login(self):
      RegisterFrame.destroy()
      self.Welcome()   
   
   #create a function for the user to register
   def Register(self):
      self.database()
      if self.USERNAME.get == "" or self.PASSWORD.get() == "":
         self.lbl_result2.config(text="Please complete the required field!", fg="orange")
      else:
         cursor.execute("SELECT * FROM `member` WHERE `username` = ?", (self.USERNAME.get(),))
         if cursor.fetchone() is not None:
            self.lbl_result2.config(text="Username is already taken", fg="red")
         else:
            cursor.execute("INSERT INTO `member` (username, password) VALUES(?, ?)", (str(self.USERNAME.get()), str(self.PASSWORD.get())))
            conn.commit()
            self.USERNAME.set("")
            self.PASSWORD.set("")
               
            self.lbl_result2.config(text="Successfully Created!", fg="black")
            cursor.close()
            conn.close()   
   
   #create a database to store the information of the 
   def database(self):
      global conn, cursor
      conn = sqlite3.connect("db_member.db")
      cursor = conn.cursor()
      cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, firstname TEXT, lastname TEXT)")
             
      
         
      
# main routine
if __name__ == "__main__":
   root = Tk()
   root.geometry("1140x500+0+0")
   frames = CampProgram(root)
   root.title("school camp program")
   root.mainloop()


