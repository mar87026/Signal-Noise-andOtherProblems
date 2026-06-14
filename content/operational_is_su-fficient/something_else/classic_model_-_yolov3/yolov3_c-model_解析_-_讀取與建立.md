# Yolov3 C-Model 解析 - 讀取與建立

轉換cfg為設定，建立layer

由 network.c load_network帶入設定

```c
network *load_network(char *cfg, char *weights, int clear)
{
    network *net = parse_network_cfg(cfg);
    if(weights && weights[0] != 0){
        load_weights(net, weights);
    }
    if(clear) (*net->seen) = 0;
    return net;
}
```

parser.c parse_network_cfg

```c

```