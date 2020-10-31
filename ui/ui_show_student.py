import tkinter


class ShowStudent:
    def __init__(self, *data):
        print(data)

        # 대충 창 설정 하는 내용
        self.root = tkinter.Tk()

        self.root.title("파일 불러오기")
        # self.root.geometry("500x100")
        self.root.resizable(0, 0)
