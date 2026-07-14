# Pangisha Smart House

Pangisha Smart House is a full-stack property rental platform that helps landlords list properties and enables tenants to discover homes with ease. The application combines a Flask REST API backend with a React and Vite frontend to deliver a secure, responsive, and user-friendly experience.

## Overview

The platform supports:
- user registration and login
- property listing and management
- image upload for properties
- favorites and property inquiries
- protected API access with JWT authentication

## Features

### Authentication
- secure user registration
- login with JWT-based authentication
- password hashing with Flask-Bcrypt
- protected routes for authenticated users

### Property Management
- add new properties
- view available listings
- view detailed property information
- update and delete property records
- upload property images

### User Experience
- responsive and modern interface
- navigation with React Router
- interactive alerts with SweetAlert2
- API integration with Axios

## Tech Stack

### Backend
- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-JWT-Extended
- Flask-Bcrypt
- Flask-CORS
- SQLite or PostgreSQL
- Cloudinary

### Frontend
- React
- Vite
- React Router DOM
- Axios
- Tailwind CSS
- SweetAlert2

## Project Structure

```text
pangisha-smarthouse/
├── server/                 # Flask backend
│   ├── app.py
│   ├── config.py
│   ├── extensions.py
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   └── requirements.txt
├── pangisha_frontend/      # React frontend
│   ├── src/
│   ├── public/
│   └── package.json
└── README.md
```

## Prerequisites

Before you begin, make sure you have the following installed:
- Python 3.10+
- Node.js 18+
- npm

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/kalebu1960/pangisha-smarthouse.git
cd pangisha-smarthouse
```

### 2. Backend setup

```bash
cd server
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a file named `.env` inside the `server` folder with the following values:

```env
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret
DATABASE_URL=sqlite:///instance/pangisha-dev.db

# Optional for image uploads
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

If you prefer PostgreSQL for development or production, use a PostgreSQL URL instead of the SQLite example above.

### 3. Run database migrations

```bash
flask db upgrade
```

If you want sample data, you can optionally seed the database:

```bash
python seed.py
```

### 4. Start the backend

```bash
python3 app.py
```

The backend will run at:

```text
http://127.0.0.1:5555
```

## Frontend setup

Open a second terminal and run:

```bash
cd pangisha_frontend
npm install
npm run dev
```

The frontend will run at:

```text
http://localhost:5173
```

If you want the frontend to target a different backend URL, create a `.env` file inside `pangisha_frontend` and set:

```env
VITE_API_URL=http://127.0.0.1:5555
```

## Running the app locally

1. Start the backend from the `server` folder.
2. Start the frontend from the `pangisha_frontend` folder.
3. Open `http://localhost:5173` in your browser.

## Authentication

After a successful login, the backend returns a JWT token. The frontend stores it in local storage and attaches it automatically to protected requests.

## DEPLOYMENT NOTES

- `SECRET_KEY`
- `JWT_SECRET_KEY`
- `DATABASE_URL` with a PostgreSQL connection string

## Contributing

If you would like to contribute, please create a feature branch, make your changes, and open a pull request.