import sys

def main():
    for line in sys.stdin:
        input_data = line.strip()
        
        # 独自のロジックを実行
        response = f"Echo: {input_data}\n"
        
        # 結果を標準出力に書き出す
        sys.stdout.write(response)
        # flushがないと永続待ちになる
        sys.stdout.flush()
        # １行処理したら強制切断する
        break

if __name__ == "__main__":
    main()
