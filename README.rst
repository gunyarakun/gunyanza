gunyanza: A shogi AI with deep learning
=======================================

ディープラーニングという機械学習の手法を用いた将棋AIです。

元アイデアはErik Bernhardssonさんによる `deep pink <https://github.com/erikbern/deep-pink>`_ です。

詳しくは、`ブログエントリ <http://blog.wktk.co.jp/ja/entry/2015/08/05/gunyanza>`_ を参照のこと。

How to use
----------

まずは、cuDNNをインストールしておいてください。基本、全スクリプトでGPUを使うようになっています。

以下のようにして、学習と、学習結果を用いたコンピュータ同士の対戦を観覧することができます。

```sh
pip install -r requirements.txt
# 棋譜からサンプリングした盤面を元にランダムな手を生成し、HDF5形式で保存
mkdir random_boards
./generate_random_boards_to_hdf5 kifu random_boards
# 学習
mkdir model
./learn random_boards model 100000 500 0.1
# 学習が進むのを待つ。誤差が最小値を10回更新するごとに、modelディレクトリにmodel.pickleが出力される

# 学習したモデルを使ってコンピュータ同士で対戦
./play_game model/gunyanza.model.pickle
```

FAQ
---

Q: generate_random_boards_to_hdf5 が以下のようなエラーを出す

::

  RuntimeError: Unable to register datatype (Can't insert duplicate key)

A: hdf5 1.8.13以前が使われていると発生します。以下のコマンドでh5pyが使っているhdf5のバージョンを確認しましょう。hdf5 1.8.14以降を使っても、以下のコマンドでは1.8.13以前が出る場合には、h5pyはpipなどを使わずに、setup.pyを使ってインストールしてください。

::

  import h5py
  print h5py.version.info

Q: Out of memory的なこと言われるんですけど

A: batch_sizeを減らしてください。

Q: cuDNN/Chainerがインストールできません！

A: 頑張れ！ Google Groupに書いたらサポートが手厚い予感がするぞ。

Q: なんでGPL3なの

A: 依存ライブラリのpython-shogiは、GPL3のpython-chessを元にしているのでGPL3です。そのpython-shogiにべったりなのと、元ネタのErikさんのコードのライセンスが不明なので、とりあえずGPL3で。こだわりはないです。
