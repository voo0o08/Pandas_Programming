'''
입력받은 내용을 파일에 저장하는 프로그램
- 조건 : 대문자X, 소문자x가 입력 시 입력 받기 중단
'''
import time

filename = "ex_test_file.txt"
# file = open(filename, mode="w", encoding="utf8")

with open(filename, mode="a", encoding="utf8") as f:
    while True:
        userInput = input("입력할 문장을 입력해주세요.")

        # 종료 검사
        if userInput in ["x", "X"]:
            print("종료합니다~")
            break

        # 파일에 시간 일시 정지 후 반복하기
        time.sleep(1)

        f.write(userInput+"\n")
    f.write(f"최종 저장 시간 : {f.write(time.ctime())}\n")
# file.close()