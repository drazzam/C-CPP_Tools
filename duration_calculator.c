#include <stdio.h>
// Made By Ahmed Y. Azzam!
// Enjoy It!

/*
 * This function calculates the number of years, months, and days
 * between two dates.
 *
 * @param year1 The year of the first date
 * @param month1 The month of the first date
 * @param day1 The day of the first date
 * @param year2 The year of the second date
 * @param month2 The month of the second date
 * @param day2 The day of the second date
 * @param years The number of years between the two dates (output)
 * @param months The number of months between the two dates (output)
 * @param days The number of days between the two dates (output)
 */
void date_diff(int year1, int month1, int day1, int year2, int month2, int day2, int *years, int *months, int *days) {
  // Calculate the number of years
  *years = year2 - year1;

  // Calculate the number of months
  *months = month2 - month1;
  if (*months < 0) {
    // If the number of months is negative, reduce the number of years by 1
    // and add 12 months to the number of months
    *years -= 1;
    *months += 12;
  }

  // Calculate the number of days
  *days = day2 - day1;
  if (*days < 0) {
    // If the number of days is negative, reduce the number of months by 1
    // and add the number of days in the previous month to the number of days
    *months -= 1;
    *days += 30; // Assume all months have 30 days for simplicity
  }
}

int main() {
  int year1, month1, day1, year2, month2, day2;
  int years, months, days;

  // Prompt the user for the first date
  printf("Enter The First Date (YYYY MM DD): ");
  scanf("%d %d %d", &year1, &month1, &day1);

  // Prompt the user for the second date
  printf("Enter The Second Date (YYYY MM DD): ");
  scanf("%d %d %d", &year2, &month2, &day2);

  // Calculate the number of years, months, and days between the two dates
  date_diff(year1, month1, day1, year2, month2, day2, &years, &months, &days);

  // Print the result
  printf("\nThe Duration Between The Two Dates: \n");
  printf("-----------------\n Years: %d\n Months: %d\n Days: %d\n-----------------\n", years, months, days);

  return 0;
}
