t = linspace(0, 1, 500)
a = 2;
b = 3;

# f_t = f(t)
f_t = t.^(a-1) .* (1-t).^(b-1);

# plot
figure;
plot(t, f_t, 'b-', 'LineWidth', 2);
hold on;
% beri warna dibawah line
fill(t, f_t, 'c', 'FaceAlpha', 1);

title('Plot fungsi integran')
xlabel('t')
ylabel('f(t) = t^(a-1)(1-t)^(b-1)');
grid on;
legend('f(t)', 'Area = Nilai B(2,3)');
hold off;

