# character_code_conversion

指定したファイルの文字コードを表示、変換します。

## Usage

```
$ python3 main.py
```

## Example

```
$ python3 main.py
読み込むファイル名を入力してください> README.md
文字コード推定結果: utf-8
改行コード推定結果: LF
文字種別の推定結果:文字列,全角

現在の文字コード:utf-8
利用可能な文字コード:['utf-8', 'iso-2022-jp', 'shift-jis', 'euc_jp']
変換後の文字コードを入力してください> shift-jis

現在の改行コード:LF
利用可能な改行コード:['CRLF', 'CR', 'LF']
変換後の改行コードを入力してください> CRLF

出力するファイル名を入力してください> output.txt
変換後の文字コード: shift-jis
変換後の改行コード: CRLF
```
