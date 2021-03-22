from tkinter import *
import tkinter as tk
from tkinter import messagebox

import StrackerMain
import StrackerFunc





def load_gui(self):

    self.lbl_fname = tk.Label(self.master,text="First Name:")
    self.lbl_fname.grid(row=0,column=0,padx=(27,0),pady=(5,0),sticky=N+W)
    self.lbl_lname = tk.Label(self.master,text="Last Name:")
    self.lbl_lname.grid(row=2,column=0,padx=(27,0),pady=(5,0),sticky=N+W)
    self.lbl_phone = tk.Label(self.master,text="Phone Number:")
    self.lbl_phone.grid(row=4,column=0,padx=(27,0),pady=(5,0),sticky=N+W)
    self.lbl_email = tk.Label(self.master,text="Email Address:")
    self.lbl_email.grid(row=6,column=0,padx=(27,0),pady=(5,0),sticky=N+W)
    self.lbl_user = tk.Label(self.master,text="List of Enrolled students:")
    self.lbl_user.grid(row=0,column=2,padx=(0,0),pady=(5,0),sticky=N+W)
    self.lbl_Course = tk.Label(self.master,text="Current course:")
    self.lbl_Course.grid(row=8,column=0,padx=(27,0),pady=(5,0),sticky=N+W)

    self.txt_fname = tk.Entry(self.master, text="")
    self.txt_fname.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_lname = tk.Entry(self.master, text="")
    self.txt_lname.grid(row=3,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_phone = tk.Entry(self.master, text="")
    self.txt_phone.grid(row=5,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_email = tk.Entry(self.master, text="")
    self.txt_email.grid(row=7,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_Course = tk.Entry(self.master, text="")
    self.txt_Course.grid(row=9,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)


    self.scrollbar1= Scrollbar(self.master,orient=VERTICAL)
    self.lstList1 = Listbox(self.master,exportselection=0,yscrollcommand=self.scrollbar1.set)
    self.lstList1.bind("<<ListboxSelect>>",lambda event: StrackerFunc.onSelect(self,event))
    self.scrollbar1.config(command=self.lstList1.yview)
    self.scrollbar1.grid(row=1,column=5,rowspan=7,columnspan=1,padx=(0,0),pady=(0,0),sticky=N+E+S+W)
    self.lstList1.grid(row=1,column=2,rowspan=8,columnspan=3,padx=(0,0),pady=(0,0),sticky=N+E+S+W)

    self.btn_Sub = tk.Button(self.master,width=12,height=2,text="Submit",command=lambda: StrackerFunc.addToList(self))
    self.btn_Sub.grid(row=9,column=2,padx=(25,0),pady=(45,10),sticky=W)
    self.btn_Del = tk.Button(self.master,width=12,height=2,text="Delete",command=lambda: StrackerFunc.onDelete(self))
    self.btn_Del.grid(row=9,column=3,padx=(25,0),pady=(45,10),sticky=W)

    StrackerFunc.create_db(self)
    StrackerFunc.onRefresh(self)
    

if __name__ == "__main__":
    pass
