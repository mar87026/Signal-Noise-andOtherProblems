# Compiler Logic

## Alias 告知編譯器不可將物件放入register，每次都去RAM取值

### votaile

1. 常和extern共用，但要注意不論是定義還是宣告，votaile和extern都不能省略
2. 每次都要走匯流排去RAM拿值，會比較花時間

## Alias 告知編譯器去它方尋找定義

### extern

1. 不是指標。但會在**`編譯期`** 標記會有一塊記憶體，型態是XXX、名為OOO，會在宣告它的時候，第一次給它實際記憶體，並連結所有呼喚到該物件的地方連結到該記憶體。
2. 定義必須為**`global varaible`** 他不管於local還是global皆是宣告並賦值，宣告時再加入extern告知: 先讓我用，然後去其他地方找它的定義。
3. 如果定義時就賦值，CPU會直接定義它並配置記憶體、成為單純的**`global varaible`** ，失去1.特性
4. 因為宣告者是直接操作叫做XXX的記憶體，雖然通常是去快取拿，但是值是會繼承的。

那麼，要怎麼確保這個記憶體的值是我們想要的呢? 不是 **`volatile`** 

[Resource Control : Mutex/atomic](/operational_is_su-fficient/coding/compiler_logic/resource_control_mutex_atomic.md)

| Heap | Stack |
| --- | --- |
| 堆 | 棧 |
| 撰寫人員設計 | 系統自動產生 |
| 手動輸出入，會有memeory leak問題；且比stack慢 | 快，通常只會移動pointer而已；但容量很小，也就是所謂的stack overflow |
| 當multi-thread運作時，資源可多線程共用 | 不可共用，是線程的私有財產 |
| malloc, calloc, realloc，其實是在記憶體裡找夠位置的地方挖一個空間來用，不連續沒alignment，完全是DMA的噩夢 |  |
| 如果資料量龐大、有共享需求，建議使用 unique_ptr與shared_ptr |  |