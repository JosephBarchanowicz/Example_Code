%Written By: Joe Barchanowicz
%Curve Fitting Exponential Function

x = [ 0; 1; 2; 3; 5];
y = [2.1; 3.3; 5.4; 8.9; 24.4];

X=x
Y= log(y)

a = polyfit(X, Y, 1)

A = a(1)
c = exp(a(2))

stem(x, y)
title('Exponential Fit to Raw Data')
hold on 
%plot(x, c*exp(A*x))
x_dense = 0:.1: 5;
plot(x_dense, c*exp(A*x_dense),'r-')


