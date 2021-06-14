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
      
      #string variable for the entry, and set value to the entry
      varQuantity1 = StringVar()
      varQuantity1.set("266")
      varQuantity2 = StringVar()
      varQuantity2.set("111")
      varQuantity3 = StringVar()
      varQuantity3.set("246")
      varQuantity4 = StringVar()
      varQuantity4.set("154")
      varQuantity5 = StringVar()
      varQuantity5.set("508")
      varQuantity6 = StringVar()
      varQuantity6.set("0")
      varQuantity7 = StringVar()
      varQuantity7.set("0")
      varQuantity8 = StringVar()
      varQuantity8.set("0")
      varQuantity9 = StringVar()
      varQuantity9.set("0")
      varQuantity10 = StringVar()
      varQuantity10.set("0")     
      
      varQuantity11 = StringVar()
      varQuantity11.set("420")
      varQuantity12 = StringVar()
      varQuantity12.set("0")
      varQuantity13 = StringVar()
      varQuantity13.set("138")
      varQuantity14 = StringVar()
      varQuantity14.set("0")
      varQuantity15 = StringVar()
      varQuantity15.set("252")
      varQuantity16 = StringVar()
      varQuantity16.set("0")  
      varQuantity17 = StringVar()
      varQuantity17.set("341") 
      varQuantity18 = StringVar()
      varQuantity18.set("0")    
      varQuantity19 = StringVar()
      varQuantity19.set("90") 
      varQuantity20 = StringVar()
      varQuantity20.set("0") 
      varQuantity21 = StringVar()
      varQuantity21.set("220")  
      varQuantity22 = StringVar()
      varQuantity22.set("0") 
      varQuantity23 = StringVar()
      varQuantity23.set("1220")  
      varQuantity24 = StringVar()
      varQuantity24.set("0")       
      
           
      
      #Entry widget
      self.e1 = Entry(self.Homepage, textvariable = varQuantity1, state = DISABLED)
      self.e1.grid(row=2, column = 1)   
      
      self.e2 = Entry(self.Homepage, textvariable = varQuantity2, state = DISABLED)
      self.e2.grid(row=3, column = 1)   
      
      self.e3 = Entry(self.Homepage, textvariable = varQuantity3, state = DISABLED)
      self.e3.grid(row=4, column = 1)   
             
      self.e4 = Entry(self.Homepage, textvariable = varQuantity4, state = DISABLED)
      self.e4.grid(row=5, column = 1)      
       
      self.e5 = Entry(self.Homepage, textvariable =  varQuantity5, state = DISABLED)
      self.e5.grid(row=6, column = 1)      
      
      self.e6 = Entry(self.Homepage, textvariable= varQuantity6, state = DISABLED)
      self.e6.grid(row=2, column = 2)      
      
      self.e7 = Entry(self.Homepage, textvariable= varQuantity7, state = DISABLED)
      self.e7.grid(row=3, column = 2)      
      
       
      self.e8 = Entry(self.Homepage, textvariable= varQuantity8, state = DISABLED)
      self.e8.grid(row=4, column = 2)      
      
      self.e9 = Entry(self.Homepage, textvariable= varQuantity9, state = DISABLED)
      self.e9.grid(row=5, column = 2)   
      
      self.e10 = Entry(self.Homepage, textvariable= varQuantity10, state = DISABLED)
      self.e10.grid(row=6, column = 2)   
      
      self.e11 = Entry(self.Homepage, textvariable = varQuantity11, state = DISABLED)
      self.e11.grid(row =7, column =1)
      
      self.e12 = Entry(self.Homepage, textvariable = varQuantity12, state = DISABLED)
      self.e12.grid(row = 7, column =2)
      
      self.e13 = Entry(self.Homepage, textvariable = varQuantity13, state = DISABLED)
      self.e13.grid(row= 8, column =1)
      
      self.e14 = Entry(self.Homepage, textvariable = varQuantity14, state = DISABLED)
      self.e14.grid(row = 8, column =2)
      
      self.e15 = Entry(self.Homepage, textvariable = varQuantity15, state = DISABLED)
      self.e15.grid(row= 9, column =1)
      
      self.e16 = Entry(self.Homepage, textvariable = varQuantity16, state = DISABLED)
      self.e16.grid(row = 9, column =2)     
      
      self.e17 = Entry(self.Homepage, textvariable = varQuantity17, state = DISABLED)
      self.e17.grid(row= 10, column =1)
      
      self.e18 = Entry(self.Homepage, textvariable = varQuantity18, state = DISABLED)
      self.e18.grid(row = 10, column =2)
      
      self.e19 = Entry(self.Homepage, textvariable = varQuantity19, state = DISABLED)
      self.e19.grid(row= 11, column =1)
      
      self.e20 = Entry(self.Homepage, textvariable = varQuantity20, state = DISABLED)
      self.e20.grid(row = 11, column =2)     
      
      self.e21 = Entry(self.Homepage, textvariable = varQuantity21, state = DISABLED)
      self.e21.grid(row = 12, column =1)
      
      self.e22 = Entry(self.Homepage, textvariable = varQuantity22, state = DISABLED)
      self.e22.grid(row = 12, column =2)   
      
      self.e23 = Entry(self.Homepage, textvariable = varQuantity23, state = DISABLED)
      self.e23.grid(row = 13, column =1)
      
      self.e24 = Entry(self.Homepage, textvariable = varQuantity24, state = DISABLED)
      self.e24.grid(row = 13, column =2)      
      
      
      self.view = ttk.Button(self.Homepage, text = "Next", command= self.show_view)
      self.view.grid(row = 1, column = 3)      
            
      
      #create another frame
      self.calculate = Frame(parent)
      self.title_label_1 = Label(self.calculate, text = "calculate calory", bg = "blue", fg = "white", width = 80, padx = 90, pady = 20, font = ("Time", '14', "bold italic"))
      self.title_label_1.grid(columnspan = 10)          
      self.cal = ttk.Button(self.calculate, text="Add", command=self.show).grid(row = 2, column = 3)
      
           
      cols = ('item', 'price', 'qty', 'total') 
      self.listBox = ttk.Treeview(self.calculate, column = cols, show='headings')
      
      #add the header into the treeview diagram
      for col in cols:
         self.listBox.heading(col, text=col)
         self.listBox.grid(row=1, column=0, columnspan=10)
         self.listBox.grid(row =1, column = 0)      
             
  
      
          #------------------------------- --------------------------------
      
                
          #------------------------------- --------------------------------
          
      l1 = Label(self.Homepage, text = 'To-Do List')
      l2 = Label(self.Homepage, text='Enter task title: ')
      a1 = Label(self.Homepage, text = "Calories amount KJ:")
      a2 = Label(self.Homepage, text = "Quantity:")
   
             
   
          #Place geometry
      
      a1.grid(row=1, column =1)
      a2.grid(row=1, column = 2)      
      
      
      

   
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


