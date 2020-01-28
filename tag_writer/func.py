import usb_tag_reader as reader
import tkinter as tk


r_tag = tk.StringVar()
actual_tag = tk.IntVar()
w_tag = tk.StringVar()

rb_var_save = tk.IntVar()  # 1 - save one, 2 - save on click >>>
rb_var_source = tk.IntVar()  # 1 - tag from list, 2 - auto increment +1
rb_var_source.set(1)  # set default value
rb_var_save.set(1)  # set default value

tag_list = []
tag_list_index = 0


def load_tag(input_tags):
    """split tags (separated by enter) and save to list"""
    global tag_list
    tag_list = list(input_tags[:-1].split('\n'))
    actual_tag.set(tag_list[0])
    print(tag_list)


def set_read_tag():
    """show read tag on screen"""
    r_tag.set(reader.read_tag_int())


def write_tag():
    """check if value from list is integer and write tag"""
    if isinstance(actual_tag.get(), int):
        tag = actual_tag.get()
        reader.save_tag_and_check(tag)
    else:
        pass


def change_tag(inc):
    """increase or decrease tag number from list or +/-1. If option check - automatically write tag"""
    if rb_var_source.get() == 1:
        global tag_list_index
        tag_list_index = tag_list_index + inc
        if tag_list_index >= len(tag_list):
            tag_list_index = 0
        if tag_list_index < 0:
            tag_list_index = len(tag_list) - 1

        actual_tag.set(tag_list[tag_list_index])

    elif rb_var_source.get() == 2:
        tag = actual_tag.get()
        actual_tag.set(tag + inc)

    if rb_var_save.get() == 2:
        write_tag()



