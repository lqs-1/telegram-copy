import sys
import shutil
import os
import time

class Applications(object):
    '''第一步填充数据'''
    def fill_args(self):
        while True:
            drive_letter = input("请输入可执行文件处于那个盘(如C,D不区分大小写):")
            if drive_letter:
                break
            else:
                pass

        apps_dir = input("请输入多个应用存放的文件夹,不填默认存储在桌面的Applications文件夹:")

        if not apps_dir:
            apps_dir = 'C:\\Users\\lee7s\\Desktop\\Applications'

        while True:
            app_name = input("请输入要多开的应用名称(可执行文件,不带后缀,区分大小写):")
            if app_name:
                app_name = app_name + ".exe"
                break
            else:
                pass

        while True:
            app_prefix = input("请输入每个应用文件夹的前缀:")
            if app_prefix:
                break
            else:
                pass

        while True:
            copy_num = input("请输入创建的个数:")
            if copy_num:
                break
            else:
                pass

        return drive_letter, apps_dir, app_name, app_prefix, copy_num

    def do_start(self):
        # 填充数据
        drive_letter, apps_dir, app_name, app_prefix, copy_num = self.fill_args()

        # 询问是否创建
        flag = input("请三思,是否立即运行多开程序,如有顾虑可立即关闭此应用(是否继续?[yes/no]):")

        if flag == "no":
            sys.exit()

        # 寻找应用文件路径
        app_path = self.find_app_path(app_name, drive_letter)

        if app_path is None:
            print(f"应用不在{drive_letter}盘,请换盘")
            time.sleep(5)
            sys.exit()

        self.copy_application(app_name, app_path, apps_dir, app_prefix, int(copy_num))

        print("所有多开创建结束! 可随时关闭程序")
        input()


    def find_app_path(self, app_name, drive_letter):
        '''第二步 找文件'''
        # drive_letter
        root_path = os.path.join(drive_letter + ':\\')

        # 遍历指定磁盘的文件和目录
        for root, dirs, files in os.walk(root_path):
            # 在文件列表中查找目标文件
            if app_name in files:
                # 找到文件，返回完整路径
                return os.path.join(root, app_name)

        # 没有找到文件
        return None


    def copy_application(self, app_name, app_path, apps_dir, app_prefix, copy_num):
        # 循环创建多个Telegram实例
        for i in range(1, copy_num + 1):
            # 创建实例文件夹，用于存放Telegram可执行文件和快捷方式
            instance_folder = f'{apps_dir}\\{app_prefix}_{i}'
            os.makedirs(instance_folder, exist_ok=True)

            # 复制Telegram可执行文件到实例文件夹
            shutil.copy(app_path, instance_folder)

            print(f"{app_name}的第{i}个分身创建成功! 位于 {instance_folder} 文件夹下")


if __name__ == '__main__':

    app = Applications()

    app.do_start()





