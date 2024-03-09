import datetime
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

while True:
    #パスの設定
    datetime_now = datetime.datetime.now().strftime('%m_%d_%H:%M:%S')
    log_file_name = f"log_{datetime_now}"
    if getattr(sys, 'frozen', False):
        os.makedirs(f"{os.path.dirname(sys.executable)}/csv_files/{log_file_name}", exist_ok=True)
        log_file_name = f"{os.path.dirname(sys.executable)}/csv_files/{log_file_name}/{log_file_name}.csv"
        with open(log_file_name, 'w') as f:
            f.write("time,value\n")
    else:
        os.makedirs(f"csv_files/{log_file_name}", exist_ok=True)
        log_file_name = f"csv_files/{log_file_name}/{log_file_name}.csv"
        with open(log_file_name, 'w') as f:
            f.write("time,value\n")
    #演算
    print("値を入力してください")
    n = int(input())
    repeat = False
    count = 1
    with open(log_file_name, 'a') as f:
        f.write(str(count) + "," + str(n) + "\n")
        print("\r" + str(count) + "回書き込み", end="")
    while n != 1:
        if(n%2 == 0): #偶数
            n /= 2
        else: #奇数
            n *= 3
            n += 1
        with open(log_file_name, 'a') as f:
            count += 1
            f.write(str(count) + "," + str(n) + "\n")
            print("\r" + str(count) + "回書き込み", end="")
    print(f"\n{n}になりました")
    #グラフ
    input_csv = pd.read_csv(log_file_name)
    plt.plot(input_csv["time"], input_csv["value"])
    plt.xlabel("time")
    plt.ylabel("value")
    plt.savefig(f"{os.path.dirname(log_file_name)}/graph_{datetime_now}.png", format="png", dpi=300)
    print(f"{os.path.dirname(log_file_name)}に画像を保存しました。")
    print("グラフを表示しますか?(y/n)")
    graph_show = input()
    if graph_show == "y":
        plt.show()
    print("もう一度実行しますか?(y/n)")
    if input() != "y":
        break
