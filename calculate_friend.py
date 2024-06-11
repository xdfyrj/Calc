# 계산 벗

cmd_list = '''------------------------------
* COMMAND *
(command) help : command manuals
calculate
memory
delete
clear
result
exit'''
bar = "------------------------------"
print(cmd_list)

mem_list = []
res = None

def run(execute):
    try:
        return eval(execute)
    except Exception as err:
        print(f"Error!! Please enter the correct command!")
        print(f"{err}")
        return None

while True:
    print(bar)
    print('memory : ' + str(mem_list))
    cmd = input().strip().split()
    if not cmd:
        print("Error!! Please enter the command!")
        continue

    command = cmd[0]

    if command == "help":
        if len(cmd) > 1:
            if cmd[1] == "calc" or cmd[1] == "calculate":
                print('------------------------------\ncalculate\n값을 계산\n계산 결과는 res 변수에 저장\n사용 방법 : calc [수식]')
            elif cmd[1] == "mem" or cmd[1] == "memory":
                print('------------------------------\nmemory\n값을 저장\n사용 방법 : mem [값]\n호출 방법 : mem[번호]\nex) calc mem1 * 2')
            elif cmd[1] == "del" or cmd[1] == "delete":
                print('------------------------------\ndelete\n메모리 값을 삭제\n사용 방법 : del [번호] 또는 del all')
            elif cmd[1] == "res" or cmd[1] == "result":
                print('------------------------------\nresult\n가장 최근의 계산 결과를 출력')
            elif cmd[1] == "exit":
                print('------------------------------\nexit\n종료')
            else:
                print("Error!! Please enter the correct command!")
        else:
            print(cmd_list)
        continue

    if command == "exit":
        print("Bye")
        print(bar)
        break

    elif command == "calc" or command == "calculate":
        if len(cmd) > 1:
            print(bar)
            print(cmd)
            execute = ''.join(cmd[1:])
            result = run(execute)
            res = result
            if result is not None:
                print(result)
        else:
            print("Error!! Please enter the correct command!")

    elif command == "mem" or command == "memory":
        if len(cmd) > 1:
            execute = ''.join(cmd[1:])
            try:
                print(bar)
                if (execute[0] == '\'' or execute[0] == '"') and (execute[-1] == '\'' or execute[-1] == '"'):
                    result = execute[1:-1]
                    mem_list.append(result)
                    exec(f'mem{len(mem_list)} = "{mem_list[-1]}"')
                    print(f'mem{len(mem_list)} = "{result}"')
                else:
                    result = eval(execute)
                    mem_list.append(result)
                    exec(f'mem{len(mem_list)} = {mem_list[-1]}')
                    print(f'mem{len(mem_list)} = {result}')
            except Exception as error:
                print(f"Error in memory assignment: {error}")
        else:
            print("Error!! Please enter the correct command!")

    elif command == "del" or command == "delete":
        if len(cmd) > 1:
            if cmd[1].lower() == "all":
                mem_list = []
            elif cmd[1].isdigit():
                idx = int(cmd[1])
                if 1 <= idx <= len(mem_list):
                    del mem_list[idx - 1]
                else:
                    print("Error!! Invalid memory index!")
            else:
                print("Error!! Please enter the correct command!")
        else:
            print("Error!! Please enter the correct command!")

    elif command == "res" or command == "result":
        if res is not None:
            print(res)
        else:
            print("Error!! Please calculate first!")

    elif command == "clear":
        print("\033[H\033[J", end="")

    else:
        print("Error!! Please enter the correct command!")
