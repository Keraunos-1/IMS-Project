from tkinter import *
import tkinter.messagebox as tkMessageBox
import tkinter as tk
from tkinter import messagebox
import sqlite3
import tkinter.ttk as ttk
import matplotlib.pyplot as plt
from tkinter import PhotoImage
from tkinter import Tk, Frame, Label, Menu, SOLID
from datetime import datetime

root = Tk()
root.title("Welcome to Inventory System")

width = 1024
height = 520
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#b0c4de")

USERNAME = StringVar()
PASSWORD = StringVar()
PRODUCT_NAME = StringVar()
DATE = StringVar()
PRODUCT_BELONG = StringVar()
PRODUCT_PRICE = IntVar()
PRODUCT_QTY = IntVar()
SEARCH = StringVar()

def Database():
    """
    Establishes a connection to the database and creates the necessary tables if they do not exist.
    
    This function connects to the 'pythontut.db' SQLite database using the `sqlite3.connect()` method.
    It then creates two tables, 'admin' and 'product', if they do not already exist.
    
    Parameters:
    None
    
    Returns:
    None
    """
    global conn, cursor
    conn = sqlite3.connect("pythontot.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `admin` (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `product` (product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, product_name TEXT, date TEXT, product_belong TEXT, product_qty TEXT, product_price TEXT)")
    cursor.execute("SELECT * FROM `admin` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `admin` (username, password) VALUES('admin', 'admin')")
        conn.commit()

def Exit():
    """
    This function is used to exit the program after asking for confirmation from the user.
    
    It displays a message box with the title 'Inventory System' and the message 'Are you sure you want to exit?'. 
    The message box has a warning icon.
    
    If the user clicks 'yes', it destroys the root window and exits the program.
    
    Parameters:
    None
    
    Returns:
    None
    """
    result = tkMessageBox.askquestion('Inventory System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

def Exit2():
    """
    This function is used to exit the program after asking for confirmation from the user.
    
    It displays a message box with the title 'Inventory System' and the message 'Are you sure you want to exit?'. 
    The message box has a warning icon.
    
    If the user clicks 'yes', it destroys the 'Home' window and exits the program.
    
    Parameters:
    None
    
    Returns:
    None
    """
    result = tkMessageBox.askquestion('Inventory System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        Home.destroy()
        exit()

def ShowLoginForm():
    """
    This function shows the login form for the Inventory System. 
    It initializes the login form, sets its title, dimensions, and position on the screen. 
    The login form is made non-resizable and then the LoginForm function is called.
    """
    global loginform
    loginform = Toplevel()
    loginform.title("Inventory System/Account Login")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    loginform.resizable(0, 0)
    loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    LoginForm()

def LoginForm():
    """
    This function creates a login form with labels for username and password, text fields for user input, and a login button. 
    It sets up the visual components using Frames, Labels, Entries, and Buttons with specific fonts and dimensions. 
    The login button is configured to trigger the 'Login' function when clicked or when the 'Return' key is pressed. 
    """
    global lbl_result
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

def Home():
    """
    This function is the main window of the program. It creates a new Tkinter window, 
    sets its title, geometry and size, background color and adds a title frame with a 
    label displaying "Inventory System". It also creates a menu bar with two menus: 
    "Account" and "Inventory". The "Account" menu has two options: "Logout" and "Exit", 
    while the "Inventory" menu has two options: "Add new" and "View". The function also 
    destroys the login window when it is called.
    """
    global Home
    Home = Tk()
    Home.title("Inventory System/Home")
    width = 1024
    height = 520
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Home.resizable(0, 0)
    Home.configure(bg='#4682b4')
    Title = Frame(Home, bd=1, relief=SOLID)
    Title.pack(pady=10)
    lbl_display = Label(Title, text="Inventory System", font=('arial', 45), bg="#b0c4de")
    lbl_display.pack()
    menubar = Menu(Home)
    filemenu = Menu(menubar, tearoff=0)
    filemenu2 = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Logout", command=Logout)
    filemenu.add_command(label="Exit", command=Exit2)
    filemenu2.add_command(label="Add new", command=ShowAddNew)
    filemenu2.add_command(label="View", command=ShowView)
    menubar.add_cascade(label="Account", menu=filemenu)
    menubar.add_cascade(label="Inventory", menu=filemenu2)
    Home.config(menu=menubar)
    Home.mainloop()
    loginform.destroy()


def ShowAddNew():
    global addnewform
    addnewform = Toplevel()
    addnewform.title("Inventory System/Add new")
    width = 600
    height = 600
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform.resizable(0, 0)
    AddNewForm()  # Use mainloop to display the Toplevel window

def AddNewForm():
    TopAddNew = Frame(addnewform, width=600, height=100, bd=1, relief=SOLID)
    TopAddNew.pack(side=TOP, pady=20)
    lbl_text = Label(TopAddNew, text="Add New Product", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidAddNew = Frame(addnewform, width=600)
    MidAddNew.pack(side=TOP, pady=50)
    lbl_productname = Label(MidAddNew, text="Product Name:", font=('arial', 25), bd=10)
    lbl_productname.grid(row=0, sticky=W)
    lbl_date = Label(MidAddNew, text="Date:", font=('arial', 25), bd=10)
    lbl_date.grid(row=1, sticky=W)
    lbl_productname = Label(MidAddNew, text="Product Belong:", font=('arial', 25), bd=10)
    lbl_productname.grid(row=2, sticky=W)
    lbl_qty = Label(MidAddNew, text="Product Quantity:", font=('arial', 25), bd=10)
    lbl_qty.grid(row=3, sticky=W)
    lbl_price = Label(MidAddNew, text="Product Price:", font=('arial', 25), bd=10)
    lbl_price.grid(row=4, sticky=W)
    productname = Entry(MidAddNew, textvariable=PRODUCT_NAME, font=('arial', 25), width=15)
    productname.grid(row=0, column=1)
    date = Entry(MidAddNew, textvariable=DATE, font=('arial', 25), width=15)
    date.grid(row=1, column=1)
    productbelong = Entry(MidAddNew, textvariable=PRODUCT_BELONG, font=('arial', 25), width=15)
    productbelong.grid(row=2, column=1)
    productqty = Entry(MidAddNew, textvariable=PRODUCT_QTY, font=('arial', 25), width=15)
    productqty.grid(row=3, column=1)
    productprice = Entry(MidAddNew, textvariable=PRODUCT_PRICE, font=('arial', 25), width=15)
    productprice.grid(row=4, column=1)
    btn_add = Button(MidAddNew, text="Save", font=('arial', 18), width=30, bg="#009ACD", command=AddNew)
    btn_add.grid(row=7, columnspan=2, pady=20)
    
# This function adds a new product to the database with the provided information.
def AddNew():
    Database()
    # Execute an Insert Query to add a new product to the database.
    cursor.execute("INSERT INTO product (product_name, date, product_belong, product_qty, product_price) VALUES (?, ?, ?, ?, ?)", (str(PRODUCT_NAME.get()), str(DATE.get()), str(PRODUCT_BELONG.get()), int(PRODUCT_QTY.get()), int(PRODUCT_PRICE.get())))
    conn.commit()
    PRODUCT_NAME.set("")
    DATE.set("")
    PRODUCT_BELONG.set("")
    PRODUCT_PRICE.set("")
    PRODUCT_QTY.set("")
    cursor.close()
    conn.close()
    
def ViewForm():
    """
    This function is used to display the 'View Products' form. It does the following:
    1. Creates and places three frames (TopViewForm, LeftViewForm, MidViewForm) in the viewform window.
    2. Creates and places a label (lbl_text) in the TopViewForm.
    3. Creates and places a label (lbl_txtsearch) and an entry (search) in the LeftViewForm.
    4. Creates and places three buttons (btn_search, btn_reset, btn_delete) in the LeftViewForm.
    5. Creates and places two scrollbars (scrollbarx, scrollbary) and a treeview widget (tree) in the MidViewForm.
    6. Configures the treeview widget with columns and headings.
    7. Calls the `DisplayData` function to populate the treeview widget with data from the database.
    """
    global tree  # makes the tree variable global
    # create and place frames
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)
    # create and place labels and buttons
    lbl_text = Label(TopViewForm, text="View Products", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=Search)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(LeftViewForm, text="Delete", command=Delete)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_update = Button(LeftViewForm, text="Update", command=update)
    btn_update.pack(side=TOP, padx=10, pady=10, fill=X)
    # create and place scrollbars and treeview widget
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("ProductID", "Product Name", "Date", "Product Belong", "Product Qty", "Product Price"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    # configure treeview widget
    tree.heading('ProductID', text="ProductID",anchor=W)
    tree.heading('Product Name', text="Product Name",anchor=W)
    tree.heading('Date', text="Date",anchor=W)
    tree.heading('Product Belong', text="Product Belong", anchor=W)
    tree.heading('Product Qty', text="Product Qty",anchor=W)
    tree.heading('Product Price', text="Product Price",anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=120)
    tree.column('#2', stretch=NO, minwidth=0, width=120)
    tree.column('#3', stretch=NO, minwidth=0, width=200)
    tree.column('#4', stretch=NO, minwidth=0, width=200)
    tree.column('#5', stretch=NO, minwidth=0, width=200)
    tree.pack()
    DisplayData()  # call the DisplayData function to populate the treeview widget

def DisplayData():
    """
    This function is used to display data from the database in the treeview widget. It does the following:
    1. Calls the `Database` function to establish a connection to the database.
    2. Executes a SQL query to fetch all the rows from the `product` table.
    3. Loops through the fetched data and inserts it into the treeview widget.
    4. Closes the cursor and the connection to the database.
    
    This function is called when the program starts and whenever the user clicks the "Reset" button.
    """
    Database() # Establish a connection to the database
    cursor.execute("SELECT * FROM `product`") # Fetch all rows from the product table
    fetch = cursor.fetchall() # Fetch all rows
    for data in fetch: # Loop through the fetched data
        tree.insert('', 'end', values=(data)) # Insert the data into the treeview widget
    cursor.close() # Close the cursor
    conn.close() # Close the connection to the database
    

# This function searches the database for the product_name that matches the text in the search bar.
def Search():
    # delete(*tree.get_children()) only works when there is something to get deleted. So first check if anything is selected.
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        Database()
        cursor.execute("SELECT * FROM `product` WHERE `product_name` LIKE ?", ('%'+str(SEARCH.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
# This function deletes the selected item from the tree widget, and then refreshes the display of the data.
def Reset():
    # delete(*tree.get_children()) only works when there is something to get deleted. So first check if anything is selected.
    tree.delete(*tree.get_children())
    # then call DisplayData() to re-populate the Tree Widget with all the data.
    DisplayData()
    # finally, set the SEARCH variable to an empty string to clear the search bar.
    SEARCH.set("")
    
# The function first checks if an item is currently selected in a tree widget. If an item is selected, it retrieves the product_name, product_qty, and product_price values of the selected item. 
# Then, it prompts the user to enter new values for product_name, product_qty, and product_price. 
# After that, it calls a function named Database to establish a connection to the database and a cursor object to execute SQL queries.
# The function then executes an SQL UPDATE query to update the product table with the new values. The WHERE clause specifies that the update should be applied to the row with the same product_name as the selected item.
# Finally, it commits the changes to the database, closes the cursor and connection, and calls a function named DisplayData to refresh the display of the data.
def update():
    selected_item = tree.focus()
    if selected_item:
        product_name = tree.item(selected_item)['values'][0]
        date = tree.item(selected_item)['values'][1]
        product_belong = tree.item(selected_item)['values'][2]
        product_qty = tree.item(selected_item)['values'][3]
        product_price = tree.item(selected_item)['values'][4]
    else:
        print("No item selected")
        return

    update_window = tk.Toplevel(root)
    update_window.title("Inventory/Update Product")
    update_window.geometry("400x200")

    name_label = tk.Label(update_window, text="Product Name:")
    name_label.grid(row=0, column=0, padx=5, pady=5)
    name_entry = tk.Entry(update_window)
    name_entry.grid(row=0, column=1, padx=5, pady=5)
    name_entry.insert(0, product_name)
    
    date_label = tk.Label(update_window, text="Date:")
    date_label.grid(row=1, column=0, padx=5, pady=5)
    date_entry = tk.Entry(update_window)
    date_entry.grid(row=1, column=1, padx=5, pady=5)
    date_entry.insert(0, date)
    
    belong_label = tk.Label(update_window, text="Office Belong:")
    belong_label.grid(row=2, column=0, padx=5, pady=5)
    belong_entry = tk.Entry(update_window)
    belong_entry.grid(row=2, column=1, padx=5, pady=5)
    belong_entry.insert(0, product_belong)

    qty_label = tk.Label(update_window, text="Quantity:")
    qty_label.grid(row=3, column=0, padx=5, pady=5)
    qty_entry = tk.Entry(update_window)
    qty_entry.grid(row=3, column=1, padx=5, pady=5)
    qty_entry.insert(0, product_qty)

    price_label = tk.Label(update_window, text="Price:")
    price_label.grid(row=4, column=0, padx=5, pady=5)
    price_entry = tk.Entry(update_window)
    price_entry.grid(row=4, column=1, padx=5, pady=5)
    price_entry.insert(0, product_price)
    
    def update_product():
        new_product_name = name_entry.get()
        new_product_qty = qty_entry.get()
        new_product_price = price_entry.get()
        new_entry_date = date_entry.get()
        new_product_belong = belong_entry.get()
        Database()
        cursor.execute("""
            UPDATE product
            SET product_name = ?, date = ?, product_belong = ?, product_qty = ?, product_price = ?
            WHERE product_name = ?""", 
        (new_product_name, new_entry_date, new_product_belong, new_product_qty, new_product_price, product_name))
        conn.commit()
        cursor.close()
        conn.close()
        DisplayData()

    update_button = tk.Button(update_window, text="Update", command=update_product)
    update_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
    
def Delete():
    """
    This function is used to delete a selected product from the inventory.
    It first checks if an item is selected in the tree view. If no item is selected,
    it prints a message saying "No item selected".
    If an item is selected, it asks the user for confirmation using a message box.
    If the user confirms, it executes a SQL DELETE query to remove the selected item from the database.
    After the deletion is complete, it updates the display by calling the DisplayData function.
    """
    selected_item = tree.focus()
    if selected_item:
        result = tkMessageBox.askquestion('Inventory System', 'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            Database()
            cursor.execute("DELETE FROM `product` WHERE `product_name` = ?", (tree.item(selected_item)['values'][1],))
            conn.commit()
            cursor.close()
            conn.close()
            tree.delete(selected_item)
    else:
        print("No item selected")

    # Create a new Toplevel window and set its title.
    # Specify the dimensions of the window and calculate the position to center it on the screen.
    # Set the window's geometry (size and position) and make it non-resizable.
    # Call the ViewForm function to populate the window with content.
def ShowView():
    global viewform
    viewform = Toplevel()
    viewform.title("Sales and Inventory Management System/View Product")
    width = 1000
    height = 400
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.resizable(0, 0)
    ViewForm()

def Logout():
    result = tkMessageBox.askquestion('Inventory System', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes': 
        admin_id = ""
        root.deiconify()
        Home.destroy()
        
def Login(event=None):
    """
    This function is used to handle the login process in the application. It takes an optional event parameter which is used to trigger the function when an event occurs. The function performs the following steps:
    
    1. It initializes the global variable `admin_id`.
    2. It calls the `Database()` function to establish a connection to the database.
    3. It checks if the `USERNAME` and `PASSWORD` variables are empty. If either of them is empty, it displays a message to complete the required field and sets the text color of `lbl_result` to red.
    4. If the `USERNAME` and `PASSWORD` variables are not empty, it executes a SQL query to check if the provided username and password exist in the `admin` table of the database.
    5. If a matching record is found, it retrieves the admin ID, clears the `USERNAME` and `PASSWORD` variables, clears the text of `lbl_result`, and calls the `ShowHome()` function to display the home page.
    6. If no matching record is found, it displays a message indicating invalid username or password and clears the `USERNAME` and `PASSWORD` variables.
    7. It closes the cursor and the database connection.
    
    Note: This function assumes that the necessary database connection and cursor objects have been initialized before calling this function.
    """
    global admin_id
    Database()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
            data = cursor.fetchone()
            admin_id = data[0]
            USERNAME.set("")
            PASSWORD.set("")
            lbl_result.config(text="")
            ShowHome()
        else:
            lbl_result.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    cursor.close()
    conn.close() 

def ShowHome():
    """
    This function is responsible for displaying the main window of the program. It performs the following steps:
    
    1. It hides the root window.
    2. It calls the Home function to create and display the main window.
    3. It starts the main event loop of the main window.
    4. It destroys the login form window.
    
    Note: This function assumes that the Home function and the loginform window have been previously defined.
    """
    root.withdraw()
    Home()
    Home.mainloop()
    loginform.destroy()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Account", command=ShowLoginForm)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="Menu", menu=filemenu)
root.config(menu=menubar)
Title = Frame(root, bd=1, relief=SOLID)
Title.grid(row=1, column=1,pady=10)
lbl_display = Label(Title, text="Welcome to the Inventory! Good Day! ", font=('arial', 45), bg="#4682b4")
lbl_display.pack()

if __name__ == '__main__':
    root.mainloop()
