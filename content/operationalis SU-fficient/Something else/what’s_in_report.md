# What’s in report

Loss

![results.png](What%E2%80%99s%20in%20report/results.png)

| train訓練/val驗證組 | value |
| --- | --- |
| box loss | 訓練框損失 |
| obj loss | 是否為物件 |
| cls loss | 分類判定損失 |
| overfitting | 以上參數train降但是val升 |

| metrics 模型性能 |  |
| --- | --- |
| precision | 抓到的物件裡，有多少是真的 TP / (TP + FP) |
| recall | 所有真實物件被抓到了多少 TP / (TP + Face Number) |
| mAP 0.5 | mean Average Precision 平均精確率 IoU>0.5算抓對 |
| mAP 0.5:0.95 | 對maP 0.5 0.55 0.6...0.95共十個門檻取平均 |

![image.png](What%E2%80%99s%20in%20report/image.png)

|  |  |
| --- | --- |
| FAR false acceptance rate | 錯誤接受的次數/測試接受的次數，數字越高代表辨識能力越好；多個方法針對同一個資料庫做辨識，FAR1%、0.1%代表100、1000個冒充者當中，僅接受一次失誤。 |
| FRR false rejection rate | 偽陰性，正確但是被判斷成錯誤的 |
| TAR true acceptance rate | 正確被判斷出來 |
| EER equal error rate | 等錯誤率，當FAR= FRR時，是落在多少 |
| RANK-1 | 辨識同一個資料庫時，一次判斷成功的比例 |
| RANK-5 | 辨識同個資料庫時，正確答案在前五名的比例 |