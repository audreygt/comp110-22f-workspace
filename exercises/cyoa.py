"""Creating a game called Tech Repair using Comp Questions."""

__author__ = "730545277"


def main() -> None:
    player_name: input = str("What is your name?")
    print(f"Hello {player_name}, this is a game called Tech Repair.\ You currently are working as a tech repair person in the UNC shop.\ To fix the device and add accessories for the device to work, you must answer questions correctly relating to COMP 110 material.")
    FIXING_DEVICE: str = "\U0001F4BB\U0001FAAB"
    print(f"This is the device you will be fixing: {FIXING_DEVICE}.")

if __name__ == "__main__":
    main()
