# something else

*don't wait until you "know everything" to challenge. you will never know everything.*

[classification-nearest neighbors](something%20else/classification-nearest_neighbors.md)

[classification-hyperplane](something%20else/classification-hyperplane.md)

[depthwise separable convolution](something%20else/depthwise_separable_convolution.md)

[linear classification](something%20else/linear_classification.md)

[classic model - yolov3](something%20else/classic_model_-_yolov3.md)

[classic model - blazeface](something%20else/classic_model_-_blazeface.md)

[loss](something%20else/loss.md)

[what’s in report](something%20else/what%e2%80%99s%20in%20report%202c327c1a893c801f86abda40c3d41708.md)

[troubleshooting](something%20else/troubleshooting.md)

[quantization](something%20else/quantization.md)

[besides the training ](something%20else/besides_the_training.md)

| item |  |
| --- | --- |
| artificial intelligence | 使機器展現智慧的所有方法，不代表都是機器自我學習 |
| machine learning | 指的是由計算機從資料中學習的方法，但都需要人工去告訴它哪個是特徵，dp屬於ml的一種 |
| surpervised learning | 監督式學習，例如knn，由操作者告訴模型該以什麼公式為分類基準、以哪條線作為標準 |
| self-supervised | 自監督式，如gpt系列，會將一段資料遮住部分，由模型自己猜那一部份是什麼，不需要人類標記答案 |
| deep learning | deep learning 是ml裡面特別擅長於辨識的一群，無論是語音辨識、圖形辨識；和監督式比起來，他只需要標籤就能自我學習資料的特徵。其核心是多層(deep)的類神經網路(neural network) |
| network | 一種結構類型，通常指類神經網路，現在主流的model是network，例如cnn、rnn，但不是所有的model是network類型，也許只是簡單的數學式；由很多layer(層)組成 |
| model | 訓練好的模型，已經具備某種技能，所有的learning成果都能稱為model |
| weight | the learned values stored in the model. |

| 實驗目的 | 過程 |  |
| --- | --- | --- |
| 想知道拍攝視角對辨識能力的影響 | 以yolo v3交叉訓練與辨識coco128與visdrone | 蠻糟的，coco128底對visdrone辨識會把船辨識成車；visdrone底對coco128 precision很低 |
| multi-viewnormalizationforfacerecognition | 找資料時發現**dual-view normalization for face recognition** | 先看dual，然後確定就是dual硬擴大成7*2個角度 |
| **dual-view normalization for face recognition** | 實驗結果頗不合理，單純作為知識補充就好 |  |

| toolchain noum |  |
| --- | --- |
| pytorch | library, pythonic, user friendly, dominate the scholarship |
| tenserflow | library, developed early so most company already and hard to change it in industry. |
| dlib | toolkit, written in c++, similar as opencv |
| caffe | a classic framework by bair, written in c++ with python interface |

| cost of the metrics |  |
| --- | --- |
| learning rate | the time each epoch convergence take. |
| floating point operations(flops) | 2(regardless of floating )*sum( k * k * cin * cout * hout * wout) |
| multiply-accumulates(macs) | sum( k * k * cin * cout * hout * wout), in int8 hardware, a "mac" is often a single cycle instruction, so you just count the macs. |
| parameters | total number of weights, sum( k * k * cin * cout) |
| latency | actual execution time on specific hardware. |
| peak memory | the most ram used at any single moment |

| technique in training/test |  |
| --- | --- |
| letter box |  |
| single shot multibox detector(ssd) | doing feature detection with splitting the workflow into several steps. the former step doing detail detection in high resoltion and downsample layer by layer. and transfer the smaller image with feature channel into next step. reduce the flops in later step. |