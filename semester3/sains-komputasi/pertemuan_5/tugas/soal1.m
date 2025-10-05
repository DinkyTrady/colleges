t = linspace(0, 10*pi, 1000)

# Pendefinisian z
z = t;

# menentukan nilai lintasan 1
x1 = cos(t);
y1 = sin(t);

# menentukan nilai lintasan 2
x2 = cos(t);
y2 = -sin(t);

% Plotting
figure;

plot3(x1, y1, z, 'b', 'LineWidth', 2); # Lintasan 1
hold on;
plot3(x2, y2, z, 'r', 'LineWidth', 2); # Lintasan 2
hold off;
title('Helix ganda 3D');
legend('Lintasan 1', 'Lintasan 2');
xlabel('Sumbu X');
ylabel('Sumbu Y');
zlabel('Sumbu Z');
grid on;
axis equal;
