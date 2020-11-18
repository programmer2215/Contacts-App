from tkinter import * 
import db 
  
master = Tk()
master.title('Contacts')
master.geometry('830x500+350+200')
master.config(bg= '#b4eb34')

ref_var = StringVar()
ent = Entry(master, textvariable= ref_var)
ent.grid(row=0, column=0)

txt = Label(master, text='Search by: ', bg='#b4eb34', font=(16)).grid(row=0, column=1)


click = StringVar()
drop_down = OptionMenu(master, click, 'FirstName', 'LastName', 'Gender', 'Phone', 'Email', 'Address')
drop_down.grid(row = 0, column = 2)

click_182 = StringVar()
l0 = Label(master, text='Sort: ', bg='#b4eb34', font=(18)).grid(row=0, column=3)
drop_down2 = OptionMenu(master, click_182, 'A-Z', 'Z-A')
drop_down2.grid(row = 0, column = 4, sticky = 'NW')

b_1 = Button(master, text= 'Clear Sort', command = lambda : click_182.set(None))
b_1.grid(row = 2, column = 4, sticky = 'SS')

ln_filler = Label(master, text='   ', bg='#b4eb34').grid(row=2, column=0)

l1 = Label(master, text='First Name', bg='#b4eb34').grid(row=3, column=0)
l2 = Label(master, text='Last Name', bg='#b4eb34').grid(row=3, column=1)
l3 = Label(master, text='Gender', bg='#b4eb34').grid(row=3, column=2)
l4 = Label(master, text='Phone', bg='#b4eb34').grid(row=3, column=3)
l5 = Label(master, text='Email ID', bg='#b4eb34').grid(row=3, column=4)
l6 = Label(master, text='Address', bg='#b4eb34').grid(row=3, column=5)



fn_list = Listbox(master, height=20, bg='#d3f4f5')
fn_list.grid(row=4, column=0)
ln_list = Listbox(master, height=20, bg='#d3f4f5')
ln_list.grid(row=4, column=1)
gen_list = Listbox(master, height=20, bg='#d3f4f5')
gen_list.grid(row=4, column=2)
phn_list = Listbox(master, height=20, bg='#d3f4f5')
phn_list.grid(row=4, column=3)
eml_list = Listbox(master, height=20, bg='#d3f4f5')
eml_list.grid(row=4, column=4)
adr_list = Listbox(master, width= 40, height=20, bg='#d3f4f5')
adr_list.grid(row=4, column=5)




def refresh():
    try:
        fn_list.delete(0, END)
        ln_list.delete(0, END)
        gen_list.delete(0, END)
        phn_list.delete(0, END)
        eml_list.delete(0, END)
        adr_list.delete(0, END)
    except AttributeError:
        pass

def highlight(row):
    if (row % 2) != 0:
        fn_list.itemconfig(row, bg = '#52e3ba')
        ln_list.itemconfig(row, bg = '#52e3ba')
        gen_list.itemconfig(row, bg = '#52e3ba')
        phn_list.itemconfig(row, bg = '#52e3ba')
        eml_list.itemconfig(row, bg = '#52e3ba')
        adr_list.itemconfig(row, bg = '#52e3ba')

def show_results():
    refresh()
    
    ref = (ref_var.get()).capitalize()
    field = click.get()
    sort = click_182.get()
    data = db.view_contact(ref, field, sort)
    if len(data) > 0:
        for record in data:
            fn_list.insert(END, record[0])
            ln_list.insert(END, record[1])
            gen_list.insert(END, record[2])
            phn_list.insert(END, record[3])
            eml_list.insert(END, record[4])
            adr_list.insert(END, record[5])
    for i in range(0, len(fn_list.get(0, END))):
        highlight(i)
    del data


        


def new_contact_window():
    global fname, lname, genvar, phone, email, address, root
    root = Tk()
    root.config(bg= '#b4eb34')
    temp_l  = Label(root, bg='#b4eb34', text='\nCreate New Contact\n', font=("Helvetica", 16)).pack()
    
    temp_2  = Label(root, bg='#b4eb34', text='\nFirst Name\n', font=("Helvetica", 14)).pack()

    fname = Entry(root, bg='#7edbf2')
    fname.pack()
    
    temp_3  = Label(root, bg='#b4eb34', text='\nLast Name\n', font=("Helvetica", 14)).pack()
    
    lname = Entry(root,bg='#7edbf2', width=30)
    lname.pack()

    temp_4  = Label(root, bg='#b4eb34', text='\nGender\n', font=("Helvetica", 14)).pack()

    genvar = StringVar()
    drop_down_gen = OptionMenu(root, genvar, 'Male', 'Female', 'Not specified')
    drop_down_gen.pack()


    temp_6  = Label(root, bg='#b4eb34', text='\nPhone\n', font=("Helvetica", 14)).pack()

    phone = Entry(root, bg='#7edbf2' , width=30)
    phone.pack()

    temp_6  = Label(root, bg='#b4eb34', text='Email ID', font=("Helvetica", 14)).pack() 
       
    email = Entry(root,bg='#7edbf2',width=30)
    email.pack()
    
    temp_7  = Label(root, bg='#b4eb34', text='Address', font=("Helvetica", 14)).pack()
    
    address = Text(root, bg='#7edbf2',height=5, width=45)
    address.pack()
    global stat_var
    stat_var = StringVar()
    stat_lab = Label(root, bg='#b4eb34', textvariable = stat_var, font=("Helvetica", 14))
    stat_lab.pack()
    

    create = Button(root, text = 'create', command=create_contact).pack()
    root.mainloop()

def create_contact():
    a = (fname.get()).capitalize()
    b = (lname.get()).capitalize()
    c = (genvar.get()).capitalize()
    d = (phone.get()).capitalize()
    e = (email.get()).capitalize()
    f = (address.get("1.0", "end")).capitalize()
    exists = db.limit_duplication([a, b, c, d, e])
    if exists:
        fname.delete(0, END)
        lname.delete(0, END)
        phone.delete(0, END)
        email.delete(0, END)
        address.delete('0.0', "end")
        stat_var.set('Contact already exists') 
    else:
        db.create_record(a,b,c,d,e,f)
        stat_var.set('Contact created')
        root.quit() 


create = Button(master, text = 'create new contact', command= new_contact_window).grid(row=1, column=1, columnspan = 2, sticky='SW')

search = Button(master, text = 'search', command=show_results).grid(row=1, column=0)


master.mainloop()
