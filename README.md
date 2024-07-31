# CodeVerse
![cv2](https://github.com/user-attachments/assets/9f6b92da-a399-4ff1-83aa-d90d949fd5d1)

## Table of Contents

- [Introduction](#introduction)
- [Problem Statement](#problem-statement)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)

## Introduction

**CodeVerse** is a user onboarding and community engagement platform designed for individuals interested in coding and computer science. It identifies users' skill levels and provides them with tailored resources and community channels to enhance their learning and growth. CodeVerse aims to foster a supportive environment where users can engage with relevant content, participate in discussions, and interact with others at similar skill levels to promote continuous learning.

## Problem Statement

### Problem Statement for Hackathon

We have selected to create a user onboarding and community engagement platform specifically designed for individuals interested in the field of coding and computer science. The platform aims to identify the skill levels of users (Beginner, Intermediate, Expert) and provide them with tailored resources, community channels, and regular engagement to enhance their learning and growth.

### Requirements

1. **User Sign-Up and Profile Setup**:
   - Users must sign up and specify their skill level as Beginner, Intermediate, or Expert.

2. **Skill Evaluation and Recommendations**:
   - **Beginner**: After sign-up, quiz users to identify their interests in various coding and technology fields. Based on the quiz results, automatically add them to specified community channels.
   - **Intermediate**: Conduct a quiz to verify their skill level. Based on the results:
     - If identified as a Beginner, redirect them to beginner resources.
     - If confirmed as Intermediate, suggest relevant channels and ask if they want to explore other technologies. Provide options to join related community channels.
   - **Expert**: Evaluate their expertise level through a quiz. If confirmed as an expert, redirect them to specific channels based on their interests.


### Main Features

1. **Skill Level Quizzes**:
   - A series of quizzes to evaluate the users' skill levels and interests.

2. **Tailored Channel Suggestions**:
   - Provide channel recommendations tailored to the skill levels of Beginners, Intermediates, and Experts.

3. **Community Channels**:
   - Create and manage community channels for various tech fields. Automatically add users to these channels based on their skill levels and interests.

### Target Audience

- Individuals interested in coding and the computer field, ranging from complete beginners to experts.

### Goals

- Effectively identify users' skill levels and interests.
- Provide personalized resources and community engagement.
- Regularly assess and engage users to ensure continuous learning and growth.

This platform should enhance the learning experience for users at all skill levels and foster a supportive community for individuals passionate about coding and technology.

## Updates from Initial Problem Statement

After the initial implementation, we have integrated the **Gemenai API** to provide answers to users' questions, replacing the blog feature with dynamic Q&A support. We now provide three main channels: **Frontend**, **Backend**, and **AI**. More channels will be added in the future.

### Home Page Features

- **Navigation Bar**: Includes links to different sections and authentication options.
- **Hero Text**: A welcoming message that highlights the platform's features.
- **Channel Options**: 
  - Three primary options: **Frontend**, **Backend**, and **AI**.
  - Clicking an option opens a pop-up with an introductory description of the selected tech field.
  - Users can join channels if they are signed up and logged in.

## Features

- **Dynamic User Onboarding**: Tailored onboarding experience based on skill level (Beginner, Intermediate, Expert).
- **Skill Evaluation Quizzes**: Identify user skill levels and interests to offer personalized channel suggestions.
- **Gemenai API Integration**: Provides intelligent Q&A support to enhance learning.
- **Community Channels**: Dedicated channels for Frontend, Backend, and AI with more to come.
- **User Authentication**: Secure login and sign-up system.
- **Regular Engagement Emails**: Automated emails to encourage continuous engagement and learning.
- **Intuitive User Interface**: Clean and responsive UI designed with Django templates and HTML/CSS.

## Tech Stack

### Backend

- **Django**: High-level Python web framework for backend development.
- **Gemenai API**: AI-powered API for dynamic Q&A support.

### Frontend

- **HTML5**: Markup language for structuring content.
- **CSS3**: Styling for web pages.
- **JavaScript**: Client-side scripting for dynamic interactions.

### Database

- **MySQL**: Relational database for data storage.

### Admin Portal

- **Django Admin**: Built-in admin interface for managing platform content.
- **Jazmine**: Testing framework for the admin portal.

### Authentication

- **Custom Authentication System**: Secure user authentication mechanism.

### Deployment

- **Akash Network**: Deployment platform for hosting the application.

### Installation
To get a local copy of CodeVerse up and running, follow these steps:

## Prerequisites
- Python 3.8+: Make sure you have Python installed.
- MySQL: Ensure MySQL is installed and running.

### Installation Steps
- Clone the repository:

```
git clone https://github.com/dpshah23/CodeVerse.git
cd CodeVerse
```

- Create a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
- Install dependencies:


```
pip install -r requirements.txt
```
- Configure the database:

Update codeverse/settings.py with your MySQL database credentials.

- Apply migrations:

```
python manage.py migrate
```

- Run the development server:
```
python manage.py runserver
```
Access the application at http://127.0.0.1:8000/.

### Usage
Once the server is running, you can:

- Sign Up: Create a new account specifying your skill level.
- Take Skill Assessment Quizzes: Complete quizzes to determine your skill level and interests.
- Explore Community Channels: Join channels that align with your interests.
- Receive Regular Updates: Stay engaged with automated emails and participate in channel discussions.
- Utilize AI-Powered Q&A: Use the Gemenai API to get answers to your coding questions.
- Functions and Templates

### Here's a detailed overview of the main functions and templates used in CodeVerse:

Main Functions
- User Authentication:

signup(request): Handles user registration and profile setup.
login(request): Authenticates users and manages sessions.
logout(request): Logs out users and clears sessions.
Skill Level Assessment:

quiz_view(request): Displays quizzes based on user skill level.
submit_quiz(request): Processes quiz submissions and updates user profiles.
- Channel Management:

join_channel(request): Allows users to join selected channels.
view_channel(request, channel_id): Displays channel content and discussions.

- AI-Powered Q&A:

ask_question(request): Handles user queries and retrieves answers from the Gemenai API.
### Templates
- base.html: Base template with common UI elements and layout.
- index.html: Home page template displaying hero text and channel options.
- signup.html: User registration form.
- login.html: User login form.
- quiz.html: Quiz interface for skill assessment.
- channel.html: Displays channel details and discussions.
- profile.html: User profile page with account settings.

## Flow of the System
The flow of the CodeVerse system is designed to provide a seamless user experience:

- Home Page:

Users are greeted with a navigation bar and hero text, introducing the platform's core features.
Options for Frontend, Backend, and AI channels are presented, allowing users to explore their interests.
- User Sign-Up:

New users create an account by specifying their skill level: Beginner, Intermediate, or Expert.
A welcome email is sent, and the user's profile is initialized.
- Skill Assessment:

Users take quizzes to identify their skill levels and coding interests.
Quiz results determine the personalized channel recommendations.
- Channel Exploration:

Users can view and join community channels based on their interests.
Channel pages offer discussion forums, resources, and Q&A support through the Gemenai API.
- Regular Engagement:

Every 15 days, engagement emails are sent to users with questions related to their chosen channels.
Users are encouraged to participate in ongoing discussions and track their progress.
- AI Q&A Support:

Users can ask questions through the platform and receive answers powered by the Gemenai API.

The **CodeVerse** platform employs a traditional web application architecture using Django for both the backend and Frontend rendering. It leverages Django's powerful ORM to interact with a MySQL database for data management and uses the Gemenai API to provide AI-powered responses to user queries.

The main focus of **CodeVerse Team** is to evaluate one's field of intrest and help them foster in that field also by connecting them with their community to get helped whenever they feel struck in any topic or during any of their projects.