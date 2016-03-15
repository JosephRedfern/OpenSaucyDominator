image = imread('/Users/joe/dom.png');
image = im2double(rgb2gray(image));
orig = imread('/Users/joe/dom_img.jpg');
image = imresize(im2double(image), 0.5);
%image = imrotate(image, 0);

cc = bwconncomp(image);

main_region = false(size(image));
idx = 1;
main_region(cc.PixelIdxList{idx}) = true;

edges = edge(main_region);

%sc(edges);

[H, theta, rho] = hough(edges, 'RhoResolution',0.5,'ThetaResolution',0.5);

peaks = houghpeaks(H)

theta(peaks(2));

rotated = imrotate(main_region, theta(peaks(2)));
rotated_orig = imrotate(orig, theta(peaks(2)));

sc(main_region);
figure(2);
sc(rotated);

div_width = 28;
div_height = 44;

dxmin_e = inf;
dymin_e = inf;
min_e = inf;

for dy = 1:1.2*div_height
    J = imtranslate(rotated,[0, dy],'FillValues',0,'OutputView','full');
    im = blockfun(J, [div_width div_height], @quanterror);
    sc(im);
    drawnow;
    total_error = sum(im(:));
    if total_error < min_e
        min_e = total_error;
        dymin_e = dy;
    end
    sprintf('Total error for dy: %d: %d', dy, total_error)
end

min_e = inf;
E=[];
for dx = 1:1.2*div_width
    J = imtranslate(rotated,[dx, 0],'FillValues',0,'OutputView','full');
    im = blockfun(J, [div_width div_height], @quanterror);
    sc(im);
    drawnow;
    total_error = sum(im(:));
    E(end+1)=total_error;
    if total_error < min_e
        min_e = total_error;
        dxmin_e = dx;
    end
    sprintf('Total error for dx: %d: %d', dx, total_error)
end

figure(3)
plot(E)

dxmin_e
dymin_e

J = imtranslate(rotated,[dxmin_e, dymin_e],'FillValues',0,'OutputView','full');
im = blockfun(J, [div_width div_height], @quanterror);
figure(4);
sc(im);
drawnow;
total_error = sum(im(:));
sprintf('Total error for dx: %d, dy: %d: %d', dxmin_e, dymin_e, total_error)

translated = imtranslate(rotated,[dxmin_e, dymin_e],'FillValues',0,'OutputView','full');

figure(5);
sc(im);

rotated(dxmin_e:div_height:end,:,:) = 255;       %# Change every tenth row to black
rotated(:,dymin_e:div_width:end,:) = 255;       %# Change every tenth column to black

rotated_orig(dxmin_e:div_height:end,:,:) = 255;
rotated_orig(:,dymin_e:div_width:end,:) = 255;  

figure(6);
sc(rotated);
%figure(7);
%sc(rotated_orig);

%imshow(main_region);