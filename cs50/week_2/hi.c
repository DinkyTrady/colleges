#include <stdio.h>

int main (void) {
  char b[3] = "HI!";

  // even though the array only have 3 length,
  // it still gonna have another 1 length for 0 in memory
  printf("%i %i %i %i", b[0], b[1], b[2], b[3]);

  return 0;
}
