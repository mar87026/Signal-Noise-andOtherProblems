# Pointer

*there’s no type called address, only ponter; you could not change the address, it’s written by CPU, but the pointer is editable mostly.*

```cpp
void foo(int *b) {

    *b = 10;
}
int caller = 5;
foo(&caller);
```

先是foo以整數型態的指標b作為物件caller，只接受同為指標型態的物件

a把地址副本傳送進了foo

所以其實是 (int*)b = &a; b是個整數指標的物件

而b的指標 (int*)*b = a, (int*) *b = 10 ⇒ a ⇒ 5→10;

| noun | mean | type |
| --- | --- | --- |
| caller  | caller’s value : 5 | int |
| &caller  | caller’s address | int* |
| b | b’s value, caller ’s address | pointer of int |
| *b | b’s pointer, caller ’s value | int |
| &b | &(int*), b’s address | int** |

```cpp
void swap(int*a, int* b) {
    //switch where the a and b point to
    //(int*)a = &p;
    //(int*)b = &q;
    //make (int*)a = &q, (int*)b = &p
    int temp = a; //record a, the address of caller
    *a = *b;
    *b = temp;
}
```

swap實際上就是交換兩個pointer物件的值，也就是caller的位置副本

目標是在swap裡，*a得到的是原本*b的值；*b則是*a原本的值；但你不可能交換兩個物件的”address”，你只能改變它的pointer

extend: 

[Swap: switch the ownership](/operational_is_su-fficient/coding/pointer/swap_switch_the_ownership.md)

那代表其實b可以轉指向其他物件的address，我要怎麼確保指向固定呢?

你要保護的是 caller的值 不被改動，還是 pointer物件 的值 ?

### Const

| status |  |  | 改動的是誰 |
| --- | --- | --- | --- |
| const int **b ⇒ (const int)**b | b 是個pointer，指向const int | *b指向的int不能被b修改，但可以b = &s | pointer物件的值 |
| int const **b ⇒ (int const)**b |  |  | pointer物件的值 |
| int *const b | b是個const pointer指向int | b不能修改但*b = 20可以 | caller的值 |
| const *int b | b是個int pointer ，並為不可動的常數 | b不可以修改，但*b = 15 可以 | caller的值 |

```cpp
void make_NULL(int* p) {
    p = NULL; //p的值變null，caller的值不變，但後續這個scope無法在正確從input拿取正確值了
}
```