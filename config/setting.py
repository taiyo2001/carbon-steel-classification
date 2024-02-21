from module import const
import os

const.APP_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


# 対物レンズ10倍. 入力サイズ960px. 撮影箇所x.1のデータセット(npzのバイナリファイル)
const.SC_x10_960_x1_FILE_NAME = "/sc_x10_960_x1.npz"

const.DATASET_PATH = (
    const.APP_PATH + "/dataset_npz/x.1_dataset/" + const.SC_x10_960_x1_FILE_NAME
)
const.CHECKPOINT_PATH = const.APP_PATH + "/data/model"
