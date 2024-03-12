import datetime
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

while True:
    #パスの設定
    date_now = datetime.datetime.now().strftime('%m_%d_%H:%M:%S')
    if getattr(sys, 'frozen', False):
        os.makedirs(f"{os.path.dirname(sys.executable)}/csv_files/log_{date_now}", exist_ok=True)
        log_csv_file_path = f"{os.path.dirname(sys.executable)}/csv_files/log_{date_now}/log_{date_now}.csv"
    else:
        os.makedirs(f"csv_files/log_{date_now}", exist_ok=True)
        log_csv_file_path = f"csv_files/log_{date_now}/log_{date_now}.csv"
    with open(log_csv_file_path, 'w') as f:
        f.write("time,value\n")
    #演算
    print("値を入力してください")
    n = int(input())
    repeat = False
    count = 1
    with open(f"{os.path.dirname(log_csv_file_path)}/operation_log.txt", 'w') as f:
        f.write(f"実行日時:{date_now}\n初期値:{n}\n")
    with open(log_csv_file_path, 'a') as f:
        f.write(str(count) + "," + str(n) + "\n")
        print("\r" + str(count) + "回書き込み", end="")
    while n != 1:
        if(n%2 == 0): #偶数
            n /= 2
        else: #奇数
            n *= 3
            n += 1
        with open(log_csv_file_path, 'a') as f:
            count += 1
            f.write(str(count) + "," + str(n) + "\n")
            print("\r" + str(count) + "回書き込み", end="")
    print(f"\n{n}になりました")

    #csvファイルのパス
    input_csv = pd.read_csv(log_csv_file_path)

    # lorテキストの書き込み
    with open(f"{os.path.dirname(log_csv_file_path)}/operation_log.txt", 'a') as f:
        f.write(f"演算回数:{count}\n最大値:{input_csv['value'].max()}\n最小値:{input_csv['value'].min()}")

    # グラフ
    first_column_data = input_csv[input_csv.keys()[0]]
    second_culumn_data = input_csv[input_csv.keys()[1]]

    plt.xlabel(input_csv.keys()[0])
    plt.ylabel(input_csv.keys()[1])

    plt.plot(first_column_data, second_culumn_data, linestyle='solid')
    plt.savefig(f"{os.path.dirname(log_csv_file_path)}/graph_{date_now}.png", format="png", dpi=300)
    print(f"{os.path.dirname(log_csv_file_path)}にグラフ画像を保存しました。")
    print("グラフを表示しますか?(y/n)")
    graph_show = input()
    if graph_show == "y":
        plt.show()
    print("もう一度実行しますか?(y/n)")
    if input() != "y":
        break
