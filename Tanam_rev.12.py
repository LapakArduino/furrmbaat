from tkinter import *
import tkinter as tk
from tkinter import ttk
#import tkinter
from tkinter.ttk import *
from time import sleep, strftime
import serial
from serial.serialutil import Timeout
#import ina226
import time


TURUN = 'G00 X-10000'

commPort = 'COM4'
koneksi = serial.Serial(commPort, baudrate = 115200, timeout = 1)
# = serial.Serial(port_alat, '115200', Timeout )

# creating tkinter window
root = Tk()
root.title('Tanam')

# Creating Menubar

############ Bagian Fungsi tombol ###############
def siramin():
    koneksi.write('G00 X-5000 Y-8500 Z-15600 \n'.encode())
    sleep(1)
    TURUN
    #koneksi.write('kodenga \n'.encode())

def pupukin():
    koneksi.write('G00 X0 Y0 Z0 \n'.encode())
    #koneksi.write('kodenga \n'.encode())
def tnm_lubang1():
    koneksi.write('G00 X5000 Y8500 Z15600 \n'.encode())
    sleep(1)
    TURUN

##################################################
### Fungsi Jendela
''''
ladang = tkinter.Canvas(root, bg="green", height=300, width=400)
ladang.place(x=100, y=100)
# draw arcs

def create_grid(event=None):
    w = ladang.winfo_width() # Get current width of canvas
    h = ladang.winfo_height() # Get current height of canvas
    ladang.delete('grid_line') # Will only remove the grid_line

    # Creates all vertical lines at intevals of 100
    for i in range(0, w, 50):
        ladang.create_line([(i, 0), (i, h)], tag='grid_line')

    # Creates all horizontal lines at intevals of 100
    for i in range(0, h, 50):
        ladang.create_line([(0, i), (w, i)], tag='grid_line')

ladang.pack(fill=tkinter.BOTH, expand=True)

ladang.bind('<Configure>', create_grid)




coord = 5, 5, 5, 5
lubang1 = ladang.create_rectangle( 20, 20, 120, 120, fill="#476042")
lubang2 = ladang.create_rectangle( 140, 20, 240, 120, fill="white")


def demo():
    try:
        print "Configuring INA226.."
        iSensor = ina226(INA226_ADDRESS,0)
        iSensor.configure(avg = ina226_averages_t['INA226_AVERAGES_4'],)
        iSensor.calibrate(rShuntValue = 0.02, iMaxExcepted = 2)

        time.sleep(1)

        print "Configuration Done"

        current = iSensor.readShuntCurrent()

        print "Current Value is "+str(current)+"A"

        print "Mode is "+str(hex(iSensor.getMode()))

        while True:
            print "Current: "+str(round(iSensor.readShuntCurrent(),3))+"A"+", Voltage: "+str(round(iSensor.readBusVoltage(),3))+"V"+", Power:"+str(round(iSensor.readBusPower(),3))+"W"
            #print "ShuntBus_Voltage: "+str(iSensor.readShuntVoltage())
            time.sleep(0.2)

    except KeyboardInterrupt as e:
        print '\nCTRL^C received, Terminating..'
        iSensor.close()

    except Exception as e:
        print "There has been an exception, Find detais below:"
        print str(e)
        iSensor.close()




'''

################################
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tabControl.add(tab1, text ='Dashboard')


tabControl.add(tab2, text ='Tanam')
tabControl.add(tab3, text ='Live Camera')

tabControl.pack(expand = 1, fill ="both")

ttk.Label(tab1,
          text ="Papan Kendali").grid(column = 0,
                               row = 0,
                               padx = 30,
                               pady = 30)
btn_siram = Button(root, text='Siram', command=None)
btn_siram.place(x = 30, y = 400)

ttk.Label(tab2,
          text ="Lets dive into the\
          world of computers").grid(column = 0,
                                    row = 0,
                                    padx = 30,
                                    pady = 30)

ttk.Label(tab3,
        text="sdhdufsghufgds").grid(column=0, row=0, padx=40, pady=40)

menubar = Menu(root)

# Adding File Menu and commands
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Menu', menu = file)
file.add_command(label ='New File', command = None)
file.add_command(label ='Open...', command = None)
file.add_command(label ='Save', command = None)
file.add_separator()
file.add_command(label ='Exit', command = root.destroy)

# Adding Edit Menu and commands
edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Edit', menu = edit)
edit.add_command(label ='Cut', command = None)
edit.add_command(label ='Copy', command = None)
edit.add_command(label ='Paste', command = None)
edit.add_command(label ='Select All', command = None)
edit.add_separator()
edit.add_command(label ='Find...', command = None)
edit.add_command(label ='Find again', command = None)

# Adding Help Menu
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='Tk Help', command = None)
help_.add_command(label ='Demo', command = None)
help_.add_separator()
help_.add_command(label ='About Tk', command = None)


btn_siram = Button(root, text='TANAMI', command=tnm_lubang1)
btn_siram.place(x = 30, y = 200)

btn_pupuk = Button(root, text='RESET', command=None)
btn_pupuk.place(x = 120, y = 200)

btn_benih_on = Button(root, width=10 ,  text='BALIK', command=None)
btn_benih_on.place(x = 210, y = 200)

btn_lubang3= tk.Button(tab3, text='tes tanam')
btn_lubang1 = Button(root, text='Siram', command=tnm_lubang1)
btn_lubang1.place(x = 330, y = 500)

btn_lubang2 = Button(root, text='Siram', command=None)
btn_lubang2.place(x = 30, y = 500)

'''
chkbtn1 = Checkbutton(label_frame, text = 'Checkbutton 1')
chkbtn1.place(x = 30, y = 50)
chkbtn2 = Checkbutton(label_frame, text = 'Checkbutton 2')
chkbtn2.place(x = 30, y = 80)

btn_benih_on = Button(root, text='Siram', command=None)
btn_benih_on.pack(side='top')


label_frame = LabelFrame(root, text = 'Lain')
label_frame.pack(expand = 'yes', fill = 'both')

label_frame = LabelFrame(root, text = 'Tanam Tools')
label_frame.pack(expand = 'yes', fill = 'both')
'''


# Set the position of button on the top of window


# display Menu
root.config(menu = menubar)
root.attributes('-fullscreen', True)
mainloop()