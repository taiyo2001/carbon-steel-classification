# carbon-steel-classification
ニューラルネットワークを用いた炭素鋼の鋼種識別

## フォルダー構造
<pre>

.
├── app
│   ├── main_kcs.ipynb
│   ├── main_ubuntu_AlexNet_v2.ipynb
│   └── services
│       └── gradcam.ipynb
├── bin
│   ├── docker_setup.sh
│   ├── exec_ipynb.sh
│   ├── formatter.sh
│   └── setup.sh
├── config
│   ├── __init__.py
│   └── setting.py
├── dataset_npz
├── Dockerfile
├── Makefile
├── module
│   ├── const.py
│   ├── __init__.py
│   └── machine_learning_model.py
├── README.md
├── requirements.sample.txt
├── requirements.txt
├── result
│   ├── main_ubuntu_AlexNet_v1.nbconvert.ipynb
│   ├── main_ubuntu_AlexNet_v2_drop.nbconvert.ipynb
│   ├── main_ubuntu_lenet_v2_BN.nbconvert.ipynb
│   └── services
│       └── gradcam.nbconvert.ipynb
└── setup.py

</pre>
8 directories, 22 files


## 環境構築
機械学習ライブラリにPyTorchを使用しているためGPUが必須.

## データ準備
"dataset_npz"をアプリケーション配下に設置.

### Docker
Build & Running Docker Container
```
sh bin/docker_setup.sh
```
コンテナ内に入ったらaliasを登録するために毎回以下を実行.
```
source bin/setup.sh
```

<!-- Build
```
docker build -t [name] .
```

立ち上げ
docker start [name]
docker container exec -it [name] bash
cd /root
source bin/setup.sh
```

終了
```
exit
docker stop [name]
``` -->

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
Check Linter
```
black ./ --check
```

Exec Linter
```
black ./
```
