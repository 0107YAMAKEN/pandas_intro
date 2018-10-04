import pandas as pd

columns = ["Name", "Url"]
df1 = pd.DataFrame(columns=columns) 


se = pd.Series(['データ解析の実務プロセス入門（あんちべ）』を読んで特に学びが多かったこと', 'https://review-of-my-life.blogspot.com/2018/03/moji-okosi-1.html'], columns) 
df1 = df1.append(se, columns)
se = pd.Series(['sqlite3覚書 データベースに接続したり、中身のテーブル確認したり', 'https://review-of-my-life.blogspot.com/2018/04/sqlite3.html'], columns) 
df1 = df1.append(se, columns)
se = pd.Series(['LINEから送った画像を文字起こししてくれるアプリを作るときのメモ①', '	https://review-of-my-life.blogspot.com/2018/03/moji-okosi-1.html'], columns) 
df1 = df1.append(se, columns)
df1
print(df1)
