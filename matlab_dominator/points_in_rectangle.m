function inside = points_in_rectangle(x, y, rect)

cx = rect(1);
cy = rect(2);
a = rect(3);
% s = rect(4);
s = 18;

R = [cos(a) -sin(a); sin(a) cos(a)];
rect = [s s -s;
        s/2 -s/2 s/2];
rect = R * rect;
rect(1, :) = rect(1, :) + cx;
rect(2, :) = rect(2, :) + cy;
ax = rect(1, 1);
ay = rect(2, 1);
bx = rect(1, 2);
by = rect(2, 2);
dx = rect(1, 3);
dy = rect(2, 3);

bax = bx - ax;
bay = by - ay;
dax = dx - ax;
day = dy - ay;

outside = ((x - ax) * bax + (y - ay) * bay < 0.0) | ...
((x - bx) * bax + (y - by) * bay > 0.0) | ...
((x - ax) * dax + (y - ay) * day < 0.0) | ...
((x - dx) * dax + (y - dy) * day > 0.0);
inside = ~outside;
