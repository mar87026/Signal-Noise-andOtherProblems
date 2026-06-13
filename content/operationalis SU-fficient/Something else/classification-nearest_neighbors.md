# Classification-Nearest Neighbors

資料庫分成 訓練、驗證、測試，驗證和訓練可以隸屬同一組資料，只是按照實驗次數調整以利設計hyperparameter

| Training | Validation | Test |
| --- | --- | --- |

L1 : Manhattan來顯示兩份資料的差異(尤其指圖像)

$$
d_1(I_1, I_2) = \sum_{p} |I_1^p - I_2^p|
$$

L2: Euclidean

$$
d_2(I_1, I_2) = \sqrt{\sum_p(I_1^P - I_2^p)^2}
$$

經典的Nearest Neighbors就是使用L1或是L2:記著所有訓練資料、對輸入的測試圖片尋找距離。

K-NN 則為其變化型: 由K決定 和目標最近的K個訓練資料屬於哪個項目，則判斷為該項目；如果k = 1的話，判斷結果會不夠圓滑

但KNN基本不用在圖像，因為數據太大、(訓練量隨RGB成為立方倍)且L2對於圖片變化不大有反應

![image.png](Classification-Nearest%20Neighbors/image.png)

這是訓練圖集的k =1分類，可以看出中心黃色區域只要在範圍內就是黃色分類，稍微偏一點就是綠色

![image.png](Classification-Nearest%20Neighbors/image%201.png)

白色部分交由演算法決定它該是哪個分類

以上 L1, L2的選擇、k的大小等，是由人類設定而不是機器自我學習的參數，稱為 hyper parameters