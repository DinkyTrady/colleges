#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main (void) {
  string s = get_string("Input:  ");
  printf("Output: ");
  
  // using functoin in condition loop is bad design
  // since it will always executing the function
  // while checking the condition
  // for (int i = 0; i < strlen(s); i++) {
  //   printf("%c", s[i]);
  // }
  
  // better: initalize the function output to variable
  // int length = strlen(s);
  for (int i = 0, n = strlen(s); i < n /* length */; i++) {
    printf("%c", s[i]);
  }
  printf("\n");

  return 0;
}
