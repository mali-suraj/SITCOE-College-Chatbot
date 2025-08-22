# SITCOE College AI Chatbot

An intelligent chatbot for the SITCOE college website that provides 24/7 assistance to students, faculty, and parents.

## Features

- 🤖 AI-powered responses using OpenAI GPT-3.5/4
- 📚 College-specific knowledge base (admissions, courses, fees, placements)
- 🌐 24/7 availability
- 💬 Real-time chat interface
- 📱 Responsive design with Tailwind CSS
- 🔗 Integration ready for sitcoe.ac.in

## Tech Stack

- **Backend**: Python Flask + OpenAI API
- **Frontend**: React + Tailwind CSS
- **AI**: OpenAI GPT-3.5/4
- **Deployment**: Render (Backend) + Vercel (Frontend)

## Quick Start

### Prerequisites
- Python 3.9+
- Node.js 16+
- OpenAI API key

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend Setup
```bash
cd frontend
npm install
npm start
```

## Project Structure
```
college-chatbot/
├── backend/           # Flask API server
├── frontend/          # React application
├── docs/             # Documentation
└── README.md         # This file
```

## API Endpoints

- `POST /chat` - Chat with the AI chatbot
- `GET /health` - Health check endpoint

## Deployment

1. **Backend**: Deploy to Render
2. **Frontend**: Deploy to Vercel
3. **Integration**: Embed widget in sitcoe.ac.in

## Contributing

This project is designed for SITCOE college. For modifications, please contact the development team.

## License

MIT License - See LICENSE file for details

