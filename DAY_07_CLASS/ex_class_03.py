'''
상속을 볼거랍니다~

2차원 점 클래스
클래스 이름 : pint2D
클래스 속성 : x, y, color, shape, size
클래스 기능 : 주행한다, 정지한다, 후진한다, 그리기
'''
class Point2D:
    # class 속성 => 없음

    # 객체 즉 인스턴스 생성
    def __init__(self, x, y, color, shape, size):
        self.x = x
        self.y = y
        self.color = color
        self.shape = shape
        self.size = size

    def draw(self):
        print(f"좌표 ({self.x}, {self.y}) 그리기")

    def printInfo(self):
        print(f"위치 : {self.x}, {self.y}")
        print(f"색상 : {self.color}")
        print(f"형태 : {self.shape}")