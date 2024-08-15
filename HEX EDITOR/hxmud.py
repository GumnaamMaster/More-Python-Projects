recent_addresses = ['E:/lakshya/learn_prog/Assembly/console.exe', '', 'E:/lakshya/learn_prog/python/extras/broot/prototype/copy/trial_copy/trial2ascend/DOSBox.exe', 'F:/lakshya/learn_prog/python/extras/broot/prototype/copy/trial_copy/trial2ascend/DOSBox.exe', 'E:/lakshya/learn_prog/Assembly/bare.bin', 'E:/lakshya/learn_prog/Assembly/try_while_cmp.asm', 'E:/lakshya/learn_prog/PyCA_bin/New folder/truncat.apk', 'E:/lakshya/learn_prog/python/extras/broot/prototype/copy/trial_copy/trial2ascend/outsun.exe', '/media/bunny/kakran/lakshya/learn_prog/python/extras/broot/prototype/copy/trial_copy/trial2ascend/console.exe', 'F:/lakshya/learn_prog/python/extras/broot/prototype/copy/trial_copy/trial2ascend/console.exe']

number_list = []                 # number_list is self because it is used inside open_file function.
for i in range(len(recent_addresses)):
    number_list.append(i)


from tkinter import *
from tkinter import messagebox as mBox
from tkinter import ttk
from os import path
from tkinter import filedialog as fd
from multiprocessing import Process, Queue
from datetime import datetime as dt
from decimal import *                       # this is used in highlight section to compute number of digits after decimal.
from functools import partial               #this library is for command parameter inside add_command() function for recent files.
import sys
import shutil
import os
from capstone import *
from tkinter.font import Font
from colorama import init, Fore, Back, Style                     # for colored text in text widget of decode window.

class Handle(object):
    """Handle the created GUI."""
    def __init__(self, window):

        self.window = window
        self.window.title("Hex Mud")
        self.window.minsize(width=300, height=200)
        menubar = Menu(window)
        self.window.config(menu = menubar)

        filemenu = Menu(menubar, tearoff = 0)
        filemenu.add_command(label = "New", command = self.new_file)
        filemenu.add_separator()
        filemenu.add_command(label = "Open", command = self.open_file)
        filemenu.add_separator()
        #filemenu.add_command(label = "Recent files", command = self.recent_file)
        #filemenu.add_separator()
        self.recentmenu = Menu(filemenu, tearoff = 0)

        if len(recent_addresses) != 0:

            for recent_address, s_no in zip(recent_addresses, number_list):
                self.recentmenu.add_command(label = str(s_no) + " " + recent_address, command= partial(self.recent_file, self.recentmenu, s_no))
                # partial used above to pass distinct value of s_no to its function recent_file.


        filemenu.add_cascade(label = "Recent files", menu = self.recentmenu)
        filemenu.add_separator()
        filemenu.add_command(label = "Exit", command = self.quit_prog)

        aboutmenu =  Menu(menubar, tearoff = 0)
        aboutmenu.add_command(label = "About", command = self.msg_box)

        menubar.add_cascade(label = "File", menu = filemenu)
        menubar.add_cascade(label = "Help", menu = aboutmenu)
        menubar.add_cascade(label = "Decode", command = self.dissassemble_instruct)

        self.tabnote = ttk.Notebook(self.window)
        self.click = 1

    def recent_file(self, menu, serial):

        index = menu.entrycget(serial, "label")
        self.fName = index[2:]
        self.open_file()


    def quit_prog(self):
        window.quit()
        window.destroy()
        exit()

    def msg_box_process(self):
        runT = Process(target = self.msg_box)
        #runT.setDaemon(True)
        runT.start()

    def msg_box(self):
        mBox.showinfo('About', 'HexMud Hex Editor\nVersion 1\nCopyright © 2019 - forever Bunny\nAll rights reserved\nBuild time 2019 - working')

    def new_file_process(self):
        runT = Process(target = self.new_file)
        #runT.setDaemon(True)
        runT.start()

    def new_file(self):

        self.hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

        tab = Frame(self.tabnote)
        self.tabnote.add(tab, text = 'Untitled' + str(self.click))
        self.tabnote.select(self.click-1)
        self.click += 1
        self.space_max = "   "
        self.space_min = "  "

        head_text = Text(tab, height = 1, width = 120)
        head_text.grid(row = 0, column = 0, columnspan = 18, sticky = 'nws')
        head_text.config(font = "Courier")
        head_text.insert(END, " Offset(h)" + self.space_min)

        for key in self.hex_list:

            head_text.insert(END, "0" + key + self.space_max)

        head_text.insert(END, self.space_min + "Decoded text")
        head_text.configure(state = 'disabled')
        self.tabnote.pack(expand = 1, fill = "both")

        self.text = Text(tab, height = 25, width = 120)
        self.text.grid(row = 1, column = 0,rowspan = 25, columnspan = 18, sticky = 'nws')
        self.text.config(font = "Courier")

        sb = Scrollbar(tab)
        sb.grid(row = 1, column = 19, rowspan = 25, sticky = 'ns')
#Listbox west #Scrollbar highlight #how to dump hexa.
        self.text.configure(yscrollcommand = sb.set)
        sb.configure(command = self.text.yview)


class Operate(Handle):
    """Open file and prints the hexadecimal code."""
    def __init__(self, window):
        Handle.__init__(self, window)

    def open_file_process(self):
        runT = Process(target = self.open_file, args = ((q),))
        #runT.setDaemon(True)
        runT.start()
        runT.join()

    def open_file(self):

        fpath = path.abspath(__file__)                              # path of this directory including this file let's say it x.
        fDir = path.dirname(path.abspath(__file__))    
        # path of directory.
        
        """
        updated_file_path = fDir + r"add slashupdatetemphxmud.py"           # path of directory including this last file let's say it y.

        shutil.copy(fpath, updated_file_path)                          # content of x copied to y.
        """
        try:
            if(self.fName):
                pass
        except:
            self.fName=fd.askopenfilename(parent=window, initialdir=fpath)      # fName contains path of the file which user wants to open.
            print(self.fName)
            print(type(self.fName))
            
        """

        for recent_address, s_no in zip(recent_addresses, number_list):
            self.recentmenu.delete(str(s_no) + " " + recent_address)

        if self.fName in recent_addresses:
            recent_addresses.remove(self.fName)

        if len(recent_addresses) == 10 and self.fName not in recent_addresses:
            del recent_addresses[-1]

        recent_addresses.reverse()
        recent_addresses.append(self.fName)
        recent_addresses.reverse()

        for recent_address, s_no in zip(recent_addresses, number_list):
            self.recentmenu.add_command(label = str(s_no) + " " + recent_address, command= partial(self.recent_file, self.recentmenu, s_no))

        with open(updated_file_path,"r+") as updated_file:

            source_lists = updated_file.readlines()
            del source_lists[0]
            updated_file.seek(0,0)
            updated_file.truncate()

            updated_file.write("recent_addresses = " + str(recent_addresses) + "\n")
            for source_list in source_lists:
                updated_file.write(source_list)

        os.remove(fpath)
        os.rename(updated_file_path, fpath)
        """

        print("Opening file for the second time...")
        print(str(dt.now().minute) + "minutes " + str(dt.now().second) + "seconds " + str(dt.now().microsecond) + "microsecond")

        with open(self.fName,"rb") as file_bin:
            byte_data = file_bin.readlines()

            self.data_lines = []

            for line in byte_data:
                for char in line:

                    hexa = hex(char)
                    hexa = hexa[2:].upper()

                    if len(hexa) == 1:
                        hexa = "0" + hexa

                    hexa = hexa + " "
                    self.data_lines.append(hexa)

        self.normal_lines = []

        for code in self.data_lines:
            try:
                dec = bytes.fromhex(code).decode('utf-8')
                if dec == '\n' or hex(ord(dec)) == '0x0':
                    dec = '.'
                self.normal_lines.append(dec)
            except:
                self.normal_lines.append(".")

        print("Closing file for the second time...")
        print(str(dt.now().minute) + "minutes " + str(dt.now().second) + "seconds " + str(dt.now().microsecond) + "microsecond")

        self.display_hex()
        
    def dissassemble_instruct(self):
    
        init(convert=True)  # for colorama
    
        with open(self.fName,"rb") as file_read:
            mnemonic_encod = file_read.readlines()
            
        self.instruct = "OFFSET\t\tINSTRUCTION\t\tARGUMENTS\n\n"
        self.inst_arr = []
        self.inst_arr.append(list(self.instruct))
        self.new_insert_list = ["OFFSET\t\t", "INSTRUCTION\t\t", "ARGUMENTS\n"]
        
        with open("dissassembled_program.asm","w") as file_write:
            for hex_instruct in mnemonic_encod:
                md = Cs(CS_ARCH_X86, CS_MODE_32)
                for i in md.disasm(hex_instruct, 0x00):
                
                    assem = "0x%x:\t\t%s\t\t%s\n" %(i.address, i.mnemonic, i.op_str)
                    for_file = "%s %s\n" %(i.mnemonic, i.op_str)
                    
                    offset = "0x%x:" %(i.address)
                    inst   = "%s" %(i.mnemonic)
                    argum  = "%s" %(i.op_str)
                    
                    param = [offset + "\t\t", inst + "\t\t", argum + "\n"]
                    self.new_insert_list += param
                    
                    self.instruct += assem
                    self.inst_arr.append(list(assem)) # made list of lists.
                    file_write.write(for_file)
        
        self.dissassem_window()
                   
            
    def dissassem_window(self):

        dis_window = Tk()
        dis_window.title("Dissassembly")
        dis_window.minsize(width=150, height=100)
      
        myFont = Font(family="Courier New", size=22)
        
        
        dis_text = Text(dis_window, height = 25, width = 120, font = myFont)
        dis_text.grid(row = 1, column = 0,rowspan = 25, columnspan = 18, sticky = 'nws')
        dis_text.configure(font = myFont)
        
        point = 3
        
        for things in self.new_insert_list:
        
            point += 1
            if point % 3 == 1:
                tags = ("offset",)
            elif point % 3 == 2:
                tags = ("instruction",)
            else:
                tags = ("arguments",)
                
            dis_text.insert(END, things, tags)

        dis_win_sb = Scrollbar(dis_window)
        dis_win_sb.grid(row = 1, column = 19, rowspan = 25, sticky = 'ns')
        dis_win_sb.configure(command = dis_text.yview)
 #how to dump hexa.
        dis_text.configure(yscrollcommand = dis_win_sb.set)
        dis_text.tag_config("offset", background="black", foreground="yellow")
        dis_text.tag_config("instruction", background="black", foreground="blue")
        dis_text.tag_config("arguments", background="black", foreground="green")
       
        #dis_win_tree.insert(END,self.instruct)  
        dis_text.tag_add("title", "1.0", "1.30")
        dis_text.tag_config("title", background="black", foreground="red")
        
        dis_window.mainloop()


    def calculate_hex(self):
        bit_array = []
        old_hex_line = self.hex_line
        self.char_list += '\n'
        space = " "

        if len(self.normal_lines) == self.hex_line + 16: # for last line
            rem = int(len(self.normal_lines) % 16)
            if rem == 0:
                self.hex_line = len(self.normal_lines) - 16
            else:
                self.hex_line = len(self.normal_lines) - rem

        while self.hex_line != 0:
            rem = int(self.hex_line % 16)
            bit_array.append(rem)
            self.hex_line = int(self.hex_line / 16)

        bit_array.reverse()
        left_zero = 8 - len(bit_array)

        self.new_hex_line = " "

        for i in range(left_zero):
            self.new_hex_line += '0'

        for bit in bit_array:
            self.new_hex_line += self.hex_list[bit]

        #print(self.new_hex_line)
        self.hex_line = old_hex_line
        new_bit_list = self.new_hex_line + self.space_min + self.bit_list + self.space_min + self.char_list
        if len(self.normal_lines) == self.hex_line + 16:
            new_bit_list = self.new_hex_line + self.space_min + self.bit_list + self.space_min + (94-len(new_bit_list)+len(self.char_list))*space + self.char_list

        self.content.append(new_bit_list)

    def display_hex(self):

        self.new_file()
        hex_count = 0
        self.bit_list = " "
        self.char_list = ""
        self.hex_line = -16     # because lines start with 0.

        print("back again inside display_hex and before loop of display_hex")
        print(str(dt.now().minute) + "minutes " + str(dt.now().second) + "seconds " + str(dt.now().microsecond) + "microsecond")

        self.content = []
        for data_bit, normal_bit in zip(self.data_lines, self.normal_lines):
            hex_count += 1
            self.hex_line += 1
            self.bit_list += data_bit + self.space_min
            self.char_list += normal_bit

            if (hex_count == 16) or (len(self.normal_lines) == self.hex_line + 16):
                self.calculate_hex()

                hex_count = 0
                self.bit_list = " "
                self.char_list = ""

        print("end of loop of display_hex")

        for rows in self.content:
            self.text.insert(CURRENT,rows)
        print("after display ")
        print(str(dt.now().minute) + "minutes " + str(dt.now().second) + "seconds " + str(dt.now().microsecond) + "microsecond")
        #print(self.text.index("insert"))

        self.text.bind('<Button-1>', self.getinitial)
        self.text.bind('<B1-Motion>', self.getfinalsketch)


    def getinitial(self, event):
        self.initial_cur_loc = self.text.index(CURRENT)

        try:
            for tags in self.text.tag_names():
                self.text.tag_delete(tags)
        except:
            pass

    def getfinalsketch(self, event):

        final_cur_loc = self.text.index(CURRENT)        # it gives absolute address, not in x and y coordinates, but in decimal precision.
        print(final_cur_loc)
        #print(final_cur_loc)

        selected_states = [self.initial_cur_loc, final_cur_loc] # took initial and final addresses in a list.
        equivalent_states = []                          # it will contain location where equivalent decoded text will be highlighted .

        for state in selected_states:
            weight = (0.81 - (((float(state) - (int(float(state)) + 0.13)) / 0.05) * 0.04)) + (float(state) - int(float(state)))
            # logic, based on which location is calculated.

            if weight < 1:
                upd_weight = weight
                upd_weight = round(upd_weight, 2)

            else:
                upd_weight = weight / 10
                upd_weight = round(upd_weight, 3)

            if upd_weight == 1.0 or upd_weight == 0.1:  #  troubleshoot when updated weight becomes 0.100 0r 1.00.
                upd_weight = format(0.10, '.3f')

            trunc_weight = int(str(upd_weight)[2:])           # it gives the number after decimal i.e. 2.3456 ---> 3456.
            decimal_num = abs(Decimal(str(upd_weight)).as_tuple().exponent)            # counts total number of digits after decimal.

            if type(upd_weight) == str:                # when updated weight is string i.e. in case of 0.100.
                equivalent_state = format((int(float(state)) + float(upd_weight)), '.3f')     # output from format is string type.
            else:
                equivalent_state = str(round((int(float(state)) + upd_weight), decimal_num))           # equivalent location of highlighted text.

            state_pair = (int(float(state)), trunc_weight, equivalent_state)

            equivalent_states.append(state_pair)

        if equivalent_states[0][0] < equivalent_states[1][0]:
            initial_point = equivalent_states[0][2]
            final_point = equivalent_states[1][2]
        elif equivalent_states[0][0] > equivalent_states[1][0]:
            initial_point = equivalent_states[1][2]
            final_point = equivalent_states[0][2]
        else:
            if equivalent_states[0][1] < equivalent_states[1][1]:
                initial_point = equivalent_states[0][2]
                final_point = equivalent_states[1][2]
            else:
                initial_point = equivalent_states[1][2]
                final_point = equivalent_states[0][2]

        #print(type(equivalent_states[0]))
        #print(type(equivalent_states[1]))
        #print(self.initial_cur_loc + "-->" + initial_point)
        #print(final_cur_loc + "-->" + final_point)

        #print(equivalent_states[0])
        #print(equivalent_states[1])

        #print(type(cur_loc))
        #print(eqdec_cur_loc)

        self.text.tag_config("tag1", background="blue", foreground="white")

        #try:
        #print(final_cur_loc)
        #print(str(eqfinal_cur_loc))
        #print(self.initial_cur_loc)
        #print(str(eqiniti_cur_loc))

        #if eqiniti_cur_loc > eqfinal_cur_loc:    # as tag_add() will onlyb work if parameters are in specific order i.e. first initial then final
            #streqinit_cur_loc = str(round(eqfinal_cur_loc, 2))
            #streqfin_cur_loc = str(round(eqiniti_cur_loc, 2))
        #else:
            #streqinit_cur_loc = str(round(eqiniti_cur_loc, 2))
            #streqfin_cur_loc = str(round(eqfinal_cur_loc, 2))

        self.text.tag_add("tag1", initial_point, final_point)
        #self.text.tag_add("tag2", "sel.first" , "sel.last+20.76c")
        #print(sel.first)
        #except:
            #pass
        #print(self.text.index("insert"))



window = Tk()
file = Operate(window)
window.mainloop()
