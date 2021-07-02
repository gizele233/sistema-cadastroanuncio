#include <stdio.h>

float value, view, click, share, reach;

void calculadora(){
  printf("Qual o valor a ser investido\n");
  scanf("%f", &value);

  view = value * 30;
  click = view * 0.12;
  share = click * 0.15 * 4;
  reach = view + (share * 40);
  printf("O alcance do anúncio foi: %f\n de pessoas alcançadas", reach);
}

int main(void) {
  calculadora();
  return 0;
}