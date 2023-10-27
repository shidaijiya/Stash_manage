import time


#                             _ooOoo_
#                            o8888888o
#                            88" . "88
#                            (| -_- |)
#                            O\  =  /O
#                         ____/`---'\____
#                       .'  \\|     |//  `.
#                      /  \\|||  :  |||//  \
#                      /  _||||| -:- |||||-  \
#                      |   | \\\  -  /// |   |
#                      | \_|  ''\---/''  |   |
#                      \  .-\__  `-`  ___/-. /
#                    ___`. .'  /--.--\  `. . __
#                 ."" '<  `.___\_<|>_/___.'  >'"".
#                | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#                \  \ `-.   \_ __\ /__ _/   .-` /  /
#           ======`-.____`-.___\_____/___.-`____.-'======
#                              `=---='
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#                      佛祖保佑        永无BUG
#                      Buddha bless   Never BUG
#             佛曰:
#                    写字楼里写字间，写字间里程序员；
#                    程序人员写程序，又拿程序换酒钱。
#                    酒醒只在网上坐，酒醉还来网下眠；
#                    酒醉酒醒日复日，网上网下年复年。
#                    但愿老死电脑间，不愿鞠躬老板前；
#                    奔驰宝马贵者趣，公交自行程序员。
#                    别人笑我忒疯癫，我笑自己命太贱；
#                    不见满街漂亮妹，哪个归得程序员？
#      Buddha said:
#                  In the office building, there are offices, and within the offices, there are programmers.
#                  They stay sober while sitting online, but offline, they sleep while intoxicated.
#                  Days pass, and the years go by, online and offline.
#                  I hope to grow old among computers, not bowing to the boss.
#                  Luxury cars like Mercedes and BMW may be tempting, but public transport suits a programmer.
#                  Others may laugh at my eccentricity, but I laugh at my humble fate.
#                  I don't see beautiful ladies all around; which one belongs to a programmer?

# 检查文件是否为空
def users_empty_file():
    with open('users.txt', 'r') as file:
        return not file.read().strip()

def ppe_empty_file():
    with open('ppe.txt', 'r') as file:
        return not file.read().strip()

# 登陆
def user_login():
    with open('users.txt', 'r') as file:
        user_login_data = [line.strip().split(',') for line in file]

    authenticated = False  # 增加一个认证标志
    user_state = None

    while not authenticated:
        ipt_login_user_id = input("please input your user id:").strip()
        ipt_login_user_pwd = input("please input your user password:").strip()

        for user_data in user_login_data:
            user_id_txt, _, user_pwd_txt, user_type_txt, _ = user_data
            if ipt_login_user_id == user_id_txt and ipt_login_user_pwd == user_pwd_txt:
                if user_type_txt == 'admin':
                    print("welcome admin")
                    user_state = 'admin'
                elif user_type_txt == 'staff':
                    print("weicome staff")
                    user_state = 'staff'
                else:
                    print("Unknown user type.")
                authenticated = True  # 设置认证标志为True，退出循环
                break
        else:
            print("ID or password Error")

    return user_state


# 注册
def user_signup():
    with open('users.txt', 'r') as file:
        user_id_data = [line.strip().split(',')[0] for line in file]

    authenticated = False
    while not authenticated:
        ipt_signup_user_id = input("please input user id:").strip()
        if ipt_signup_user_id in user_id_data:
            print('The username already exists')
        else:
            authenticated = True

    while True:
        ipt_signup_user_name = input('please input  name:').strip()
        if not ipt_signup_user_name:  # 检查是否为空
            print("Name cannot be empty.")
            continue

        ipt_signup_user_pwd = input('please input  password：').strip()
        if not ipt_signup_user_pwd:  # 检查是否为空
            print("Password cannot be empty.")
            continue

        ipt_signup_confirm_pwd = input('please confirm  password：').strip()
        if ipt_signup_user_pwd == ipt_signup_confirm_pwd:
            break
        else:
            print('Password inconsistency')

    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    user_data = f"{ipt_signup_user_id},{ipt_signup_user_name},{ipt_signup_user_pwd},staff,{current_time}"
    with open('users.txt', 'a+') as file:
        file.write(user_data)
        file.write('\n')
        file.close()
        print('signup success')


# 删除用户
def admin_del_user():
    with open('users.txt', 'r') as file:
        lines = file.readlines()  # 一次性读取所有行

    authenticated = False  # 增加一个认证标志

    while not authenticated:
        ipt_del_user_id = input("input your delete user id:").strip()
        user_id_count = -1  # 循环记次

        # 逐行读取内容
        for line in lines:
            user_id, *_ = line.strip().split(',')  # 使用解构赋值获取user_id
            user_id_count += 1
            if ipt_del_user_id == user_id:
                print('The user has been found')
                del lines[user_id_count]
                with open('users.txt', 'w') as file:
                    file.writelines(lines)
                print('This user has been deleted')
                authenticated = True
                break
        else:
            print('This user does not exist, please re-enter!')


# 查找用户
def admin_find_user():
    with open('users.txt', 'r') as file:
        lines = file.readlines()  # 一次性读取所有行

    authenticated = False  # 增加一个认证标志

    while not authenticated:
        ipt_del_user_id = input("input your user id to find:").strip()
        user_id_count = -1  # 循环记次

        # 逐行读取内容
        for line in lines:
            user_id, user_name, user_password, user_type, registration_date = line.strip().split(',')
            user_id_count += 1
            if ipt_del_user_id == user_id:
                print('The user has been found:')
                print('ID:', user_id)
                print('Name:', user_name)
                print('Password:', user_password)
                print('User Type:', user_type)
                print('Registration Date:', registration_date)
                authenticated = True
                break
        else:
            print('This user does not exist, please re-enter!')


# 操作用户
def admin_manage_user():
    with open('users.txt', 'r') as file:
        lines = file.readlines()

    found = False

    while not found:
        ipt_user_id = input("input your user id to modify:").strip()

        # 逐行检查内容
        for index, line in enumerate(lines):
            user_id, user_name, user_password, user_type, registration_date = line.strip().split(',')
            if ipt_user_id == user_id:
                print('The user has been found:')
                print('1. Current ID:', user_id)
                print('2. Current Name:', user_name)
                print('3. Current Password:', user_password)
                print('4. Current User Type:', user_type)
                print('5. Current Registration Date:', registration_date)
                print('')
                print("ID input '1'\n"
                      "Name input '2'\n"
                      "Password input '3'\n"
                      "User Type '4'\n"
                      "Registration Date input '5'\n")
                while True:  # Keep prompting until valid input
                    attr_to_modify = input("Please enter:").strip()
                    if attr_to_modify in ["1", "2", "3", "4", "5"]:
                        break  # Exit the loop if valid input
                    else:
                        print("Invalid choice. Please select a number between 1 and 5.")

                new_value = input(f"Enter new value for {attr_to_modify}: ").strip()

                # Modify the selected attribute based on user's choice
                if attr_to_modify == "1":
                    user_id = new_value
                elif attr_to_modify == "2":
                    user_name = new_value
                elif attr_to_modify == "3":
                    user_password = new_value
                elif attr_to_modify == "4":
                    while new_value not in ['admin', 'staff']:
                        print("Invalid User Type. Please enter either 'admin' or 'staff'.")
                        new_value = input(f"Enter new value for {attr_to_modify}: ").strip()
                    user_type = new_value
                elif attr_to_modify == "5":
                    registration_date = new_value

                # Reconstruct and replace the original line
                updated_line = f"{user_id},{user_name},{user_password},{user_type},{registration_date}\n"
                lines[index] = updated_line

                print(f"Attribute {attr_to_modify} has been modified to {new_value}.")
                print("Updated line:", updated_line)
                found = True
                break
        else:
            print('The user does not exist, please re-enter！')

    print("Writing updates to file...")
    # Write back the modified data to the file
    with open('users.txt', 'w') as file:
        file.writelines(lines)
    print("Update complete.")


# 管理员选项
def admin_options():
    while True:
        print("create a new user input '1'\n"
              "del users input '2'\n"
              "find user input '3'\n"
              "manage user input '4'\n"
              "exit input 0")

        ipt_root = input('Root@admin:').strip()
        if ipt_root == '1':
            user_signup()
        elif ipt_root == '2':
            admin_del_user()
        elif ipt_root == '3':
            admin_find_user()
        elif ipt_root == '4':
            admin_manage_user()
        elif ipt_root == '0':
            main_program()
            break
        else:
            print('Invalid character')


# 用户类型判断
def permission_execution(user_state):
    if user_state == 'admin':
        admin_options()
    else:
        print('Employee permissions')

    return user_state


# 检查是否第一次运行
def first_run():
    if users_empty_file():
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        default_admin_id = 'admin'
        default_admin_name = 'admin'
        default_admin_pwd = 'admin'
        default_admin_data = f'{default_admin_id},{default_admin_name},{default_admin_pwd},admin,{current_time}'
        with open('users.txt', 'a+') as file:
            file.write(default_admin_data)
            file.write('\n')
            file.close()
        print(f"It seems that this is your first time using this program\n"
              f"welcome We have generated a default administrator account for you, please keep your account password properly\n"
              f"Id:{default_admin_id}\n"
              f"Name:{default_admin_name}\n"
              f"password:{default_admin_pwd}\n"
              f"UserType:admin\n")
    if  ppe_empty_file():
        ppe_initialize()



# 主程序
def main_program():
    # 初始化认证标志
    authenticated = False
    while not authenticated:
        print('login or sign up')
        print("login input '1' \n"
              "sign up input '2'\n")

        login_signup = input('please selection:').strip()
        if login_signup == '1':
            user_state = user_login()
            permission_execution(user_state)
            authenticated = True
        elif login_signup == '2':
            user_signup()
        else:
            print('Invalid character')


def ppe_initialize():
    # 初始化数量
    initialize_number = 100
    ##初始化字符串
    initialize_str = f'''HC,Head Cover,{initialize_number}\nFS,Face Shield,{initialize_number}\nMS,Mask,{initialize_number}\nGL,Gloves,{initialize_number}\nGW,Gown,{initialize_number}\nSC,Shoe Covers,{initialize_number}'''
    # 写入文件
    with open('ppe.txt', 'a+') as file:
        file.write(initialize_str)
        file.close()

# 文件不存在则创建
with open('users.txt', 'a+') as file:
    file.close()
with open('ppe.txt', 'a+') as file:
    file.close()
with open('suppliers.txt', 'a+') as file:
    file.close()
# 检查是否第一次运行
first_run()
main_program()
