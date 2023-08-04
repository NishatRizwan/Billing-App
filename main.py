from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random
from tkinter import messagebox
import random,os
import tempfile


class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Billing Software")

#============================== variables ============
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,99999)
        self.bill_no.set(z)
        self.c_Email=StringVar()
        self.search_bill=StringVar()
        self.pricee=IntVar()
        self.qty=IntVar()
        self.product=StringVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
#=====================================================
        #PRODUCT CATEGORIES LIST
        self.Category=["Select Optional","Clothing","Life_Style","Mobiles"]

        #SUBTITLE CATEGORIES LIST
        self.SubCatClothing=["pant","T_shirt","Shirt"]
        self.pant=["Levis","Spykar","Mufti"]

        self.price_Levis=5000
        self.price_Spykar=7000
        self.price_Mufti=8000
        
        self.T_shirt=["Polo","Roadstar","Jack_Jones"]
        self.price_Polo=1500
        self.price_Roadstar=1700
        self.price_Jack_Jones=1800

        self.Shirt=["Peter_England","Louis_phillipe","park_Avenue"]
        self.price_Peter_England=2500
        self.price_Louis_phillipe=2700
        self.price_park_Avenue=2800

        self.SubCatLife_style=["Suns_creame","Bath_Soap","Hair_oil"]
        self.Suns_creame=["Garnier","Lotus","Denel"]
        self.price_Garnier=200
        self.price_Lotus=250
        self.price_Denel=170
        
        self.Bath_Soap=["Lux","life_Buy","Santoor","pears"]
        self.price_Lux=15
        self.price_Life_Buy=25
        self.price_Santoor=30
        self.price_Pears=35

        self.Hair_oil=["Dabar_Amla","Aamla","Jashmine","Sarso"]
        self.price_Dabar_Amla=95
        self.price_Aamla=55
        self.price_Jashmine=70
        self.price_Sarso=75

        self.SubCatMobiles=["Iphone","Oppo","Samsung"]
        self.Iphone=["14_Pro_max","13_Pro_max","7_Plus","12_mini"]
        self.price_14_Pro_max=125000
        self.price_13_Pro_max=100000
        self.price_7_Plus=30000
        self.price_12_mini=75000

        self.Oppo=["A17","A77","Reno","f21"]
        self.price_A17=12000
        self.price_A77=20000
        self.price_Reno=40000
        self.price_f21=25000

        self.Samsung=["GalaxyS21_ultra","GalaxyS21","J7","Samsung_S20"]
        self.price_GalaxyS21_ultra=120000
        self.price_GalaxyS21=95000
        self.price_J7=8000
        self.price_Samsung_S20=50000
#-----------------------------------------------------------------------
        # image1 setting
        img=Image.open("images/bags.jpg.jpg")
        img=img.resize((300,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        lbl_imag=Label(self.root,image=self.photoimg)
        lbl_imag.place(x=0,y=0,width=300,height=130)

        # image2 setting
        img_1=Image.open("images/good.jpg")
        img_1=img_1.resize((300,130),Image.LANCZOS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        lbl_imag_1=Label(self.root,image=self.photoimg_1)
        lbl_imag_1.place(x=301,y=0,width=300,height=130)

        # image3 setting
        img_2=Image.open("images/mall1.jpg.jpg")
        img_2=img_2.resize((300,130),Image.LANCZOS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        lbl_imag_2=Label(self.root,image=self.photoimg_2)
        lbl_imag_2.place(x=601,y=0,width=300,height=130)

        # image4 setting
        img_3=Image.open("images/fruits.jpg.jpg")
        img_3=img_3.resize((300,130),Image.LANCZOS)
        self.photoimg_3=ImageTk.PhotoImage(img_3)

        lbl_imag_3=Label(self.root,image=self.photoimg_3)
        lbl_imag_3.place(x=901,y=0,width=300,height=130)

        #image5 setting
        img_4=Image.open("images/j1.jpg")
        img_4=img_4.resize((300,130),Image.LANCZOS)
        self.photoimg_4=ImageTk.PhotoImage(img_4)

        lbl_imag_4=Label(self.root,image=self.photoimg_4)
        lbl_imag_4.place(x=1201,y=0,width=300,height=130)
        
#-----------------------------------------------------------------------
        # label fomatting with text port
        lbl_title=Label(self.root,text="Billing Software",font=("times new roman",35,"bold"),bg="black",fg="white")
        lbl_title.place(x=0,y=130,width=1530,height=45)

        # MAIN_FRAM
        main_frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        main_frame.place(x=0,y=176,width=1530,height=620)

        #CUSTOMER_FRAME
        customer_frame=LabelFrame(main_frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")
        customer_frame.place(x=10,y=5,width=350,height=150)

        # inside of Customer labelfram
        #MOBILE NUMBER
        self.lbl_mob=Label(customer_frame,text="Mobile.No",font=("times new roman",12,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=2) #have to check grid 

        self.entry_mob=ttk.Entry(customer_frame,textvariable=self.c_phone,font=("times new roman",12,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)

        #CUSTOMER NAME
        self.lbl_customer_name=Label(customer_frame,text="Customer name",font=("arial",12,"bold"),bg="white",bd=4)
        self.lbl_customer_name.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.entry_Customer_name=ttk.Entry(customer_frame,textvariable=self.c_name,font=("arial",11,"bold"),width=24)
        self.entry_Customer_name.grid(row=1,column=1)

        #EMAIL
        self.lbl_Emai=Label(customer_frame,text="Email",font=("arial",12,"bold"),bg="white",bd=4)
        self.lbl_Emai.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.entry_Email=ttk.Entry(customer_frame,textvariable=self.c_Email,font=("arial",11,"bold"),width=24)
        self.entry_Email.grid(row=2,column=1)

        #PRODUCT_FRAM
        Product_frame=LabelFrame(main_frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        Product_frame.place(x=370,y=5,width=620,height=150)

        # inside of product_frame
        #CATEGORIES
        self.lbl_Category=Label(Product_frame,text="Select Categories",font=("arial",12,"bold"),bd=4)
        self.lbl_Category.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.Combo_Category=ttk.Combobox(Product_frame,value=self.Category,font=("arial",10,"bold"),width=24,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)

        #SUBCATEGORY
        self.lbl_SubCategory=Label(Product_frame,text="Select Product",font=("arial",12,"bold"),bd=4)
        self.lbl_SubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.ComboSubCategory=ttk.Combobox(Product_frame,value=[""],font=("arial",9,"bold"),width=24,state="readonly")
        self.ComboSubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.pro)

        #PRODUCTNAME
        self.lbl_Productname=Label(Product_frame,text="Availability",font=("arial",12,"bold"),bd=4)
        self.lbl_Productname.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.Combo_Productname=ttk.Combobox(Product_frame,textvariable=self.product,font=("arial",9,"bold"),width=24,state="readonly")
        self.Combo_Productname.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.Combo_Productname.bind("<<ComboboxSelected>>",self.prices)

        #PRICE
        self.lbl_Price=Label(Product_frame,text="Price",font=("arial",12,"bold"),bd=4)

        self.lbl_Price.grid(row=0,column=2,sticky=W,padx=5,pady=2)
        self.Combo_Price=ttk.Combobox(Product_frame,textvariable=self.pricee,font=("arial",7,"bold"),width=24,state="readonly")
        self.Combo_Price.grid(row=0,column=3)

        #QTY
        self.lbl_Qty=Label(Product_frame,text="Quantity",font=("arial",12,"bold"),bg="white",bd=4)
        self.lbl_Qty.grid(row=1,column=2,stick=W,padx=5,pady=2) #have to check grid 

        self.Combo_Qty=ttk.Entry(Product_frame,textvariable=self.qty,font=("arial",7,"bold"),width=24)
        self.Combo_Qty.grid(row=1,column=3,sticky=W,padx=5,pady=2)
#-------------------------------------------
        # MIDDLE FRAME
        middle_frame=Frame(main_frame,bd=10)
        middle_frame.place(x=10,y=170,height=340,width=980)
#-------------------------------------------
        #SEARCH BAR
        search_frame=Frame(main_frame,bd=2,bg="white")
        search_frame.place(x=1000,y=13,width=500,height=40)

        self.lblBill=Label(search_frame,text="Bill Number",font=("arial",12,"bold"),bd=4,bg="orangered",fg="white")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)

        self.Entry_Search=ttk.Entry(search_frame,textvariable=self.search_bill,font=("arial",11,"bold"),width=24)
        self.Entry_Search.grid(row=0,column=1,sticky=W,padx=2)

        self.BtnSearch=Button(search_frame,command=self.find_bill,text="Search",font=("arial",12,"bold"),bg="orangered",fg="white",cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)

        # BILL_FRAME
        Billframe=LabelFrame(main_frame,text="Bill area",font=("times new roman",12,"bold"),bg="white",fg="red")
        Billframe.place(x=1000,y=45,width=480,height=440)
        
        # INSIDE BILL_FRAME
        #SCROLLBAR
        Scroll_y=Scrollbar(Billframe,orient=VERTICAL)
        self.textarea=Text(Billframe,yscrollcommand=Scroll_y.set,bg="white",fg="blue",font=("times new roman",12, "bold"))
        Scroll_y.pack(side=RIGHT,fill=Y)
        Scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #BOTTOM_FRAME
        Bottom_frame=LabelFrame(main_frame,text="Bottom",font=("times new roman",12,"bold"),bg="white",fg="red")
        Bottom_frame.place(x=0,y=485,width=1530,height=125)

        #SUBTOTAL
        self.lbl_Sub_total=Label(Bottom_frame,text="total",font=("arial",12,"bold"),bd=4,bg="white")
        self.lbl_Sub_total.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.entry_sub_total=ttk.Entry(Bottom_frame,textvariable=self.sub_total,font=("arial",8,"bold"),width=26)
        self.entry_sub_total.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        #GOVERMENT TAX
        self.lbl_govtax=Label(Bottom_frame,text="gov-tax",font=("arial",12,"bold"),bd=4,bg="white")
        self.lbl_govtax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.entry_govtax=ttk.Entry(Bottom_frame,textvariable=self.tax_input,font=("arial",8,"bold"),width=26)
        self.entry_govtax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        #TOTAL
        self.lbl_total=Label(Bottom_frame,text="Total",font=("arial",12,"bold"),bd=4,bg="white")
        self.lbl_total.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.entry_total=ttk.Entry(Bottom_frame,textvariable=self.total,font=("arial",8,"bold"),width=26)
        self.entry_total.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        #BUTTON
        # ADD BUTTON
        Btn_frame=Frame(Bottom_frame,bd=2,bg="white")
        Btn_frame.place(x=300,y=0)

        self.BtnAddtocard=Button(Btn_frame,command=self.ADDItem,text="Add to cart",font=("arial",12,"bold"),bg="orangered",fg="white",cursor="hand2")
        self.BtnAddtocard.grid(row=0,column=0)

        # GENERATE BUTTON
        Btn_frame=Frame(Bottom_frame,bd=2,bg="white")
        Btn_frame.place(x=410,y=0)

        self.BtnGenerate=Button(Btn_frame,command=self.gen_bill,text="Generate Bill",font=("arial",12,"bold"),bg="orangered",fg="white",cursor="hand2")
        self.BtnGenerate.grid(row=0,column=0)

        # SAVE BUTTON
        Btn_frame=Frame(Bottom_frame,bd=2,bg="white")
        Btn_frame.place(x=530,y=0)

        self.BtnSaveBill=Button(Btn_frame,command=self.save_bill,text="SAVE BILL",font=("arial",12,"bold"),bg="orangered",fg="white",cursor="hand2")
        self.BtnSaveBill.grid(row=0,column=0)

        #PRINT BUTTON
        Btn_frame=Frame(Bottom_frame,bg="white",bd=2)
        Btn_frame.place(x=640,y=0)

        self.BtnPrint=Button(Btn_frame,command=self.iprint,text="Print Bill",font=("arial",12,"bold"),bg="orangered",fg="white",cursor="hand2")
        self.BtnPrint.grid(row=0,column=0)

        #CLEAR BUTTON
        Btn_frame=Frame(Bottom_frame,bg="white",bd=2)
        Btn_frame.place(x=730,y=0)

        self.BtnClear=Button(Btn_frame,command=self.clear,text=" Clear ",font=("arial",12,"bold"),bg="orangered",fg="white",cursor="hand2")
        self.BtnClear.grid(row=0,column=0)

        Btn_frame=Frame(Bottom_frame,bg="white",bd=2)
        Btn_frame.place(x=800,y=0)

        self.BtnExit=Button(Btn_frame,command=self.root.destroy,text=" Exit ",font=("arial",12,"bold"),bg="orangered",fg="white",cursor="hand2")
        self.BtnExit.grid(row=0,column=0)
#=====================================function declaration method==================
        self.Welcome()
        self.l=[]
#=============------------------================------------============---------------=
                        # FUNCTIONS DECLARATION   
    
    #ADD TO CARD
    def ADDItem(self):
        Tax=1
        ll=[]
        self.n=self.pricee.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()==ll:
            messagebox.showerror("Error","please select the product name")
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t\t{self.qty.get()}\t\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l))-(self.pricee.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l))+((((sum(self.l))-(self.pricee.get()))*Tax)/100)))))

    #GENERATE BILL
    def gen_bill(Self):
        if Self.product.get()==" ":
            messagebox.showerror("Error","please add to card product")
        else:
            text=Self.textarea.get(10.0,(10.0+float(len(Self.l))))
            Self.Welcome()
            Self.textarea.insert(END,text)
            Self.textarea.insert(END,"\n =======================================")
            Self.textarea.insert(END,f"\n SUB-AMOUNT:\t\t\t{Self.sub_total.get()}")
            Self.textarea.insert(END,f"\n TAX-AMOUNT:\t\t\t{Self.tax_input.get()}")
            Self.textarea.insert(END,f"\n TOTAL-AMOUNT:\t\t\t{Self.total.get()}")
            Self.textarea.insert(END,"\n=======================================")
    
    # SAVE BILL
    def save_bill(self):
        op=messagebox.askyesno("save Bill","Do you want to save the bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('bills/'+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            op=messagebox.showinfo("saved",f"Bill No:{self.bill_no.get()} saved successfully")
            f1.close()
    
    #PRINT BILL
    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")

    #search bill found
    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                    f1=open(f'bills/{i}','r')
                    self.textarea.delete(1.0,END)
                    for d in f1:
                        self.textarea.insert(END,d)
                    f1.close()
                    found="yes"
        if found=="no":
            messagebox.showerror("error","invalid bill number")

    #CLEAR page
    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phone.set("")
        self.c_Email.set("")
        z=random.randint(1000,99999)
        self.bill_no.set(str(z))
        self.search_bill.set("")
        self.pricee.set(0)
        self.product.set("")
        self.qty.set(0)
        self.sub_total.set("")
        self.tax_input.set("")
        self.total.set("")
        self.l=[0]
        self.Welcome()
        
    #WELCOME-PART    
    def Welcome(Self):
        Self.textarea.delete(1.0,END)
        Self.textarea.insert(END,"\t\t\t WELCOME")
        Self.textarea.insert(END,f"\n BILL NUMBER: {Self.bill_no.get()}")
        Self.textarea.insert(END,f"\n CUSTOMER NAME: {Self.c_name.get()}")
        Self.textarea.insert(END,f"\n CUSTOMER PHONE NUMBER: {Self.c_phone.get()}")
        Self.textarea.insert(END,f"\n CUSTOMER EMAIL: {Self.c_Email.get()}")

        Self.textarea.insert(END,"\n==================================================")
        Self.textarea.insert(END,f"\n PRODUCTS\t\t\tQTY\t\t\tPRICE")
        Self.textarea.insert(END,"\n==================================================\n")
#==================================BACKEND PART==============
#SUBCATEGORY BIND
    def Categories(self,Event=""):
        if self.Combo_Category.get()=="Clothing":
            self.ComboSubCategory.config(value=self.SubCatClothing)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Life_Style":
            self.ComboSubCategory.config(values=self.SubCatLife_style)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Mobiles":
            self.ComboSubCategory.config(values=self.SubCatMobiles)
            self.ComboSubCategory.current(0)
#=================================================
#PRODUCT BIND
    def pro(self,event=""):
        if  self.ComboSubCategory.get()=="pant":
            self.Combo_Productname.config(value=self.pant)
            self.Combo_Productname.current(0)
            self.qty.set(1)
        
        if  self.ComboSubCategory.get()=="T_shirt":
            self.Combo_Productname.config(value=self.T_shirt)
            self.Combo_Productname.current(0)
            self.qty.set(1)

        if  self.ComboSubCategory.get()=="Shirt":
            self.Combo_Productname.config(value=self.Shirt)
            self.Combo_Productname.current(0)
            self.qty.set(1)
#==============================================================
        # lifestyle product
        if  self.ComboSubCategory.get()=="Suns_creame":
            self.Combo_Productname.config(value=self.Suns_creame)
            self.Combo_Productname.current(0)
            self.qty.set(1)
        
        if  self.ComboSubCategory.get()=="Bath_Soap":
            self.Combo_Productname.config(value=self.Bath_Soap)
            self.Combo_Productname.current(0)
            self.qty.set(1)

        if  self.ComboSubCategory.get()=="Hair_oil":
            self.Combo_Productname.config(value=self.Hair_oil)
            self.Combo_Productname.current(0)
            self.qty.set(1)
#==============================================================
        # Mobiles product
        if  self.ComboSubCategory.get()=="Iphone":
            self.Combo_Productname.config(value=self.Iphone)
            self.Combo_Productname.current(0)
            self.qty.set(1)

        if  self.ComboSubCategory.get()=="Oppo":
            self.Combo_Productname.config(value=self.Oppo)
            self.Combo_Productname.current(0)
            self.qty.set(1)
        
        if  self.ComboSubCategory.get()=="Samsung":
            self.Combo_Productname.config(value=self.Samsung)
            self.Combo_Productname.current(0)
            self.qty.set(1)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def prices(self,event=""):
        # PANT
        if self.Combo_Productname.get()=="Levis":
            self.Combo_Price.config(value=self.price_Levis)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Productname.get()=="Spykar":
            self.Combo_Price.config(value=self.price_Spykar)
            self.Combo_Price.current(0)
            self.qty.set(1)
        
        if self.Combo_Productname.get()=="Mufti":
            self.Combo_Price.config(value=self.price_Mufti)
            self.Combo_Price.current(0)
            self.qty.set(1)
#-----------------------------------------------------
        #T-shirt
        if self.Combo_Productname.get()=="Polo":
            self.Combo_Price.config(value=self.price_Polo)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Productname.get()=="Roadstar":
            self.Combo_Price.config(value=self.price_Roadstar)
            self.Combo_Price.current(0)
            self.qty.set(1)
        
        if self.Combo_Productname.get()=="Jack_Jones":
            self.Combo_Price.config(value=self.price_Jack_Jones)
            self.Combo_Price.current(0)
            self.qty.set(1)
#-----------------------------------------------------
        # SHIRT
        if self.Combo_Productname.get()=="Peter_England":
            self.Combo_Price.config(value=self.price_Peter_England)
            self.Combo_Price.current(0)
            self.qty.set(1)
        
        if self.Combo_Productname.get()=="Louis_phillipe":
            self.Combo_Price.config(value=self.price_Louis_phillipe)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Productname.get()=="park_Avenue":
            self.Combo_Price.config(value=self.price_park_Avenue)
            self.Combo_Price.current(0)
            self.qty.set(1)
#----------------------------------------------------- 
        # LIFESTYLE
        #SUNS CREAME
        if self.Combo_Productname.get()=="Garnier":
            self.Combo_Price.config(value=self.price_Garnier)
            self.Combo_Price.current(0)
            self.qty.set(1)
        
        if self.Combo_Productname.get()=="Lotus":
            self.Combo_Price.config(value=self.price_Lotus)
            self.Combo_Price.current(0)
            self.qty.set(1)
        
        if self.Combo_Productname.get()=="Denel":
            self.Combo_Price.config(value=self.price_Denel)
            self.Combo_Price.current(0)
            self.qty.set(1)
#----------------------------------------------------- 
        # LIFESTYLE
        # BATH
        if self.Combo_Productname.get()=="Lux":
            self.Combo_Price.config(value=self.price_Lux)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Productname.get()=="life_Buy":
            self.Combo_Price.config(value=self.price_Life_Buy)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Productname.get()=="Santoor":
            self.Combo_Price.config(value=self.price_Santoor)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Productname.get()=="pears":
            self.Combo_Price.config(value=self.price_Pears)
            self.Combo_Price.current(0)
            self.qty.set(1)
#-----------------------------------------------------     
        # HAIR OIL
        if self.Combo_Productname.get()=="Dabar_Amla":
            self.Combo_Price.config(value=self.price_Dabar_Amla)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Productname.get()=="Aamla":
            self.Combo_Price.config(value=self.price_Aamla)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Productname.get()=="Jashmine":
            self.Combo_Price.config(value=self.price_Jashmine)
            self.Combo_Price.current(0)
            self.qty.set(1)
        
        if self.Combo_Productname.get()=="Sarso":
            self.Combo_Price.config(value=self.price_Sarso)
            self.Combo_Price.current(0)
            self.qty.set(1)
#-----------------------------------------------------     
        # MOBILE
        #iphone
        if self.Combo_Productname.get()=="14_Pro_max":
            self.Combo_Price.config(value=self.price_14_Pro_max)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Productname.get()=="13_Pro_max":
            self.Combo_Price.config(value=self.price_13_Pro_max)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Productname.get()=="7_Plus":
            self.Combo_Price.config(value=self.price_7_Plus)
            self.Combo_Price.current(0)
            self.qty.set(1)
        
        if self.Combo_Productname.get()=="12_mini":
            self.Combo_Price.config(value=self.price_12_mini)
            self.Combo_Price.current(0)
            self.qty.set(1)
#-----------------------------------------------------     
        #OPPO
        if self.Combo_Productname.get()=="A17":
            self.Combo_Price.config(value=self.price_A17)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Productname.get()=="A77":
            self.Combo_Price.config(value=self.price_A77)
            self.Combo_Price.current(0)
            self.qty.set(1)
        
        if self.Combo_Productname.get()=="f21":
            self.Combo_Price.config(value=self.price_f21)
            self.Combo_Price.current(0)
            self.qty.set(1)
        
        if self.Combo_Productname.get()=="Reno":
            self.Combo_Price.config(value=self.price_Reno)
            self.Combo_Price.current(0)
            self.qty.set(1)
#-----------------------------------------------------     
        #SAMSUNG
        if self.Combo_Productname.get()=="GalaxyS21_ultra":
            self.Combo_Price.config(value=self.price_GalaxyS21_ultra)
            self.Combo_Price.current(0)
            self.qty.set(1)
        
        if self.Combo_Productname.get()=="GalaxyS21":
            self.Combo_Price.config(value=self.price_GalaxyS21)
            self.Combo_Price.current(0)
            self.qty.set(1)
        
        if self.Combo_Productname.get()=="J7":
            self.Combo_Price.config(value=self.price_J7)
            self.Combo_Price.current(0)
            self.qty.set(1)
        
        if self.Combo_Productname.get()=="Samsung_S20":
            self.Combo_Price.config(value=self.price_Samsung_S20)
            self.Combo_Price.current(0)
            self.qty.set(1)
#----------------------------------------------------- 
if __name__ =="__main__":
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()