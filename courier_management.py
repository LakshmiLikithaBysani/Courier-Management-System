print("📦 Courier Management System")

couriers = []

while True:
    print("\n1. Add Courier")
    print("2. View Couriers")
    print("3. Search Courier")
    print("4. Update Courier Status")
    print("5. Delete Courier")
    print("6. Count Couriers")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # Add Courier
    if choice == "1":
        courier_id = input("Enter courier ID: ")
        sender = input("Enter sender name: ")
        receiver = input("Enter receiver name: ")
        destination = input("Enter destination: ")

        courier = {
            "id": courier_id,
            "sender": sender,
            "receiver": receiver,
            "destination": destination,
            "status": "Booked"
        }

        couriers.append(courier)

        print("✅ Courier added successfully!")

    # View Couriers
    elif choice == "2":
        if len(couriers) == 0:
            print("❌ No couriers found.")
        else:
            print("\n📋 Courier Details")
            print("--------------------------")

            for courier in couriers:
                print("Courier ID:", courier["id"])
                print("Sender:", courier["sender"])
                print("Receiver:", courier["receiver"])
                print("Destination:", courier["destination"])
                print("Status:", courier["status"])
                print("--------------------------")

    # Search Courier
    elif choice == "3":
        search_id = input("Enter courier ID to search: ")

        found = False

        for courier in couriers:
            if courier["id"] == search_id:
                print("\n✅ Courier Found")
                print("Courier ID:", courier["id"])
                print("Sender:", courier["sender"])
                print("Receiver:", courier["receiver"])
                print("Destination:", courier["destination"])
                print("Status:", courier["status"])
                found = True

        if not found:
            print("❌ Courier not found.")

    # Update Status
    elif choice == "4":
        update_id = input("Enter courier ID: ")

        found = False

        for courier in couriers:
            if courier["id"] == update_id:
                print("\n1. Booked")
                print("2. Shipped")
                print("3. Out for Delivery")
                print("4. Delivered")

                status_choice = input("Choose new status: ")

                if status_choice == "1":
                    courier["status"] = "Booked"
                elif status_choice == "2":
                    courier["status"] = "Shipped"
                elif status_choice == "3":
                    courier["status"] = "Out for Delivery"
                elif status_choice == "4":
                    courier["status"] = "Delivered"
                else:
                    print("❌ Invalid status!")
                    break

                print("✅ Courier status updated!")
                found = True
                break

        if not found:
            print("❌ Courier not found.")

    # Delete Courier
    elif choice == "5":
        delete_id = input("Enter courier ID to delete: ")

        found = False

        for courier in couriers:
            if courier["id"] == delete_id:
                couriers.remove(courier)
                print("✅ Courier deleted successfully!")
                found = True
                break

        if not found:
            print("❌ Courier not found.")

    # Count Couriers
    elif choice == "6":
        print("📦 Total Couriers:", len(couriers))

    # Exit
    elif choice == "7":
        print("Thank you for using Courier Management System! 📦")
        break

    else:
        print("❌ Invalid choice!")
