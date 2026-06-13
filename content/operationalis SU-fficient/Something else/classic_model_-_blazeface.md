# Classic Model - BlazeFace

*Classic SSD process*

detect 6 key points in original paper(eyes, ear, nose, mouth)

#### **1. backbone1：中尺度特徵提取**

負責處理較高解析度的特徵圖，用於偵測影像中**較小的人臉**。
• **輸入與輸出**：它接收 128x 128 的影像，經過一系列 `BlazeBlock` 後，輸出尺寸為 16*16、通道數為 88 的特徵圖。
• **結構**：包含 1 層起始卷積和 11 個 `BlazeBlock`。
• **預測頭連接**：`backbone1` 的輸出會直接送往 `classifier_8` 和 `regressor_8`。這兩層預測頭會在 16* 16 的網格上進行偵測，總共提供 512 個 Anchors（16*16*2）。
****

#### **2. backbone2：大尺度特徵提取**

`backbone2` 接著 `backbone1` 的結果繼續運算，進一步縮小特徵圖以偵測影像中**較大的人臉**。
• **輸入與輸出**：它接收 `backbone1` 產出的 16*16 特徵圖，輸出尺寸進一步壓縮至 8* 8、通道數為 96。
• **結構**：包含 5 個 `BlazeBlock`，其中第一層的 `stride=2` 負責將尺寸減半。
• **預測頭連接**：它的輸出會送往 `classifier_16` 和 `regressor_16`。這兩層預測頭在 8* 8的網格上運作，提供 384 個 Anchors（8*8*6）。