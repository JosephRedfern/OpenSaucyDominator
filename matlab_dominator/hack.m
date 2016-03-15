dom_img = rgb2gray(imread('/Users/joe/Downloads/IMG_4589.JPG'));

dom = ~im2bw(dom_img);

sc(dom);
figure

dom = imrotate(dom, 30);

filled_dom = bwfill(dom, 'holes');
sc(filled_dom);

cc = bwconncomp(filled_dom);

s = regionprops(filled_dom, 'BoundingBox');
cropped = imcrop(dom, s(1).BoundingBox);
[r, c] = find(dom);

X = [r(:) c(:)]';
[u, l, av] = pca(X);
u
l

angle = rad2deg(atan2(u(1,1), u(1,2)))

cropped = imrotate(cropped, angle);
sc(cropped);
s = regionprops(bwfill(cropped, 'holes'), 'BoundingBox')
cropped = ~imcrop(cropped, s(2).BoundingBox);

ls = cropped(:, 1:floor(size(cropped, 2)/2));
rs = cropped(:, ceil(size(cropped, 2)/2):end);

figure;
sc(ls);
figure;
sc(rs);

blankls = length(find(ls==false))
filledls = length(find(ls==true))

blankrs = length(find(rs==false))
filledrs = length(find(rs==true))

sprintf('Left Side Ratio: %d', blankls/filledls)
sprintf('Right Side Ratio: %d', blankrs/filledrs)

figure;
sc(cropped);