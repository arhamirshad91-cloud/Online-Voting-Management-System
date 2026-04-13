from datetime import datetime

voters = {}

candidates = {
    1: "Imran Khan",
    2: "Fawad Chaudhry",
    3: "Hafiz Naeem"
}

votes = {
    "Imran Khan": 0,
    "Fawad Chaudhry": 0,
    "Hafiz Naeem": 0
}


def register():
    print("\n--- Voter Registration ---")
    voter_id = input("Enter Voter ID: ").strip()

    if voter_id == "":
        print("Voter ID cannot be empty.")
        return

    if voter_id in voters:
        print("Voter already registered.")
        return

    try:
        age = int(input("Enter Age: "))
        if age < 18:
            print("You must be 18 or above to register.")
            return
    except ValueError:
        print("Invalid age.")
        return

    password = input("Create Password: ")

    voters[voter_id] = {
        "password": password,
        "age": age,
        "voted": False,
        "vote_to": None,
        "vote_time": None
    }

    print("Registration successful!")


def login():
    print("\n--- Voter Login ---")
    voter_id = input("Enter Voter ID: ")
    password = input("Enter Password: ")

    if voter_id not in voters:
        print("Voter not registered.")
        return

    if voters[voter_id]["password"] != password:
        print("Incorrect password.")
        return

    if voters[voter_id]["voted"]:
        print("You have already voted.")
        return

    vote(voter_id)


def vote(voter_id):
    print("\n--- Candidates List ---")
    for key, name in candidates.items():
        print(f"{key}. {name}")

    try:
        choice = int(input("Enter candidate number: "))
    except ValueError:
        print("Invalid input.")
        return

    if choice in candidates:
        candidate = candidates[choice]
        votes[candidate] += 1

        voters[voter_id]["voted"] = True
        voters[voter_id]["vote_to"] = candidate
        voters[voter_id]["vote_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print("Vote cast successfully!")
    else:
        print("Invalid choice.")


def results():
    print("\n--- Voting Results ---")
    for candidate, count in votes.items():
        print(f"{candidate}: {count} votes")


def voter_report():
    print("\n--- Voter Report ---")
    for vid, data in voters.items():
        print("------------------------")
        print("Voter ID :", vid)
        print("Age :", data["age"])
        print("Voted :", data["voted"])
        print("Vote To :", data["vote_to"])
        print("Time :", data["vote_time"])


while True:
    print("\n===== ONLINE VOTING SYSTEM =====")
    print("1. Register")
    print("2. Login & Vote")
    print("3. View Results")
    print("4. Voter Report (Admin)")
    print("5. Exit")

    option = input("Enter your choice: ")

    if option == "1":
        register()
    elif option == "2":
        login()
    elif option == "3":
        results()
    elif option == "4":
        voter_report()
    elif option == "5":
        print("Thank you for using the system.")
        break
    else:
        print("Invalid option.")
