import datetime
import sys
import os

while True:
    #パスの設定
    log_file_name = f"log_{datetime.datetime.now().strftime('%m_%d_%H:%M:%S')}.csv"
    if getattr(sys, 'frozen', False):
        # parent_path = os.path.dirname(sys.executable)
        os.makedirs(f"{os.path.dirname(sys.executable)}/csv_files", exist_ok=True)
        log_file_name = f"{os.path.dirname(sys.executable)}/csv_files/{log_file_name}"
        with open(log_file_name, 'w') as f:
            f.write("time,value\n")
    else:
        os.makedirs("csv_files", exist_ok=True)
        log_file_name = f"csv_files/{log_file_name}"
        with open(log_file_name, 'w') as f:
            f.write("time,value\n")
    #演算
    print("値を入力してください")
    n = int(input())
    repat = False
    count = 1
    with open(log_file_name, 'a') as f:
        f.write(str(count) + "," + str(n) + "\n")
        print("\r" + str(count) + "回書き込み", end="")
    while n != 1:
        if(n%2 == 0): #偶数
            n /= 2
        else: #奇数
            n *= 3
            n =+ 1
        with open(log_file_name, 'a') as f:
            count += 1
            f.write(str(count) + "," + str(n) + "\n")
            print("\r" + str(count) + "回書き込み", end="")
    print(f"\n{n}になりました")
    print("もう一度実行しますか?(y/n)")
    if input() != "y":
        break