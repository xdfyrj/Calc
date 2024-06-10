# 계산 벗
import os

cmd_list = '''------------------------------
* COMMAND *
(command) help : command manual
list
calculate
memory
delete
clear
result
exit'''
bar = "------------------------------"
print(cmd_list)

mem_list = []
mem_idx = 1
res = None

def run(execute):
    if "os" in execute:
        return eval("print('Why are you trying to hack it?')")
    try:
        return eval(execute)
    except Exception as error:
        print(f"Error in calculation: {error}")
        return None


while True:
    print(bar)
    print('memory : ' + str(mem_list))
    cmd = input().strip().split()
    if not cmd:
        print("Error!! Please enter the command!")
        continue

    if "help" in cmd:  # 명령어 목록
        if len(cmd) > 1:
            if cmd[0] == 'list':
                print('''------------------------------
list
COMMAND LIST 출력''')
            elif cmd[0] == "calc" or cmd[0] == "calculate":
                print('''
calculate
값을 계산
계산 결과는 res에 저장
사용 방법 : calc [수식]''')
            elif cmd[0] == "mem" or cmd[0] == "memory":
                print('''------------------------------
memory
값을 저장
사용 방법 : mem [값]
호출 방법 : mem[번호] 
ex) calc mem1 + mem2''')
            elif cmd[0] == "del" or cmd[0] == "delete":
                print('''------------------------------
delete
메모리 값을 삭제
사용 방법 : del 1''')
            elif cmd[0] == "res" or cmd[0] == "result":
                print('''------------------------------
result
가장 최근의 계산 결과를 출력''')
            elif cmd[0] == "exit":
                print('''------------------------------
exit
프로그램 종료''')
            else:
                print("Error!! Please enter the correct command!")
        continue

    command = cmd[0]
    if command == "exit":  # 나가기
        print("Bye")
        print(bar)
        break

    elif command == "list":
        print(cmd_list)
        continue

    elif command == "calc" or command == "calculate":  # 계산
        if len(cmd) > 1:
            print(bar)
            execute = ''.join(cmd[1:])
            result = run(execute)
            res = result
            if result is not None:
                print(result)
        else:
            print("Error!! Please enter the correct command!")

    elif command == "del" or command == "delete":  # 메모리 삭제
        if cmd[1] == "ALL" or cmd[1] == 'all':
            mem_list = []
            continue
        if len(cmd) > 1 and cmd[1].isdigit():
            idx = int(cmd[1])
            if 1 <= idx < mem_idx:
                del mem_list[idx - 1]
                mem_idx -= 1
            else:
                print("Error!! Invalid memory index!")
        else:
            print("Error!! Please enter the correct command!")

    elif command == "mem" or command == "memory":  # 메모리 저장
        if len(cmd) > 1:
            execute = ''.join(cmd[1:])
            result = exec(f'mem{mem_idx} = {execute}')
            mem_list.append(result)
            mem_idx += 1
        else:
            print("Error!! Please enter the correct command!")

    elif command == "res" or command == "result":
        if res is not None:
            print(res)
        else:
            print("Error!! Please calculate first!")

    elif command == "clear":
        os.system('cls')

    else:  # 예외
        print("Error!! Please enter the correct command!")
