\# Fullstack Auth App



\## 📌 Overview



This is a full-stack authentication application built with Flask (backend) and React (frontend).

Users can register, login, and manage their own tasks using JWT authentication.



\---



\## 🚀 Features



\* User Registration

\* User Login (JWT Authentication)

\* Protected Routes

\* Create Tasks

\* View Tasks

\* Logout functionality



\---



\## 🛠 Tech Stack



\### Backend



\* Flask

\* Flask-JWT-Extended

\* Flask-SQLAlchemy

\* SQLite



\### Frontend



\* React (Vite)

\* Axios

\* React Router DOM



\---



\## 🔐 Authentication Flow



1\. User registers with email \& password

2\. Password is hashed using bcrypt

3\. User logs in and receives JWT token

4\. Token is stored in localStorage

5\. Protected routes require Authorization header:



&#x20;  ```

&#x20;  Authorization: Bearer <token>

&#x20;  ```



\---



\## 📂 Project Structure



```

fullstack-auth-app/

│

├── backend/

│   ├── app.py

│   ├── models.py

│   ├── config.py

│   ├── routes/

│   │   ├── auth\_routes.py

│   │   └── task\_routes.py

│

├── frontend/

│   ├── src/

│   │   ├── pages/

│   │   │   ├── Login.jsx

│   │   │   └── Dashboard.jsx

│   │   └── App.jsx

```



\---



\## ⚙️ Setup Instructions



\### 1️⃣ Clone the project



```

git clone <your-repo-link>

cd fullstack-auth-app

```



\---



\## 🖥 Backend Setup



```

cd backend

python -m venv venv

venv\\Scripts\\activate   # Windows



pip install flask flask-cors flask-jwt-extended flask-sqlalchemy bcrypt python-dotenv



python app.py

```



Server runs on:



```

http://localhost:5000

```



\---



\## 🌐 Frontend Setup



```

cd frontend

npm install

npm install axios react-router-dom



npm run dev

```



Frontend runs on:



```

http://localhost:5173

```



\---



\## 🧪 API Endpoints



\### Auth



| Method | Endpoint           | Description   |

| ------ | ------------------ | ------------- |

| POST   | /api/auth/register | Register user |

| POST   | /api/auth/login    | Login user    |



\---



\### Tasks (Protected)



| Method | Endpoint   | Description    |

| ------ | ---------- | -------------- |

| GET    | /api/tasks | Get user tasks |

| POST   | /api/tasks | Create task    |



\---



\## 🧾 Example Request



\### Register



```

POST /api/auth/register

{

&#x20; "email": "test@test.com",

&#x20; "password": "123456"

}

```



\### Login



```

POST /api/auth/login

{

&#x20; "email": "test@test.com",

&#x20; "password": "123456"

}

```



\---



\## 🔑 Authorization Example



```

Authorization: Bearer YOUR\_TOKEN

```



\---



\## 🎯 Notes



\* Each user can only access their own tasks

\* JWT is required for protected routes

\* Passwords are securely hashed using bcrypt



\---



\## 👨‍💻 Author



Developed by Tanika 🚀



