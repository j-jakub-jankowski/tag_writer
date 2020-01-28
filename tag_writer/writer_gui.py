import tkinter as tk
import usb_tag_reader as reader


class Application:
    def __init__(self):
        MainWindow()


class MainWindow:
    def __init__(self):
        window = tk.Tk()
        # window.geometry("660x360")
        window.title("Tag Writer")

        import func

        # buttons
        bt_open_reader = tk.Button(window, text='OPEN READER',
                                   font=("Arial", 15), width=15, height=1, borderwidth=3, activeforeground='red',
                                   command=lambda: reader.open_reader())
        bt_load_tag = tk.Button(window, text='LOAD TAG',
                                font=("Arial", 15), width=15, height=1, borderwidth=3, activeforeground='red',
                                command=lambda: self.get_input_tags())
        bt_read_tag = tk.Button(window, text='READ TAG',
                                font=("Arial", 15), width=15, height=3, borderwidth=3, activeforeground='red',
                                command=lambda: func.set_read_tag())
        bt_save_tag = tk.Button(window, text='SAVE TAG',
                                font=("Arial", 15), width=15, height=2, borderwidth=3, activeforeground='red',
                                command=lambda: func.write_tag())
        bt_next_tag = tk.Button(window, text='>>>>>',
                                font=("Arial", 15), width=15, height=3, borderwidth=3,
                                command=lambda: func.change_tag(1))
        bt_previous_tag = tk.Button(window, text='<<<<<',
                                    font=("Arial", 15), width=15, height=3, borderwidth=3,
                                    command=lambda: func.change_tag(-1))

        # labels
        lb_read_tag = tk.Label(window, textvariable=func.r_tag,
                               font=("Arial", 45), width=5, height=1, borderwidth=3, background='white')

        # inputs
        en_actual_tag = tk.Entry(window, textvariable=func.actual_tag,
                                 font=("Arial", 45), width=5, borderwidth=3, justify='center')

        sb_textbox = tk.Scrollbar(window)  # scrollbar for tag input
        self.txt_tag_to_write = tk.Text(window, yscrollcommand=sb_textbox.set,
                                        font=("Arial", 15), width=7, height=15, borderwidth=3)
        sb_textbox.config(command=self.txt_tag_to_write.yview)

        sb_logger = tk.Scrollbar(window)  # scrollbar for logger
        self.txt_logger = tk.Text(window, yscrollcommand=sb_logger.set,
                             font=("Arial", 8), width=110, height=15, borderwidth=3)
        sb_logger.config(command=self.txt_logger.yview)

        # options
        rb_save_one = tk.Radiobutton(window, variable=func.rb_var_save, value=1, text='ONE')
        rb_save_on_click = tk.Radiobutton(window, variable=func.rb_var_save, value=2, text='ON CLICK >>>')
        rb_from_list = tk.Radiobutton(window, variable=func.rb_var_source, value=1, text='FROM LIST')
        rb_auto_inc = tk.Radiobutton(window, variable=func.rb_var_source, value=2, text='AUTO +1')

        # layout
        bt_open_reader.grid(row=0, column=0)
        bt_load_tag.grid(row=0, column=2)

        bt_read_tag.grid(row=2, column=0)
        lb_read_tag.grid(row=2, column=1)

        bt_save_tag.grid(row=3, column=0, rowspan=2)
        rb_save_one.grid(row=3, column=1, sticky='W')
        rb_save_on_click.grid(row=4, column=1, sticky='W')
        rb_from_list.grid(row=3, column=2, sticky='W')
        rb_auto_inc.grid(row=4, column=2, sticky='W')

        bt_previous_tag.grid(row=5, column=0)
        en_actual_tag.grid(row=5, column=1)
        bt_next_tag.grid(row=5, column=2)

        self.txt_tag_to_write.grid(row=0, column=4, rowspan=6)
        sb_textbox.grid(row=0, column=5, rowspan=6, sticky='NSW')

        #self.txt_logger.grid(row=6, column=0, columnspan=5)
        #sb_logger.grid(row=6, column=5, sticky='NSW')

        # configure rows and columns size
        col_count, row_count = window.grid_size()
        for col in range(col_count):
            window.grid_columnconfigure(col, minsize=20)

        for row in range(row_count):
            window.grid_rowconfigure(row, minsize=10)

        window.mainloop()

    def get_input_tags(self):
        """get text from widget and pass to function"""
        input_tags = self.txt_tag_to_write.get('1.0', 'end')

        import func

        func.load_tag(input_tags)


apl = Application()
