import random

#数当てゲームを1回プレイする関数
def play_game():
    correct_num = random.randint(1, 50) #正解の数字をランダムに決定
    count = 0 #試行回数
    print('数当てゲーム。3回まで挑戦できます。')
    while count < 3:
        try:
            #ユーザーに数字を入力してもらう
            guess = int(input("1〜50の数字を入力してください: "))
        except ValueError:
            #数字以外が入力されたときのエラーメッセージ
            print('数字で入力してください。')
            continue
        #入力された数字が範囲外だった場合
        if guess< 1 or guess > 50:
            print('1~50の範囲で入力してください。')
            continue
        #入力された数字と正解を比較する
        if guess < correct_num:
            print("入力した数より大きいです。")
        elif guess > correct_num:
            print("入力した数より小さいです。")
        else:
            print("正解！")
            return #正解したらゲーム終了

        count += 1 #不正解だったら試行回数を1増やす

    #3回失敗したときの表示
    print(f"残念でした。数字は{correct_num}でした。")
#ゲームの起動と、再プレイをする関数
def main():
    while True:
        play_game() #ゲームを1回実行

        while True:
            #再プレイするかの確認
            replay = input("またやる(y/n)？")
            if replay == "y":
                break #外側のループに戻る。再プレイ。
            elif replay == "n":
                print('お疲れ様でした')
                return #プログラム終了
            else:
                print('yかnで答えてください。') #無効な入力時のメッセージ

#プログラム実行
main()