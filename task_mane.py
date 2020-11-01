import pandas as pd
import sys
import tkinter as tk
import time
import datetime

#メイン関数
def main():
    
    #ウィンドウ生成
    root = tk.Tk()
    root.title(u"タスクマネージャー")
    root.geometry("400x130")
    
    #ヘッダー設定
    header = tk.Label(text=u"疲労")
    header.grid(row=0, column=1)
    header = tk.Label(text=u"休みたさ")
    header.grid(row=0, column=2)
    header = tk.Label(text=u"ねむさ")
    header.grid(row=0, column=3)
    header = tk.Label(text=u"メモリ利用率")
    header.grid(row=0, column=4)
    header = tk.Label(text=u"仕事量")
    header.grid(row=0, column=5)
    header = tk.Label(text=u"ひとこと")
    header.grid(row=0, column=6)
    header = tk.Label(text=u"最終更新時間")
    header.grid(row=0, column=7)
    
    #ラベルを宣言
    label_name = [tk.Label(text=u"temp")for i in range(3)]
    label_hirou = [tk.Label(text=u"temp")for i in range(3)]
    label_yasumi = [tk.Label(text=u"temp")for i in range(3)]
    label_nemusa = [tk.Label(text=u"temp")for i in range(3)]
    label_memori = [tk.Label(text=u"temp")for i in range(3)]
    label_shigoto = [tk.Label(text=u"temp")for i in range(3)]
    label_hitokoto = [tk.Label(text=u"temp")for i in range(3)]
    label_data = [tk.Label(text=u"temp")for i in range(3)]
    
    #i行目のラベルを配置
    for i in range(3):
        label_name[i].grid(row=i + 1, column=0)
        label_hirou[i].grid(row=i + 1, column=1)
        label_yasumi[i].grid(row=i + 1, column=2)
        label_nemusa[i].grid(row=i + 1, column=3)
        label_memori[i].grid(row=i + 1, column=4)
        label_shigoto[i].grid(row=i + 1, column=5)
        label_hitokoto[i].grid(row=i + 1, column=6)
        label_data[i].grid(row=i + 1, column=7)
    
    
    refresh_data(label_name, label_hirou, label_yasumi, label_nemusa, label_memori, label_shigoto, label_hitokoto, label_data)
    
    # 読み込みボタンの作成
    btn = tk.Button(text='読み込み', command=lambda: refresh_data(label_name, label_hirou, label_yasumi, label_nemusa, label_memori, label_shigoto, label_hitokoto, label_data))
    btn.place(x=230, y=90) #ボタンを配置する位置の設定
    
    #書き込みボタンの作成
    btn = tk.Button(text='書き込み', command = write_data)
    btn.place(x=130, y=90) #ボタンを配置する位置の設定
    
    root.attributes("-topmost", True)
    
    root.mainloop()


#値をCSVから読み込んで更新する関数
def refresh_data(name, hirou, yasumi, nemusa, memori, shigoto, hitokoto, data):
    
    print("読み込み")
    #情報読み込み
    df = pd.read_csv('test.csv', header = None)
    
    #csvの内容入力をボタンへ入力するループ(vの中に1行の情報が入っている)
    for i, v in df.iterrows():
        str_buff = "temp"
        
        str_buff = v[0]
        name[i]["text"] = str_buff
        str_buff = v[1]
        hirou[i]["text"] = str_buff
        str_buff = v[2]
        yasumi[i]["text"] = str_buff
        str_buff = v[3]
        nemusa[i]["text"] = str_buff
        str_buff = v[4]
        memori[i]["text"] = str_buff
        str_buff = v[5]
        shigoto[i]["text"] = str_buff
        str_buff = v[6]
        hitokoto[i]["text"] = str_buff
        str_buff = v[7]
        data[i]["text"] = str_buff
        

#値をCSVに書き込む関数
def write_data():
    
    print("あなたのユーザーID(何行目か)を入力してください")
    user_id = int(input())
    
    #情報読み込み
    df = pd.read_csv('test.csv', header = None)
    
    #CSV内の情報を走査
    for i, v in df.iterrows():
        
        if i + 1 == user_id:
            
            #現在情報取得
            name = v[0]
            hirou= v[1]
            yasumi = v[2]
            nemusa = v[3]
            memori = v[4]
            shigoto = v[5]
            hitokoto = v[6]
            data = v[7]
            #変更情報取得
            print("あなたのユーザーIDは%dで、%sさんですね。"% (user_id, name))
            
            print("あなたの現在の疲労を10段階で記入してください。いまは%dになっています。" % hirou)
            hirou = int(input())
            print("あなたの現在の休みたさを10段階で記入してください。いまは%dになっています。" % yasumi)
            yasumi = int(input())
            print("あなたの現在の眠さを10段階で記入してください。いまは%dになっています。" % nemusa)
            nemusa = int(input())
            print("あなたの現在の脳のメモリ使用率を10段階で記入してください。いまは%dになっています。" % memori)
            memori = int(input())
            print("あなたの現在の仕事量を10段階で記入してください。いまは%dになっています。" % shigoto)
            shigoto = int(input())
            print("ひとことどうぞ。現在は「%s」となっています。" % hitokoto)
            hitokoto = input()
            
            #現在時刻取得
            dt_now = datetime.datetime.now()
            data = dt_now.strftime('%m月%d日 %H:%M:%S')
            
            print("更新ありがとうございます。読み込みボタンをおしてください。")
            
            
            #データフレームに入力
            df.iat[i, 0] = name
            df.iat[i, 1] = hirou
            df.iat[i, 2] = yasumi
            df.iat[i, 3] = nemusa
            df.iat[i, 4] = memori
            df.iat[i, 5] = shigoto
            df.iat[i, 6] = hitokoto
            df.iat[i, 7] = data
            
        
    #返還後のcsvを出力
    df.to_csv('test.csv', header = None, index = None)



#メイン関数実行
if __name__ == "__main__":
    main()
