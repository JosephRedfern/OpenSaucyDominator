im = im2double(imread('dominoes.png'));

% im = imrotate(im, 30, 'crop');

im = imresize(im, 0.25, 'nearest');
[h, w] = size(im);
[imX, imY] = meshgrid(1:w, 1:h);
imX = imX(:);
imY = imY(:);

N = 2;
[imy, imx] = find(im);
cx = imx(11000); cy = imy(100); a = deg2rad(100); s = 32;

% im = ones(256, 256);


rect = [cx cy a];
% inside = points_in_rectangle(imX, imY, rect);

% im(inside) = im(inside) + 1;
% figure(1); sc(im);
opt = optimset('display', 'iter');
[rect, fval] = fminsearch(@(x) rectobjfn(im, imX, imY, x), rect, opt);
    
