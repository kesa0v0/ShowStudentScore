import xlrd as excel
import pprint

choice_position = 4
answer_position = 5
total_etc1_position = 8
total_etc2_position = 11
name_position = 2


class ExcelDataStructure:
    # TODO: Delete preload data
    def __init__(self, file):
        # 학생들
        self.student = {}

        # 범위 찾기
        start = 0
        end = 0
        while end < 100:
            if file.cell_value(end, 1).startswith("반/번호"):
                # 시작 위치 찾기
                start = end
                print("시작위치:", start)

            if file.cell_value(end, 1).startswith("수강생"):
                # 끝 위치 찾기
                print("끝 위치:", end)
                break
            end += 1

        # 총점 찾기
        self.total_choice_score = float(file.cell_value(start + 2, choice_position)[1:-1])
        self.total_answer_score = float(file.cell_value(start + 2, answer_position)[1:-1])
        self.total_etc1_score = float(file.cell_value(start + 2, total_etc1_position)[1:-1])
        self.total_etc2_score = float(file.cell_value(start + 2, total_etc2_position)[1:-1])

        print("선택형:", self.total_choice_score)
        print("서술형:", self.total_answer_score)
        print("기타1:", self.total_etc1_score)
        print("기타2:", self.total_etc2_score)

        for number in range(start + 3, end):
            self.student[file.cell_value(number, 1).split("/")[1]] = (  # 번호
                file.cell_value(number, name_position),
                file.cell_value(number, choice_position),
                file.cell_value(number, answer_position),
                file.cell_value(number, total_etc1_position),
                file.cell_value(number, total_etc2_position)
            )

        pprint.pprint(self.student)
