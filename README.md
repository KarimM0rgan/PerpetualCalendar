# 📅 Perpetual Calendar

> A Python-based calendar utility that calculates the day of the week for any date, detects leap years, determines the day number within the year, and finds the date of Thanksgiving — all without relying on external libraries.

---

## 📌 Project Overview

This **Perpetual Calendar** program allows users to input any date and learn:
- The day of the week it falls on
- What number day of the year it is
- Whether it was a leap year
- When Thanksgiving occurred that year
- The weekday that date would fall on in 2020

Built entirely in Python without external dependencies, this project demonstrates how core date and time calculations can be achieved manually through logical operations and modular arithmetic.

---

## 🧠 Features

- 🗓️ **Day of the Week** — Calculates the weekday for any date (e.g., March 14, 2025 → Friday).
- 📆 **Day Number** — Determines how many days into the year a date falls.
- 🔁 **Leap Year Detection** — Identifies whether a given year is a leap year.
- 🦃 **Thanksgiving Calculator** — Computes the correct date of Thanksgiving (4th Thursday of November).
- 🔁 **Compare with 2020** — Displays what weekday the same date fell on in the year 2020.

---

## 🧪 Example Output

```text
Pick any date! (Maybe your birthday)
Enter a month (1-12): 11
Enter a day (1-31): 23
Enter a year: 2023

This is day number 327 of the year.
This day falls on a Thursday
In 2020, this date falls on a Monday
In 2023, New Year's day falls on a Sunday
Thanksgiving falls on the 23 of that year
Do you want to keep going? (y or n)
````

---

## 🛠️ How It Works

* **Leap Year Logic:**
  A year is a leap year if it is divisible by 4, unless it’s divisible by 100, *except* if it’s also divisible by 400.

* **Day-of-Year Calculation:**
  Uses a hard-coded cumulative day count before each month to determine how far into the year a date falls, with leap-year adjustments after February.

* **Day of Week:**
  Uses Zeller-like congruences and modular arithmetic to compute weekdays without using `datetime`.

* **Thanksgiving Date:**
  Starts at Nov 1st and moves to the fourth Thursday of the month dynamically based on the weekday.

---

## 🎓 Educational Purpose

This project was created as part of an academic assignment focused on deepening understanding of calendar algorithms, conditionals, modular math, and function design in Python.

---