import os

def main():
    print("Welcome to MACWatch")
    print("1. Start ARP Spoofing")
    print("2. Start ARP Spoofing Detection")

    choice = input("Choose an option (1/2): ")
    if choice == "1":
        os.system("python MACWatch/spoof/arp_spoofer.py")
    elif choice == "2":
        os.system("python MACWatch/detect/arp_detector.py")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
