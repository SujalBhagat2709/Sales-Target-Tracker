"""
Sales Target Studio
-------------------
Main file for Sales Target Tracker.
"""

from sales_target_tracker import SalesTargetTracker


class SalesTargetStudio:

    def __init__(self):

        self.tracker = SalesTargetTracker()

    # ----------------------------------
    # Add Record
    # ----------------------------------
    def add_record(self):

        print("\n========== ADD SALES RECORD ==========\n")

        month = input("Month: ").strip()

        target = float(
            input("Sales Target: ")
        )

        actual = float(
            input("Actual Sales: ")
        )

        record = self.tracker.add_record(
            month,
            target,
            actual
        )

        print("\nSales Record Added Successfully.")

        self.tracker.display_record(record)

    # ----------------------------------
    # View Sales Report
    # ----------------------------------
    def view_report(self):

        self.tracker.display_records()

    # ----------------------------------
    # View Summary
    # ----------------------------------
    def view_summary(self):

        self.tracker.display_summary()

    # ----------------------------------
    # Best Month
    # ----------------------------------
    def best_month(self):

        record = self.tracker.best_month()

        if record:

            print("\n========== BEST PERFORMING MONTH ==========\n")

            self.tracker.display_record(record)

        else:

            print("\nNo sales records available.")

    # ----------------------------------
    # Menu
    # ----------------------------------
    def menu(self):

        while True:

            print("\n" + "=" * 55)
            print("          SALES TARGET TRACKER")
            print("=" * 55)
            print("1. Add Sales Record")
            print("2. View Sales Report")
            print("3. View Summary")
            print("4. Best Performing Month")
            print("5. Exit")

            choice = input("\nEnter Choice: ").strip()

            if choice == "1":

                self.add_record()

            elif choice == "2":

                self.view_report()

            elif choice == "3":

                self.view_summary()

            elif choice == "4":

                self.best_month()

            elif choice == "5":

                print("\nThank you for using Sales Target Tracker.")
                break

            else:

                print("\nInvalid choice. Please try again.")


# ----------------------------------
# Main
# ----------------------------------

if __name__ == "__main__":

    studio = SalesTargetStudio()

    studio.menu()