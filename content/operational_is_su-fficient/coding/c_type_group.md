# C Type : Group

### Struct

1. 總大小是全部物件總和加上padding

### union

1. 全體物件共用同一個記憶體，總大小就是最大那個成員的大小
2. 一個時間只有一個物件發揮功用，儲存了一個會影響其他的

但如果我們多次使用這些結構，但又希望資料能串連起來，就可以用上 

[Linked List](/operational_is_su-fficient/coding//operational_is_su-fficient/coding/pointer/linked_list.md)

但這解決不了記憶體不連續的問題，不同的Linked List還是可以會落在不同記憶體上(contiguity)、還有alignment問題