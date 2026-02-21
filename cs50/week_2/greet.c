#include <cs50.h>
#include <stdio.h>

// int main(void)
// {
//   string answer = get_string("What's is your name? ");
//   printf("Hello, %s\n", answer);
//   return 0;
// }

int main(int argc, string argv[])
{
  // printf("Hello, %s", argv[1]);
  // if (argc >= 2) {
  //   printf("Hello, %s", argv[1]);
  // } else {
  //   printf("Hello World!");
  // }
  for (int i = 0; i < argc; i++) {
    printf("%s\n", argv[i]);
  }
  return 0;
}
