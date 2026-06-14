# Classic Model - YOLOv3

*You Only Look Once*，傳統上判斷 是否有物件(框)與 判斷物件為何會是兩個步驟，YOLO將他併為一次解決，一套CNN將它完成。
特色是能real time偵測，共會有 x, y, w, h, confidence 五個參數表達結果，輸入會有隨機選出、同批次一起接受訓練的圖片數(batch)

訓練架構是

| Training | Validation |
| --- | --- |

**訓練步驟 - 在開始之前**

1. 設計多個ground truth，目標在訓練圖片集中的比例最好有落差，辨識並不在乎位置。
2. 每張圖的ground truth框的大小對應到三種降取樣尺寸下、每個降取樣各預設 anchor box，一張圖共有9個預設格。

3. 整資料集透過k-means 產生 具代表性的九格(3個圖片尺寸大小、一個尺寸3個框)，為此資料集的代表框

**訓練步驟 - 正式開始**

1. 將訓練畫面降取樣、通常是原尺寸1/32倍、1/16倍、1/8倍，再切成多個1*1的網格，通常稱為feature map，所以輸入圖如果要訓練，最好先做一下最佳resize尺寸的訓練。
2. 每個降取樣、每個網格都會進行預測，預測格(Anchor Box)參數包括 x, y, w, h, 是否有物件、是什麼類別
3. 選擇最佳格子、畫框。

| trouble shooting |  |
| --- | --- |
| 輸入尺寸需求 | 需要是32的倍數，如果不是，YOLO會將畫面補上灰邊直到符合條件 |
| IoU，框越大越有利嗎? | 不是，主要是看結果框和正解框重疊面積和總面積的比例 |
| 小框與大框對目標的差異 | 大對大，小對小 |
| Ground Truth的品質怎樣算好? | Target在畫面中的大小最好廣泛分布 |
| 要怎麼判斷是不是overfitting | loss正常要隨著訓練次數下降，但如果train的loss上升，而val下降，則有overfitting的可能 |
| 為什麼要對資料集做k-means找出代表九格，有什麼意義 |   1. The represent anchor boxes stand for the datasets' siduation. simliar as the size L, M ,XL in clothes. it can be classify the image/feature group quickly in practice. 
  2. 2. display the cover range of dataset: it's very close bw 2 sets of anchors, maybe we should add something new. |

| 指令與參數 train | python [train.py](http://train.py/) --img 640 --batch 32 --epochs 220 
--data your.yaml --weights [yolov3-tiny.pt](http://yolov3-tiny.pt/) 
--hyp hyp.scratch-low.yaml --cos-lr --label-smoothing 0.1 |
| --- | --- |
| img | 訓練時的影像尺寸，640代表輸入影像為640*640；以最長邊符合設定，另一邊則等比例縮放；若640*480的畫面設定480，長邊原640縮為480，原480則等比例變360，360不足480則上下各padding 60灰邊補足。 |
| batch | 每次訓練的批次大小，YOLOv3-tiny通常能用大一點的batch size |
| epochs | 完整看過訓練資料的次數，100 是基本，如果dataset小可以用更多epochs |
| weight | 權重，初始參考權重；可以讓訓練加快，不用也可以，就是晚很多收斂 |
| data | 資料集相關設定。包含train val test影像路徑、類別數量和名稱 |
| hyp | 超參數組， 人工設定的參數，不會隨著機器訓練而改變 |
| cos-lr | 餘弦學習率調整 |
| label-smoothing | 分類之間的差異平滑化，不以是與否強制分類；目的是降低overfitting |

| 指令與參數 detect | python [detect.py](http://detect.py/) --weights [best.pt](http://best.pt/) --source path/to/images |
| --- | --- |
| weights  |  |

![image.png](classic_model_-_yolov3/image.png)

[Yolov3 C-Model 解析 - 讀取與建立](classic_model_-_yolov3/yolov3_c-model_%e8%a7%a3%e6%9e%90_-_%e8%ae%80%e5%8f%96%e8%88%87%e5%bb%ba%e7%ab%8b_2cc27c1a893c804f9c7eded9cf078c8a.md)

[Yolov3 C-Model 解析 - 偵測](classic_model_-_yolov3/yolov3_c-model_%e8%a7%a3%e6%9e%90_-_%e5%81%b5%e6%b8%ac_2cd27c1a893c800f933be2ee9b8791d1.md)