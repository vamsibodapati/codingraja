import java.util.ArrayList;
class Account {
    String accNumber;
    String accType;
    double balance;
    public Account(String accNumber, String accType, double balance) {
        this.accNumber = accNumber;
        this.accType = accType;
        this.balance = balance;
    }
    void deposit(double amount) {
        balance += amount;
        System.out.println("Deposit of " + amount + " successful. New balance: " + balance);
    }

    void withdraw(double amount) {
        if (amount <= balance) {
            balance -= amount;
            System.out.println("Withdrawal of " + amount + " successful. New balance: " + balance);
        } else {
            System.out.println("Insufficient funds");
        }
    }
    void transfer(double amount, Account recipientAccount) {
        if (amount <= balance) {
            balance -= amount;
            recipientAccount.deposit(amount);
            System.out.println("Transfer of " + amount + " successful. New balance: " + balance);
        } else {
            System.out.println("Insufficient funds");
        }
    }
}
class Transaction {
    Account fromAccount;
    Account toAccount;
    double amount;
    String transactionType;
    public Transaction(Account fromAccount, Account toAccount, double amount, String transactionType) {
        this.fromAccount = fromAccount;
        this.toAccount = toAccount;
        this.amount = amount;
        this.transactionType = transactionType;
    }
    void displayTransaction() {
        System.out.println("Transaction: " + transactionType + ", Amount: " + amount + ", From: " + fromAccount.accNumber + ", To: " + toAccount.accNumber);
    }
}
class User {
    String username;
    String password;
    ArrayList<Account> accounts = new ArrayList<>();

    public User(String username, String password) {
        this.username = username;
        this.password = password;
    }
    void addAccount(Account account) {
        accounts.add(account);
    }
    boolean authenticate(String username, String password) {
        return this.username.equals(username) && this.password.equals(password);
    }
}
class Bank {
    ArrayList<User> users = new ArrayList<>();
    ArrayList<Transaction> transactions = new ArrayList<>();
    User createUser(String username, String password) {
        User newUser = new User(username, password);
        users.add(newUser);
        return newUser;
    }
    Transaction makeTransaction(Account fromAccount, Account toAccount, double amount, String transactionType) {
        Transaction newTransaction = new Transaction(fromAccount, toAccount, amount, transactionType);
        transactions.add(newTransaction);
        return newTransaction;
    }
}
public class OnlineBankingSystem {
    public static void main(String[] args) {
        Bank bank = new Bank();
        User user1 = bank.createUser("user1", "password1");
        Account savingsAcc = new Account("12345", "Savings", 1000);
        Account checkingAcc = new Account("54321", "Checking", 500);
        user1.addAccount(savingsAcc);
        user1.addAccount(checkingAcc);

        savingsAcc.deposit(500);
        checkingAcc.withdraw(200);
        savingsAcc.transfer(300, checkingAcc);

        for (Transaction transaction : bank.transactions) {
            transaction.displayTransaction();
        }

        System.out.println("Savings account balance: " + savingsAcc.balance);
        System.out.println("Checking account balance: " + checkingAcc.balance);
    }
}