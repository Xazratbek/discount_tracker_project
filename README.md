# Discount Tracker Project

## Overview

The Discount Tracker Project is a web application that helps users track discounts on various products from different online stores and marketplaces. The application fetches and displays information about product prices before and after discounts, allowing users to stay informed about the best deals.

## Features

- **Product Listings:** View a list of products along with their original and discounted prices.
- **Store Integration:** Retrieve information from multiple online stores and marketplaces.
- **Price Tracking:** Keep track of how product prices change over time.
- **User Profiles:** Allow users to create profiles, save favorite products, and set preferences for notifications.
- **Advanced Filters:** Filter products based on various criteria, including categories, brands, and stores.
- **Price History Graphs:** Visualize the historical price data for each product.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/discount-tracker-project.git
   cd discount-tracker-project

Create a virtual environment and install dependencies:
python -m venv venv
source venv/bin/activate (or venv\Scripts\activate on Windows)
pip install -r requirements.txt

Apply database migrations:
python manage.py migrate

Run the development service:
python manage.py runserver

Usage
Visit the homepage to browse the list of available products and discounts.
Create a user profile to save favorite products and receive personalized recommendations.
Explore advanced filters to find products based on specific criteria.
Stay updated on price changes and discounts over time.
Customize notification preferences to receive alerts for your favorite products.
Contributing
Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and commit them.
Push your changes to your fork.
Submit a pull request.
