# carbon-steel-classification
ニューラルネットワークを用いた炭素鋼の鋼種識別

## 研究目的
実用化に向けて組織画像の自動認識時における識別過程の可視化から得る情報をもとに識別精度の向上をはかる

## フォルダー構造
<pre>


/tmp
作成ファイル保存場所
</pre>

## データセットについて
容量が重いデータセットはリポジトリに入れられないので個別に"dataset_npz"をroot配下に設置


## Jupyter Notebookの実行方法
`/app`内のJupyter Notebookを実行するときは、APP_PATHで以下を叩くと実行結果ファイル`/result/${file_name}_epoch_${epochs}.nbconvert.ipynb`が出力される.
```
ipynb ${file_name} ${epochs}
```
※第2引数は省略可

ex. 300epochs分を回す`/app/alex_net.ipynb`を実行するとき

実行コマンド
```
ipynb alex_net 300
```
出力ファイル：`/result/alex_net_epoch_300.nbconvert.ipynb`

## フォーマットの実行方法
フォーマットチェック
```
black ./ --check
```

フォーマット実行
```
black ./
```
