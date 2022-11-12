# Shader

<img width="1148" alt="截屏2022-11-06 上午10 19 55" src="https://user-images.githubusercontent.com/76422688/200308836-95f63e7f-34f1-4261-93c5-445b70db864f.png">

<img width="1148" alt="截屏2022-11-06 上午10 19 55" src="https://user-images.githubusercontent.com/76422688/201072088-f41db148-0235-40d3-9142-d1b0e18af79b.jpg">

# How to make it
  
## Rotate
Assume that there is a square in the 3D space and it have three point in x(1,0,0),y(0,1,0),z(0,0,1) axis.
We use three point to make a matrix
```
origin=[
[ 1, 0, 0],
[ 0, 1, 0],
[ 0, 0, 1]
]
#x↑,y↑,z↑
```
<img width="742" alt="截屏2022-11-10 下午7 11 58" src="https://user-images.githubusercontent.com/76422688/201463377-5436e46e-98ca-42bf-930e-f61e41c0bdb1.png">

Now, we start to rotate this sphere with Y axis ϴ degree. This square will become following diagram.

<img width="742" alt="截屏2022-11-10 下午7 13 00" src="https://user-images.githubusercontent.com/76422688/201463455-da41dee8-5f44-4d23-a088-7dbcf526e5e3.png">

The matrix also become
```
rotated_y=[
[ cosϴ, 0   , -sinϴ],
[ 0   , 1   , 0    ],
[ sinϴ, 0   ,  cosϴ]
]
# x↑,   y↑,   z↑
```
So there is a transition matrix make the orgin become to rotated_y
```
transition matrix * origin = rotated_y
```
In this way, we can calculate that the transition matrix of y is 
```
transition_y=[
[ cosϴ , 0   ,  sinϴ],
[ 0    , 1   , 0    ],
[ -sinϴ, 0   ,  cosϴ]
]
```

Likewise, the rotation of x and z also obey this rule

So the rotation of x is
<img width="742" alt="截屏2022-11-10 下午7 14 45" src="https://user-images.githubusercontent.com/76422688/201466905-634887da-ed5d-4997-93df-77924e4b911f.png">


