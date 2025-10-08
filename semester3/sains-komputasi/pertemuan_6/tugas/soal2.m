a = 2;
b = 3;

gam_a = gamma(a);
gam_b = gamma(b);
gam_hasil = gamma(a + b);
verif = ((gam_a * gam_b) / gam_hasil);

fprintf('hasil gamma dari variable a = %f, b = %f, dan hasil = %f\n', gam_a, gam_b, gam_hasil);
fprintf('jadi hasil verifikasi %f\n', verif);
