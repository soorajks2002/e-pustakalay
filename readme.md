![App Screenshot](https://github.com/soorajks2002/Library-Management-System-DJANGO/blob/master/screenshots/banner.png?raw=true)

# **e-पुस्तकालय**
## Installation

### 1. Install Required Packages

  ```bash
  pip install -r requirements.txt
  ```
    
### 2. Create Dummy Data (optional)

  ```bash
  python manage.py shell
  ```

   inside the shell
  ```bash
  exec(open('create_db.py').read())      
  ```

  to delete the dummy data, inside the shell
  ```bash
  exec(open('delete_db.py').read())      
  ```

  to exit shell
  ```bash
  exit()
  ```

### 3. Create SuperUser

  ```bash
  python manage.py create superuser
  ```

### 4. Make Migrations for Models

  ```bash
  python manage.py makemigrations
  
  python manage.py migrate
  ```

### 4. Start Server

  ```bash
  python manage.py runserver
  ```

 to run application on any port (eg: **80008**) rather than the default **8080**
 ```bash
  python manage.py runserver 8008
  ```
## Screenshots

### 1. Homepage
![App Screenshot](https://github.com/soorajks2002/Library-Management-System-DJANGO/blob/master/screenshots/homepage.png?raw=true)

### 2. Sign-UP Page
![App Screenshot](https://github.com/soorajks2002/Library-Management-System-DJANGO/blob/master/screenshots/sign-up.png?raw=true)

### 3. Log-IN Page
![App Screenshot](https://github.com/soorajks2002/Library-Management-System-DJANGO/blob/master/screenshots/login.png?raw=true)

### 4. Wrong Credentials
![App Screenshot](https://github.com/soorajks2002/Library-Management-System-DJANGO/blob/master/screenshots/wrong-credentials.png?raw=true)

### 5. Lodged-IN Homepage
![App Screenshot](https://github.com/soorajks2002/Library-Management-System-DJANGO/blob/master/screenshots/lodgedin-page.png?raw=true)

### 6. Homepage After Genre Based Sorting
![App Screenshot](https://github.com/soorajks2002/Library-Management-System-DJANGO/blob/master/screenshots/homepage-genre.png?raw=true)

### 7. Genre Specific Books Page
![App Screenshot](https://github.com/soorajks2002/Library-Management-System-DJANGO/blob/master/screenshots/genre.png?raw=true)

### 8. Book Details Page
![App Screenshot](https://github.com/soorajks2002/Library-Management-System-DJANGO/blob/master/screenshots/book-details.png?raw=true)

### 9. Author Details Page
![App Screenshot](https://github.com/soorajks2002/Library-Management-System-DJANGO/blob/master/screenshots/author-details.png?raw=true)

### 10. Book Order Page
![App Screenshot](https://github.com/soorajks2002/Library-Management-System-DJANGO/blob/master/screenshots/order-page.png?raw=true)

### 11. User Details Page
![App Screenshot](https://github.com/soorajks2002/Library-Management-System-DJANGO/blob/master/screenshots/user-page.png?raw=true)

### 12. New Book Creation Page
![App Screenshot](https://github.com/soorajks2002/Library-Management-System-DJANGO/blob/master/screenshots/new-book.png?raw=true)

### 13. Newly Created Book Details
![App Screenshot](https://github.com/soorajks2002/Library-Management-System-DJANGO/blob/master/screenshots/new-book-page.png?raw=true)

### 14. New Author Creation Page
![App Screenshot](https://github.com/soorajks2002/Library-Management-System-DJANGO/blob/master/screenshots/new-author.png?raw=true)

### 15. Newly Created Author Details
![App Screenshot](https://github.com/soorajks2002/Library-Management-System-DJANGO/blob/master/screenshots/new-author-page.png?raw=true)
