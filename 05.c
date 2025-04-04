#include <stdio.h>
#include <string.h>
int main(){
    char nome[50];
    int idade, mes;

    printf("Digite seu nome ");
    scanf("%s", nome);

    printf("Quantos anos você tem? ");
    scanf("%d", &idade);

    printf("Qual o número do mês que você nasceu? (ex: 1, 2, 10): ");
    scanf("%d", &mes);

  
    if ((idade > 18) && (mes > 6)) {
        printf("Você é maior de idade e nasceu após junho.\n");
    } else if ((idade < 18) && (mes > 6)) {
        printf("Você é menor de idade e nasceu após junho.\n");
    } else if ((idade > 18) && (mes < 6)) {
        printf("Você é maior de idade e nasceu antes de junho.\n");
    } else if ((idade < 18) && (mes < 6)) {
        printf("Você é menor de idade e nasceu antes de junho.\n");
    } else {
        printf("Você tem exatamente 18 anos ou nasceu em junho.\n");
    }

 return 0;
}
