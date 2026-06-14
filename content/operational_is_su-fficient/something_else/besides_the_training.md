# Besides the Training

### Train on the server :

What do you should is keeping the traing process out of Child process which controled by PC(local).

```jsx
sudo apt install tmux
```

start and working in new space which protected by tmux.

```jsx
tmux new -s my_train
```

training your own project

```jsx
python train.py
```

Press `Ctrl` + `B` together, release them, and then press `D`.
now you can deal another issue, leave training alone.

back to space:

```jsx
tmux a -t my_train
```

remember to close tmux session safely( within it)

```jsx
exit
```

show the tmux session:

```jsx
tmux ls
```

kill it from outside:

```jsx
tmux kill-session -t my_train
```