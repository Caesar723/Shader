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
```
transition_x=[
[ 1 , 0      , 0],
[ 0 , cosϴ   , sinϴ    ],
[ 0 , -sinϴ  , cosϴ]
]
```

the rotation of z is
<img width="742" alt="截屏2022-11-10 下午7 14 45" src="https://user-images.githubusercontent.com/76422688/201467008-8651fb29-6a21-4dd5-9148-fb465fe1725b.png">
```
transition_z=[
[ cosϴ , -sinϴ, 0],
[ sinϴ , cosϴ , 0],
[ 0    , 0    , 1]
]
```

## How to draw the outline
Firstly, we set a point(0,1,0) and use the rotation matrix of z 
Use loop to ratate several times with ϴ degree until it rotate 180 degree
```
for z in range(180//ϴ):
  point = transition_z * point
  ...
```
<img width="627" alt="截屏2022-11-10 下午7 53 25" src="https://user-images.githubusercontent.com/76422688/201467305-2e9d1d17-1643-44bb-9721-6b4273bbd93d.png">

Then , each point must be rotate with y axis 
```
for y in range(360//ϴ):
  point = transition_y * point
  ...
```
<img width="689" alt="截屏2022-11-10 下午7 58 36" src="https://user-images.githubusercontent.com/76422688/201467414-4380223d-f4bc-4e43-84b1-5aca5e46f71c.png">
<img width="689" alt="截屏2022-11-10 下午8 00 44" src="https://user-images.githubusercontent.com/76422688/201467427-4ad71738-691f-4a79-9793-78db5c3a6541.png">
<img width="689" alt="截屏2022-11-10 下午8 04 41" src="https://user-images.githubusercontent.com/76422688/201467434-6a22ef5c-6fe1-4d33-9ad1-ecf69595361f.png">

Finally , we connect each point and from a sphere which contain lots of triangle

<img width="447" alt="截屏2022-11-10 下午8 11 03" src="https://user-images.githubusercontent.com/76422688/201467507-15d8ff3d-c771-4315-884a-c1cef87f0ca6.png">

## How achieve shader
Now , we take a triangle from this sphere
<img width="549" alt="截屏2022-11-10 下午8 44 58" src="https://user-images.githubusercontent.com/76422688/201467596-7cfa9d34-ff10-4522-9a75-2a1fc879aede.png">

We must know the normal of this triangle 
this triangle contain three points
we can use three points to from two line equation

```
line1=point1+λ(point1-point2)
line2=point2+μ(point3-point2)
```
So we can use two direction vectors to from a normal
x is Cross product
```
normal=(point1-point2)x(point3-point2)
```
The red bar is the normal of the triangle

<img width="549" alt="截屏2022-11-10 下午8 49 34" src="https://user-images.githubusercontent.com/76422688/201467928-1726fc48-a45d-4b19-b139-206c0f0f95c4.png">

We set the sun light is the yellow bar and it is a displacement vector
We must know the angle between two bar
<img width="549" alt="截屏2022-11-10 下午8 50 13" src="https://user-images.githubusercontent.com/76422688/201468032-7db507ce-67dd-4d18-b957-f93c6e74b495.png">

the formular is （. is Dot Product）
```
cosϴ=(vector1 . vector2)/(|vector1|*|vector2|)
```


Different triangle have different normal 
We can use the different angle  between normal and sun light to determine the intensity of light

<img width="549" alt="截屏2022-11-10 下午8 54 34" src="https://user-images.githubusercontent.com/76422688/201468254-fa4f6a8a-ab65-435d-94f8-ae5111623cc7.png">




