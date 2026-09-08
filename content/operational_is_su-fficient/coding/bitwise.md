# BITWISE

*The engineering magic*

1. Positive integers could deploy it without binarize.
2. negative one should be 2’s implement first.
3. operation on site could be size_t or something like it.

AND  &

OR |

NOT OR ~(a|b) 皆無者為一

XOR ^ 不同者為一

NOT AND ~(a&b)

NOT ~

### Set

```jsx
register |= (1<<3); //設定register 第三個bit為1
```

### Get

```jsx
size_t k = register & (1<<3); //取得register 第三個bit
```

### Clear

```jsx
register &= ~(1<<3); //clear 第三個bit
```

### Toggle(inverse)

```jsx
register ^= (1 << 3); //若原為0，和1不同則改為1；原為1，則轉為0
```