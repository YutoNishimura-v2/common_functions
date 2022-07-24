# common_functions
汎用性高い関数置き場

## 作成時のルール
1ファイル 1機能まで。ただし、セットになっているような機能は同じにして良い (in/out のような場合)

## 各種関数説明
- 概要だけで良さそう。入出力とかは各ファイル参照。

### image_processing
#### imread_imout_for_japanese
- opencv そのままの imread imwrite は日本語パスを受け付けない。
- それを克服するための関数。

### parallelization
#### parallel_processing_for_bigdata
- 大量のデータを並列に処理したい場合向け。
- 一度に処理するフォルダ数を制限する機能がついていることで、大量データをメモリを溢れさせることなく処理できるようになっている。
- 一方で、本当に多い場合総ファイル数を数えて入力するところが一番大変かもしれない。


## TODO
- matplotlib 関連の、簡単に出力できるテンプレを作りたい。
  - いちいち set_xaxis だっけ？ とか悩むのが嫌。
