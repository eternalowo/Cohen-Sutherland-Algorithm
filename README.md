<h1>Cohen-Sutherland Algorithm</h1>

The algorithm divides the plane into 9 parts by straight lines that form the sides of the rectangle. Each of the 9 parts is assigned a four-bit code. The bits (from the youngest to the oldest) mean "to the left", "to the right", "below", "above". In other words, the three parts of the plane to the left of the rectangle have the lowest bit equal to 1, and so on.

The algorithm determines the code of the segment ends. If both codes are zero, then the segment is completely in the rectangle. If the bitwise AND of the codes is not zero, then the segment does not intersect the rectangle (since this means that both ends of the segment are on the same side of the rectangle). In other cases, the algorithm selects the end of the segment (or one of the ends) that has a non-zero code (that is, located outside the rectangle), finds the nearest intersection point of the segment with one of the straight lines forming the sides of the rectangle, and uses this intersection point as the new end of the segment. The shortened segment is passed through the algorithm again.



![Screenshot_1](https://user-images.githubusercontent.com/98911288/204525729-5ef441fc-6ad6-484e-8b0e-407e48895124.png)


<h3>Some tests: </h3>

<h4>Line is completely inside the rectangle</h4>
![image](https://user-images.githubusercontent.com/98911288/204526227-4b29c2d4-a3ab-4232-9d89-ffa2936717c1.png)

![image](https://user-images.githubusercontent.com/98911288/204526168-1a87b54b-74b7-41ed-9b92-397288aa036e.png)
