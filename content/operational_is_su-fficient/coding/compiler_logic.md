# Compiler Logic

| Heap | Stack |
| --- | --- |
| 堆 | 棧 |
| 撰寫人員設計 | 系統自動產生 |
| 手動輸出入，會有memeory leak問題；且比stack慢 | 快，通常只會移動pointer而已；但容量很小，也就是所謂的stack overflow |
| 當multi-thread運作時，資源可多線程共用 | 不可共用，是線程的私有財產 |
| 如果資料量龐大、有共享需求，建議使用 unique_ptr與shared_ptr |  |