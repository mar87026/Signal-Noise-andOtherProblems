# Inspiration as Flicker

*Tips, The links between algorithm and tuning*

1. **相機運動速度過快時，為避免畫面模糊或出現鬼影：**
    1. 可降低曝光時間、提高畫面亮度
2. 監視器在暗處時，為避免雜訊可增加曝光時間、降低 FPS，以提升 SNR；但也會讓鬼影更明顯。
3. 在其他條件不變的情況下，Bitrate 上升代表畫面包含更多細節，或出現較多不可預期的運動；若可用 Bitrate 提升，通常表示畫質可隨之提升。bitrate = ∑(bits per frame) × FPS
4. **畫面上出現 8×8、16×16 的色塊：**
    1. 通常是bitrate不足，使得CODEC時的量化不能維持高頻細節
5. **漸層處出現一圈圈的顏色：**
    1. 通常是bit-depth位深不足以傳達細節變化，建議檢查輸出時有沒有做好平滑漸層
6. 若邊緣模糊或出現鋸齒，且無法調整 up-scaling 演算法，建議在前端加入低通濾波。
7. AE 提升整體亮度時會改變全畫面，可能使 encoder 在做 Motion Estimation 時誤判 residual 上升而導致畫質下降；可讓 AE 通知 encoder：一定程度的畫面變化屬於 AE 效果。
8. **紅色區域通常較容易出現雜訊：**
    1. 因感測器對於紅光的QE效率較差，SNR比較低使得紅色區域天生就比較髒
    2. 若當下是藍光場景(晴天場景)，可能是AWB將紅色通道補償過多了
    3. LSC可能會使邊緣的紅光過度強化
    4. Saturation和CCM會放大顏色的差異，可以關閉試試看變化
9. RD cost = D (distortion) + Rate * lambda