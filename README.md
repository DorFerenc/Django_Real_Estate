# BT Real Estate App

## Overview

BT Real Estate App is a fully functional real estate application built using Python Django and HTML. The app allows users to browse, search, and inquire about real estate listings. The application is designed with a clean and mobile-friendly interface, featuring essential real estate functionalities.

## Features

### Frontend Pages
- **Home**: Welcome page showcasing featured listings and a quick search.
- **About**: Information about the company, including a list of realtors and a "Seller of the Month" feature.
- **Listings**: Browse available real estate listings with pagination.
- **Single Listing**: Detailed view of a single property, including images, property details, and an inquiry form.
- **Search**: Search for properties based on keywords, city, state, bedrooms, and price.
- **Register**: User registration page for creating an account.
- **Login**: User login page to access the dashboard.
- **Dashboard**: User dashboard to track inquiries submitted through the site.

### Design Specifications
- **Branding**: Utilizes the BTRE logo on both the frontend and admin panels.
- **Colors**: Main branding colors are blue (#10284e) and green (#30caa0).
- **Mobile Friendly**: Fully responsive design that works on all devices.
- **Social Media & Contact Info**: Displayed prominently across the site.

### Functionality
- **Admin Management**: 
  - Manage listings, realtors, contact inquiries, and website users.
  - Role-based user management (staff and non-staff).
  - Ability to set listings to unpublished.
- **Listings Display**: 
  - Display property listings with pagination.
  - Search functionality on the homepage and search page.
  - Listings can be searched by keyword, city, state, bedrooms, and price.
- **Realtors Display**: 
  - List realtors on the about page with a “Seller of the Month” feature.
- **Listing Page Features**:
  - Main image and up to 5 additional images with a lightbox gallery.
  - Property details including title, address, price, bedrooms, bathrooms, square feet, lot size, garage, listing date, and realtor info.
  - Inquiry form to submit questions directly to the realtor(s).
  - Both registered and unregistered users can submit inquiries, with registered users limited to one inquiry per listing.
- **User Authentication**: Frontend register/login system to track user inquiries.

### Possible Future Functionality
- **Google Maps Integration**: Display the property location on a map.
- **Buyer Testimonials**: Allow users to leave testimonials about their buying experience.

## Technology Stack

- **Python**: Basic Python concepts like lists, dictionaries, functions, and conditionals.
- **Django**: 
  - Web framework used for building and managing the application.
  - Custom apps within Django to handle different functionalities.
- **PostgreSQL**: 
  - Database setup locally and remotely for managing application data.
- **Bootstrap**: Used for responsive and clean UI design.

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone <Project link>
    ```
2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```
3. **Activate the virtual environment**:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```
4. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```
5. **Create migrations**:
    ```bash
     python manage.py makemigrations
    ```
6. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```
7. **Run the development server**:
    ```bash
    python manage.py runserver
    ```
8. **Access the application**:
    - Open a web browser and go to `http://localhost:8000`
