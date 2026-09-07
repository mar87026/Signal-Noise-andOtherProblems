# Coding

每個Object(通常稱為物件，比較沒有單指一個項目而有一群、一定容量同意義的數值)

在執行時都有自己的Lifecycle、pointer(address)、type、state/value與resource這些概念；這幾項都不是永恆不變的。

變數型態，諸如vector、uint_ptr、int都是在補充敘述這幾個特性，但不是全部，像是lifetime就不是它們能標註的

Compiler也會額外透過語意去分配stack、register、heap或其他storage

C/C++ development就是操作這些資訊以達到最高效益

[Compiler Logic](/operational_is_su-fficient/coding/compiler_logic.md)

[BITWISE](/operational_is_su-fficient/coding/bitwise.md)

[Pointer](/operational_is_su-fficient/coding/pointer.md)

[C++ Basic Type](/operational_is_su-fficient/coding/c++_basic_type.md)

# Lifecycle

在scope(function)中存在、消亡於scope結束的，通常稱為local variable；如果是存在於整個program time(life time)的則稱為global variable。但仍有許多綴詞去變化他們

```cpp
int *a;
int *FOO {
    int k[] = {1,2,3,4};
    return k;
}
a = FOO();
(*a)+=4; 
```

這程式在*a++=4最容易出錯，但有很大的可能一直都相安無事。

k是object address也許是0x5678，state 是{1,2,3,4}，這裡不用有owner概念，它在FOO結束時結束Lifecycle。

address會作為value交給a，k消亡

因此(*a)+=4;  不一定會得到5，而是任何數值都有可能，也可能這一塊address會被其他object接著reused，也可能直接導致崩潰

那我該怎麼正確地傳出k object的value呢?

### 給予回傳值Life time

```jsx
int *a;
int *FOO {
    static int k[] = {1,2,3,4};
    return k;
}
a = FOO();
(*a)+=4; 
```

### 給予caller一個空間

```cpp
int a[4];
void FOO(int* caller) {
    caller[0] = 1;
    caller[1] = 2;
    caller[2] = 3;
    caller[3] = 4;
}
FOO(a);
(*a)+=4;
```

這邊傳進的是a的address副本，並沒有包含它的相關說明，因此得手動傳入value

而a傳入FOO，並不影響a對於這塊resource的ownership

### 回傳一個完整的object

```cpp
array<int,4> FOO {
    return {1,2,3,4};
}
array <int,4> a = FOO();
(*a)+=4; 
```

### 另一種回傳一個完整的object: 直接告訴CPU用heap，轉移這個address

```cpp
int* FOO {
    int* k = new int [4] {1,2,3,4};
    return k;
}
int* a = FOO();
(*a)+=4;

delete[] a;//IMPORTANT!!!
```

[Prefix : LifeCycle](/operational_is_su-fficient/coding/prefix_lifecycle.md)

# RESOURCE

為確保資源調度、資料安全，有了Owner的概念

```cpp
std::vector<int> a {1,2,3,4};
std::vector<int> b = std::move(a);
```

a依舊存在，但不再擁有原本的resource

```cpp
vector a
address 0x1000
lifecycle still live
resource 0x5678
state capacity 4
      pointer 0x5678
      size 4
      value {1,2,3,4}
```

會變成

```cpp
vector a
address 0x1000
lifecycle still live
resource x
value capacity ?
      pointer ?
      size ?
      value ?
```

它依舊是個vector，你可以push_back可以clear，但注意.data()這類pointer動作的owner已不再是原主a，是否可以繼續使用要看具體情況。

a 依舊可以繼續使用，因此

```jsx
a.clear();
a.push_back(5);
//////////////
vector a
address 0x1000
lifecycle still live
resource 0x7890
value capacity 1
      pointer 0x7890
      size 1
      value {5}
```

有大概概念後，來討論ISP處理frame的resource交換吧

[Power-On to Pipeline](/operational_is_su-fficient/power-on_to_pipeline.md)

由上面那篇複製了

![image.png](/operational_is_su-fficient/coding/image.png)

ISP processor透過Memory Control、DMA取得RAM buffer裡儲存的frame資訊，完成操作後，將成果再透過DMA、Memory Control送回RAM buffer；其他processor，例如AI NPU會再走相近路線去RAM把資訊拿出來做相對應的處理。

這樣的話，資料會有三個狀態→未處理frame的A、處理中的B、已料理好的C。

通常A會是stream in、line by line輸入，通常在需要做filter的時候才會做line buffer暫存材料
B會是暫存且不穩定的狀態，所以會最要求它的ownership不能擅動
C是成果，但千萬別和A混在一起放。

因此3狀態可以各預備兩個buffer: 手上拿一個處理，桌上放一個待命；絕不直接將手上的交給下一個狀態，DMA負責將桌上不同狀態own 的buffer交換，processor只在完成動作後，會將手上的籃子和桌上的交換。因此我們需要一種type強調resource owner唯一性或是分享性。以及定義交換前後buffer的狀態。

extend: 

[Swap: switch the ownership](/operational_is_su-fficient/coding/pointer/swap_switch_the_ownership.md)

[C++ Resource Control Type](/operational_is_su-fficient/coding/c++_resource_control_type.md)

[C & C++](/operational_is_su-fficient/coding/c_&_c++.md)

[Linked List](/operational_is_su-fficient/coding/linked_list.md)

[Segmentation fault/Memory Issue](/operational_is_su-fficient/coding/segmentation_fault_memory_issue.md)

[Trouble Shooting](/operational_is_su-fficient/coding/trouble_shooting.md)