def process_atm_sequence(initial_balance, transactions):
    balance = initial_balance
    daily_withdrawn = 0.0
    max_daily_limit = 20000.0
    min_balance = 500.0
    
    logs = []
    
    for tx_type, amount in transactions:
        if amount <= 0:
            logs.append((tx_type, amount, balance, "FAILED: Invalid Amount"))
            continue
            
        if tx_type == "DEPOSIT":
            balance += amount
            logs.append((tx_type, amount, balance, "SUCCESS"))
            
        elif tx_type == "WITHDRAW":
            if daily_withdrawn + amount > max_daily_limit:
                logs.append((tx_type, amount, balance, "FAILED: Exceeds Daily Limit"))
            elif balance - amount < min_balance:
                logs.append((tx_type, amount, balance, "FAILED: Insufficient Balance"))
            else:
                balance -= amount
                daily_withdrawn += amount
                logs.append((tx_type, amount, balance, "SUCCESS"))
                
    return balance, logs

tx_list = [
    ("DEPOSIT", 5000),
    ("WITHDRAW", 8000),
    ("WITHDRAW", 15000), # Exceeds daily limit (8000 + 15000 > 20000)
    ("WITHDRAW", 6000),  # Leaves balance below 500
    ("WITHDRAW", 3000)   # Valid
]

final_bal, log_history = process_atm_sequence(10000, tx_list)

print("--- ATM Transaction Audit Log ---")
for t_type, amt, bal, status in log_history:
    print(f"Tx: {t_type:<8} | Amount: ₹{amt:<7.2f} | Balance: ₹{bal:<8.2f} | Status: {status}")
print(f"Final Closing Balance: ₹{final_bal:.2f}")