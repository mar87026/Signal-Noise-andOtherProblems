# char & string

strlen

```c
size_t strlen(const char *str) {
    size_t count = 0;
    while (str[count] != '\0') {
        count++;
    }
    return count;
}
```

strcmp

```c
int strcmp(const char *str1, const char *str2) {
// return 0 while str1 == str2
//return -1 while str1 is shorter or char of str1 in first distinct pair is priot to str2
//return 1 while str2 is shorter or char of str2 in first distinct pair is priot to str1
int count = 0;
while ((str1[count] != '\0') && (str2[count] != '\0')) {
if (str1[count] > str2[count]) return1;
if (str1[count] < str2[count]) return 1;
count++;
}
if (str1[count] == '\0' && str2[count] == '\0') {
     return 0;
}
if (str1[count] == '\0') return -1;
if (str2[count] == '\0') return 1;

}
```

strcpy

```c
void strcpy(char* dst, const char *src) {
    int count = 0;
    //dst must annonuce outside.
    while (src[count] != '\0') {
        dst[count] = src[count];
        count++;
    }
    dst[count] = '\0';
}

char* strcpy(const char *src) {
    int count = 0;
    int init_size = 256;
    char* dst = malloc(init_size*sizeof(char));
    char *tmp = NULL;
    while (src[count] != '\0') {
        dst[count] = src[count];
        count++;
        if (count == init_size) {
            init_size += init_size;
            tmp = realloc(dst, init_size*sizeof(char);
            if (tmp != NULL) dst = tmp;
            else {
                free(dst);
                
            }
            tmp = NULL;
        }
    }
    dst[count] = '\0';
    tmp = realloc(dst, sizeof(count);
    if (tmp != NULL) dst = tmp;
   
    tmp = NULL;
    return dst;
}

```