import tkinter
import tkinter.filedialog
import tkinter.messagebox

import xlrd as excel

import ui.ui_search_student
from data import ExcelDataStructure
import tool


class LoadFile:

    # 실행 커맨드들
    def confirm_downed(self):
        print("confirm!")
        try:
            data = ExcelDataStructure(excel.open_workbook(self.link.get()).sheet_by_index(0))
            self.serach_studnet_window = ui.ui_search_student.SearchStudent(data)

        except Exception as e:
            tkinter.messagebox.showerror("메세지 상자", e)

    def find_pressed(self):
        print("find")
        self.link.set(tkinter.filedialog.askopenfilename(title="Select File",
                                                         filetypes=(("Excel File", "*.xls"), ("all files", "*.*"))))
        print(self.link.get())

    def __init__(self):
        # 대충 창 설정 하는 내용
        self.root = tkinter.Tk()

        self.root.title("파일 불러오기")
        self.root.resizable(0, 0)
        tool.center(self.root)

        # ui 구성품
        label_filename = tkinter.Label(self.root, text="파일: ")
        label_filename.grid(row=0, column=0)

        self.link = tkinter.StringVar()
        text_filename = tkinter.Entry(self.root, width=50, textvariable=self.link)
        text_filename.grid(row=0, column=1)

        button_find = tkinter.Button(self.root, text="찾기", command=self.find_pressed, width=10)
        button_find.grid(row=0, column=2)

        button_confirm = tkinter.Button(self.root, text="불러오기", command=self.confirm_downed, width=20)
        button_confirm.grid(row=1, column=1)

        # ui 실행
        self.root.mainloop()
