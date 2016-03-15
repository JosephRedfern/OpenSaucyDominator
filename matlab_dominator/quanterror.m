function [ error ] = quanterror( x )
%QUANTERROR Summary of this function goes here
%   Detailed explanation goes here
    n = numel(x);
    nonzero = nnz(x);
    
    if nonzero > 0.5*n
        error = abs(x-1);
        error = sum(error(:));
    else
         error = abs(x);
        error = sum(error(:));
  
    end

error = error / n;
end

