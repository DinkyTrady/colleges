% Definisi variable
n = 200;
x = randn(n, 1);
y = randn(n, 1);
z = randn(n, 1);

% Plotting
figure;
scatter3(x, y, z, 'filled');
xlabel('X');
ylabel('Y');
zlabel('Z');
title('Sebaran Titik Acak (Distribusi Normal)');
grid on;

% vim:ft=matlab
