# Library Management System (LBMS) General Usage Guide  

Welcome to the Library Management System (LBMS). This guide will walk you through the general usage of the system, including accessing the application, navigating its features, and performing core actions like managing books, accounts, and users.

---

## **Getting Started**  

### **Prerequisites**  
1. Ensure you have access to the deployed version of the LBMS or have set up the development environment locally.  
2. Use a modern web browser (e.g., Chrome, Firefox, Edge) for the best experience.  
3. If running locally, follow the setup instructions in the repository's README file to start the Django development server.  

### **Accessing the Application**  
- Open the application URL in your browser.  
- If you're running the system locally, access it at:  
  ```
  http://127.0.0.1:8000/
  ```  

---

## **User Accounts**  

### **1. Login**  
- Navigate to the **Login Page** via the homepage or directly at `/accounts/login/`.  
- Enter your username and password, then click **Login**.  
- Upon successful login, you will be redirected to the dashboard or homepage.  

### **2. Sign Up**  
- New users can register via the **Sign Up Page** located at `/accounts/signup/`.  
- Fill out the required fields, including username, email, and password.  
- Upon successful registration, you will be redirected to the login page to access your account.  

### **3. Logout**  
- To log out, click the **Logout** link in the navigation menu.  
- You will be redirected to a confirmation page indicating you’ve successfully logged out.  

---

## **Managing the Library**  

### **1. Viewing the Library**  
- Navigate to the **Library Page** to view the catalog of books available in the system.  
- The catalog displays a list of books, including their title, author, and availability status.  

### **2. Searching for Books**  
- Use the search bar at the top of the Library Page to find books by title, author, or genre.  

### **3. Borrowing Books**  
- Select a book from the catalog and click **Borrow** to check it out.  
- Confirm your selection to complete the borrowing process.  

### **4. Returning Books**  
- Navigate to the **My Account** page to see your borrowed books.  
- Select the book you wish to return and click **Return**.  

---

## **Administrative Actions**  
*(For users with admin permissions only)*  

### **1. Adding Books**  
- Access the **Admin Panel** to add new books to the library.  
- Fill out the book details (e.g., title, author, genre) and save.  

### **2. Managing Users**  
- View, edit, or remove user accounts via the **Admin Panel**.  

---

## **Testing the Application**  

### **Automated Testing**  
- The system includes automated tests for functionality such as login, signup, and core features.  
- To run the tests, use the following command in the terminal:  
  ```
  pytest
  ```  
- Check the test results to ensure the application is functioning correctly.  

---

## **Support and Documentation**  
- For further assistance, refer to the detailed documentation in the repository’s `/docs` folder.  
- If you encounter issues, submit a bug report via the **Issues** tab on the repository.  

---

## **Known Issues and Limitations**  
- The current version may have limitations in advanced features such as analytics or bulk imports.  
- For a complete list of known issues, see the repository’s **Issues** section.  

---

## **Feedback and Contributions**  
- Contributions are welcome! Fork the repository, make your changes, and submit a pull request.  
- Feedback can be submitted via email or the repository discussion board.  

---

Thank you for using the Library Management System! 😊  