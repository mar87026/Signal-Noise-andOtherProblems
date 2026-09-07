# Prefix : LifeCycle

*在scope(function)中存在、消亡於scope結束的，通常稱為local variable；如果是存在於整個program time(life time)的則稱為global variable。但仍有許多綴詞去變化他們*

## Local Object to LifeTime

1. const

const 可以使的local object的生命週期與lifetime相等

1. static

## 賦予scope物件life time

### static

1. 對local 修飾: 不代表物件變為global，僅是在program結束時才消亡而已；且在執行到它時才初始化
2. 對global修飾: 強調在這支cpp中，此物件不受外來的、同名物件影響，甚至extern也不能更動