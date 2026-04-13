# 🗳️ Online Voting System (Python)

A simple **command-line based Online Voting System** built using Python. This project demonstrates core programming concepts such as dictionaries, functions, condition handling, and basic user authentication.

---

## Features

* **Voter Registration**

  * Register with Voter ID, age, and password
  * Age validation (18+ only)

* **Secure Login System**

  * Login with Voter ID and password
  * Prevents duplicate voting

* **Voting Functionality**

  * Displays candidate list
  * Allows users to cast vote
  * Records vote time

* **Voting Results**

  * Displays total votes for each candidate

* **Voter Report (Admin)**

  * Shows all registered voters
  * Displays voting status and timestamps

---

## Technologies Used

* **Python 3**
* Built-in modules:

  * `datetime`

---

## Project Structure

```
online-voting-system/
│
├── voting.py      # Main Python program
└── README.md      # Project documentation
```

---


## Sample Workflow

1. Register a new voter
2. Login using credentials
3. Cast your vote
4. View results
5. Admin can check voter report

---

## Limitations

* Data is stored in memory (resets after program ends)
* No database integration
* No encryption for passwords
* Basic command-line interface only

---

## Future Improvements

* Add database (MySQL / SQLite)
* Implement password hashing for security
* Create GUI (Tkinter / Web App)
* Add admin authentication
* Export voting results to file

---

## Author

**Arham Irshad**
Software Developer (Student)

---

## License

This project is open-source and available under the MIT License.

---

## Support

If you like this project, consider giving it a ⭐ on GitHub!
