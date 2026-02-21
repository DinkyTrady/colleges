#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void) {
  string s = get_string("Before : ");
  printf("After  : ");

  for (int i = 0, n = strlen(s); i < n; i++) {
    // not use ctype.h
    // if (s[i] >= 'a' && s[i] <= 'z') {
    //   // Change s[i] to uppercase
    //   printf("%c", s[i] - 32);
    // } else {
    //   // Just print s[i]
    //   printf("%c", s[i]);
    // }
    // use ctype.h
    printf("%c", toupper(s[i]));
  }
  printf("\n");

  return 0;
}
