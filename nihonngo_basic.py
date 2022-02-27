
# Press the green button in the gutter to run the script.
if __name__ == '__日本语basic__':
    print_hi('PyCharm')

# 2月9日 単語

# 鳴きます 指鸟、兽、虫类生物鸣叫；
# 鳴ります 指电铃声响起，用在闹铃、电话铃等机械音上，也可以用于表示雷鸣。

print ('''
凧を揚げる　たこをあげる
国旗を揚げる　こっきをあげる
ご主人　ごしゅじん
量り売り　はかりうり
繰り返します　くりかえします
練習を繰り返します　れんしゅをくりかえします
間に合います　まにあいます
鳴きます　なくます  
鳴ります　なります
慣れます　なれます
市場（いちば）：农贸市场、集市等进行日常购物的地方
市場（しじょう）：含义更为广泛
　　　　　　　　　　1) = 市場（いちば）
　　　　　　　　　　2)（经济学用语）进行交易行为的场所或较大地区 。
「もうぺらぺらでしょう」　读0调、二类形容词
「日本語をぺらぺら話す」　读1调

''')

# 拟声词
print ('''
ぎゅうぎゅう：紧紧的，满满的
くたくた：筋疲力尽，疲惫不堪
すやすや：安静地，香甜地（睡） 
ぱくぱく：大吃特吃，大嚼特嚼
ごくごく：咕嘟咕嘟　
すらすら：平滑地流利地，流畅地，顺利地，痛快地　　
にこにこ：笑嘻嘻；笑眯眯
じろじろ：盯着看，目不转睛地看；凝视
ぺらぺら：流利地，喋喋不休地
ザーザー：哗啦啦
ガタガタ：喀哒喀哒，摇摇晃晃
ワンワン：汪汪
ニャーニャー：（猫叫）喵
コケコッコー：（公鸡叫）
ブーブー：（猪叫）
''')

# 2月12日 第一课语法复习

# ～は　～です
print ("～は　～です : ~ 是 ~ ")
Namemei = ["琴子", "夢がある人", "中国人","夏生", "小春"]
zhuge = ["わたし", "森さん", "私の兄", "私の弟", "わたしの好きな人"]
num = [0,1,2,3,4]
for i in num:
    print(f"{zhuge[i]}は{Namemei[i]}です")

# ～は　～では（じゃ）ありません
print ("\n～は　～では（じゃ）ありません : ~不是~ ")
Namemei = ["琴子", "森さん", "私の兄","夏生", "小春"]
zhuge = ["社員", "日本人", "学生", "歌う人", "悪人"]
foudList = ["では", "じゃ"]
#foudNum = 0
#while foudNum < 2:
    #foudNum = foudNum + 1
   # if foudNum >= 2:
      #  foudNum = 0
      # 死循环版本

      #for i in num:
        #print(f"{i%2}") #奇数为1，偶数为2
        #print(f"{Namemei[i]}は{zhuge[i]}{foudList[i%2]}ありません")
        # 用奇偶数版本输出
num = [0,1,2,3,4]

for i in num:
    for n in [0,1]:
        print(f"{Namemei[i]}は{zhuge[i]}{foudList[n]}ありません")

# 悪人　あくにん　０
# 歌う人 うたうひと　

# ～は　～ですか
print ("\n～は　～ですか : ~是 ~吗？")
Namemei = ["琴子", "夢がある人", "中国人","夏生", "小春"]
zhuge = ["わたし", "森さん", "私の兄", "私の弟", "わたしの好きな人"]
num = [0,1,2,3,4]
for i in num:
    print(f"{zhuge[i]}は{Namemei[i]}ですか")
















