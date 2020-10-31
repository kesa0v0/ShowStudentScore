import tkinter

import ui.ui_show_student


class SearchStudent:
    def confirm_downed(self):
        number = self.text_number.get()
        print("confirm!")
        print("Number:", number)

        ui.ui_show_student.ShowStudent(number + self.file[number])

    def __init__(self, file):
        # 엑셀 파일 열기
        self.file = file

        # 대충 창 설정 하는 내용
        self.root = tkinter.Tk()

        self.root.title("학생 선택")
        # root.geometry("500x100")
        self.root.resizable(0, 0)

        # ui 구성품
        self.label_filename = tkinter.Label(self.root, text="번호: ")
        self.label_filename.grid(row=0, column=0)

        self.text_number = tkinter.Entry(self.root, width=50)
        self.text_number.grid(row=0, column=1)

        self.button_confirm = tkinter.Button(self.root, text="찾기", command=self.confirm_downed, width=20)
        self.button_confirm.grid(row=1, column=1)

        # ui 실행
        self.root.mainloop()
