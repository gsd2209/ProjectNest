# ProjectNest
ProjectNest is a modern project management application designed to streamline team collaboration, task tracking, and project organization. It allows users to create and manage projects, assign tasks, set priorities, track progress, and communicate effectively through comments, all within a user-friendly interface. Built with robust authentication and a well-structured API, it offers a reliable and scalable solution for managing workflows efficiently.

This README file provides instructions on how to set up the project locally, migrate the database, and run the server. It also includes API documentation for the available endpoints.

---

## **Prerequisites**

Before setting up the project, ensure you have the following installed on your local machine:

- Python 3.8 or higher
- pip (Python package installer)
- Virtualenv (optional but recommended)
- MYSQL (or any other database you're using)

---

## **Setting Up the Project Locally**

Follow these steps to set up the project on your local machine:

### 1. **Clone the Repository**
```bash
git clone https://github.com/gsd2209/Project_Management-Application.git
cd Project
```

### 2. **Create a Virtual Environment**
```bash
python -m venv myenv
source myenv/scripts/activate  # On Windows: myenv\Scripts\activate
```

### 3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4. **Configure the Environment Variables**

Create a `.env` file in the root of the project and configure the following variables:
```
DEBUG=True
SECRET_KEY=your_secret_key
```

### 5. **Migrate the Database**
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. **Run the Server**
```bash
python manage.py runserver
```
The application will be accessible at `http://127.0.0.1:8000/`.

---

## **API Documentation**

This project provides a REST API for managing users, projects, tasks, and comments. Below are the available endpoints:

### **Authentication**
- **POST** `/api/token/` - Obtain JWT token.
- **POST** `/api/token/refresh/` - Refresh JWT token.

### **Users**
- **POST** `/api/users/register/` - Register a new user.
- **POST** `/api/users/login/` - Log in a user.
- **GET** `/api/users/{id}/` - Retrieve details of a specific user.
- **PUT/PATCH** `/api/users/{id}/` - Update user details.
- **DELETE** `/api/users/{id}/` - Delete a user.

### **Projects**
- **GET** `/api/projects/` - List all projects.
- **POST** `/api/projects/` - Create a new project.
- **GET** `/api/projects/{id}/` - Retrieve project details.
- **PUT/PATCH** `/api/projects/{id}/` - Update project details.
- **DELETE** `/api/projects/{id}/` - Delete a project.

### **Tasks**
- **GET** `/api/projects/{project_id}/tasks/` - List tasks for a project.
- **POST** `/api/projects/{project_id}/tasks/` - Create a new task.
- **GET** `/api/tasks/{id}/` - Retrieve task details.
- **PUT/PATCH** `/api/tasks/{id}/` - Update task details.
- **DELETE** `/api/tasks/{id}/` - Delete a task.

### **Comments**
- **GET** `/api/tasks/{task_id}/comments/` - List comments for a task.
- **POST** `/api/tasks/{task_id}/comments/` - Add a new comment.
- **GET** `/api/comments/{id}/` - Retrieve comment details.
- **PUT/PATCH** `/api/comments/{id}/` - Update a comment.
- **DELETE** `/api/comments/{id}/` - Delete a comment.

---

## **Testing the API**

You can test the API endpoints using tools like:
- [Postman](https://www.postman.com/)

For example, to test obtaining a token:
```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "your_username", "password": "your_password"}'
```

---


