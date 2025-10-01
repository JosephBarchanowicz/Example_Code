%Written By: Joe Barchanowicz
%Gaussian Elimination 

function D = gauss_elim_V3(A)

I = 2;
K = 1;

N = length(A);
M = size(A,1);

for k = K:N-1
    for i = I:M
        if A(k,k) == 0
            %Row swapping
            j = k;
            while j <= M
                temp = A(K, K:N);
                A(K, K:N) = A(K+1, K:N);
                A(K+1, K:N) = temp;
                j=j+1;
            end
        end
        lambda = A(i, k)/A(k, k);
        if lambda ~= 0 
            A(i, k:N) = A(i,k:N) - lambda * A(k, k:N);
        end
    end
    I = I +1;
    K = K +1;
end

Pre_Back_Sub_A_b = A

P = length(A);
b = A(:,P);
A(:,P) = [];
P = length(A);
Q = size(A,1);

%solve initial equation
b(Q) = b(Q)/A(P,Q);

for i = Q-1:-1:1
    count = 0;
   for g = P:-1:i+1
       if count == 0
           c =  -1*(A(i,g)* b(g));
       else
           c = -1*(A(i,g)* b(g)) + c;
       end
       count = count + 1;
   end
   b(i) = (b(i) + c)/A(i,i);
end
Ak_bk = [A b]
end

