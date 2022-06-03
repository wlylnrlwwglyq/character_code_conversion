import unicodedata
import sys
import os.path


CHARACTER_CODES = ["utf-8","iso-2022-jp","shift-jis","euc_jp"]
LINEFEED_CODES = [b'\r\n',b'\r',b'\n']
LINEFEED_CODE_NAMES = ["CRLF","CR","LF"]


def guess_character_code(data):
    guess_character_codes = []
    for i in CHARACTER_CODES:
        try:
            data.decode(i)
            guess_character_codes.append(i)
        except:
            pass
    if len(guess_character_codes) == 4:
        return "ascii"
    elif len(guess_character_codes) == 1:
        return guess_character_codes[0]
    elif len(guess_character_codes) == 2:
        if "euc_jp" in guess_character_codes:
            return "euc_jp"
        else:
            return "utf-8"
    else:
        for i in guess_character_codes:
            if i[1] != len(data):
                return "iso-2022-jp"
    return "ascii"


def guess_linefeed_code(data):
    for i in LINEFEED_CODES:
        if i in data:
            return LINEFEED_CODE_NAMES[LINEFEED_CODES.index(i)]
    return "CRLF"

def is_numeric(data):
    return data.decode(guess_character_code(data)).isnumeric()


def is_full_width(data):
    text = data.decode(guess_character_code(data))
    for i in text:
        c = unicodedata.east_asian_width(i)
        if c == "F" or c == "W" or c == "A":
            return True
    return False


def convert_character_code(data,from_code,to_code):
    return data.decode(from_code).encode(to_code)


def convert_linefeed_code(data,from_code,to_code):
    return data.replace(from_code,to_code)


def main():
    input_filename = input("読み込むファイル名を入力してください> ")
    if not os.path.isfile(input_filename):
        print("\""+input_filename+"\"というファイルは見つかりませんでした")
        sys.exit(1)

    #データ読み込み
    with open(input_filename,"rb") as f:
        data = f.read()

    #文字コード推定
    character_code = guess_character_code(data)
    print("文字コード推定結果:",character_code)
    #改行コード推定
    linefeed_code_name = guess_linefeed_code(data)
    print("改行コード推定結果:",linefeed_code_name)
    #文字種別の推定
    print("文字種別の推定結果:",end="")
    if is_numeric(data):
        print("数値",end="")
    else:
        print("文字列",end="")
    if is_full_width(data):
        print(",全角")
    else:
        print(",半角")

    #文字コード変換
    print()
    print("現在の文字コード:"+character_code)
    print("利用可能な文字コード:"+str(CHARACTER_CODES))
    new_character_code = input("変換後の文字コードを入力してください> ")
    if not new_character_code in CHARACTER_CODES:
        print("\""+new_character_code+"\"は利用可能な文字コードではありません")
        sys.exit(1)
    
    #改行コード変換
    print()
    print("現在の改行コード:"+linefeed_code_name)
    print("利用可能な改行コード:"+str(LINEFEED_CODE_NAMES))
    new_linefeed_code_name = input("変換後の改行コードを入力してください> ")
    if not new_linefeed_code_name in LINEFEED_CODE_NAMES:
        print("\""+new_linefeed_code_name+"\"は利用可能な改行コードではありません")
        sys.exit(1)

    #出力ファイルを指定
    print()
    output_filename = input("出力するファイル名を入力してください> ")
    if output_filename == "":
        print("ファイル名を指定してください")
        sys.exit(1)

    data2 = convert_character_code(data,character_code,new_character_code)
    data2 = convert_linefeed_code(data2,LINEFEED_CODES[LINEFEED_CODE_NAMES.index(linefeed_code_name)],LINEFEED_CODES[LINEFEED_CODE_NAMES.index(new_linefeed_code_name)])

    print("変換後の文字コード:",guess_character_code(data2))
    print("変換後の改行コード:",guess_linefeed_code(data2))

    #変換後のデータを出力する
    with open(output_filename,"wb") as f:
        f.write(data2)


if __name__ == "__main__":
    main()
