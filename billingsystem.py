from tkinter import*
import random
from tkinter import messagebox
class Restaurant_Billing:
   def __init__(self, root):
        self.root = root
        
        self.root.maxsize(width=1370, height=720)
        self.root.minsize(width=1370, height=720)
        self.root.title("Restaurant Billing System")
        bg_color  = "#E0FFFF"
        
        title = Label(self.root, text="Restaurant Billing System", bd=12, relief= GROOVE,bg =bg_color,
font=("Calibri", 36, "bold"), pady =2).pack(fill=X)
         
        self.Tuborg_Strong= IntVar()
        self.Redlabel= IntVar()
        self.Ruslan= IntVar()
        self.Black_Chimney= IntVar()
        self.Rum= IntVar()
        self.Old_Durbar= IntVar()
        
        


        self.cname= StringVar()
        self.cphone=StringVar()
        self.cBill=StringVar()
        x=random.randint(1000,9999)
        self.cBill.set(str(x))
        self.search=StringVar()
        self.drinks_price=StringVar()

        F1=LabelFrame(self.root, text="Customer Details",bg =bg_color, font=("Calibri", 18, "bold"))
        F1.place(x=0, y=80, relwidth=1)

        cname_label=Label(F1,text="Customer Name", bg =bg_color, font=("Calibri", 18, "bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=20, textvariable=self.cname, font="arial 15",relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphone_label=Label(F1,text="Phone No.", bg =bg_color, font=("Calibri", 18, "bold")).grid(row=0,column=2,padx=20,pady=5)
        cphone_txt=Entry(F1,width=20, textvariable=self.cphone,font="arial 15",relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        cBill_label=Label(F1,text="Bill No.", bg =bg_color, font=("Calibri", 18, "bold")).grid(row=0,column=4,padx=20,pady=5)
        cBill_txt=Entry(F1,width=20, textvariable=self.cBill, font="arial 15",relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        search_btn=Button(F1,text="search",width=10, font="arial 12 bold").grid(row=0,column=6)

         #....................DrinksItems Frame......................

        F2=LabelFrame(self.root,text="DRINKSITEMS",bg =bg_color, font=("Calibri", 15, "bold"))
        F2.place(x=5, y=170, relwidth=325,height=380)

        beer_label=Label(F2,text="Tuborg Strong",bd=7, bg =bg_color, font=("Calibri", 16, "bold")).grid(row=0,column=2,padx=10,pady=10,sticky="w")
        beer_txt=Entry(F2,width=10, textvariable= self.Tuborg_Strong, font="arial 12").grid(row=0,column=5,pady=5,padx=10)

        vodka_label=Label(F2,text="Redlabel", bg =bg_color,bd=7, font=("Calibri", 16, "bold")).grid(row=1,column=2,padx=10,pady=10,sticky="w")
        vodka_txt=Entry(F2,width=10, textvariable= self.Redlabel, font="arial 12").grid(row=1,column=5,pady=5,padx=10)

        hard_label=Label(F2,text="Ruslan", bg =bg_color,bd=7, font=("Calibri", 16, "bold")).grid(row=2,column=2,padx=10,pady=10,sticky="w")
        hard_txt=Entry(F2,width=10,textvariable= self.Ruslan, font="arial 12").grid(row=2,column=5,pady=5,padx=10)

        soft_label=Label(F2,text="Black Chimney", bg =bg_color,bd=7, font=("Calibri", 16, "bold")).grid(row=3,column=2,padx=10,pady=10,sticky="w")
        soft_txt=Entry(F2,width=10, textvariable= self.Black_Chimney, font="arial 12").grid(row=3,column=5,pady=5,padx=10)

        bth_label=Label(F2,text="Rum", bg =bg_color,bd=7, font=("Calibri", 16, "bold")).grid(row=4,column=2,padx=10,pady=10,sticky="w")
        bth_txt=Entry(F2,width=10, textvariable= self.Rum, font="arial 12").grid(row=4,column=5,pady=5,padx=10)

        bee_label=Label(F2,text="Old Durbar", bg =bg_color,bd=7, font=("Calibri", 16, "bold")).grid(row=5,column=2,padx=10,pady=10,sticky="w")
        bee_txt=Entry(F2,width=10, textvariable= self.Old_Durbar, font="arial 12").grid(row=5,column=5,pady=5,padx=10)

       #............Bill Area.................
        F3=Label(self.root,relief=GROOVE)
        F3.place(x=1000,y=180,width=325,height=380)
        Bill_title= Label(F3, text= "BIll Area", font = "arial 12 bold", bd = 7, relief= GROOVE).pack(fill=X) 
        scrol_y=Scrollbar(F3,orient= VERTICAL)
        self.txtarea= Text(F3,yscrollcommand= scrol_y.set)
        scrol_y.pack(side= RIGHT, fill=Y)
        scrol_y.config(command= self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)
        #.......Buttom frame..........
        F4=LabelFrame(self.root, text="Bill Menu",bg =bg_color, font=("Calibri", 18, "bold"))
        F4.place(x=0, y=560, relwidth=1, height=140 )
        totaldrinks_label=Label(F4,text="Totaldrinks price", bg =bg_color,bd=7, font=("Calibri", 16, "bold")).grid(row=4,column=2,padx=10,pady=10,sticky="w")
        totaldrinks_txt=Entry(F4, width=10,textvariable= self.drinks_price, font=("arial 12")).grid(row=4,column=5,pady=5,padx=10)

        #..........button..........
        btn_F= Frame(F4,bd= 7, relief= GROOVE)
        btn_F.place(x=880,width=500,height=90)

        total_btn=Button(btn_F, command= self.total, text="Total",bg=bg_color,bd=2,pady=15,width=10,font="arial 12").grid(row=0,column=0,padx=5,pady=5)
        GBill_btn=Button(btn_F, text="Generate Bill",command=self.bill_area,  bg=bg_color,bd=2,pady=15,width=10,font="arial 12").grid(row=0,column=2,padx=5,pady=5)
        CBil_btn=Button(btn_F,text="clear",command=self.clear_data, bg=bg_color,bd=2,pady=15,width=10,font="arial 12").grid(row=0,column=3,padx=5,pady=5)
        EBi_btn=Button(btn_F,text="Exit",command=self.Exit_window,bg=bg_color,bd=2,pady=15,width=10,font="arial 12").grid(row=0,column=4,padx=5,pady=5)
        self.welcome_Bill()
        
   def total(self):
        
       self.T_s=self.Tuborg_Strong.get()*350
       self.B_C=self.Black_Chimney.get()*1600 
       self.R=self.Ruslan.get()*1600
       self.O_D=self.Old_Durbar.get()*1600
       self.R_L=self.Redlabel.get()*1600
       self.Ru=self.Rum.get()*1600
                
       self.total_drinks_price=float(
                self.T_s+ 
                self.B_C+ 
                self.R+ 
                self.O_D+
                self.R_L+
                self.Ru
       )
       self.drinks_price.set(str(self.total_drinks_price))
   def welcome_Bill(self):
       self.txtarea.delete('1.0', END)
       self.txtarea.insert(END,"\twelcome to our restaurant")
       self.txtarea.insert(END,f"\nCustomer Name : {self.cname.get()}")
       self.txtarea.insert(END,f"\nPhone No. : {self.cphone.get()}")
       self.txtarea.insert(END,f"\nBill No. :{self.cBill.get()}")
       self.txtarea.insert(END,"\n------------------------------------")
       self.txtarea.insert(END,"\nPRODUCTS\t\tQTY\tPrice")
       self.txtarea.insert(END,"\n-------------------------------------")
   

   def bill_area(self):
       
       if self.cname.get()=="" or self.cphone.get()=="":
          op = messagebox.askyesno("ERROR","customer id required?")
       else:
            self.welcome_Bill()
            if self.Tuborg_Strong.get()!=0:
               self.txtarea.insert(END,f"\n Tuborg Strong\t\t{self.Tuborg_Strong.get()}\t{self.T_s}")

            if self.Black_Chimney.get()!=0:
               self.txtarea.insert(END,f"\n Black chimney\t\t{self.Black_Chimney.get()}\t{self.B_C}")
            if self.Ruslan.get()!=0:
               self.txtarea.insert(END,f"\n Ruslan\t\t{self.Ruslan.get()}\t{self.R}")
            if self.Old_Durbar.get()!=0:
               self.txtarea.insert(END,f"\n Old Durbar\t\t{self.Old_Durbar.get()}\t{self.O_D}")
                           
                        
            if self.drinks_price.get()!=0:
               self.txtarea.insert(END,f"\n Total\t\t\t{self.drinks_price.get()}")
               self.save_bill()

   def save_bill(self):
       op = messagebox.askyesno("save bill","Do you want to save bill?")
       if op>0:
          self.bill_dates= self.txtarea.get('1.0',END)
          f = open("Bill/"+ str(self.cBill.get())+".txt","w")
          f.write(self.bill_dates)
          f.close()
          messagebox.showinfo("Saved", f"Bill No. :{self.cBill.get} successfully saved")
       else:
            return
   def clear_data(self):
       op= messagebox.askyesno("clear","do you want to clear?")
       if op>0:
         self.Tuborg_Strong.set(0)
         self.Redlabel.set(0)
         self.Ruslan.set(0)
         self.Black_Chimney.set(0)
         self.Rum.set(0)
         self.Old_Durbar.set(0)
         self.cname.set("")
         self.cphone.set("")
         self.cBill.set("")
         x=random.randint(1000,9999)
         self.cBill.set(str(x))
         self.search.set("")
         self.drinks_price.set("")
         self.welcome_Bill()  
   def Exit_window(self):
       op= messagebox.askyesno("exit", "do youn want to exit")
       if op > 0:
          self.root.destroy()
       

root = Tk()
object = Restaurant_Billing(root)
root.mainloop()








       

   
  
   
        
        
         
                        
                
          
                       
        
                         
               
                
  
   


                

        
        


