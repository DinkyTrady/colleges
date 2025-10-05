n = -5:0.5:5;
[X, Y] = meshgrid(n, n);
Z = sqrt(X.^2 + Y.^2);
figure(2);
surf(X, Y, Z);
title('Permukaan 3D fungsi z = sqrt(x^2 + Y^2)');
xlabel('Sumbu X');
ylabel('Sumbu Y');
zlabel('Sumbu Z');
axis equal;

% vim:ft=matlab
