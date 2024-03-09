import java.util.ArrayList;
class Book {
    String title;
    String author;
    String genre;
    boolean available;

    public Book(String title, String author, String genre, boolean available) {
        this.title = title;
        this.author = author;
        this.genre = genre;
        this.available = available;
    }
}
class Patron {
    String name;
    String contactInfo;
    ArrayList<Book> borrowedBooks;
    public Patron(String name, String contactInfo) {
        this.name = name;
        this.contactInfo = contactInfo;
        this.borrowedBooks = new ArrayList<>();
    }
}
class Library {
    ArrayList<Book> books;
    ArrayList<Patron> patrons;
    ArrayList<String> borrowRecords;
    public Library() {
        this.books = new ArrayList<>();
        this.patrons = new ArrayList<>();
        this.borrowRecords = new ArrayList<>();
    }
    public void addBook(Book book) {
        this.books.add(book);
    }
    public void addPatron(Patron patron) {
        this.patrons.add(patron);
    }
    public void borrowBook(Book book, Patron patron) {
        if (book.available) {
            book.available = false;
            patron.borrowedBooks.add(book);
            this.borrowRecords.add(book.title + " has been borrowed by " + patron.name + ".");
        } else {
            System.out.println("Sorry, this book is not available for borrowing.");
        }
    }
    public void returnBook(Book book, Patron patron) {
        if (patron.borrowedBooks.contains(book)) {
            book.available = true;
            patron.borrowedBooks.remove(book);
            System.out.println(book.title + " has been returned by " + patron.name + ".");
        } else {
            System.out.println("This book was not borrowed by this patron.");
        }
    }
    public void calculateFine(Book book, int daysOverdue) {
        // Implement fine calculation logic here
    }
    public ArrayList<Book> searchBooks(String keyword) {
        ArrayList<Book> results = new ArrayList<>();
        for (Book book : this.books) {
            if (book.title.toLowerCase().contains(keyword.toLowerCase())) {
                results.add(book);
            }
        }
        return results;
    }
    public ArrayList<Patron> searchPatrons(String keyword) {
        ArrayList<Patron> results = new ArrayList<>();
        for (Patron patron : this.patrons) {
            if (patron.name.toLowerCase().contains(keyword.toLowerCase())) {
                results.add(patron);
            }
        }
        return results;
    }
    public void generateReports() {
        // Implement report generation logic here
    }
}
public class Main {
    public static void main(String[] args) {
        Library library = new Library();
        Book book1 = new Book("Python Programming", "John Doe", "Programming", true);
        Book book2 = new Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic", true);
        Patron patron1 = new Patron("Alice", "alice@example.com");
        library.addBook(book1);
        library.addBook(book2);
        library.addPatron(patron1);
        library.borrowBook(book1, patron1);
        library.returnBook(book1, patron1);
        ArrayList<Book> searchResults = library.searchBooks("Python");
        System.out.println("Search results for 'Python': " + searchResults);
    }
}