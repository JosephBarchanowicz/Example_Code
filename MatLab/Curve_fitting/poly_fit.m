x = [0 1 3 4], y =[-1 2 2 5]
Pn = polyfit(x, y, 1)
new_y = polyval(Pn, x)

stem(x, y)
hold on
plot(x,new_y)

errors_sq = (y-new_y).^2
E2 = sum(errors_sq)