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
      
      
      
   #----------------------function to disable and enable the checkbutton---------------
   def disable(self):
      if self.var1.get() == 0:
         self.e6.config(state =DISABLED)
      elif self.var1.get() == 1:
         self.e6.config(state = NORMAL)   
      else:
         pass
      
   def disable1(self):
      if self.var2.get() == 0:
         self.e7.config(state =DISABLED)
      elif self.var2.get() == 1:
         self.e7.config(state = NORMAL)   
      else:
         pass      

   def disable2(self):
      if self.var3.get() == 0:
         self.e8.config(state =DISABLED)
      elif self.var3.get() == 1:
         self.e8.config(state = NORMAL)   
      else:
         pass   

   def disable3(self):
      if self.var4.get() == 0:
         self.e9.config(state =DISABLED)
      elif self.var4.get() == 1:
         self.e9.config(state = NORMAL)   
      else:
         pass
      
   def disable4(self):
      if self.var5.get() == 0:
         self.e10.config(state =DISABLED)
      elif self.var5.get() == 1:
         self.e10.config(state = NORMAL)   
      else:
         pass
      
   def disable5(self):
      if self.var6.get() == 0:
         self.e12.config(state =DISABLED)
      elif self.var6.get() == 1:
         self.e12.config(state = NORMAL)   
      else:
         pass
      
   def disable6(self):
      if self.var7.get() == 0:
         self.e14.config(state =DISABLED)
      elif self.var7.get() == 1:
         self.e14.config(state = NORMAL)   
      else:
         pass      
    
   def disable7(self):
      if self.var8.get() == 0:
         self.e16.config(state =DISABLED)
      elif self.var8.get() == 1:
         self.e16.config(state = NORMAL)   
      else:
         pass
      
   def disable8(self):
      if self.var9.get() == 0:
         self.e18.config(state =DISABLED)
      elif self.var9.get() == 1:
         self.e18.config(state = NORMAL)   
      else:
         pass   
    
   def disable9(self):
      if self.var10.get() == 0:
         self.e20.config(state =DISABLED)
      elif self.var10.get() == 1:
         self.e20.config(state = NORMAL)   
      else:
         pass    
    
   def disable10(self):
      if self.var11.get() == 0:
         self.e22.config(state =DISABLED)
      elif self.var11.get() == 1:
         self.e22.config(state = NORMAL)   
      else:
         pass
      
   def disable11(self):
      if self.var12.get() == 0:
         self.e24.config(state =DISABLED)
      elif self.var12.get() == 1:
         self.e24.config(state = NORMAL)   
      else:
         pass      
      
      
   #---------------------------------------------------------------------------
    
      
      
   #calculate and print the result on the treeview diagram   
   def show(self):
         tot = 0         
         if (self.var1.get()):
            calories = int(self.e1.get())
            quantity = int(self.e6.get())
            self.tot = int(calories * quantity)
            tempList = [['Pizza', self.e1.get(), self.e6.get(), self.tot]]
            tempList.sort(key=lambda e: e[1], reverse=True)
            for i, (item, calories, quantity, self.tot) in enumerate(tempList, start=1):
               self.listBox.insert("", "end", values=(item, calories, quantity, self.tot))
       
         if (self.var2.get()):
            calories = int(self.e2.get())
            quantity = int(self.e7.get())
            self.tot = int(calories * quantity)
            tempList = [['Bun', self.e2.get(), self.e7.get(), self.tot]]
            tempList.sort(key=lambda e: e[1], reverse=True)
            for i, (item, calories, quantity, self.tot) in enumerate(tempList, start=1):
               self.listBox.insert("", "end", values=(item, calories, quantity, self.tot))
       
         if (self.var3.get()):
            calories = int(self.e3.get())
            quantity = int(self.e8.get())
            self.tot = int(calories * quantity)
            tempList = [['Chicken Fry', self.e3.get(), self.e8.get(), self.tot]]
            tempList.sort(key=lambda e: e[1], reverse=True)
            for i, (item, calories, quantity, self.tot) in enumerate(tempList, start=1):
               self.listBox.insert("", "end", values=(item, calories, quantity, self.tot))
      
         if (self.var4.get()):
            calories = int(self.e4.get())
            quantity = int(self.e9.get())
            self.tot = int(calories * quantity)
            tempList = [['spring roll', self.e4.get(), self.e9.get(), self.tot]]
            tempList.sort(key=lambda e: e[1], reverse=True)
            for i, (item, calories, quantity, self.tot) in enumerate(tempList, start=1):
               self.listBox.insert("", "end", values=(item, calories, quantity, self.tot))
       
         if (self.var5.get()):
            calories = int(self.e5.get())
            quantity = int(self.e10.get())
            self.tot = int(calories * quantity)
            tempList = [['Fish Fried Rice', self.e5.get(), self.e10.get(), self.tot]]
            tempList.sort(key=lambda e: e[1], reverse=True)
            for i, (item, calories, quantity, self.tot) in enumerate(tempList, start=1):
               self.listBox.insert("", "end", values=(item, calories, quantity, self.tot))
               
            
         if (self.var6.get()):
            calories = int(self.e11.get())
            quantity = int(self.e12.get())
            self.tot = int(calories * quantity)
            tempList = [['Hotpot', self.e11.get(), self.e12.get(), self.tot]]
            tempList.sort(key=lambda e: e[1], reverse=True)
            for i, (item, calories, quantity, self.tot) in enumerate(tempList, start=1):
               self.listBox.insert("", "end", values=(item, calories, quantity, self.tot))
            
            
         if (self.var7.get()):
            calories = int(self.e13.get())
            quantity = int(self.e14.get())
            self.tot = int(calories * quantity)
            tempList = [['Noodle', self.e13.get(), self.e14.get(), self.tot]]
            tempList.sort(key=lambda e: e[1], reverse=True)
            for i, (item, calories, quantity, self.tot) in enumerate(tempList, start=1):
               self.listBox.insert("", "end", values=(item, calories, quantity, self.tot))
               
         if (self.var8.get()):
            calories = int(self.e15.get())
            quantity = int(self.e16.get())
            self.tot = int(calories * quantity)
            tempList = [['Sushi', self.e15.get(), self.e16.get(), self.tot]]
            tempList.sort(key=lambda e: e[1], reverse=True)
            for i, (item, calories, quantity, self.tot) in enumerate(tempList, start=1):
               self.listBox.insert("", "end", values=(item, calories, quantity, self.tot))
               
         if (self.var9.get()):
            calories = int(self.e17.get())
            quantity = int(self.e18.get())
            self.tot = int(calories * quantity)
            tempList = [['Paella', self.e17.get(), self.e18.get(), self.tot]]
            tempList.sort(key=lambda e: e[1], reverse=True)
            for i, (item, calories, quantity, self.tot) in enumerate(tempList, start=1):
               self.listBox.insert("", "end", values=(item, calories, quantity, self.tot))
            
         if (self.var10.get()):
            calories = int(self.e19.get())
            quantity = int(self.e20.get())
            self.tot = int(calories * quantity)
            tempList = [['Kimchi', self.e19.get(), self.e20.get(), self.tot]]
            tempList.sort(key=lambda e: e[1], reverse=True)
            for i, (item, calories, quantity, self.tot) in enumerate(tempList, start=1):
               self.listBox.insert("", "end", values=(item, calories, quantity, self.tot))
            
            
         if (self.var11.get()):
            calories = int(self.e21.get())
            quantity = int(self.e22.get())
            self.tot = int(calories * quantity)
            tempList = [['Fried Salmon fish', self.e21.get(), self.e22.get(), self.tot]]
            tempList.sort(key=lambda e: e[1], reverse=True)
            for i, (item, calories, quantity, self.tot) in enumerate(tempList, start=1):
               self.listBox.insert("", "end", values=(item, calories, quantity, self.tot))
               
         if (self.var12.get()):
            calories = int(self.e23.get())
            quantity = int(self.e24.get())
            self.tot = int(calories * quantity)
            tempList = [['Cheeseburger with fries', self.e23.get(), self.e24.get(), self.tot]]
            tempList.sort(key=lambda e: e[1], reverse=True)
            for i, (item, calories, quantity, self.tot) in enumerate(tempList, start=1):
               self.listBox.insert("", "end", values=(item, calories, quantity, self.tot))
            
            
            
         self.totText = StringVar()
         balText = IntVar()         
             
         sum1 = 0.0               
         for child in self.listBox.get_children():
            sum1 += float(self.listBox.item(child, 'values')[3])
         self.totText.set(sum1)         
         
         
         
         self.tot = Entry(self.calculate, text="", font="arial 22 bold", textvariable=self.totText)
         self.tot.grid(row = 4, column = 1)
         self.showtotal = Label(self.calculate, text = "(Over 2800 is unhealthy)Total calories:", font = ("Time", '14', "bold italic"))
         self.showtotal.grid(row = 3, column =1)
         check_calories = ttk.Button(self.calculate, text = "check the healthness of your selection", command = self.check_calories)
         check_calories.grid(row= 4, column =2)
         
   def check_calories(self):
      if float(self.tot.get()) >= 2800:
         self.labeling = Label(self.calculate, text = "Your selection is exceeding the regular calories intake per day, please back to homepage and select the dishes again", fg = 'red')
         self.labeling.grid(row =5, column = 2)
         self.back_to_homepage = Button(self.calculate, text = "Back to homepage", command = self.back_homepage)
         self.back_to_homepage.grid(row = 5, column = 3)
      elif float(self.tot.get())==0.0:
         self.warn5= Label(self.calculate, text = "You did not select for the quantity, Please retry", fg ='red')
         self.warn5.grid(row = 5, column = 2)
         self.back_to_homepage1 = Button(self.calculate, text = "Back to homepage", command = self.back_homepage1)
         self.back_to_homepage1.grid(row = 5, column = 3)            
         
         
      else:
         success = Label(self.calculate, text = "You menu has been suceessfully added!!", fg = "green")
         success.grid(row = 5, column =2)
         print_recipt = Button(self.calculate, text = "  print recipt   ", command  = self.recipt)
         print_recipt.grid(row = 5, column = 3)
         log_out = Button(self.calculate, text = "log out", command = self.logout)
         log_out.grid(row = 6, column = 4)

   def show_view(self):
      if self.var1.get() == 0:
         self.w = Label(self.Homepage, text = "Please select food and quantity in the menu ", fg = 'red')
         self.w.grid(row = 3, column = 3)   
      else:
         self.Homepage.grid_remove()
         self.calculate.grid()     
         
         
      if self.var2.get() == 0:
         self.w = Label(self.Homepage, text = "Please select food and quantity in the menu ", fg = 'red')
         self.w.grid(row = 3, column = 3)   
      else:
         self.Homepage.grid_remove()
         self.calculate.grid()    
         
         
      if self.var3.get() == 0:
         self.w = Label(self.Homepage, text = "Please select food and quantity in the menu ", fg = 'red')
         self.w.grid(row = 3, column = 3)   
      else:
         self.Homepage.grid_remove()
         self.calculate.grid()    
         
         
      if self.var4.get() == 0:
         self.w = Label(self.Homepage, text = "Please select food and quantity in the menu ", fg = 'red')
         self.w.grid(row = 3, column = 3)   
      else:
         self.Homepage.grid_remove()
         self.calculate.grid()    
         
         
      if self.var5.get() == 0:
         self.w = Label(self.Homepage, text = "Please select food and quantity in the menu ", fg = 'red')
         self.w.grid(row = 3, column = 3)   
      else:
         self.Homepage.grid_remove()
         self.calculate.grid()    
         
         
      if self.var6.get() == 0:
         self.w = Label(self.Homepage, text = "Please select food and quantity in the menu ", fg = 'red')
         self.w.grid(row = 3, column = 3)   
      else:
         self.Homepage.grid_remove()
         self.calculate.grid()    
         
         
         
      if self.var7.get() == 0:
         self.w = Label(self.Homepage, text = "Please select the food in the menu ", fg = 'red')
         self.w.grid(row = 3, column = 3)   
      else:
         self.Homepage.grid_remove()
         self.calculate.grid()    
         
         
      if self.var8.get() == 0:
         self.w = Label(self.Homepage, text = "Please select food and quantity in the menu", fg = 'red')
         self.w.grid(row = 3, column = 3)   
      else:
         self.Homepage.grid_remove()
         self.calculate.grid()    
         
         
      if self.var9.get() == 0:
         self.w = Label(self.Homepage, text = "Please select food and quantity in the menu", fg = 'red')
         self.w.grid(row = 3, column = 3)   
      else:
         self.Homepage.grid_remove()
         self.calculate.grid()    
         
         
      if self.var10.get() == 0:
         self.w = Label(self.Homepage, text = "Please select food and quantity in the menu ", fg = 'red')
         self.w.grid(row = 3, column = 3)   
      else:
         self.Homepage.grid_remove()
         self.calculate.grid()    
         
         
      if self.var11.get() == 0:
         self.w = Label(self.Homepage, text = "Please select the food in the menu ", fg = 'red')
         self.w.grid(row = 3, column = 3)   
      else:
         self.Homepage.grid_remove()
         self.calculate.grid()    
         
         
      if self.var12.get() == 0:
         self.w = Label(self.Homepage, text = "Please select food and quantity in the menu ", fg = 'red')
         self.w.grid(row = 3, column = 3)   
      else:
         self.Homepage.grid_remove()
         self.calculate.grid()    
         
      
   def back_homepage1(self):
      self.listBox.delete(*self.listBox.get_children())
      self.warn5.destroy()
      self.totText.set("0.0")
      self.back_to_homepage1.grid_remove()      
      self.calculate.grid_forget()
      self.Homepage.grid()
      
      
   def back_homepage(self):
      self.listBox.delete(*self.listBox.get_children())
      self.labeling.destroy()
      self.back_to_homepage.grid_remove()
      self.totText.set("0.0")
      self.calculate.grid_forget()
      self.Homepage.grid()
      

   def recipt(self):
      tott = float(self.totText.get())
      top = Toplevel()
      top.geometry("300x300")
   
      top.config(bg="white")
      l = Label(top, text='---------RECIEPT----------')
      l.pack()
      l.config(bg="white")
      heading = Label(top, text='\tItem\tcalories\tQuantity\tTOTAL')
      heading.pack()
      heading.config(bg="white")
   
      for child in self.listBox.get_children():
         item = (self.listBox.item(child, 'values')[0])
         calories = float(self.listBox.item(child, 'values')[1])
         quantity = float(self.listBox.item(child, 'values')[2])
         self.tot = float(self.listBox.item(child, 'values')[3])
         item1 = Label(top, text=f'{item}\t{calories}\t{quantity}\t{self.tot}')
         item1.config(bg="white")
         item1.pack()
   
      self.tot = Label(top, text=f'Total\t{tott}')
      self.tot.config(bg="white")
      self.tot.pack()
         
   def logout(self):
      if messagebox.askokcancel("Quit", "Do you want to quit?"):
         root.destroy()
   
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


