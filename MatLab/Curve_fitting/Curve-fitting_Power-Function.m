%Written By: Joe Barchanowicz
%Curve Fitting Power Function

x = [1; 2; 3; 4; 5]
y = [4; 20; 50; 97; 162]

%X=x
X= log(x)
Y= log(y)
Pn = polyfit(X, Y, 1)

A = Pn(1)
B = Pn(2);
c = exp(Pn(2))

stem(x, y)
title('Best Fit to Raw Data')
hold on
xdense = .1:.1: 5;
plot(xdense, c*xdense.^A,'r-')
