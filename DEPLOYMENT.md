# SITCOE College Chatbot - Deployment Guide

This guide covers deploying the chatbot to production environments and integrating it with the SITCOE college website.

## 🚀 Quick Deployment

### Option 1: Automated Setup (Recommended)
```bash
# Run the setup script
python setup.py

# Add your OpenAI API key to backend/.env
# Then start both services
```

### Option 2: Manual Setup
```bash
# Backend
cd backend
pip install -r requirements.txt
python app.py

# Frontend (new terminal)
cd frontend
npm install
npm start
```

## 🌐 Production Deployment

### Backend Deployment (Render/Heroku)

#### Render (Recommended)
1. **Create Render Account**
   - Sign up at [render.com](https://render.com)
   - Connect your GitHub repository

2. **Deploy Backend**
   - Create new Web Service
   - Connect your repository
   - Set build command: `pip install -r requirements.txt`
   - Set start command: `python app.py`
   - Add environment variables:
     - `OPENAI_API_KEY`: Your OpenAI API key
     - `FLASK_ENV`: production
     - `FLASK_DEBUG`: false

3. **Get Backend URL**
   - Your backend will be available at: `https://your-app-name.onrender.com`

#### Heroku Alternative
1. **Install Heroku CLI**
2. **Deploy**:
   ```bash
   cd backend
   heroku create sitcoe-chatbot-backend
   heroku config:set OPENAI_API_KEY=your_key_here
   git push heroku main
   ```

### Frontend Deployment (Vercel/Netlify)

#### Vercel (Recommended)
1. **Create Vercel Account**
   - Sign up at [vercel.com](https://vercel.com)
   - Connect your GitHub repository

2. **Deploy Frontend**
   - Import your repository
   - Set build command: `npm run build`
   - Set output directory: `build`
   - Add environment variable:
     - `REACT_APP_API_URL`: Your backend URL

3. **Update API URL**
   - In `frontend/src/App.js`, change the fetch URL to your backend URL

#### Netlify Alternative
1. **Create Netlify Account**
2. **Deploy**:
   ```bash
   cd frontend
   npm run build
   # Drag and drop the build folder to Netlify
   ```

## 🔗 Website Integration

### Option 1: Widget Embed (Recommended)
Add this code to your SITCOE website (`sitcoe.ac.in`):

```html
<!-- SITCOE College Chatbot Widget -->
<div id="sitcoe-chatbot-widget"></div>
<script>
  // Load the chatbot widget
  (function() {
    const script = document.createElement('script');
    script.src = 'https://your-frontend-url.vercel.app/widget.js';
    script.async = true;
    document.head.appendChild(script);
  })();
</script>
```

### Option 2: Iframe Embed
```html
<iframe 
  src="https://your-frontend-url.vercel.app" 
  width="400" 
  height="600" 
  frameborder="0"
  style="position: fixed; bottom: 20px; right: 20px; z-index: 1000;"
>
</iframe>
```

### Option 3: Direct Link
```html
<a href="https://your-frontend-url.vercel.app" target="_blank" class="chatbot-link">
  💬 Chat with AI Assistant
</a>
```

## 🔧 Configuration

### Environment Variables
```bash
# Backend (.env)
OPENAI_API_KEY=your_openai_api_key_here
FLASK_ENV=production
FLASK_DEBUG=false
PORT=5000

# Frontend (build-time)
REACT_APP_API_URL=https://your-backend-url.onrender.com
```

### CORS Configuration
Update `backend/app.py` for production:
```python
# Update CORS origins for production
CORS(app, origins=[
    "https://sitcoe.ac.in",
    "https://www.sitcoe.ac.in",
    "https://your-frontend-url.vercel.app"
])
```

## 📱 Mobile Optimization

The chatbot is already mobile-responsive, but you can enhance it:

```css
/* Add to your website's CSS */
@media (max-width: 768px) {
  #sitcoe-chatbot-widget {
    width: 100%;
    height: 100vh;
  }
}
```

## 🔒 Security Considerations

1. **API Key Protection**
   - Never expose API keys in frontend code
   - Use environment variables
   - Consider API key rotation

2. **Rate Limiting**
   - Implement rate limiting on backend
   - Add user authentication if needed

3. **Input Validation**
   - Sanitize user inputs
   - Implement content filtering

## 📊 Monitoring & Analytics

### Backend Monitoring
```python
# Add to app.py
import logging
logging.basicConfig(level=logging.INFO)

@app.route("/metrics")
def metrics():
    return jsonify({
        "total_requests": request_count,
        "active_users": active_users,
        "uptime": uptime
    })
```

### Frontend Analytics
```javascript
// Add Google Analytics or similar
gtag('event', 'chatbot_interaction', {
  'event_category': 'engagement',
  'event_label': 'sitcoe_chatbot'
});
```

## 🚨 Troubleshooting

### Common Issues

1. **CORS Errors**
   - Check CORS configuration in backend
   - Verify frontend URL is in allowed origins

2. **API Connection Issues**
   - Verify backend URL is correct
   - Check if backend is running
   - Verify OpenAI API key

3. **Build Errors**
   - Clear node_modules and reinstall
   - Check Node.js version compatibility

### Support
- Check logs in your deployment platform
- Verify environment variables
- Test locally first

## 🔄 Updates & Maintenance

### Regular Updates
1. **Dependencies**: Update packages monthly
2. **OpenAI API**: Monitor API usage and costs
3. **Content**: Update college information regularly

### Backup Strategy
- Keep local development copy
- Use Git for version control
- Backup environment variables

## 📈 Performance Optimization

1. **Backend**
   - Implement caching for common questions
   - Use connection pooling
   - Monitor response times

2. **Frontend**
   - Implement lazy loading
   - Use service workers for offline support
   - Optimize bundle size

---

**Need Help?** Check the logs in your deployment platform or contact the development team.



