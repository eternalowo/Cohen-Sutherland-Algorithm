<h1>Cohen-Sutherland Algorithm</h1>

The algorithm divides the plane into 9 parts by straight lines that form the sides of the rectangle. Each of the 9 parts is assigned a four-bit code. The bits (from the youngest to the oldest) mean "to the left", "to the right", "below", "above". In other words, the three parts of the plane to the left of the rectangle have the lowest bit equal to 1, and so on.

The algorithm determines the code of the segment ends. If both codes are zero, then the segment is completely in the rectangle. If the bitwise AND of the codes is not zero, then the segment does not intersect the rectangle (since this means that both ends of the segment are on the same side of the rectangle). In other cases, the algorithm selects the end of the segment (or one of the ends) that has a non-zero code (that is, located outside the rectangle), finds the nearest intersection point of the segment with one of the straight lines forming the sides of the rectangle, and uses this intersection point as the new end of the segment. The shortened segment is passed through the algorithm again.

<h3>function cohen_sutherland_line_clip(line_first, line_second, rect_min, rect_max):</h3>
Cohen–Sutherland clipping algorithm clips a line from line_first (x, y) to line_second (x, y) against a rectangle with diagonal from rect_min (x, y) to rect_max (x, y) returns True if line were clipped, or it were inside rectangle with coordinates of clipped line and False if line doesn't cross rectangle and coordinates of given line.

<h3>function compute_out_code(point, rect_min, rect_max):</h3>
Compute the bit code for a point (x, y) using the clip rectangle bounded diagonally by rect_min (x, y), and rect_max (x, y)

 

![Screenshot_1](https://user-images.githubusercontent.com/98911288/204525729-5ef441fc-6ad6-484e-8b0e-407e48895124.png)


<h3>Some tests: </h3>

<h4>Line is completely inside the rectangle</h4>


![image](https://user-images.githubusercontent.com/98911288/204526227-4b29c2d4-a3ab-4232-9d89-ffa2936717c1.png)


![image](https://user-images.githubusercontent.com/98911288/204526168-1a87b54b-74b7-41ed-9b92-397288aa036e.png)


<h4>Line crossing one of rectangle sides</h4>

![image](https://user-images.githubusercontent.com/98911288/204528081-77e93d62-0c4a-4064-9418-d05238af8663.png)

![image](https://user-images.githubusercontent.com/98911288/204527909-4dca8515-4b78-415b-96dd-a42b7482fa22.png)

<h4>Line crossing two sides of rectangle</h4>

![image](https://user-images.githubusercontent.com/98911288/204528609-f10eebe8-1fe6-4047-9fd4-b068b56037a8.png)

![image](https://user-images.githubusercontent.com/98911288/204528528-84fd0361-5068-4386-9605-87efbc1a1f73.png)

<h4>Line doesn't cross any of rectangle sides</h4>

![image](https://user-images.githubusercontent.com/98911288/204528907-6eee9b09-6b9c-41a0-8f18-db30ea828802.png)

![image](https://user-images.githubusercontent.com/98911288/204529029-7d122e21-95e8-461d-bc39-1ddb2aa11786.png)
