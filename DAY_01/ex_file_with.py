'''
입출력 코드 작성 시 권장하는 방법
- opne() / close() 함께 동작하는 경우의 IO에 권장
- 예) 파일 입출력, 데이터 베이스 등등
- 문법 : with open() as 별칭 :
- close()를 알아서 처리해줌
'''
filename = "fruits.txt"

# 쓰기
with open(filename, mode="w", encoding="utf8") as f:
    f.write("사과\n")
    f.write("바나나\n")
    f.write("배\n")

# 읽기
with open(filename, mode="r", encoding="utf8") as f:
    print(f.read())

