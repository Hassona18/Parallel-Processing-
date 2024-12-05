import threading


class BankAccount:
    def _init_(self, balance):  # Constructor accepts 'balance'
        self.balance = balance
        self.lock = threading.Lock()  # Lock for thread safety

    def transfer(self, amount, thread_name):
        with self.lock:  # Ensure thread-safe operation
            if self.balance >= amount:
                print(f"{thread_name}: Transferring ${amount}")
                self.balance -= amount
                print(
                    f"{thread_name}: Transfer complete. Remaining balance: ${self.balance}"
                )
            else:
                print(f"{thread_name}: Insufficient funds for ${amount}")


def bank_thread(account, amount, thread_name):
    account.transfer(amount, thread_name)


# Create an instance of BankAccount with an initial balance
account = BankAccount(500)

# Create threads for bank transactions
t1 = threading.Thread(target=bank_thread, args=(account, 300, "Thread-1"))
t2 = threading.Thread(target=bank_thread, args=(account, 300, "Thread-2"))

# Start the threads
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()
