#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <time.h>

void print_some_cake(void);

int main(int argc, char *argv[])
{
  srand(time(NULL));

  int temp;
  do {
    printf("hello\n");
    printf("Choose 1 - 3\n");
    printf("input the number: ");
    if (scanf("%d", &temp) == EOF) {
      printf("\nEnd of input detected. exiting.\n");
      exit(0);
    };

    switch (temp) {
      case 1:
        print_some_cake();
        break;
      default:
        printf("thanks for playing\n");
        exit(0);
    }
  } while (temp < 5 && temp > 0);
  return 0;
}

void print_some_cake(void) {
  char *cakes[] = {"Blueberry", "Strawberry", "Chocolate", "Puff", "Vanilla"};
  int random_index = rand() % 5;

  printf("pointer cakes: %p\n", &cakes[random_index]); // the pointer of where the data in array
  printf("pointer cakes: %p\n", cakes[random_index]); // pointer of where the string
  printf("Random cakes: %s\n", cakes[random_index]);
}
