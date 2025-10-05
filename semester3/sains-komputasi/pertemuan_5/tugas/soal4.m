n = -5:0.5:5;
[X, Y] = meshgrid(n, n);
Z = sqrt(X.^2 + Y.^2);
figure;

# Plot 1
subplot(1, 2, 1);
surf(X, Y, Z);
title('Sudut pandang default');
xlabel('Sumbu X');
ylabel('Sumbu Y');
zlabel('Sumbu Z');
axis equal;

# Plot 2
subplot(1, 2, 2);
surf(X, Y, Z);
title('Sudut pandang dari atas');
xlabel('Sumbu X');
ylabel('Sumbu Y');
zlabel('Sumbu Z');
axis equal;
view(0, 90);
