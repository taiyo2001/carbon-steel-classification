from torch import nn, randn


class AlexNet(nn.Module):
    def __init__(self, n_output, n_hidden, input):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 32, 3, padding=(1, 1))
        self.conv2 = nn.Conv2d(32, 32, 3, padding=(1, 1))
        self.conv3 = nn.Conv2d(32, 64, 3, padding=(1, 1))
        self.conv4 = nn.Conv2d(64, 64, 3, padding=(1, 1))
        self.conv5 = nn.Conv2d(64, 128, 3, padding=(1, 1))
        self.conv6 = nn.Conv2d(128, 128, 3, padding=(1, 1))
        self.relu = nn.ReLU(inplace=True)
        self.maxpool = nn.MaxPool2d((2, 2))
        self.flatten = nn.Flatten()
        # self.l1 = nn.Linear(7311488, n_hidden)
        # self.l1 = nn.Linear(6272, n_hidden) # 32
        # self.l1 = nn.Linear(508032, n_hidden)  # 256

        # TODO: flattenに入れる前の入力画像(特徴MAP)のサイズを取得
        self.l1 = nn.Linear(131072, n_hidden)  # 256 v2
        # input_size_into_FLATTEN = get_input_size_into_FLATTEN(input)
        # print("input_size_into_FLATTEN: {}".format(input_size_into_FLATTEN))
        # dummy_input = randn(*input)
        # dummy_output = self.features(dummy_input)
        # flattened_size = dummy_output.view(dummy_output.size(0), -1).size(1)
        # self.l1 = nn.Linear(flattened_size, n_hidden)  # 256 v2
        # self.l1 = nn.Linear(460800, n_hidden) # 480

        self.l2 = nn.Linear(n_hidden, n_output)
        self.dropout1 = nn.Dropout(0.2)
        self.dropout2 = nn.Dropout(0.3)
        self.dropout3 = nn.Dropout(0.4)
        self.bn1 = nn.BatchNorm2d(32)
        self.bn2 = nn.BatchNorm2d(32)
        self.bn3 = nn.BatchNorm2d(64)
        self.bn4 = nn.BatchNorm2d(64)
        self.bn5 = nn.BatchNorm2d(128)
        self.bn6 = nn.BatchNorm2d(128)

        self.features = nn.Sequential(
            self.conv1,
            self.bn1,
            self.relu,
            self.conv2,
            self.bn2,
            self.relu,
            self.maxpool,
            self.dropout1,
            self.conv3,
            self.bn3,
            self.relu,
            self.conv4,
            self.bn4,
            self.relu,
            self.maxpool,
            self.dropout2,
            self.conv5,
            self.bn5,
            self.relu,
            self.conv6,
            self.bn6,
            self.relu,
            self.maxpool,
            self.dropout3,
        )

        self.classifier = nn.Sequential(self.l1, self.relu, self.l2)

    def forward(self, x):
        x1 = self.features(x)
        x2 = self.flatten(x1)
        x3 = self.classifier(x2)
        return x3


# TODO: flattenに入れる前の入力画像(特徴MAP)のサイズを取得
def get_input_size_into_FLATTEN(input):
    print("x before shape: {}".format(input.shape))

    # flattenに入れる前の入力画像(特徴MAP)のサイズ確認
    conv1 = nn.Conv2d(3, 32, 3)
    conv2 = nn.Conv2d(32, 32, 3)
    maxpool = nn.MaxPool2d((2, 2))
    relu = nn.ReLU(inplace=True)

    x1 = conv1(input)
    x2 = relu(x1)
    x3 = conv2(x2)
    x4 = relu(x3)
    x5 = maxpool(x4)

    print("x1 shape: {}".format(x1.shape))
    print("x2 shape: {}".format(x2.shape))
    print("x3 shape: {}".format(x3.shape))
    print("x4 shape: {}".format(x4.shape))
    print("x5 shape: {}".format(x5.shape))

    features = nn.Sequential(conv1, relu, conv2, relu, maxpool)

    outputs = features(input)
    print("outputs: {}".format(outputs))

    flatten = nn.Flatten()
    outputs2 = flatten(outputs)
    print("outputs shape: {}".format(outputs.shape))
    print("outputs2 shape: {}".format(outputs2.shape))

    return outputs2.shape
