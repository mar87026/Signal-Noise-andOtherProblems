# Resource Control: Lock

改變不了資源的多寡，就改變掌控的時機

```c
volatile int count;

void *work(void* a) {
count++
}
```

counter不是atomic operation 
會有讀取、計算、寫入重複步驟，這時候可能有另一個thread 插入，因此控制誰能夠掌握主導權（critical section) 在thread process大概會長這樣：

```c
pthread_mutex_lock(&lock);//thread1 掌握主導權

if (buffer->ready) {//動作前先確認資源真的有空
    work(buffer);
}
pthread_mutex_unlock(&lock);//thread1 釋放主導權
```

work如果很耗時間，要確保它佔用資源的時間夠少

```c
pthread_mutex_lock(&lock);

if (buffer->ready) {
    buffer->ready = 0;
    local_buffer = buffer;//取走資源
}
pthread_mutex_unlock(&lock);
work(local_buffer);
```

可以參考:

[C++ Resource Control Type](/operational_is_su-fficient/coding/pointer/../c++_resource_control_type.md)

## 誰擁有資源

### Mutex

### 誰控制critical section

### condition_variable

## 現在還有多少資源

Semaphore