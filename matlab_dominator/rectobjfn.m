function cost = rectobjfn(im, X, Y, rect)

rect
inside = points_in_rectangle(X, Y, rect);
sample = im(inside);
cost = numel(sample) - nnz(sample);

im(inside) = im(inside) + 1;
figure(1); sc(im);
drawnow;
1
