# Alias : LifeCycle

*在scope(function)中存在、消亡於scope結束的，通常稱為local variable；如果是存在於整個program time(life time)的則稱為global variable。但仍有許多綴詞去變化他們*

## 賦予物件life time

### static

1. 對**local object**修飾: 不代表物件變為global，僅是在program結束時才消亡而已；且在第一次執行到它時才初始化，並保留結果。
2. 對**global object**修飾: 強調在這支cpp中，此物件不受外來的、同名物件影響，甚至extern也不能更動
3. 對Function修飾: 僅此cpp可以動用這個function，完全不受外來者使用

##