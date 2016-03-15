function im = bwdownsample(im, tgt)

factor = floor(log(nnz(im) / tgt) / log(4));
if factor < 1
    return
end
bs = 2^factor;
padw = mod(size(im, 2), bs);
if padw
    im = [im repmat(im(:, end), 1, padw)];
end
padh = mod(size(im, 1), bs);
if padh
    im = [im; repmat(im(end, :), padh, 1)];
end

im = blockfun(im, [bs bs], @sum) >= (bs * bs / 2);
