# Microblog Flask Application 🚀

This repository contains a functional microblog Flask app. It is the result of completing Miguel Grinberg's [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/). Thanks to him for bringing such a rich tutorial for all kinds of expertise.

---

## Key Features ✨

- **User Authentication:** Users can register, login and their passwords are securely handled.
- **Social Interactions:** Follow & unfollow functionality between users.
- **Private Messaging:** Send & receive private messages between users.
- **Email support:** Users can request a password reset and receive notifications via email.
- **Responsive Design with Bootstrap:** The interface is optimized both for desktop and mobile viewports.
- **Deployment:** Triple deployment with Vagrant (VM); Docker (Container) and Render (personal choice vs Heroku)
- **Bing Translations:** Translate posts by using Azure's translation API in real time.
- **REST API:** Secured JSON-based endpoints ready to be implemented with external services.

---

## Tech Stack 🛠️

- **Backend:** Flask, SQLAlchemy.
- **Frontend:** Flask-WTF, Bootstrap.
- **Database:** SQLite (dev) & PostgreSQL (prod).
- **Deployment:** Docker.

---

## How to run this project locally 🔧

1. Clone this repository:
    ```bash
   git clone https://github.com/frarlo/microblog.git
   ```

2. Create a virtual environment inside the project folder and install the required dependencies. The commands differ slightly depending on the operating system:  


   - **Linux-based systems**:  
     ```bash
      python3 -m venv venv
      source venv/bin/activate
      pip install -r requirements.txt
     ```

   - **Windows systems**:  
     ```powershell
      python3 -m venv venv
      venv\Scripts\activate
      pip install -r requirements.txt
     ```

3. Set up the database:
   ```bash
   flask db upgrade
   ```
   
4. Compile the translations:
   ```bash
   flask translate compile
   ```
   
5. Run the application:
   ```bash
   flask run
   ```
   
6. Access the application, which will be accessible at:
      ```bash
   http://localhost:5000
   ```
   
Note: Some app features (emails, translations, elasticsearch) will not work if the system variables are not defined beforehand.

---

# Why This Project 🤔

This project allowed me to dive into Flask, a framework that was completely new to me. This project gave me the opportunity to showcase and practice my skills in:

- Web development.
- Backend architecture.
- API integration.
- Responsive design and deployment practices.

---

# License 📄

This project is licensed under the MIT License. See the LICENSE file for further details.

---

Feel free to connect with me through here if you have suggestions or any questions regarding this project!😊