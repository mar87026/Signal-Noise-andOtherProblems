# C++ Basic Type

C/C++的object有各種型態，但都有共同的lifecylce、address、state/value、resource概念，為了定義好後兩者，產生了type這個概念

### Container - For data type objects

| name | profile | ini | base | inform in | inform out | copy | find |
| --- | --- | --- | --- | --- | --- | --- | --- |
| vector | 可以動態調整大小的陣列升級版 | vector<int> a (25, 0); <br> vector<int> a (b); |  |  |  |  | find(a.begin()+i, a.end(), k); |
| map | 有序，自動排序 |  |  | O(log n) |  |  | O(log n) |
| unordered_map | 無序 |  |  |  |  |  | O(1) |
| set | 有序，不允許元素重複 |  |  |  |  |  |  |
| unordered_set | 無序也無法排序，不允許元素重複 |  |  |  |  |  |  |
| deque | 可從頭和尾輸入 |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |

### Container - For duplicate Objects

| Class | Struct | Union |
| --- | --- | --- |
| 類別 | 結構 | 共用體 |
| user-defined data type, define function and variable with the key word class. |  | replaced with variant  after C++17 |
| public, private, protected | all public |  |
| each variable, each register, whole size must care about the alignment | each variable, each register, whole size must care about the alignment | all variables on same register, whole size is depended on the biggest variable, and one of them live at same time. |