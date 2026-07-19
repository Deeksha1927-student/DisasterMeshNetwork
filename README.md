# Disaster MeshConnect

## Overview
Disaster MeshConnect is a hybrid emergency communication system that enables communication during disasters when mobile networks and internet services fail. It uses mesh networking to relay messages between nearby devices and can integrate satellite communication for long-range connectivity.

## Features
- User Registration and Login
- SOS Alert System
- GPS Location Sharing
- Rescue Dashboard
- Mesh Communication Concept
- Satellite Communication Support

## Technologies Used
- Python
- Flask
- HTML
- CSS
- JavaScript
- SQLite

## Project Structure
```
Disaster-MeshConnect/
│── app.py
│── database.db
│── requirements.txt
│── static/
│   ├── style.css
│   └── script.js
│── templates/
│   ├── login.html
│   ├── register.html
│   ├── home.html
│   ├── sos.html
│   └── dashboard.html
└── README.md
```

## Installation

1. Clone the repository.
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python app.py
   ```
4. Open your browser and visit:
   ```
   http://127.0.0.1:5000/
   ```

## How It Works
1. Register a new user.
2. Log in to the application.
3. Send an SOS alert with GPS location.
4. The rescue dashboard receives and displays the emergency request.
5. In disaster scenarios, messages are relayed through nearby mesh nodes or satellite communication when available.

## Applications
- Disaster Management
- Emergency Response
- Defense & Border Security
- Remote Area Communication
- Healthcare & Rescue Services

## Future Enhancements
- Real-time mesh communication using ESP32 devices.
- Satellite communication integration.
- AI-based disaster prediction.
- Offline messaging.
- Mobile application support.

## Team
**Project:** Disaster MeshConnect  
**Developed By:** Deeksha Gomathi

## License
This project is developed for educational and hackathon purposes.
