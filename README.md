# FAQs:
### What is Bookmarked?  
Bookmarked is a website that is built on the concept of making it easier for people to find and read books. The website enables users to:  
- Search through a large catalogue of books
- Save or BOOKMARK books that they want to read 
- Track books they have read
- Recommend books to other users
- Rate books using a 5-star review system
- Follow other users to see what they are reading
- Have discussions with other users through the community   
### Is Bookmarked free to use?
Absolutely, account creation is free, given the email is not already in use. 
### Is there an open-source version?  
The core version of Bookmarked is open-source and free to use. Developers can host the website by following the provided installation guide.

# User Manual:
## Account Creation:
Click the ‘Begin Your Reading Journey’ button in the centre of the homepage or the “Login” button on the top right of the homepage. If the user already has an account they can log in, if not they can choose to sign up using a valid email address, a unique username, and a secure password. 

## Navigation:
- The Bookshelf page contains a personal collection of saved books and reading progress on each book.
- The Community page allows users to explore trending books, discuss topics on various forums, and view recommendations from users the user is following. 
- The Lists page to see existing book lists or create new book lists. 
- The Search bar can be used to find specific books or filter all books from given categories

## Book Details: 
Upon clicking on a book, the book title, publication years, author, and a detailed synopsis are displayed. The read button will take the user to reading the given book.  The bookmark button will add the book to the user’s bookshelf. The stars will create a review to share with the community. Alongside the star system, the like button will also help the system make better recommendations for the user. 
# Developer Manual: 
## Installation guide: 
1. Make sure you have Git and Node.js installed. 
2. Go to https://github.com/desa-thomas/bookmarked and clone the git. Open the command prompt and cd to the bookmarked folder.

3. Run the following commands
- git fetch --all
- git pull
- git checkout develop

4. Once you're on the develop branch, run the following commands:  
- cd frontend
- npm i
- npm run dev
 
5. Open http:localhost:5173 in a web browser (there should be a link when you run the command that you can click)

## Troubleshooting:
If you get an error message that states “git command not found”, Git might not be installed. Go to the command prompt and type: git --version. If the error persists, follow Step 1 of the Installation Guide.

If you get an error message that states “npr command not found”, Node.js might not be installed. Go to the command prompt and type: node -v. If the error persists, follow Step 1 of the Installation Guide.

