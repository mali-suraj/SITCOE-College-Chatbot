# SITCOE College Chatbot - Project Structure

This document provides a comprehensive overview of the project structure and organization.

## 📁 Root Directory Structure

```
college-chatbot/
├── README.md                 # Project overview and setup instructions
├── DEPLOYMENT.md            # Deployment and production guide
├── PROJECT_STRUCTURE.md     # This file - project structure documentation
├── setup.py                 # Automated setup script
├── test_backend.py          # Backend testing script
├── backend/                 # Flask backend application
├── frontend/                # React frontend application
└── docs/                    # Additional documentation
```

## 🔧 Backend Structure (`backend/`)

```
backend/
├── app.py                   # Main Flask application
├── requirements.txt         # Python dependencies
├── env.example             # Environment variables template
├── .env                     # Environment variables (created during setup)
├── Procfile                # Heroku/Render deployment configuration
├── runtime.txt             # Python version specification
└── __init__.py             # Python package initialization
```

### Backend Components

#### `app.py` - Main Application
- **Flask Server**: Main web server setup
- **OpenAI Integration**: GPT-3.5/4 API integration
- **CORS Configuration**: Cross-origin resource sharing setup
- **API Endpoints**:
  - `POST /chat` - Main chat functionality
  - `GET /health` - Health check endpoint
  - `GET /knowledge` - Knowledge base access

#### Knowledge Base
- **Admissions**: Process, requirements, documents, deadlines
- **Courses**: Computer, Mechanical, Electrical, Civil, AI & DS
- **Fees**: Tuition, other fees, scholarships, payment
- **Placements**: Companies, packages, rates, internships
- **Faculty**: Qualifications, experience, research, ratio
- **Events**: Technical, cultural, workshops, seminars
- **Facilities**: Labs, library, sports, hostel

## 🎨 Frontend Structure (`frontend/`)

```
frontend/
├── public/
│   ├── index.html          # Main HTML file
│   ├── favicon.ico         # Website icon
│   └── manifest.json       # PWA manifest
├── src/
│   ├── App.js              # Main React component
│   ├── App.css             # Tailwind CSS imports
│   ├── index.js            # React entry point
│   └── index.css           # Global styles
├── package.json            # Node.js dependencies and scripts
├── tailwind.config.js      # Tailwind CSS configuration
└── postcss.config.js       # PostCSS configuration
```

### Frontend Components

#### `App.js` - Main Component
- **Chat Interface**: Message display and input
- **State Management**: Messages, loading states, UI states
- **API Integration**: Backend communication
- **Quick Questions**: Pre-defined question buttons
- **Responsive Design**: Mobile and desktop optimization

#### Styling
- **Tailwind CSS**: Utility-first CSS framework
- **Custom Colors**: SITCOE brand colors
- **Responsive Design**: Mobile-first approach
- **Animations**: Loading states and transitions

## 🚀 Setup and Installation

### Prerequisites
- **Python 3.9+**: Backend runtime
- **Node.js 16+**: Frontend runtime
- **OpenAI API Key**: For AI functionality

### Automated Setup
```bash
# Run the setup script
python setup.py

# The script will:
# 1. Check prerequisites
# 2. Install backend dependencies
# 3. Install frontend dependencies
# 4. Create environment files
```

### Manual Setup
```bash
# Backend
cd backend
pip install -r requirements.txt
cp env.example .env
# Edit .env with your OpenAI API key

# Frontend
cd frontend
npm install
```

## 🔄 Development Workflow

### 1. Start Development
```bash
# Terminal 1 - Backend
cd backend
python app.py

# Terminal 2 - Frontend
cd frontend
npm start
```

### 2. Testing
```bash
# Test backend functionality
python test_backend.py

# Test frontend (manual)
# Open http://localhost:3000
```

### 3. Development Features
- **Hot Reload**: Both frontend and backend
- **Error Handling**: Comprehensive error messages
- **Logging**: Backend request logging
- **CORS**: Development-friendly CORS setup

## 🌐 Production Deployment

### Backend Deployment
- **Platform**: Render (recommended) or Heroku
- **Environment**: Production Flask settings
- **Scaling**: Auto-scaling based on demand
- **Monitoring**: Health checks and logging

### Frontend Deployment
- **Platform**: Vercel (recommended) or Netlify
- **Build**: Optimized production build
- **CDN**: Global content delivery
- **Performance**: Lighthouse optimization

### Website Integration
- **Widget Embed**: JavaScript widget loading
- **Iframe**: Direct iframe integration
- **Direct Link**: External chatbot link

## 🔒 Security Features

### Backend Security
- **Environment Variables**: Secure API key storage
- **Input Validation**: User input sanitization
- **CORS Protection**: Origin validation
- **Error Handling**: Secure error messages

### Frontend Security
- **HTTPS Only**: Production HTTPS enforcement
- **Content Security**: CSP headers
- **XSS Protection**: Input sanitization
- **API Security**: Secure API communication

## 📊 Monitoring and Analytics

### Backend Monitoring
- **Health Checks**: `/health` endpoint
- **Request Logging**: All API requests
- **Error Tracking**: Exception handling
- **Performance Metrics**: Response times

### Frontend Analytics
- **User Interactions**: Chat engagement
- **Performance**: Load times and responsiveness
- **Error Tracking**: Frontend error monitoring
- **Usage Statistics**: Chatbot usage patterns

## 🔧 Configuration Options

### Backend Configuration
```python
# Environment variables
OPENAI_API_KEY=your_key_here
FLASK_ENV=production
FLASK_DEBUG=false
PORT=5000
```

### Frontend Configuration
```javascript
// API endpoint configuration
const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';
```

### Tailwind Configuration
```javascript
// Custom color palette
colors: {
  'sitcoe-blue': '#1e40af',
  'sitcoe-light-blue': '#3b82f6',
  'sitcoe-dark-blue': '#1e3a8a',
}
```

## 📱 Responsive Design

### Mobile Optimization
- **Touch-Friendly**: Large touch targets
- **Responsive Layout**: Adaptive sizing
- **Performance**: Optimized for mobile devices
- **Accessibility**: Screen reader support

### Desktop Features
- **Full Interface**: Complete chat experience
- **Keyboard Shortcuts**: Enter to send
- **Mouse Interactions**: Hover effects
- **Window Management**: Minimize/maximize

## 🔄 Future Enhancements

### Planned Features
1. **Voice Integration**: Speech-to-text and text-to-speech
2. **Multilingual Support**: Marathi, Hindi, English
3. **Admin Dashboard**: FAQ management interface
4. **Analytics Dashboard**: Usage statistics and insights
5. **Advanced AI**: Custom training and fine-tuning

### Scalability Considerations
- **Database Integration**: Persistent storage
- **User Authentication**: User accounts and history
- **Multi-tenant Support**: Multiple college support
- **API Rate Limiting**: Usage control and monitoring

## 📚 Documentation

### Code Documentation
- **Inline Comments**: Detailed code explanations
- **Function Docstrings**: API documentation
- **README Files**: Setup and usage instructions
- **Deployment Guide**: Production deployment steps

### User Documentation
- **FAQ Integration**: Common questions and answers
- **Help System**: In-app help and guidance
- **Tutorial**: First-time user experience
- **Support**: Contact information and help

---

This project structure provides a solid foundation for a production-ready college chatbot with clear separation of concerns, comprehensive documentation, and scalable architecture.



