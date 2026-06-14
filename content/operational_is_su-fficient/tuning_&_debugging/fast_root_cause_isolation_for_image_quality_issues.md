# Fast Root Cause Isolation for Image Quality Issues

用在行車紀錄器、門鈴等，需要隨時啟動但又因為隱私和省電需求不得不以超低功率運作的情況，以下是步驟

1. **Always on**: 以sensor極低幀率(1fps甚至更低)和低解析度運作
    1. 數據不會進入主記憶體，進入SoC內部的專屬低功耗緩存，僅做簡單的人形偵測
2. Trigger: 用Radar或PIR(被動紅外線)或是任何感測器感測物體移動
3. Output first frame:
    1. Context Saving:保存最後一次穩定的參數，至少有個能看的畫面而不是完全的第一幀
    2. Fast 3A: 在頭3-5幀會無視步長限制極快收斂，並且展示模糊的預覽圖，等收斂後再轉為正常畫面
    3. pre-exposure: 如果sensor能夠配合做簡單的人形偵測，則在真正被啟動前(按門鈴前)就已經啟動3A了