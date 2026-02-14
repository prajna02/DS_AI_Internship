import time
import random


def display_status(name, total_distance, travelled, battery):
    print("\n==============================")
    print(f"Robot      : {name}")
    print(f"Distance   : {round(travelled, 2)}m / {total_distance}m")
    print(f"Battery    : {battery}%")
    print("==============================")


def main():
    print("===== 🤖 RoboController PRO (Manual + Random) =====")

    name = input("Enter Robot Name: ")
    total_distance = float(input("Enter target distance (meters): "))

    travelled = 0
    battery = 100
    checkpoints = []

    while True:

        display_status(name, total_distance, travelled, battery)

        print("\nChoose Action:")
        print("1. Move Forward")
        print("2. Obstacle Detected")
        print("3. Human Detected")
        print("4. Show Checkpoints")
        print("5. Exit")

        choice = input("Enter option: ")

        # ---------------- MOVE FORWARD ----------------
        if choice == "1":

            if battery <= 0:
                print("⚠ Battery dead! Cannot move.")
                continue

            travelled += 10
            battery -= random.randint(2, 4)   # Random battery usage
            checkpoints.append(f"Moved Forward at {round(travelled,2)}m")
            print("✅ Moving Forward")

        # ---------------- OBSTACLE ----------------
        elif choice == "2":

            if battery <= 0:
                print("⚠ Battery dead! Cannot move.")
                continue

            print("⚠ Obstacle detected!")

            # Random direction automatically chosen
            direction = random.choice(["left", "right"])

            travelled += 5
            battery -= random.randint(4, 6)

            checkpoints.append(
                f"Obstacle avoided → Auto moved {direction.capitalize()} at {round(travelled,2)}m"
            )

            print(f"Robot automatically moved {direction.capitalize()} to avoid obstacle.")

        # ---------------- HUMAN ----------------
        elif choice == "3":
            print("🚨 Human detected! Robot stopping immediately.")
            checkpoints.append("Stopped - Human detected")
            break

        # ---------------- SHOW CHECKPOINTS ----------------
        elif choice == "4":
            print("\n📍 CHECKPOINT LOG:")
            if not checkpoints:
                print("No checkpoints recorded yet.")
            else:
                for i, cp in enumerate(checkpoints, 1):
                    print(f"{i}. {cp}")

        # ---------------- EXIT ----------------
        elif choice == "5":
            print("Exiting RoboController...")
            break

        else:
            print("Invalid choice. Please select 1-5.")

        # ---------------- TARGET CHECK ----------------
        if travelled >= total_distance:
            print("\n🎯 Target Reached Successfully!")
            checkpoints.append("Target Reached")
            break

        time.sleep(1)

    # ---------------- FINAL SUMMARY ----------------
    print("\n===== 🚀 FINAL SUMMARY =====")
    print(f"Robot Name              : {name}")
    print(f"Total Distance Travelled: {round(travelled, 2)}m")
    print(f"Battery Remaining       : {battery}%")

    print("\n📍 Complete Journey Log:")
    if not checkpoints:
        print("No movement recorded.")
    else:
        for i, cp in enumerate(checkpoints, 1):
            print(f"{i}. {cp}")


if __name__ == "__main__":
    main()
