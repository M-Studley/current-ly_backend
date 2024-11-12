# Current-ly

**Current-ly** is a web application focused on helping residents of Tbilisi, Georgia, track and report utility outages.
This app empowers users to report issues with power, water, and other utilities by location. It provides real-time
updates and notifications, historical data analysis, and helps people make informed choices about where to live based on
utility reliability.

## Features

- **Report Outages:** Users can submit outage reports for specific locations or general areas for privacy.
- **Real-Time Updates:** Users receive notifications when outage statuses change.
- **Historical Data:** Analyze historical outage data to track reliability by area.
- **Location-Based Outage Information:** Provides outage details using a map interface to enhance user accessibility.

## Tech Stack

- **Backend:** FastAPI, SQLAlchemy, PostgreSQL
- **Frontend:** React.js
- **Database:** PostgreSQL (Dockerized)
- **Data Storage & Caching:** Firebase for notifications, Redis for caching
- **Geospatial Data:** GeoAlchemy2 to handle location-based data and mapping
- **Authentication:** JWT-based authentication for secure user access
- **Containerization:** Docker for PostgreSQL and potentially the full app stack

## Getting Started

### Prerequisites

- **Python** (3.12+)
- **Docker** (for PostgreSQL setup)
- **Node.js**
- **Redis**

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/M-Studley/current-ly_backend.git
   cd Current-ly
   ```

2. **Backend Setup**
    - Create a virtual environment:
      ```bash
      python3 -m venv env
      source env/bin/activate  # On Windows, use `env\Scripts\activate`
      ```
    - Install backend dependencies:
      ```bash
      pip install -r requirements.txt
      ```
    - Apply database migrations:
      ```bash
      alembic upgrade head
      ```

3. **Run Dockerized PostgreSQL**
   ```bash
   docker-compose up -d
   ```

4. **Frontend Setup** (if applicable)
   ```bash
   cd frontend
   npm install
   npm start
   ```

### Configuration

Create an `.env` file at the root with the following settings:

```env
DATABASE_URL=postgresql://user:password@localhost:(desired port #)/currently
JWT_SECRET_KEY=your_jwt_secret
FIREBASE_CONFIG=your_firebase_config
REDIS_URL=redis://localhost:(desired port #)/0
```

### Running the App

1. **Backend Server**:
   ```bash
   uvicorn app.main:app --reload
   ```

2. **Frontend Server** (if using React):
   ```bash
   cd frontend
   npm start
   ```

## Usage

1. Visit the app’s home page to view current outages or report a new one.
2. Use the map interface to view or report outages by specific or general locations.
3. Receive real-time updates on outage resolutions.

## Future Enhancements

- Implement more detailed outage history analytics
- User role-based access for administrators and verified reporters
- Expand utility tracking and add user notification preferences

## License

This project is licensed under the MIT License.

## File Tree

/current-ly/
│
├── app/
│ │
│ ├── api/
│ │ └── routes/
│ ├── db/
│ │ ├── __init__.py
│ │ ├── pg_connection.py
│ │ └── redis_connection.py
│ ├── models/
│ │ ├── __init__.py
│ │ └── base.py
│ ├── schemas/
│ ├── utils/
│ │
│ ├── __init__.py
│ ├── config.py
│ └── main.py
│
├── tests/
│ ├── __init__.py
│ ├── test_api.py
│ ├── test_helpers.py
│ ├── test_pg_db.py
│ └── test_redis_db.py
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt
