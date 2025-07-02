# 🚚 GatorGlide Delivery System – AVL Tree Based Order Manager

**Course:** COP 5536 - Data Structures and Algorithms  
**Project:** GatorGlide Delivery System  
**Language:** Python  
**Due Date:** April 3, 2024

---

## 📌 Description

This project simulates a real-world logistics system for GatorGlide Delivery Co. using **AVL trees** to manage order priorities and Estimated Time of Arrivals (ETAs). The system allows for real-time order creation, cancellation, searching, ranking, and delivery tracking.

Two AVL trees are used:
- One for managing **order priorities**
- One for managing **ETAs** of undelivered orders

Each order is ranked and scheduled based on a computed priority:
```
priority = 0.3 * (orderValue / 50) - 0.7 * orderCreationTime
```

The system also adjusts ETAs dynamically as new orders are added or canceled.

---

## 📂 Project Structure

```
Garg_Mayank/
├── avlTree.py              # AVL tree logic for order priority & ETA tracking
├── gatorDelivery.py        # Main order management system
├── testcase1.txt           # Test case file 1
├── testcase2.txt           # Test case file 2
├── testcase3.txt           # Test case file 3
├── Run.txt                 # Instructions or sample inputs
├── Report.pdf              # Project report
```

---

## 💡 Features

- AVL-based dynamic rebalancing for order priority and ETA updates
- Supports operations:
  - `createOrder`
  - `cancelOrder`
  - `print(orderId)` / `print(time1, time2)`
  - `getRankOfOrder(orderId)`
- Auto-updates ETAs for affected orders on any modification
- Prevents disruption from duplicate or outdated orders

---

## 🧪 How to Run

1. Ensure Python 3 is installed.
2. Run the main file:
   ```bash
   python gatorDelivery.py
   ```
3. Follow instructions or use test inputs from `Run.txt` or `testcase*.txt`.

---

## 🛠 Technologies Used

- Python 3.x
- Self-balanced Binary Search Trees (AVL)
- Command-line I/O

---

## 👨‍💻 Author

Mayank Garg  
University of Florida  
COP 5536 – Spring 2024
