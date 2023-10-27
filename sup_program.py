
def add_sup():
    while True:
        with open('suppliers.txt', 'r') as file:
            lines = file.readlines()
            non_empty_lines = [line.strip() for line in lines if line.strip()]  # 去除空白字符并过滤空行
            line_count = len(non_empty_lines)
            # print(f"总共有 {line_count} 行非空内容。")
        totality = 5

        if line_count == totality:
            print(
                'Sorry, you have already added enough vendors and cannot add any more, or you can choose to delete the vendor')
            break
        else:
            print(f"You can also currently add {totality - line_count} home supplier")
            ipt_select = input('Do you want to add more? To continue, press enter and enter any content to exit:')
            if not ipt_select:
                ipt_sup_id = input('Please enter the supply id:').strip()
                if not ipt_sup_id:
                    print('Cannot be empty')
                    continue
                with open('suppliers.txt', 'r') as file:
                    lines = file.readlines()
                    for line in lines:
                        line = line.strip()  # 去除行首尾的空白字符
                        if not line:  # 如果行为空，则跳过
                            continue
                        sup_id_txt, sup_name_txt, sup_item_int_txt = line.split(',')
                        if ipt_sup_id == sup_id_txt:
                            print('suppliers exists！')
                            break
                    else:
                        ipt_sup_name = input('Please enter a supply name:').strip()
                        if not ipt_sup_name:
                            print('Cannot be empty')
                            continue
                        ipt_sup_item_int = input('Quantity of suppliers goods:').strip()
                        if not ipt_sup_name:
                            print('Cannot be empty')
                            continue
                        sup_id = ipt_sup_id
                        sup_name = ipt_sup_name
                        sup_item_int = ipt_sup_item_int
                        add_suppliers = f"{sup_id},{sup_name},{sup_item_int}"
                        print(add_suppliers)
                        with open('suppliers.txt', 'a+') as file:
                            file.write(add_suppliers)
                            file.write('\n')
            else:
                break


def del_sup():
    with open('suppliers.txt', 'r') as file:
        lines = file.readlines()  # 一次性读取所有行

    authenticated = False  # 增加一个认证标志

    while not authenticated:
        ipt_del_sup_id = input("input your delete suppliers id:").strip()
        sup_id_count = -1  # 循环记次

        # 逐行读取内容
        for line in lines:
            sup_id_txt, *_ = line.strip().split(',')
            sup_id_count += 1
            if ipt_del_sup_id == sup_id_txt:
                print('The user has been found')
                del lines[sup_id_count]
                with open('suppliers.txt', 'w') as file:
                    file.writelines(lines)
                print('This user has been deleted')
                authenticated = True
                break
        else:
            print('This user does not exist, please re-enter!')


def manage_sup():
    with open('suppliers.txt', 'r') as file:
        lines = file.readlines()

    found = False

    while not found:
        print("Tip: If you do not know the user id you can enter '0' to return to the previous level")
        ipt_sup_id = input("input your sup id to modify:").strip()
        if ipt_sup_id == '0':
            break
        else:
            # 逐行检查内容
            for index, line in enumerate(lines):
                sup_id_txt, sup_name_txt, sup_item_int_txt = line.strip().split(',')
                if ipt_sup_id == sup_id_txt:
                    print('The supplier has been located:')
                    print('1. Current ID:', sup_id_txt)
                    print('2. Current Name:', sup_name_txt)
                    print('3. Current Inventory quantity:', sup_item_int_txt)
                    print('')
                    print("ID input '1'\n"
                          "Name input '2'\n"
                          "Inventory quantity input '3'\n")
                    while True:  # Keep prompting until valid input
                        attr_to_modify = input("Please enter:").strip()
                        if attr_to_modify in ["1", "2", "3"]:
                            break  # Exit the loop if valid input
                        else:
                            print("Invalid choice. Please select a number between 1 and 3.")

                    new_value = input(f"Enter new value for {attr_to_modify}: ").strip()

                    # Modify the selected attribute based on user's choice
                    if attr_to_modify == "1":
                        sup_id_txt = new_value
                    elif attr_to_modify == "2":
                        sup_name_txt = new_value
                    elif attr_to_modify == "3":
                        sup_item_int_txt = new_value
                    # Reconstruct and replace the original line
                    updated_line = f"{sup_id_txt},{sup_name_txt},{sup_item_int_txt}\n"
                    lines[index] = updated_line

                    print(f"Attribute {attr_to_modify} has been modified to {new_value}.")
                    print("Updated line:", updated_line)
                    found = True
                    break
            else:
                print('The vendor does not exist, please re-enter！')

    # Write back the modified data to the file
    with open('suppliers.txt', 'w') as file:
        file.writelines(lines)


def find_all_sup():
    with open('suppliers.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()  # 去除行首尾的空白字符
            if not line:  # 如果行为空，则跳过
                continue
            sup_id_txt, sup_name_txt, sup_item_int_txt = line.split(',')
            print(f'Supplier id：{sup_id_txt}')
            print(f'Supplier name：{sup_name_txt}')
            print(f'Quantity of suppliers goods：{sup_item_int_txt}')
            print('-----------------------------------')


def sup_program():
    # 初始化认证标志
    authenticated = False
    while not authenticated:
        print('add suppliers input 1\n'
              'del suppliers input 2\n'
              'manage suppliers input 3\n'
              'find_all_suppliers input 4\n')
        ipt_managing_sup = input('please selection:').strip()
        if ipt_managing_sup == '1':
            add_sup()
        elif ipt_managing_sup == '2':
            del_sup()
        elif ipt_managing_sup == '3':
            manage_sup()
        elif ipt_managing_sup == '4':
            find_all_sup()
        else:
            print('Invalid character')

sup_program()