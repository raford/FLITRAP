#!/usr/bin/env python

# Author: Raymond A. Ford
#
# Date 2 May 2015
#
# Email: raford85@yahoo.com
#   Public Key  : https://pgp.mit.edu/pks/lookup?search=raford85&op=index
#   KeyID       : 55082894
#
# License: GPLv3 https://www.gnu.org/licenses/gpl-3.0.html
#
# Description:
#    This script makes use of several pieces of data obtained from the HHMI
#    Janelia Farm, Bloomington Drosophila Stock Center, and FlyBase ---
#    obtained via webscraping --- to allow a researcher to access data 
#    related to D. melanogaster GAL4 lines without having to visit these
#    sites. This in turn allows a researcher to work more effecitively and not
#    waste his or her precious time. This GUI application is unique in several
#    ways: the researcher is able to copy a BDSC stock number's fasta sequence
#    to his or her machine's clipboard with the press of a button, and the
#    researcher is able to press a button to view the expression data video
#    for a searched line (provided he or she is connected to the Internet).
#    Moreover, this application was developed in Python 2.7.X and requires
#    only the scientific Python stack to run, as it uses the Tkinter module
#    that is available in the Python standard library. This application should
#    run on Microsoft's Windows, Apple's OSX, and various GNU/Linux 
#    distributions with little problems. Additionally, we have made binaries
#    available for Microsoft Windows 7 and Apple's OSX Yosemite.
#
# Icon Source: Adapted from https://openclipart.org/detail/145735/cartoon-fly
#     The site states that the image is free available and able to be used in
#     both commercial and noncommercial settings. The image is titled
#     "Cartoon Fly" and was created by PrintKiller on 2011-06-17.
#
# Data Sources:
#     * FASTA files created from data obtained via webscraping both FlyBase
#       and the HHMI Janelia Farm using data obtained from the Bloomington
#       Drosophila Stock Center (BDSC).

#     * Other data obtained from the Bloomington Drosophila Stock Center and
#       the HHMI Janelia Farm (HHMIJF)
#
#     + FlyBase : http://flybase.org/
#     + HHMIJF  : http://flweb.janelia.org/cgi-bin/flew.cgi
#     + BDSC    : http://flystocks.bio.indiana.edu/
#
# Funding sources:
#     This work is supported in part by the NSF grant DUE-0926721 and 
#     NIH-NIMHD grant 5G12MD007592.
#
# Research mentors:
#    * Prof. Ming-Ying Leung, Dept. of Mathematical Sciences,
#        The University of Texas at El Paso.
#
#    * Prof. Kyung-An Han, Dept. of Biological Sciences,
#        The University of Texas at El Paso.

import os
import pandas
import webbrowser
from Tkinter import *


def get_complete_fly(current_directory):
	"""
	This function will use the current working directory to find and
    return the path of the complete_fly.csv file created through 
    wescraping relevant data from janelia.org and flybase.org on
    2 May 2015.
	----------
	current_directory  :=  the current working directory
	"""
	data = "complete_fly.csv"
	return current_directory + data


def get_stk_index(list, stock_number):
	"""
	This function will find the index number of a particular stock
    number and return that index number.
	----------
	list          :=  A list containing all of the stock numbers. This
                        list is created in the actual program.
	stock_number  :=  The stock number that we are trying to find the
                        index number of.
	"""
	if stock_number in list:
		return list.index(stock_number)
	else:
		return "nichts"


def get_fragment(index_number):
	"""
	This will use the given index_number to find the fragment 
    associated with a particular stock number. It then returns that 
    fragment as a string.
	----------
	index_number  :=  The index number of the stock number in question
	"""
	return complete_fly['Fragment'][index_number]


def get_fbsf(index_number):
	"""
	This will use the given index_number to find the fbsf associated 
    with a particular stock number. It then returns that fbsf as a 
    string.
	----------
	index_number  :=  The index number of the stock number in question
	"""
	return complete_fly['FBsf'][index_number]


def get_insertion(index_number):
	"""
	This will use the given index number to find the insertion 
    associated with a particular stock number. It then returns that 
    insertion as a string.
	----------
	index_number  :=  The index number of the stock number in question
	"""
	return complete_fly['Insertion'][index_number]


def get_gene(index_number):
	"""
	This will use the given index number to find the gene associated 
    with a particular stock number. It then returns that gene as a 
    string.
	----------
	index_number  :=  The index number of the stock number in question
	"""
	return complete_fly['Gene'][index_number]


def get_fbgn(index_number):
	"""
	This will use the given index number to find the FBgn associated 
    with a particular stock number. It then returns that tag as a 
    string.
	----------
	index_number  :=  The index number of the stock number in question
	"""
	return complete_fly['FBgn'][index_number]


def get_ncbi(index_number):
	"""
	This will use the given index number to find the NCBI tag 
    associated with a particular stock number. It then returns that tag
    as a string.
	----------
	index_number  :=  The index number of the stock number in question
	"""
	return complete_fly['NCBI'][index_number]


def get_coordinates(index_number):
	"""
	This will use the given index number to find the coordinates for a 
	particular stock number. It then returns the coordinates as a 
    string.
	----------
	index_number  :=  The index number of the stock number in question
	"""
	return complete_fly['Coordinate'][index_number]


def get_length(index_number):
	"""
	This will use the given index number to find the length for a 
	particular stock number. It then returns the length as a string.
	----------
	index_number  :=  The index number of the stock number in question
	"""
	raw_len = complete_fly['SeqLength'][index_number]
	return '(' + str(raw_len)[:-1] + 'bp)'


def get_left_primer(index_number):
	"""
	This function will use the given index number to obtain the left 
    primer for a particular stock number. It then returns the primer
    as a string.
	----------
	index_number  :=  The index number of the stock number in question
	"""
	return complete_fly['LeftPrimer'][index_number]


def get_right_primer(index_number):
	"""
	This function will use the given index number to obtain the right 
    primer for a particular stock number. It then returns the primer as
    a string.
	----------
	index_number  :=  The index number of the stock number in question
	"""
	return complete_fly['RightPrimer'][index_number]


def get_fasta(current_directory, stock_number):
	"""
	This function will locate and open the FASTA file for a given stock
    number. It will return the contents of the file if such a file 
    exists, and will return 'No such file exists' for stock numbers 
    that do not have a FASTA file.
	----------
	current_directory  :=  The current working directory.
	stock_number       :=  The stock number that we want the FASTA file for.
	"""
	data_location = "/DMel_FASTA_files/"
	file_location = DATALOCATION + data_location + stock_number + ".fasta"
	try:
		fasta_raw = open(file_location, 'r')
		read_fasta_raw = fasta_raw.read()
		fasta_raw.close()
		return read_fasta_raw + '\n'
	except:
		return "No such file exists"


def get_weburl(index_number):
	"""
	This will use the given index number to find the url for a 
	particular stock number. It then returns the url as a string.
	----------
	index_number  :=  The index number of the stock number in question
	"""
	return complete_fly['VideoLink'][index_number]


def copy_to_clipboard():
	root.clipboard_clear()
	root.clipboard_append(fasta_str)
	return ''


def callback(event):
	webbrowser.open_new(weburl)


def fly_search(*args):
	try:
		value = int(user_input.get())
		status.set('')
		index = get_stk_index(stock_list, value)
		var_stk.set(str(complete_fly['StockNumber'][index]))
		var_frag.set(get_fragment(index))
		var_fbsf.set(get_fbsf(index))
		var_insertion.set(get_insertion(index))
		var_gene.set(get_gene(index))
		var_fbgn.set(get_fbgn(index))
		var_ncbi.set(get_ncbi(index))
		var_coord.set(get_coordinates(index))
		var_length.set(get_length(index))
		var_l_primer.set(get_left_primer(index))
		var_r_primer.set(get_right_primer(index))
		global fasta_str # This is needed for the 'copy' button to work.
		fasta_str = get_fasta(DATALOCATION, str(value))
		var_fasta.set(fasta_str)
		global weburl # This is needed for the video page button to work.
		weburl = get_weburl(index)
		var_link.set(weburl)
		root.clipboard_clear()
		root.clipboard_append(fasta_str)	
	except:
		status.set("Not a valid stock number!")
		var_stk.set('')
		var_frag.set('')
		var_fbsf.set('')
		var_insertion.set('')
		var_gene.set('')
		var_fbgn.set('')
		var_ncbi.set('')
		var_coord.set('')
		var_length.set('')
		var_l_primer.set('')
		var_r_primer.set('')
		var_fasta.set('')
		var_link.set('')
		pass


# Read data in and place BDSC stock numbers into a list
DATALOCATION = os.getcwd() + '/Data/'
complete_fly = pandas.read_csv(get_complete_fly(DATALOCATION))
stock_list = list(complete_fly['StockNumber']) 


# Build the GUI frame.
root = Tk()
root.title("Fly Line Information Trap")
mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


# User input to search for stock number
user_input = StringVar()
user_input_entry = Entry(mainframe, width=7, textvariable=user_input)
user_input_entry.grid(column=1, row=0, sticky=(W, E))


# Error notification if user input is invalid
status = StringVar()
Label(mainframe, textvariable=status).grid(column=1, row=1, sticky=(W, E))


# This section draws all of the empty boxes for each section. Each box has its
# own block of code.
box_stk = Entry(mainframe, width=35, state='readonly', 
                readonlybackground='white', fg='black')
var_stk = StringVar()
box_stk.config(textvariable=var_stk, relief='sunken')
box_stk.grid(column=1, row=2, sticky=W)

box_frag = Entry(mainframe, width=35, state='readonly', 
                readonlybackground='white', fg='black')
var_frag = StringVar()
box_frag.config(textvariable=var_frag, relief='sunken')
box_frag.grid(column=1, row=3, sticky=W)

box_fbsf = Entry(mainframe, width=35, state='readonly', 
                readonlybackground='white', fg='black')
var_fbsf = StringVar()
box_fbsf.config(textvariable=var_fbsf, relief='sunken')
box_fbsf.grid(column=1, row=4, sticky=W)

box_insertion = Entry(mainframe, width=35, state='readonly', 
                    readonlybackground='white', fg='black')
var_insertion = StringVar()
box_insertion.config(textvariable=var_insertion, relief='sunken')
box_insertion.grid(column=1, row=5, sticky=W)

box_gene = Entry(mainframe, width=35, state='readonly', 
                readonlybackground='white', fg='black')
var_gene = StringVar()
box_gene.config(textvariable=var_gene, relief='sunken')
box_gene.grid(column=1, row=6, sticky=W)

box_fbgn = Entry(mainframe, width=35, state='readonly', 
                readonlybackground='white', fg='black')
var_fbgn = StringVar()
box_fbgn.config(textvariable=var_fbgn, relief='sunken')
box_fbgn.grid(column=1, row=7, sticky=W)

box_ncbi = Entry(mainframe, width=35, state='readonly', 
                readonlybackground='white', fg='black')
var_ncbi = StringVar()
box_ncbi.config(textvariable=var_ncbi, relief='sunken')
box_ncbi.grid(column=1, row=8, sticky=W)

box_coord = Entry(mainframe, width=35, state='readonly', 
                readonlybackground='white', fg='black')
var_coord = StringVar()
box_coord.config(textvariable=var_coord, relief='sunken')
box_coord.grid(column=1, row=9, sticky=W)

box_length = Label(mainframe)
var_length = StringVar()
box_length.config(textvariable=var_length, relief='flat')
box_length.grid(column=2, row=9, sticky=W)

box_l_primer = Entry(mainframe, width=35, state='readonly', 
                    readonlybackground='white', fg='black')
var_l_primer = StringVar()
box_l_primer.config(textvariable=var_l_primer, relief='sunken')
box_l_primer.grid(column=1, row=10, sticky=W)

box_r_primer = Entry(mainframe,  width=35,state='readonly', 
                    readonlybackground='white', fg='black')
var_r_primer = StringVar()
box_r_primer.config(textvariable=var_r_primer, relief='sunken')
box_r_primer.grid(column=1, row=11, sticky=W)

box_fasta = Entry(mainframe, width=35, state='readonly', 
                readonlybackground='white', fg='black') 
var_fasta = StringVar()
box_fasta.config(textvariable=var_fasta, relief = 'sunken')
box_fasta.grid(column=1, row=12, sticky=W)


# Labels for the data to be pulled
Label(mainframe, text="Enter a Stock Number:").grid(column=0, row=0, sticky=W)
Label(mainframe, text="Stock Number:").grid(column=0, row=2, sticky=E)
Label(mainframe, text="Fragment:").grid(column=0, row=3, sticky=E)
Label(mainframe, text="FBsf:").grid(column=0, row=4, sticky=E)
Label(mainframe, text="Insertion:").grid(column=0, row=5, sticky=E)
Label(mainframe, text="Gene:").grid(column=0, row=6, sticky=E)
Label(mainframe, text="FBgn:").grid(column=0, row=7, sticky=E)
Label(mainframe, text="NCBI:").grid(column=0, row=8, sticky=E)
Label(mainframe, text="Coordinates: ").grid(column=0, row=9, sticky=E)
Label(mainframe, text="Left Primer: ").grid(column=0, row=10, sticky=E)
Label(mainframe, text="Right Primer:").grid(column=0, row=11, sticky=E)
Label(mainframe, text="FASTA: ").grid(column=0, row=12, sticky=E)


# Hyperlink button for expression data video
link = Button(mainframe, text="Click Here to View Expression Data Video", 
            fg="blue")
var_link = StringVar()
link.grid(column=1, row=13, sticky=W)
link.bind("<Button-1>", callback)


# Find button can be clicked or the user can just press the Enter/Return key.
Button(mainframe, text="Find", command=fly_search).grid(column=2, 
                                                        row=0, sticky=W)
root.bind('<Return>', fly_search)


# Button can be clicked or the user can just press the CTRL+C key combo.
Button(mainframe, text="Copy", command=copy_to_clipboard).grid(column=2, 
                                                            row=12, sticky=W)

# Pad the 'boxes' by 5 pixels on each side
for child in mainframe.winfo_children():
	child.grid_configure(padx=5, pady=5)

user_input_entry.focus()
mainframe.columnconfigure(1, weight=1)
root.mainloop()