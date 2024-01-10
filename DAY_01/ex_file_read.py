'''
파일 입출력 => 출력 즉, 읽기(Read)
- 사용 내장 함수 : open()

기본 동작 : 읽고 -> 쓰고 -> 닫고
'''

# 1단계 파일 열기 : open()
file = open("message.txt", encoding="UTF-8")
print(f"file => {type(file)}, {file}\n")

# 2단계 IO작업 : read()
# 파일 내의 모든 내용을 다 읽어 옴
fileRead = file.read(5)
print(fileRead)

# 2단계 IO작업 : read(n) / defualt = -1 => 숫자 n을 넣으면 n byte를 읽어줌
fileRead = file.read(5)
print(fileRead)

# 2단계 IO 한줄 씩 읽기 : readline()
# 전체 파일을 다 보려면 반복문을 돌린다
while True:
    fline = file.readline()
    if not fline: break
    print(f"line => {type(fline)}, {fline})

# 3단계 닫기 : close()
file.close()