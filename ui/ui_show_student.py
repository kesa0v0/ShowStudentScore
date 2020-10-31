import tkinter

import tool


class ShowStudent:
    def close(self):
        self.root.quit()
        self.root.destroy()

    def __init__(self, number, data):
        print(data)
        # name, choice, answer, etc1, etc2

        # 대충 창 설정 하는 내용
        self.root = tkinter.Tk()

        self.root.title("결과")
        self.root.resizable(0, 0)
        tool.center(self.root, (20, 20))

        # ui 구성품
        # 이름
        self.name_guide = tkinter.Label(self.root, text="이름: ")
        self.name_guide.grid(row=0, column=0)

        self.name_show = tkinter.Label(self.root, text=data[0])
        self.name_show.grid(row=0, column=1)

        # 번호
        self.name_guide = tkinter.Label(self.root, text="번호: ")
        self.name_guide.grid(row=1, column=0)

        self.name_show = tkinter.Label(self.root, text=number)
        self.name_show.grid(row=1, column=1)

        # 선택형
        self.choice_guide = tkinter.Label(self.root, text="선택형: ")
        self.choice_guide.grid(row=2, column=0)

        self.choice_show = tkinter.Label(self.root, text=data[1])
        self.choice_show.grid(row=2, column=1)

        # 서답형
        self.answer_guide = tkinter.Label(self.root, text="서답형: ")
        self.answer_guide.grid(row=3, column=0)

        self.answer_show = tkinter.Label(self.root, text=data[2])
        self.answer_show.grid(row=3, column=1)

        # 기타 1
        self.etc1_guide = tkinter.Label(self.root, text="기타1: ")
        self.etc1_guide.grid(row=4, column=0)

        self.etc1_show = tkinter.Label(self.root, text=data[3])
        self.etc1_show.grid(row=4, column=1)

        # 기타 2
        self.etc2_guide = tkinter.Label(self.root, text="기타2: ")
        self.etc2_guide.grid(row=5, column=0)

        self.etc2_show = tkinter.Label(self.root, text=data[4])
        self.etc2_show.grid(row=5, column=1)

        # 총합
        self.etc2_guide = tkinter.Label(self.root, text="총점수: ")
        self.etc2_guide.grid(row=6, column=0)

        self.etc2_show = tkinter.Label(self.root, text=data[1]+data[2]+data[3]+data[4])
        self.etc2_show.grid(row=6, column=1)

        # 나가기 버튼
        self.button_exit = tkinter.Button(self.root, text="OK", command=self.close, width=20)
        self.button_exit.grid(row=7, column=1)

        # ui 실행
        self.root.mainloop()
