"""
Sales Target Tracker
--------------------
File: sales_target_tracker.py

Features
--------
✔ Add Monthly Sales Record
✔ Monthly Sales Target
✔ Actual Sales
✔ Achievement Percentage
✔ Remaining Target
✔ Monthly Status
✔ Best Performing Month
✔ Sales Summary
"""

class SalesTargetTracker:

    def __init__(self):

        self.records = []

    # ----------------------------------
    # Achievement Percentage
    # ----------------------------------
    def achievement_percentage(self,
                               target,
                               actual):

        if target == 0:
            return 0

        return round((actual / target) * 100, 2)

    # ----------------------------------
    # Remaining Target
    # ----------------------------------
    def remaining_target(self,
                         target,
                         actual):

        if actual >= target:
            return 0

        return target - actual

    # ----------------------------------
    # Monthly Status
    # ----------------------------------
    def monthly_status(self,
                       target,
                       actual):

        if actual >= target:
            return "Target Achieved"

        elif actual >= target * 0.80:
            return "Near Target"

        return "Below Target"

    # ----------------------------------
    # Add Sales Record
    # ----------------------------------
    def add_record(self,
                   month,
                   target,
                   actual):

        achievement = self.achievement_percentage(
            target,
            actual
        )

        remaining = self.remaining_target(
            target,
            actual
        )

        status = self.monthly_status(
            target,
            actual
        )

        record = {

            "Month": month,
            "Target": target,
            "Actual Sales": actual,
            "Achievement %": achievement,
            "Remaining Target": remaining,
            "Status": status

        }

        self.records.append(record)

        return record

    # ----------------------------------
    # Total Target
    # ----------------------------------
    def total_target(self):

        return sum(
            item["Target"]
            for item in self.records
        )

    # ----------------------------------
    # Total Sales
    # ----------------------------------
    def total_sales(self):

        return sum(
            item["Actual Sales"]
            for item in self.records
        )

    # ----------------------------------
    # Best Month
    # ----------------------------------
    def best_month(self):

        if not self.records:
            return None

        return max(
            self.records,
            key=lambda item:
            item["Achievement %"]
        )

    # ----------------------------------
    # Sales Summary
    # ----------------------------------
    def summary(self):

        total_target = self.total_target()

        total_sales = self.total_sales()

        achievement = self.achievement_percentage(
            total_target,
            total_sales
        )

        return {

            "Total Months":
                len(self.records),

            "Total Target":
                total_target,

            "Total Sales":
                total_sales,

            "Overall Achievement %":
                achievement

        }

    # ----------------------------------
    # Display Record
    # ----------------------------------
    def display_record(self,
                       record):

        print("\n========== SALES RECORD ==========\n")

        for key, value in record.items():

            print(f"{key:<22}: {value}")

    # ----------------------------------
    # Display All Records
    # ----------------------------------
    def display_records(self):

        if not self.records:

            print("\nNo sales records available.")

            return

        print("\n========== SALES REPORT ==========\n")

        for index, record in enumerate(
                self.records,
                start=1):

            print(f"Month {index}")

            print("-" * 40)

            for key, value in record.items():

                print(f"{key:<22}: {value}")

            print()

    # ----------------------------------
    # Display Summary
    # ----------------------------------
    def display_summary(self):

        report = self.summary()

        print("\n========== SUMMARY ==========\n")

        for key, value in report.items():

            print(f"{key:<25}: {value}")


# ----------------------------------
# Example
# ----------------------------------

if __name__ == "__main__":

    tracker = SalesTargetTracker()

    while True:

        print("\n1. Add Sales Record")
        print("2. View Sales Report")
        print("3. View Summary")
        print("4. Best Performing Month")
        print("5. Exit")

        choice = input("\nEnter Choice: ")

        if choice == "1":

            month = input(
                "Month: "
            )

            target = float(
                input(
                    "Sales Target: "
                )
            )

            actual = float(
                input(
                    "Actual Sales: "
                )
            )

            record = tracker.add_record(
                month,
                target,
                actual
            )

            tracker.display_record(record)

        elif choice == "2":

            tracker.display_records()

        elif choice == "3":

            tracker.display_summary()

        elif choice == "4":

            best = tracker.best_month()

            if best:

                print("\n========== BEST MONTH ==========\n")

                tracker.display_record(best)

            else:

                print("\nNo records available.")

        elif choice == "5":

            print(
                "\nThank you for using Sales Target Tracker."
            )

            break

        else:

            print("\nInvalid choice.")