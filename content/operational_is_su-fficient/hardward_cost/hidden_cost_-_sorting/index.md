# Hidden Cost - Sorting

*We learn digital signal processing at beginning with high level language, but implemented in RTL*

Make a statistic within 16*16 grids whose overlapped an image. then you will get a histogram

![image.png](/operational_is_su-fficient/hardward_cost/hidden_cost_-_sorting/image.png)

If I tend to get max and minimum ones

```python
min = min(min, x)
max = max(max, x)
```

about 510 times comparing and 2 comp.

How about adaptive the histogram? Get the 15th、31th,…255th

Sort? It takes 255! times comparisons(bubble sort)

# CDF