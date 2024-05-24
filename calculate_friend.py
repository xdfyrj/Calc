# 계산 벗

cmd_list = '''------------------------------
* 사용할 수 있는 명령어 *
help (명령어) : 명령어의 설명
calc
mem
del
exit'''
bar = "------------------------------"
print(cmd_list)

mem_list = []
mem_idx = 1

while True:
    print(bar)
    print('memory : ' + str(mem_list))
    cmd = input().strip().split()
    if "exit" in cmd[0]:  # 나가기
        print("Bye")
        exit()
    elif "help" in cmd[0]:  # 명령어 목록
        if cmd[-1] == "calc" or cmd[-1] == "calculate":
            print('''calculate
값을 계산
사용 방법 : calc [수식]''')
        elif cmd[-1] == "mem" or cmd[-1] == "memory":
            print('''memory
값을 저장
사용 방법 : mem [값]
호출 방법 : mem[번호] 
            ex) calc mem1 + mem2''')
        elif cmd[-1] == "del" or cmd[-1] == "delete":
            print('''delete
메모리 값을 삭제
사용 방법 : del 1''')
        elif cmd[-1] == "exit":
            print('''exit
프로그램 종료''')
        continue

    elif "calc" in cmd[0] or "calculate" in cmd[0]:  # 계산
        del cmd[0]
        run = "print(" + ''.join(str(i) for i in cmd) + ')'

    elif "del" in cmd[0] or "delete" in cmd[0]:  # 메모리 삭제
        run = "del mem" + list(cmd)[-1]
        del mem_list[int(list(cmd)[-1])-1]
        mem_idx -= 1

    elif "mem" in cmd[0] or "memory" in cmd[0]:  # 메모리 저장
        if ord("0") <= ord(list(cmd)[-1]) <= ord("9"):
            mem_list.append(int(list(cmd)[-1]))
        else:
            mem_list.append(list(cmd)[-1])
        run = 'mem' + str(mem_idx) + '=' + list(cmd)[-1]
        mem_idx += 1

    else:  # 예외
        print("Error!! Please enter the correct command!!")
        continue

    try:
        print('------------------------------')
        exec(run)
    except:
        print("Error!! Please enter the correct command!!")

