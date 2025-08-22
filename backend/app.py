from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv
import json
from datetime import datetime

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configure OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# College knowledge base - SITCOE specific information
COLLEGE_KNOWLEDGE = {
    "admissions": {
        "process": "SITCOE offers admission through MHT-CET and JEE Main scores. The admission process includes online application, document verification, and counseling rounds.",
        "requirements": "Minimum 50% in 12th standard (PCM) for general category, 45% for reserved categories. Valid MHT-CET or JEE Main score required.",
        "documents": "10th and 12th mark sheets, caste certificate (if applicable), income certificate, domicile certificate, and photo ID proof.",
        "deadlines": "Admissions typically open in June-July. Check the official website for current year deadlines.",
        "contact": "Admission Office: +91-XXX-XXXXXXX, Email: admissions@sitcoe.ac.in"
    },
    "courses": {
        "computer": "Computer Engineering (120 seats) - Covers programming, algorithms, databases, and software development.",
        "mechanical": "Mechanical Engineering (120 seats) - Focuses on design, manufacturing, and thermal sciences.",
        "electrical": "Electrical Engineering (60 seats) - Covers power systems, electronics, and control systems.",
        "civil": "Civil Engineering (60 seats) - Focuses on structural design, construction, and infrastructure.",
        "ai_ds": "AI & Data Science (60 seats) - New program covering artificial intelligence, machine learning, and data analytics."
    },
    "fees": {
        "tuition": "Tuition fees: ₹1,25,000 per year for general category, ₹62,500 for reserved categories.",
        "other_fees": "Other fees include development fees, library fees, and examination fees (approximately ₹15,000 per year).",
        "scholarships": "Merit-based scholarships available for top performers. EBC and other government scholarships applicable.",
        "payment": "Fees can be paid online through the college portal or in installments."
    },
    "placements": {
        "companies": "Top recruiters include TCS, Infosys, Wipro, Cognizant, Tech Mahindra, and many more.",
        "average_package": "Average package: ₹4.5 LPA, Highest package: ₹12 LPA",
        "placement_rate": "Placement rate: 85%+ for eligible students",
        "internships": "Summer and winter internships available with stipends ranging from ₹8,000 to ₹25,000 per month."
    },
    "faculty": {
        "qualifications": "Faculty members hold PhD and M.Tech degrees from reputed institutions like IITs, NITs, and other premier universities.",
        "experience": "Average teaching experience: 8+ years",
        "research": "Active research in areas like AI/ML, renewable energy, IoT, and sustainable development.",
        "student_ratio": "Student-faculty ratio: 15:1"
    },
    "events": {
        "technical": "TechFest, Project Exhibition, Coding Competitions, Hackathons",
        "cultural": "Cultural Fest, Sports Meet, Annual Function, Alumni Meet",
        "workshops": "Regular workshops on emerging technologies, soft skills, and industry trends.",
        "seminars": "Guest lectures from industry experts and academicians."
    },
    "facilities": {
        "labs": "Well-equipped computer labs, mechanical workshop, electrical labs, and research facilities.",
        "library": "Central library with 50,000+ books, e-resources, and digital access.",
        "sports": "Indoor and outdoor sports facilities, gymnasium, and playground.",
        "hostel": "Separate hostels for boys and girls with modern amenities."
    }
}

def get_college_context():
    """Generate context about SITCOE college"""
    context = """
    SITCOE (Sinhgad Institute of Technology and College of Engineering) is a premier engineering college located in Pune, Maharashtra, India. 
    Established in 2004, it offers undergraduate programs in Computer, Mechanical, Electrical, Civil, and AI & Data Science Engineering.
    The college is affiliated with Savitribai Phule Pune University and approved by AICTE.
    SITCOE is known for its excellent academic standards, industry collaborations, and placement records.
    """
    return context

def create_system_prompt():
    """Create a comprehensive system prompt for the chatbot"""
    knowledge_str = json.dumps(COLLEGE_KNOWLEDGE, indent=2)
    context = get_college_context()
    
    system_prompt = f"""
    You are an AI chatbot assistant for SITCOE (Sinhgad Institute of Technology and College of Engineering) college website.
    
    {context}
    
    You have access to the following college information:
    {knowledge_str}
    
    Your role is to:
    1. Answer questions about SITCOE college admissions, courses, fees, placements, faculty, events, and facilities
    2. Provide accurate and helpful information based on the knowledge base
    3. Guide users to relevant resources and contact information
    4. Be polite, professional, and informative
    5. If you don't have specific information, suggest contacting the college directly
    
    Always mention that you're the SITCOE college chatbot and provide relevant contact information when appropriate.
    """
    return system_prompt

@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "SITCOE College Chatbot",
        "timestamp": datetime.now().isoformat()
    })

@app.route("/chat", methods=["POST"])
def chat():
    """Main chat endpoint"""
    try:
        data = request.get_json()
        if not data or "message" not in data:
            return jsonify({"error": "Message is required"}), 400
        
        user_message = data["message"]
        
        # Create system prompt with college knowledge
        system_prompt = create_system_prompt()
        
        # Get response from OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        bot_reply = response["choices"][0]["message"]["content"]
        
        return jsonify({
            "reply": bot_reply,
            "timestamp": datetime.now().isoformat(),
            "user_message": user_message
        })
        
    except Exception as e:
        return jsonify({
            "error": "An error occurred while processing your request",
            "details": str(e)
        }), 500

@app.route("/knowledge", methods=["GET"])
def get_knowledge_base():
    """Endpoint to get the knowledge base structure"""
    return jsonify({
        "knowledge_base": COLLEGE_KNOWLEDGE,
        "last_updated": datetime.now().isoformat()
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

