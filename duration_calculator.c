#include <stdio.h>
#include <string.h>
#include <math.h>
// Made By Ahmed Y. Azzam!
// Enjoy It!

int main (void){
  while(1){
  int day_of_year_1, month_of_year_1, year_1;
  printf("\nEnter The Day: ");
  scanf("%d", &day_of_year_1);
  printf("Enter The Month: ");
  scanf("%d", &month_of_year_1);
  printf("Enter The Year: ");
  scanf("%d", &year_1);
  int day_of_year_2, month_of_year_2, year_2;
  printf("Enter The Day: ");
  scanf("%d", &day_of_year_2);
  printf("Enter The Month: ");
  scanf("%d", &month_of_year_2);
  printf("Enter The Year: ");
  scanf("%d", &year_2);
  int calc_day, calc_month, year_calc, total_days;
  year_calc= (year_2-year_1);
  calc_day= abs(day_of_year_2-day_of_year_1);
  calc_month= abs(month_of_year_2-month_of_year_1);
  total_days= (year_calc*365)+(calc_month*30)+(calc_day);
  printf("-----------------------\n Years: %d \n Months: %d \n Days: %d \n", year_calc, calc_month, calc_day);
  printf(" The Total Number of Days Is: %d\n-----------------------", total_days);
    }
  }
