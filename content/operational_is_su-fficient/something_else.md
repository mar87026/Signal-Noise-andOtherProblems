# Something else

*Don't wait until you "know everything" to challenge. You will never know everything.*

[Classification-Nearest Neighbors](something_else/classification-nearest_neighbors.md)

[Classification-hyperplane](something_else/classification-hyperplane.md)

[Depthwise Separable Convolution](something_else/depthwise_separable_convolution.md)

[Linear Classification](something_else/linear_classification.md)

[Classic Model - YOLOv3](something_else/classic_model_-_yolov3.md)

[Classic Model - BlazeFace](something_else/classic_model_-_blazeface.md)

[LOSS](something_else/loss.md)

[What’s in report](something_else/what_s_in_report.md)

[TroubleShooting](something_else/troubleshooting.md)

[Quantization](something_else/quantization.md)

[Besides the Training ](something_else/besides_the_training.md)

| Item |  |
| --- | --- |
| Artificial Intelligence | 使機器展現智慧的所有方法，不代表都是機器自我學習 |
| Machine Learning | 指的是由計算機從資料中學習的方法，但都需要人工去告訴它哪個是特徵，DP屬於ML的一種 |
| Surpervised Learning | 監督式學習，例如kNN，由操作者告訴模型該以什麼公式為分類基準、以哪條線作為標準 |
| Self-Supervised | 自監督式，如GPT系列，會將一段資料遮住部分，由模型自己猜那一部份是什麼，不需要人類標記答案 |
| Deep learning | deep learning 是ML裡面特別擅長於辨識的一群，無論是語音辨識、圖形辨識；和監督式比起來，他只需要標籤就能自我學習資料的特徵。其核心是多層(deep)的類神經網路(Neural Network) |
| Network | 一種結構類型，通常指類神經網路，現在主流的Model是Network，例如CNN、RNN，但不是所有的Model是Network類型，也許只是簡單的數學式；由很多Layer(層)組成 |
| Model | 訓練好的模型，已經具備某種技能，所有的Learning成果都能稱為Model |
| weight | The learned values stored in the model. |

| 實驗目的 | 過程 |  |
| --- | --- | --- |
| 想知道拍攝視角對辨識能力的影響 | 以Yolo v3交叉訓練與辨識coco128與VisDrone | 蠻糟的，coco128底對VisDrone辨識會把船辨識成車；VisDrone底對coco128 precision很低 |
| MULTI-VIEWNORMALIZATIONFORFACERECOGNITION | 找資料時發現**Dual-View Normalization for Face Recognition** | 先看dual，然後確定就是dual硬擴大成7*2個角度 |
| **Dual-View Normalization for Face Recognition** | 實驗結果頗不合理，單純作為知識補充就好 |  |

| toolchain noum |  |
| --- | --- |
| pytorch | library, pythonic, user friendly, dominate the scholarship |
| tenserflow | library, developed early so most company already and hard to change it in industry. |
| dlib | toolkit, written in C++, similar as opencv |
| caffe | a classic framework by BAIR, written in C++ with python interface |

| Cost of the Metrics |  |
| --- | --- |
| Learning Rate | The time each epoch convergence take. |
| Floating Point Operations(FLOPs) | 2(regardless of floating )*Sum( K * K * Cin * Cout * Hout * Wout) |
| Multiply-Accumulates(MACs) | Sum( K * K * Cin * Cout * Hout * Wout), in INT8 hardware, a "MAC" is often a single cycle instruction, so you just count the MACs. |
| Parameters | Total number of weights, Sum( K * K * Cin * Cout) |
| Latency | Actual execution time on specific hardware. |
| Peak Memory | The most RAM used at any single moment |

| technique in Training/Test |  |
| --- | --- |
| Letter box |  |
| Single Shot Multibox Detector(SSD) | Doing feature detection with splitting the workflow into several steps. The former step doing detail detection in high resoltion and downsample layer by layer. And transfer the smaller image with feature channel into next step. Reduce the FLOPs in later step. |