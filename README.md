# PROJO (In Development)
Open Source - Project Management Tool specially designed for any startups or big tech companies.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features & Requirements](#features--requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [License](#license)

---

## Project Overview 

PROJO is a project management tool designed to help teams manage tasks, collaborate, and track progress. The tool includes features such as user registration, task management, project planning, file sharing, and real-time collaboration.

---

## Features & Requirements

Below is the list of features to be implemented for **PROJO**. Each feature includes a status tracker to easily track progress.

| Feature | Description | Status |
| ------ | ----------- | -------- |
| **Sign Up / Registration** | User registration using a custom user model with email, password, avatar, and role. | ⏳In Progress |
| **Login / Authentication (JWT)** | User login with JWT authentication for stateless sessions. | ⏳In Progress |
| **User Profile Management** | Ability for users to update their profile, including avatar and bio. | 🕒Planning |
| **Project Creation** | Users can create projects, define project name, description, and deadlines. | 🕒Planning |
| **Task Creation** | Users can create tasks, assign them to team members, set deadlines, and track progress. | 🕒Planning |
| **Task Assignment** | Ability to assign tasks to users and track their status (To Do, In Progress, Done). | 🕒Planning |
| **Real-Time Collaboration** | Users can comment on tasks and projects in real-time. | 🕒Planning |
| **File Uploads** | Allow users to upload files to tasks and projects. | 🕒Planning |
| **Notifications** | Send notifications to users for task updates, project changes, etc. | 🕒Planning |
| **Reports & Dashboards** | Users can generate reports and view project statistics through a dashboard. | 🕒Planning |
| **Admin Dashboard** | Admin can manage users, projects, tasks, and view analytics. | 🕒Planning |
| **Search Functionality** | Implement search for users, tasks, and projects. | 🕒Planning |
| **User Permissions** | Define user roles (Admin, Manager, User) with different access levels. | 🕒Planning |
| **Task Deadlines** | Add deadline tracking for tasks and alert users. | 🕒Planning |
| **Dark Mode** | Implement a dark mode option for the UI. | 🕒Planning |

---

## Installation

1. **Clone the repository**:
```bash
git clone https://github.com/TharunNo1/PROJO.git
cd PROJO
```
2. **Create a Virtual environment**:
  ```bash
  python -m venv venv
  source venv/bin/activate  # For macOS/Linux
  venv\Scripts\activate     # For Windows
  ```
3. **Install required packages**:
  ```bash
  pip install -r requirements.txt
  ```
4. **Apply database migrations**:
  ```bash
  python manage.py migrate
  ```
5. **Run the development server** :
  ```bash
  python manage.py runserver
  ```

## Usage

### 1. **Sign Up & Log In**  
Create an account with your email and password, then log in to access your personalized dashboard.

### 2. **Create Projects**  
Start new projects, define deadlines, and invite team members to collaborate.

### 3. **Add & Assign Tasks**  
Create tasks, assign them to team members, and track progress with simple status updates.

### 4. **Collaborate in Real-Time**  
Comment, share updates, and stay in sync with your team on each task.

### 5. **Manage Your Profile**  
Update your profile, upload an avatar, and adjust your settings at any time.


## License
This project is licensed under the MIT License - see the LICENSE file for details.



