import tkinter
from tkinter import *
from tkinter import messagebox
import random
import time
import mysql.connector
root = Tk()
root.title("Billing")
root.geometry("2000x1000")
bg_color = '#add8e6'
l = []
a = []
C1f = IntVar()
C2f = IntVar()
C3f = IntVar()
C4f = IntVar()
C5f = IntVar()
C6f = IntVar()
C7f = IntVar()
C8f = IntVar()
C9f = IntVar()
C10f = IntVar()
C11f = IntVar()
C12f = IntVar()
C13f = IntVar()
C14f = IntVar()
C15f = IntVar()
C16f = IntVar()
C17f = IntVar()
C18f = IntVar()
C19f = IntVar()
C20f = IntVar()

c_name = StringVar()
c_phone = StringVar()
bill_no = StringVar()
c_address = StringVar()
e_name = StringVar()

x = random.randint(1000, 9999)
bill_no.set(str(x))

title = Label(root, pady=1, text="Billing Software", bd=12, bg=bg_color, fg='black',
              font=('times new roman', 25, 'bold'), relief=GROOVE, justify=CENTER)
title.pack(fill=X)

F1 = LabelFrame(root, bd=10, relief=GROOVE, text='Customer Details', font=('times new romon', 15, 'bold'), fg='Brown',
                bg=bg_color)
F1.place(x=0, y=80, relwidth=4)

name_lbl = Label(F1, text='Customer Name', font=('times new romon', 18, 'bold'), bg=bg_color, fg='black').grid(row=0,
                                                                                                               column=0,
                                                                                                               padx=20,
                                                                                                               pady=5)
name_txt = Entry(F1, width=15, textvariable=c_name, font='arial 15 bold', relief=SUNKEN, bd=7).grid(row=0, column=1,
                                                                                                    padx=10, pady=5)

phone_lbl = Label(F1, text='Phone No. ', font=('times new romon', 18, 'bold'), bg=bg_color, fg='black').grid(row=0,
                                                                                                             column=2,
                                                                                                             padx=20,
                                                                                                             pady=5)

phone_txt = Entry(F1, width=15, font='arial 15 bold', textvariable=c_phone, relief=SUNKEN, bd=7).grid(row=0, column=3,
                                                                                                      padx=10, pady=5)
address_txt = Entry(F1, width=40, font='arial 15 bold', textvariable=c_address, relief=SUNKEN, bd=7).grid(row=1, column=6,
                                                                                                          columnspan=2,
                                                                                                          padx=8,
                                                                                                          pady=5)

add_lbl = Label(F1, text='Address ', font=('times new romon', 18, 'bold'), bg=bg_color, fg='black').grid(columnspan=1,
                                                                                                             row=1,
                                                                                                             column=5,
                                                                                                             padx=40,
                                                                                                             pady=5)
emp_name_lbl = Label(F1, text='Employee Name ', font=('times new romon', 18, 'bold'), bg=bg_color, fg='black').grid(columnspan=1,
                                                                                                             row=1,
                                                                                                             column=0,
                                                                                                             padx=40,
                                                                                                             pady=5)
emp_name_txt = Entry(F1, width=40, font='arial 15 bold', textvariable=e_name, relief=SUNKEN, bd=7).grid(row=1, column=1,
                                                                                                          columnspan=3,
                                                                                                          padx=10,
                                                                                                          pady=5)

class App(Frame):
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.master = master
        self.label = Label(text="", font=('times new roman',18,'bold'),bg=bg_color,fg='black')
        self.label.place(x=860,y=110)
        self.update_clock()

    def update_clock(self):
        now = time.strftime('\tDate: %x \t \t %M:%I:%S %p')
        self.label.configure(text=now)
        self.after(1000, self.update_clock)


app = App(root)

# product details
F2 = LabelFrame(root, text='Product Details', font=('times new romon', 15, 'bold'), fg='Brown', bg=bg_color)
F2.place(x=20, y=215, width=800, height=600)

scrol_y = Scrollbar(F2)
scrol_y.pack(side=RIGHT, fill=Y)
scrol_y.pack()

product_lbl = Label(F2, text="Product Name", bg=bg_color, font=('times new roman', 15, 'bold'))
product_lbl.place(x=40, y=10)

price_label = Label(F2, text="Price", bg=bg_color, font=('times new roman', 15, 'bold'))
price_label.place(x=260, y=10)

quantity_lbl = Label(F2, text="Quantity", bg=bg_color, font=('times new roman', 15, 'bold'))
quantity_lbl.place(x=420, y=10)

C1 = Checkbutton(F2, text="Veggie Pizza ", anchor="w", bg=bg_color, variable=C1f, font=('times new roman', 12))
C1.place(x=50, y=40, width=300)
# p=price
p1 = Label(F2, text="₹ 99", anchor="w", bg=bg_color, font=('times new roman', 12))
p1.place(x=260, y=40)

C2 = Checkbutton(F2, text="Chessse pizza ", anchor="w", bg=bg_color, variable=C2f, font=('times new roman', 12))
C2.place(x=50, y=65, width=300)
# p=price
p2 = Label(F2, text="₹ 89", anchor="w", bg=bg_color, font=('times new roman', 12))
p2.place(x=260, y=65)

C3 = Checkbutton(F2, text="Margherita Pizza ", anchor="w", bg=bg_color, variable=C3f, font=('times new roman', 12))
C3.place(x=50, y=90, width=300)
# p=price
p3 = Label(F2, text="₹ 69", anchor="w", bg=bg_color, font=('times new roman', 12))
p3.place(x=260, y=90)

C4 = Checkbutton(F2, text="Chicken Pizza", anchor="w", bg=bg_color, variable=C4f, font=('times new roman', 12))
C4.place(x=50, y=115, width=300)
# p=price
p4 = Label(F2, text="₹ 109", anchor="w", bg=bg_color, font=('times new roman', 12))
p4.place(x=260, y=115)

C5 = Checkbutton(F2, text="Zinger Burger", anchor="w", bg=bg_color, variable=C5f, font=('times new roman', 12))
C5.place(x=50, y=140, width=300)
# p=price
p5 = Label(F2, text="₹ 99", anchor="w", bg=bg_color, font=('times new roman', 12))
p5.place(x=260, y=140)

C6 = Checkbutton(F2, text="Chicken Burger", anchor="w", bg=bg_color, variable=C6f, font=('times new roman', 12))
C6.place(x=50, y=165, width=300)
# p=price
p6 = Label(F2, text="₹ 89", anchor="w", bg=bg_color, font=('times new roman', 12))
p6.place(x=260, y=165)

C7 = Checkbutton(F2, text="Chicken Chesse Burger", anchor="w", bg=bg_color, variable=C7f, font=('times new roman', 12))
C7.place(x=50, y=190, width=300)
# p=price
p7 = Label(F2, text="₹ 139", anchor="w", bg=bg_color, font=('times new roman', 12))
p7.place(x=260, y=190)

C8 = Checkbutton(F2, text="Grilled Tikka Burger", anchor="w", bg=bg_color, variable=C8f, font=('times new roman', 12))
C8.place(x=50, y=215, width=300)
# p=price
p8 = Label(F2, text="₹ 119", anchor="w", bg=bg_color, font=('times new roman', 12))
p8.place(x=260, y=215)

C9 = Checkbutton(F2, text="Chicken Shawarma ", anchor="w", bg=bg_color, variable=C9f, font=('times new roman', 12))
C9.place(x=50, y=240, width=300)
# p=price
p9 = Label(F2, text="₹ 80", anchor="w", bg=bg_color, font=('times new roman', 12))
p9.place(x=260, y=240)

C10 = Checkbutton(F2, text="Chicken Chesse Shawarma", anchor="w", bg=bg_color, variable=C10f,
                  font=('times new roman', 12))
C10.place(x=50, y=265, width=300)
# p=price
p10 = Label(F2, text="₹ 110", anchor="w", bg=bg_color, font=('times new roman', 12))
p10.place(x=260, y=265)

C11 = Checkbutton(F2, text="Vegetable Shawarma ", anchor="w", bg=bg_color, variable=C11f, font=('times new roman', 12))
C11.place(x=50, y=290, width=300)
# p=price
p11 = Label(F2, text="₹ 60", anchor="w", bg=bg_color, font=('times new roman', 12))
p11.place(x=260, y=290)

C12 = Checkbutton(F2, text="Maggi", anchor="w", bg=bg_color, variable=C12f, font=('times new roman', 12))
C12.place(x=50, y=315, width=300)
# p=price
p12 = Label(F2, text="₹ 30", anchor="w", bg=bg_color, font=('times new roman', 12))
p12.place(x=260, y=315)

C13 = Checkbutton(F2, text="Chesse Maggi", anchor="w", bg=bg_color, variable=C13f, font=('times new roman', 12))
C13.place(x=50, y=340, width=300)
# p=price
p13 = Label(F2, text="₹ 60", anchor="w", bg=bg_color, font=('times new roman', 12))
p13.place(x=260, y=340)

C14 = Checkbutton(F2, text="Cold Coffee Latte", anchor="w", bg=bg_color, variable=C14f, font=('times new roman', 12))
C14.place(x=50, y=365, width=300)
# p=price
p14 = Label(F2, text="₹ 60", anchor="w", bg=bg_color, font=('times new roman', 12))
p14.place(x=260, y=365)

C15 = Checkbutton(F2, text="Vanilla Cappuccino", anchor="w", bg=bg_color, variable=C15f, font=('times new roman', 12))
C15.place(x=50, y=390, width=300)
# p=price
p15 = Label(F2, text="₹ 100", anchor="w", bg=bg_color, font=('times new roman', 12))
p15.place(x=260, y=390)

C16 = Checkbutton(F2, text="Black Coffee", anchor="w", bg=bg_color, variable=C16f, font=('times new roman', 12))
C16.place(x=50, y=415, width=300)
# p=price
p16 = Label(F2, text="₹ 20", anchor="w", bg=bg_color, font=('times new roman', 12))
p16.place(x=260, y=415)

C17 = Checkbutton(F2, text="Tea", anchor="w", bg=bg_color, variable=C17f, font=('times new roman', 12))
C17.place(x=50, y=440, width=300)
# p=price
p17 = Label(F2, text="₹ 15", anchor="w", bg=bg_color, font=('times new roman', 12))
p17.place(x=260, y=440)

C18 = Checkbutton(F2, text="Vanila Ice-cream  ", anchor="w", bg=bg_color, variable=C18f, font=('times new roman', 12))
C18.place(x=50, y=465, width=300)
# p=price
p18 = Label(F2, text="₹ 30", anchor="w", bg=bg_color, font=('times new roman', 12))
p18.place(x=260, y=465)

C19 = Checkbutton(F2, text="Butterscoch Ice-cream", anchor="w", bg=bg_color, variable=C19f,
                  font=('times new roman', 12))
C19.place(x=50, y=490, width=300)
# p=price
p19 = Label(F2, text="₹ 40", anchor="w", bg=bg_color, font=('times new roman', 12))
p19.place(x=260, y=490)

C20 = Checkbutton(F2, text="Strwaberry Ice-cream", anchor="w", bg=bg_color, variable=C20f, font=('times new roman', 12))
C20.place(x=50, y=515, width=300)
# p=price
p20 = Label(F2, text="₹ 50", anchor="w", bg=bg_color, font=('times new roman', 12))
p20.place(x=260, y=515)

# for quantity add
sp = Spinbox(F2, from_=1, to=50)
sp.place(x=400, y=40)

sp1 = Spinbox(F2, from_=1, to=50)
sp1.place(x=400, y=65)

sp2 = Spinbox(F2, from_=1, to=50)
sp2.place(x=400, y=90)

sp3 = Spinbox(F2, from_=1, to=50)
sp3.place(x=400, y=115)

sp4 = Spinbox(F2, from_=1, to=50)
sp4.place(x=400, y=140)

sp5 = Spinbox(F2, from_=1, to=50)
sp5.place(x=400, y=165)

sp6 = Spinbox(F2, from_=1, to=50)
sp6.place(x=400, y=190)

sp7 = Spinbox(F2, from_=1, to=50)
sp7.place(x=400, y=215)

sp8 = Spinbox(F2, from_=1, to=50)
sp8.place(x=400, y=240)

sp9 = Spinbox(F2, from_=1, to=50)
sp9.place(x=400, y=265)

sp10 = Spinbox(F2, from_=1, to=50)
sp10.place(x=400, y=290)

sp11 = Spinbox(F2, from_=1, to=50)
sp11.place(x=400, y=315)

sp12 = Spinbox(F2, from_=1, to=50)
sp12.place(x=400, y=340)

sp13 = Spinbox(F2, from_=1, to=50)
sp13.place(x=400, y=365)

sp14 = Spinbox(F2, from_=1, to=50)
sp14.place(x=400, y=390)

sp15 = Spinbox(F2, from_=1, to=50)
sp15.place(x=400, y=415)

sp16 = Spinbox(F2, from_=1, to=50)
sp16.place(x=400, y=440)

sp17 = Spinbox(F2, from_=1, to=50)
sp17.place(x=400, y=465)

sp18 = Spinbox(F2, from_=1, to=50)
sp18.place(x=400, y=490)

sp19 = Spinbox(F2, from_=1, to=50)
sp19.place(x=400, y=515)

# for bill area
F3 = Frame(root, relief=GROOVE, bd=10)
F3.place(x=850, y=220, width=650, height=600)


def welcome():
    textarea.config(state=NORMAL)  # Allow editing temporarily
    textarea.delete(1.0, END)
    textarea.insert(END, "\t \t Welcome Smartbyte Retail")
    textarea.insert(END, f"\n\nBill Number:\t\t{bill_no.get()}")
    textarea.insert(END, f"\nCustomer Name:\t\t{c_name.get()}")
    textarea.insert(END, f"\nPhone Number:\t\t{c_phone.get()}")
    textarea.insert(END, f"\n\n==================================================")
    textarea.insert(END, "\nProduct\t\tQTY\t\tPrice")
    textarea.insert(END, f"\n==================================================\n")
    textarea.configure(font='arial 15 bold')
    textarea.config(state=DISABLED)  # Make it read-only



bill_title = Label(F3, text='Bill Area', font='arial 15 bold', bd=7, relief=GROOVE).pack(fill=X)
scrol_y = Scrollbar(F3, orient=VERTICAL)
textarea = Text(F3, yscrollcommand=scrol_y)
scrol_y.pack(side=RIGHT, fill=Y)
scrol_y.config(command=textarea.yview)
textarea.pack()
welcome()  # this function call for bill area


def gbill():
    if c_name.get() == "" or c_phone.get() == "":
        messagebox.showerror("Error", "Customer details are required!")
        return

    textarea.config(state=NORMAL)  # Enable editing

    # Clear and re-add the welcome message with customer details
    textarea.delete(1.0, END)
    textarea.insert(END, "\t \t Welcome Smartbyte Retail")
    textarea.insert(END, f"\n\nBill Number:\t\t{bill_no.get()}")
    textarea.insert(END, f"\nCustomer Name:\t\t{c_name.get()}")
    textarea.insert(END, f"\nPhone Number:\t\t{c_phone.get()}")
    textarea.insert(END, f"\nAddress:\t\t{c_address.get()}")
    textarea.insert(END, f"\n\n==================================================")
    textarea.insert(END, "\nProduct\t\tQTY\t\tPrice")
    textarea.insert(END, f"\n==================================================\n")

    # Reinsert all previously added products
    for var, item, price, qty in [
        (C1f, C1, p1, sp), (C2f, C2, p2, sp1), (C3f, C3, p3, sp2), (C4f, C4, p4, sp3),
        (C5f, C5, p5, sp4), (C6f, C6, p6, sp5), (C7f, C7, p7, sp6), (C8f, C8, p8, sp7),
        (C9f, C9, p9, sp8), (C10f, C10, p10, sp9), (C11f, C11, p11, sp10), (C12f, C12, p12, sp11),
        (C13f, C13, p13, sp12), (C14f, C14, p14, sp13), (C15f, C15, p15, sp14), (C16f, C16, p16, sp15),
        (C17f, C17, p17, sp16), (C18f, C18, p18, sp17), (C19f, C19, p19, sp18), (C20f, C20, p20, sp19)
    ]:
        if var.get() == 1:  # If item is selected
            item_price = int(price.cget("text").replace("₹ ", ""))
            quantity = int(qty.get())
            total_price = item_price * quantity
            textarea.insert(END, f"{item.cget('text')}\t\t{quantity}\t\t₹{total_price}\n")

    # Calculate and display the total bill amount
    total_amount = sum(total_price_list)
    textarea.insert(END, f"\n======================================")
    textarea.insert(END, f"\nTotal Payable Amount :\t\t₹ {total_amount}")
    textarea.insert(END, f"\n======================================")

    textarea.config(state=DISABLED)  # Prevent further editing

# use for to save the bill when bill is generate
def save_bill():
    if c_name.get() == "" or c_phone.get() == "":
        messagebox.showerror("Error", "Customer details are required!")
        return

    try:
        # Connect to MySQL database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",  # Default user in XAMPP/WAMP
            password="",  # Default password is empty
            database="billing_python_final"  # Your database name
        )
        cursor = conn.cursor()

        bill_number = bill_no.get()
        customer_name = c_name.get()
        phone_number = c_phone.get()
        address=c_address.get()
        emp_name= e_name.get()
        items_list = []
        total_amount = 0  # Initialize total amount

        for var, item, price, qty in [
            (C1f, C1, p1, sp), (C2f, C2, p2, sp1), (C3f, C3, p3, sp2), (C4f, C4, p4, sp3),
            (C5f, C5, p5, sp4), (C6f, C6, p6, sp5), (C7f, C7, p7, sp6), (C8f, C8, p8, sp7),
            (C9f, C9, p9, sp8), (C10f, C10, p10, sp9), (C11f, C11, p11, sp10), (C12f, C12, p12, sp11),
            (C13f, C13, p13, sp12), (C14f, C14, p14, sp13), (C15f, C15, p15, sp14), (C16f, C16, p16, sp15),
            (C17f, C17, p17, sp16), (C18f, C18, p18, sp17), (C19f, C19, p19, sp18), (C20f, C20, p20, sp19)
        ]:
            if var.get() == 1:  # If item is selected
                item_name = item.cget("text")
                unit_price = int(price.cget("text").replace("₹ ", ""))
                quantity = int(qty.get())
                total_price = unit_price * quantity

                # Append item details with unit price and total price
                items_list.append(f"{item_name} ({quantity} x ₹{unit_price} = ₹{total_price})")

                # Calculate total amount
                total_amount += total_price

        # Convert item list to a string for storing in MySQL
        items_string = ", ".join(items_list)

        # Insert bill into the database
        cursor.execute(
            "INSERT INTO bills_counter1 (bill_no, customer_name, phone, address, items, total_price,employee_name) VALUES (%s, %s, %s,%s, %s, %s, %s)",
            (bill_number, customer_name, phone_number, address, items_string, total_amount, emp_name)
        )

        conn.commit()  # Save changes
        conn.close()  # Close connection

        messagebox.showinfo("Success", "Bill has been saved to the database!")

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")


#
def additem():
    textarea.config(state=NORMAL)  # Allow editing

    textarea.delete(10.0, END)  # Clear previous added items, keeping the header
    global total_price_list
    total_price_list = []  # Reset total price list

    # List of checkbuttons, spinboxes, and prices
    items = [
        (C1f, C1, p1, sp), (C2f, C2, p2, sp1), (C3f, C3, p3, sp2), (C4f, C4, p4, sp3),
        (C5f, C5, p5, sp4), (C6f, C6, p6, sp5), (C7f, C7, p7, sp6), (C8f, C8, p8, sp7),
        (C9f, C9, p9, sp8), (C10f, C10, p10, sp9), (C11f, C11, p11, sp10), (C12f, C12, p12, sp11),
        (C13f, C13, p13, sp12), (C14f, C14, p14, sp13), (C15f, C15, p15, sp14), (C16f, C16, p16, sp15),
        (C17f, C17, p17, sp16), (C18f, C18, p18, sp17), (C19f, C19, p19, sp18), (C20f, C20, p20, sp19)
    ]

    for var, item, price, qty in items:
        if var.get() == 1:  # If item is selected
            item_price = int(price.cget("text").replace("₹ ", ""))  # Extract price
            quantity = int(qty.get())  # Get quantity
            total_price = item_price * quantity  # Calculate total for the item
            total_price_list.append(total_price)  # Store total price for billing
            textarea.insert(END, f"{item.cget('text')}\t\t{quantity}\t\t₹{total_price}\n")

    if not total_price_list:
        messagebox.showerror('Error', 'Please select an item')

    textarea.config(state=DISABLED)  # Prevent editing

# use for clear selected item on bill
def clear():
    response = messagebox.askyesno("Save Bill", "Do you want to save the bill?")

    if response:  # If user clicks 'Yes'
        messagebox.showinfo("Info", "click on the Save Bill Button")
    else:  # If user clicks 'No'
        c_name.set('')  # Clear customer name
        c_phone.set('')  # Clear phone number
        welcome()  # Reset the bill area


# for exit of billing software
def exit():
    exit_bill = messagebox.askyesno("Exit", "Do you really want to exit?")
    if exit_bill > 0:
        root.destroy()

# Button
save_btn = Button(F2, text="Save Bill", font=('times new roman', 15, 'bold'), command=save_bill, background="yellow")
save_btn.place(x=600, y=450, width=160, height=60)

exit_btn = Button(F2, text="Exit", font=('times new roman', 15, 'bold'), command=exit, background="yellow")
exit_btn.place(x=600, y=350, width=160, height=60)

clear_btn = Button(F2, text="Clear", font=('times new roman', 15, 'bold',), command=clear, background="yellow")
clear_btn.place(x=600, y=250, width=160, height=60)

add_btn = Button(F2, text="Add Item", font=('times new roman', 15, 'bold'), command=additem, background="yellow")
add_btn.place(x=600, y=150, width=160, height=60)

genrate_btn = Button(F2, text="Generate Bill", font=('times new roman', 15, 'bold'), command=gbill, background="yellow")
genrate_btn.place(x=600, y=50, width=160, height=60)
root.mainloop()