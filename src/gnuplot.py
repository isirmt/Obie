import importcsv
import subprocess 
import csv

#支出だけのリスト生成
def moneylist(DB):
  money = []
  for i in range(len(DB)):
    money.append(DB[i][4])

#同じ日のデータをまとめる
def daylist(DB):
  money = 0
  daylist = []
  base =[DB[0][0],DB[0][1],DB[0][2]]

  for i in range(len(DB)):
    if (base == [DB[i][0],DB[i][1],DB[i][2]]) == True:
      money += int(DB[i][4])
    elif (base == [DB[i][0],DB[i][1],DB[i][2]]) == False:
      daylist.append([DB[i-1][0],DB[i-1][1],DB[i-1][2],money])
      money = int(DB[i][4])
      base = [DB[i][0],DB[i][1],DB[i][2]]

    if i+1 == len(DB):  #終了時のbaseとmoneyをリストに格納
      daylist.append([DB[i][0],DB[i][1],DB[i][2],money])
  
  return daylist

#同じ月のデータをまとめる
def monthlist(DB):
  money = 0
  monthlist = []

  base = [DB[0][0],DB[0][1]]
  for i in range(len(DB)):
    if (base == [DB[i][0],DB[i][1]]) == True:
      money += int(DB[i][4])
    elif (base == [DB[i][0],DB[i][1]]) == False:
      monthlist.append([DB[i-1][0],DB[i-1][1],money])
      money = int(DB[i][4])
      base = [DB[i][0],DB[i][1]]

    if i+1 == len(DB):  #終了時のbaseとmoneyをリストに格納
      monthlist.append([DB[i][0],DB[i][1],money])
  
  return monthlist

#同じ年のデータをまとめる
def yearlist(DB):
  money = 0
  yearlist = []

  base = [DB[0][0]]
  for i in range(len(DB)):
    if (base == [DB[i][0]]) == True:
      money += int(DB[i][4])
    elif (base == [DB[i][0]]) == False:
      yearlist.append([DB[i-1][0],money])
      money = int(DB[i][4])
      base = [DB[i][0]]

    if i+1 == len(DB):  #終了時のbaseとmoneyをリストに格納
      yearlist.append([DB[i][0],money])
  
  return yearlist



"""
#日付のリスト生成
hani = len(i)
print(hani)
a = "{}-{}-{}"
#リストの最初
y = i[0][0]
m = i[0][1]
d = i[0][2]
f = a.format(y, m, d)
forgraph.append(f)
#リストの続き
for x in range(1,hani):
    y = i[x][0]
    m = i[x][1]
    d = i[x][2]
    d1 = i[x-1][2]
    if d!=d1:
      b = a.format(y, m, d)
      forgraph.append(b)
#日付順にソート
forgraph.sort(key=lambda x:x[0])

#日付と金額を結合
for x in range(len(j)):
  date = forgraph[x]
  m = j[x]
  data.append([date,m])

print(len(j))
print(len(forgraph))

#グラフ用csv生成
body = data

with open('forgraph.csv', 'w') as f:
 
  writer = csv.writer(f)
  writer.writerows(body)

f.close()
"""

def gnuplot():
  #Gnuplot呼び出し
  proc = subprocess.Popen(['gnuplot','-p'], 
                          shell=True,
                          stdin=subprocess.PIPE,
                          )
  proc.stdin.write(b"file='forgraph.csv'\n")
  proc.stdin.write(b'set grid\n')
  proc.stdin.write(b'set style fill solid border lc rgb "black"/n')
  proc.stdin.write(b'set boxwith/n')
  proc.stdin.write(b'set xdata time\n')
  proc.stdin.write(b'set timefmt "%Y-%m-%d"\n')

  #月日だけの表示にしたかったけどコマンド動かなかった
  #proc.stdin.write(b'set format x "%m-%d"\n')

  #範囲指定したかったけどコマンド動かなかった
  #proc.stdin.write(b'set xrange ["2021-04-01":"2021-04-30"]\n')

  proc.stdin.write(b'set datafile separator ","\n')
  proc.stdin.write(b'set boxwidth 0.5 relative\n')
  proc.stdin.write(b'plot file using 0:2:xtic(1) with boxes lw 2 lc rgb "light-green" notitle;pause -1\n')
  proc.stdin.write(b'quit\n') #close the gnuplot window

def makecsv(DB):
  with open("forgraph.csv",mode ='w', newline='', encoding='utf-8-sig') as f:

    writer = csv.writer(f)
    writer.writerows(DB)


if __name__ == '__main__':
  csvList,file = importcsv.inputlist()
  list = importcsv.csvSort(csvList,5,2)

  moneylist(list)
  a = daylist(list)
  a = yearlist(list)

  makecsv(a)
  gnuplot()
