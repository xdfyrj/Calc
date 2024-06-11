# 계산 벗

cmd_list = '''------------------------------
* COMMAND *
help (command) : command manuals
calculate
memory
delete
clear
result
exit'''
bar = "------------------------------"
res_bar = "-----------result-------------"
err_bar = "-----------error--------------"
print("\033[H\033[J", end="")
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
    cmd_input = input().strip()

    if not cmd_input:
        print(err_bar)
        print("Error!! Please enter the command!")
        continue

    cmd = cmd_input.split(maxsplit=1)
    command = cmd[0]
    args = cmd[1] if len(cmd) > 1 else ""

    if command == "help":
        if args:
            if args in ["calc", "calculate"]:
                print('-----------calculate----------\n값을 계산\n계산 결과는 res 변수에 저장\n사용 방법 : calc [수식]')
            elif args in ["mem", "memory"]:
                print(
                    '--------------memory----------\n값을 저장\n사용 방법 : mem [값]\n호출 방법 : mem[번호]\nex) calc mem1 * 2')
            elif args in ["del", "delete"]:
                print('------------delete------------\n메모리 값을 삭제\n사용 방법 : del [번호] 또는 del all')
            elif args in ["res", "result"]:
                print('------------result------------\n가장 최근의 계산 결과를 출력')
            elif args == "exit":
                print('-------------exit-------------\n계산기 종료')
            else:
                print(err_bar)
                print("Error!! Please enter the correct command!")
        else:
            print("\033[H\033[J", end="")
            print(cmd_list)
        continue

    if command == "exit":
        print(bar)
        print("Are you sure you want to exit? [ Y / n ]")
        sure = input().strip()
        if sure.lower() == 'y' or sure == '예':
            print(bar)
            print("Bye Bye😭")
            print(bar, end='')
            exit()
        elif sure.lower() == 'n' or sure == "아니오":
            print(bar)
            print("Great! Let's calculate!")
            continue
        else:
            continue

    elif command in ["calc", "calculate"]:
        if args:
            print(res_bar)
            result = run(args)
            res = result
            print(result)
        else:
            print(err_bar)
            print("Error!! Please enter the correct command!")

    elif command in ["mem", "memory"]:
        if args:
            try:
                if (args[0] in ['\'', '"']) and (args[-1] in ['\'', '"']):
                    result = args[1:-1]
                    mem_list.append(result)
                    exec(f'global mem{len(mem_list)}')
                    exec(f'mem{len(mem_list)} = "{mem_list[-1]}"')
                    print(res_bar)
                    print(f'mem{len(mem_list)} = "{result}"')
                else:
                    result = str(eval(args))
                    if result.isdigit():
                        mem_list.append(int(result))
                        exec(f'global mem{len(mem_list)}')
                        exec(f'mem{len(mem_list)} = {mem_list[-1]}')
                        print(res_bar)
                        print(f'mem{len(mem_list)} = {int(result)}')
                    else:
                        mem_list.append(result)
                        exec(f'global mem{len(mem_list)}')
                        exec(f'mem{len(mem_list)} = "{mem_list[-1]}"')
                        print(res_bar)
                        print(f'mem{len(mem_list)} = "{result}"')
            except Exception as error:
                print(err_bar)
                print(f"Error in memory assignment: {error}")
        else:
            print(err_bar)
            print("Error!! Please enter the correct command!")

    elif command in ["del", "delete"]:
        if args:
            if args.lower() == "all":
                for idx in range(len(mem_list)):
                    try:
                        exec(f'del mem{idx+1}')
                    except Exception:
                        continue
                mem_list = []
            elif args.isdigit():
                idx = int(args)
                if 1 <= idx <= len(mem_list):
                    mem_list[idx - 1] = None
                    try:
                        exec(f'del mem{idx}')
                    except Exception:
                        print(err_bar)
                        print("Error!! no value in memory!")
                else:
                    print(err_bar)
                    print("Error!! Invalid memory index!")
            else:
                print(err_bar)
                print("Error!! Please enter the correct command!")
        else:
            print(err_bar)
            print("Error!! Please enter the correct command!")

    elif command in ["res", "result"]:
        if res is not None:
            print(res_bar)
            print(res)
        else:
            print(err_bar)
            print("Error!! Please calculate first!")

    elif command == "clear":
        print("\033[H\033[J", end="")

    else:
        print(err_bar)
        print("Error!! Please enter the correct command!")
