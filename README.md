# Vue Start

This app is the starting point for all of our 
Vue applications.  To write a new Vue app 
in py4web, clone this application in your apps 
folder, and work on it. 
# CSE183_Final

# Local Journalism Site
# Overview
Our Local Journalism Site is a community-driven platform designed to promote local journalism. It allows users to submit their own stories and photos, set a radius of interest, and engage with stories shared by others.

# Key Features
User Registration and Location Setting: Users can register and set their location.

Story Submission: Users can submit their own stories, including title, body text, photos, and a radius of interest.

Story Viewing: Users can view stories based on their location and the radius of interest set by the author.

Monetization: Users can pay to view stories, and payments are distributed among the stories they've read.

Voting System: Users can vote on stories, providing a mechanism to remove spam or irrelevant content.

# System Requirements
Front-end: HTML, CSS, JavaScript (with frameworks like React or Angular for ease of use)
Back-end: Python (using frameworks like Django or Flask for server-side handling)
Database: SQL database (MySQL, SQLite, or PostgreSQL)
# Database Structure
Our system includes several database tables to handle the various features:
User Table: Stores user data including username, password, and location.
Story Table: Stores story data including title, body, photos, radius of interest, and author.
Payment Table: Stores payment data including user, amount, and the stories read.
Vote Table: Stores voting data including user, story, and vote value.
# API Endpoints
The following are the key API endpoints necessary for our system:

Register/Login: Endpoints for user registration and login.
Submit Story: Endpoint for submitting a story.
Get Stories: Endpoint for retrieving stories based on a user's location and story's radius of interest.
Payment: Endpoint for processing payments and distributing among the stories read.
Vote: Endpoint for submitting votes on stories.
# User Interface
The user interface will include pages for:

Login/Registration: Where users can register or log in.
Story Submission: Where users can submit a new story.
Story Feed: Where users can view and vote on stories.
Payment Page: Where users can make payments.
Security Measures
User Authentication: All users are authenticated before being allowed to interact with the site.
Input Validation: All input is validated to protect against common web-based attacks.
Payment Security: All payment data is encrypted and processed securely.
# Future Enhancements
Comment System: Allow users to comment on stories.
User Profiles: Allow users to create profiles that display their stories and activity.
Advanced Sorting and Filtering: Provide more options for users to sort and filter stories in their feed.

The Local Journalism Site is a dynamic platform that fosters community engagement and supports local journalism. By allowing users to share their stories and engage with the content of others, we bring local stories to the forefront and promote independent journalism.