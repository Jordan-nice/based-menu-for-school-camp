from tkinter import*
from random import*
from tkinter import ttk
import sqlite3 as sq
import tkinter.messagebox as tkMessageBox





class CampProgram:
   
   def __init__ (self, parent): 
      self.root = root
      self.root.configure(background='red')
      self.Welcome = Frame(parent)
      self.Welcome.grid(row=0, column=0)
      self.TittleLabel = Label(self.Welcome, text = "Welcome to the School Camp Menu  program", bg = "red", fg = "white", width = 90, padx = 105, pady = 20, font = ("Time", '14', "bold italic"))
      self.TittleLabel.grid(columnspan = 4)
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
      self.schoolname = Label(self.Welcome, text = 'school name:')
      self.schoolname.grid(row = 6, column = 1)
      self.username_entry = Entry(self.Welcome, width = 20)
      self.username_entry.grid(row =5, column = 2)
      self.schoolname_entry = Entry(self.Welcome, width= 20)
      self.schoolname_entry.grid(row = 6, column =2)
      
      self.Homepage = Frame(parent)
      
     #self.Homepage.grid(row =0, column = 0)      
      self.TittleLabel_1 = Label(self.Homepage, text = "homepage", bg = "red", fg = "white", width = 90, padx = 105, pady = 20, font = ("Time", '14', "bold italic"))
      self.TittleLabel_1.grid(columnspan = 10)
      
      menu_list = Label(self.Homepage, text = '''choose ingradients to make up your menu''')
      menu_list.grid(row = 1, column =0 )
      
   
      
      

      
      #========================================VARIABLES========================================
      USERNAME = StringVar()
      PASSWORD = StringVar()
      PRODUCT_NAME = StringVar()
      PRODUCT_PRICE = IntVar()
      PRODUCT_QTY = IntVar()
      SEARCH = StringVar()      
      
      
      
          #------------------------------- Functions--------------------------------
      def Database():
         global conn, cursor
         conn = sq.connect("python1.db")
         cursor = conn.cursor()
         cursor.execute("CREATE TABLE IF NOT EXISTS `admin` (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
         cursor.execute("CREATE TABLE IF NOT EXISTS `product` (product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, product_name TEXT, product_qty TEXT, product_price TEXT)")
         cursor.execute("SELECT * FROM `admin` WHERE `username` = 'admin' AND `password` = 'admin'")
         if cursor.fetchone() is None:
            cursor.execute("INSERT INTO `admin` (username, password) VALUES('admin', 'admin')")
            conn.commit()
            
      def ShowAddItem():
         global loginform
         loginform = Toplevel()
         loginform.title("Add items into menu")
         width = 600
         height = 500
         screen_width = root.winfo_screenwidth()
         screen_height = root.winfo_screenheight()
         x = (screen_width/2) - (width/2)
         y = (screen_height/2) - (height/2)
         loginform.resizable(0, 0)
         loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
         modifymainmenu()      
          
      def modifymainmenu():
         TopLoginForm = Frame(loginform, width=600, height=100, bd=1, relief=SOLID)
         TopLoginForm.pack(side=TOP, pady=20)
         lbl_text = Label(TopLoginForm, text="Administrator Login", font=('arial', 18), width=600)
         lbl_text.pack(fill=X)
         MidLoginForm = Frame(loginform, width=600)
         MidLoginForm.pack(side=TOP, pady=50)
         lbl_username = Label(MidLoginForm, text="Username:", font=('arial', 25), bd=18)
         lbl_username.grid(row=0)
         lbl_password = Label(MidLoginForm, text="Password:", font=('arial', 25), bd=18)
         lbl_password.grid(row=1)
         lbl_result = Label(MidLoginForm, text="", font=('arial', 18))
         lbl_result.grid(row=3, columnspan=2)
         username = Entry(MidLoginForm, textvariable=USERNAME, font=('arial', 25), width=15)
         username.grid(row=0, column=1)
         password = Entry(MidLoginForm, textvariable=PASSWORD, font=('arial', 25), width=15, show="*")
         password.grid(row=1, column=1)
         btn_login = Button(MidLoginForm, text="Login", font=('arial', 18), width=30, command=Login)
         btn_login.grid(row=2, columnspan=2, pady=20)
         btn_login.bind('<Return>', Login)
         

         
      
      def ShowAddNew():
         global addnewform
         addnewform = Toplevel()
         addnewform.title("view menu programme")
         height = 500
         width = 600
         screen_width = root.winfo_screenwidth()
         screen_height = root.winfo_screenheight()
         x = (screen_width/2) - (width/2)
         y = (screen_height/2) - (height/2)
         addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
         addnewform.resizable(0, 0)
         AddNewForm()
      
      def AddNewForm():
         TopAddNew = Frame(addnewform, width=600, height=100, bd=1, relief=SOLID)
         TopAddNew.pack(side=TOP, pady=20)
         lbl_text = Label(TopAddNew, text="Add New Product", font=('arial', 18), width=600)
         lbl_text.pack(fill=X)
         MidAddNew = Frame(addnewform, width=600)
         MidAddNew.pack(side=TOP, pady=40)
         lbl_productname = Label(MidAddNew, text="Cuisine Name:", font=('arial', 25), bd=10)
         lbl_productname.grid(row=0, sticky=W)
         lbl_qty = Label(MidAddNew, text="Calory amount: ", font=('arial', 25), bd=10)
         lbl_qty.grid(row=1, sticky=W)
         lbl_price = Label(MidAddNew, text="Protein Amount:", font=('arial', 25), bd=10)
         lbl_price.grid(row=2, sticky=W)
         productname = Entry(MidAddNew, textvariable=PRODUCT_NAME, font=('arial', 25), width=15)
         productname.grid(row=0, column=1)
         productqty = Entry(MidAddNew, textvariable=PRODUCT_QTY, font=('arial', 25), width=15)
         productqty.grid(row=1, column=1)
         productprice = Entry(MidAddNew, textvariable=PRODUCT_PRICE, font=('arial', 25), width=15)
         productprice.grid(row=2, column=1)
         btn_add = Button(MidAddNew, text="Save", font=('arial', 18), width=30, bg="red", command=AddNew)
         btn_add.grid(row=3, columnspan=2, pady=20)
         btn_view = Button(MidAddNew, text="view menu", font=('arial', 18), width=30, bg="red", command=ShowView)
         btn_view.grid(row = 4, columnspan =2, pady =20)
         
      
      def AddNew():
         Database()
         cursor.execute("INSERT INTO `product` (product_name, product_qty, product_price) VALUES(?, ?, ?)", (str(PRODUCT_NAME.get()), int(PRODUCT_QTY.get()), int(PRODUCT_PRICE.get())))
         conn.commit()
         PRODUCT_NAME.set("")
         PRODUCT_PRICE.set("")
         PRODUCT_QTY.set("")
          
      def ShowView():
         global viewform
         viewform = Toplevel()
         viewform.title("view the menu")
         width = 1300
         height = 710
         screen_width = root.winfo_screenwidth()
         screen_height = root.winfo_screenheight()
         x = (screen_width/2) - (width/2)
         y = (screen_height/2) - (height/2)
         viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
         viewform.resizable(0, 0)
         ViewForm()
      
      
      
      def ViewForm():
         global tree
         TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
         TopViewForm.pack(side=TOP, fill=X)         
         lbl_text = Label(TopViewForm, text="View menu", font=('arial', 18), width=600)
         lbl_text.pack(fill=X)         
         LeftViewForm = Frame(viewform, width=600)
         LeftViewForm.pack(side=LEFT, fill=Y)
         MidViewForm = Frame(viewform, width=600)
         MidViewForm.pack(side=RIGHT, fill=X)
         lbl_txtsearch = Label(MidViewForm, text="Search", font=('arial', 15))
         lbl_txtsearch.pack(side=TOP, anchor=W)
         search = Entry(MidViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
         search.pack(side=TOP,   padx=10, fill=X)
         btn_search = Button(MidViewForm, text="Search", command=Search)
         btn_search.pack(side=TOP,padx=10, pady=10, fill=X)
         btn_reset = Button(MidViewForm, text="Reset", command=Reset)
         btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
         btn_delete = Button(MidViewForm, text="Delete", command=Delete)
         btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
         homepage = Button(MidViewForm, text = "confirm ")
         homepage.pack()
         scrollbary = Scrollbar(LeftViewForm, orient=VERTICAL)
         tree = ttk.Treeview(LeftViewForm, columns=("ProductID", "Product Name", "Product Qty", "Product Price"), selectmode="extended", height=100, yscrollcommand=scrollbary.set)
         scrollbary.config(command=tree.yview)
         scrollbary.pack(side=RIGHT, fill=Y)
         m1 = Button(LeftViewForm, text = 'Add food to main menu', font=('arial', 18), width=20, bg = "red", command=ShowAddNew)
         m1.pack()
         tree.heading('ProductID', text="CuisineID",anchor=W)
         tree.heading('Product Name', text="Cuisine Name",anchor=W)
         tree.heading('Product Qty', text="Calories ammount(kj)",anchor=W)
         tree.heading('Product Price', text="Protein amount(g)",anchor=W)
         tree.column('#0', stretch=NO, minwidth=0, width=0)
         tree.column('#1', stretch=NO, minwidth=0, width=0)
         tree.column('#2', stretch=NO, minwidth=0, width=200)
         tree.column('#3', stretch=NO, minwidth=0, width=180)
         tree.column('#4', stretch=NO, minwidth=0, width=160)
         tree.pack()
         DisplayData()    
         
         
         
      
      def DisplayData(self):
         Database()
         cursor.execute("SELECT * FROM `product`")
         fetch = cursor.fetchall()
         for data in fetch:
            tree.insert('', 'end', values=(data))
   
          
      def Search():
          if SEARCH.get() != "":
              tree.delete(*tree.get_children())
              Database()
              cursor.execute("SELECT * FROM `product` WHERE `product_name` LIKE ?", ('%'+str(SEARCH.get())+'%',))
              fetch = cursor.fetchall()
              for data in fetch:
                  tree.insert('', 'end', values=(data))
              cursor.close()
              conn.close()

            
      def Reset():
          tree.delete(*tree.get_children())
          DisplayData()
          SEARCH.set("")
      
      def Delete():
          if not tree.selection():
             print("ERROR")
          else:
              result = tkMessageBox.askquestion('base-menu system', 'Are you sure you want to delete this record?', icon="warning")
              if result == 'yes':
                  curItem = tree.focus()
                  contents =(tree.item(curItem))
                  selecteditem = contents['values']
                  tree.delete(curItem)
                  Database()
                  cursor.execute("DELETE FROM `product` WHERE `product_id` = %d" % selecteditem[0])
                  conn.commit()
                  cursor.close()
                  conn.close()
                    
          
          
       
      
          
          
          
          
          
      
      
                
          #------------------------------- Functions--------------------------------
          
      l1 = Label(self.Homepage, text = 'To-Do List')
      l2 = Label(self.Homepage, text='Enter task title: ')
      e1 = Entry(self.Homepage, width=21)
      t = Button(self.Homepage, text = "show menu", command = ShowView)
      
      t1 = Listbox(self.Homepage, height=11, width =100, selectmode='SINGLE')
      
      
      
   
          #Place geometry
      
      e1.grid(row=1, column =1)
      
      t.grid(row = 2, column = 0)
      t1.grid(row =2, column =3)
      
      
          

      
      
   def homepage(self):
      self.schoolname_entry.get()
      self.username_entry.get()
      if self.username_entry.get() == "":
         if self.schoolname_entry.get() == "":
            print("Please enter school name")
         pass
         print("please enter username")
      else:      
         print("incorrect")
         self.Welcome.grid_remove()
         self.Homepage.grid()         
   
         

if __name__ == "__main__":
   root = Tk()
   root.geometry("1250x550+0+0")
   frames = CampProgram(root)
   root.title("based-menu planning program")
   root.mainloop()


