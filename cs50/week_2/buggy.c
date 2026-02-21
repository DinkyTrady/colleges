#include <stdio.h>

int main(void)
{
  char* lmao = "Hello, World!";
  char mlao[] = "Hello, World!";
  for (int i = 0; i < 3; i++)
  {
    printf("#\n");
  };
  printf("pointer of lmao %p\n", lmao);
  printf("value of lmao %s\n", lmao);

  printf("pointer of mlao %p\n", mlao);
  printf("value of mlao %s\n", mlao);
}
