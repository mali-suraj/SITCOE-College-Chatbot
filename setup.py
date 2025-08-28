#!/usr/bin/env python3
"""
SITCOE College Chatbot Setup Script
This script automates the setup process for both backend and frontend.
"""

import os
import sys
import subprocess
import platform

def run_command(command, cwd=None):
    """Run a shell command and return the result"""
    try:
        result = subprocess.run(
            command,
            shell=True,
            cwd=cwd,
            capture_output=True,
            text=True,
            check=True
        )
        print(f"OK: {command}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running: {command}")
        print(f"Error: {e.stderr}")
        return None

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 9):
        print("Python 3.9+ is required")
        print(f"Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"Python {version.major}.{version.minor}.{version.micro} detected")
    return True

def check_node_version():
    """Check if Node.js is installed"""
    try:
        result = subprocess.run(['node', '--version'], capture_output=True, text=True)
        if result.returncode != 0:
            print("Node.js not found")
            return False

        version_str = result.stdout.strip().lstrip('v')
        parts = version_str.split('.')
        major = int(parts[0]) if parts and parts[0].isdigit() else 0
        print(f"Node.js v{version_str} detected")
        if major < 18:
            print("Node.js 18+ is required for Vite 5")
            return False
        return True
    except FileNotFoundError:
        print("Node.js not found. Please install Node.js 18+")
        return False

def setup_backend():
    """Setup the Flask backend"""
    print("\nSetting up Backend...")
    
    if not os.path.exists('backend'):
        print("Backend directory not found")
        return False
    
    # Install Python dependencies
    print("Installing Python dependencies...")
    if run_command('pip install -r requirements.txt', cwd='backend') is None:
        return False
    
    print("Backend setup completed")
    return True

def setup_frontend():
    """Setup the React frontend"""
    print("\nSetting up Frontend...")
    
    if not os.path.exists('frontend'):
        print("Frontend directory not found")
        return False
    
    # Ensure src directory exists
    os.makedirs(os.path.join('frontend', 'src'), exist_ok=True)

    # Auto-create App.jsx if missing
    app_path = os.path.join('frontend', 'src', 'App.jsx')
    if not os.path.exists(app_path):
        print("Creating missing frontend/src/App.jsx ...")
        try:
            with open(app_path, 'w', encoding='utf-8') as f:
                f.write(
                    "import React, { useState } from 'react'\n\n"
                    "export default function App() {\n"
                    "\tconst [message, setMessage] = useState('')\n"
                    "\tconst [reply, setReply] = useState('')\n"
                    "\tconst [isLoading, setIsLoading] = useState(false)\n"
                    "\tconst [error, setError] = useState('')\n\n"
                    "\tasync function sendMessage(event) {\n"
                    "\t\tevent.preventDefault()\n"
                    "\t\tsetIsLoading(true)\n"
                    "\t\tsetError('')\n"
                    "\t\tsetReply('')\n"
                    "\t\ttry {\n"
                    "\t\t\tconst response = await fetch('http://localhost:5000/chat', {\n"
                    "\t\t\t\tmethod: 'POST',\n"
                    "\t\t\t\theaders: { 'Content-Type': 'application/json' },\n"
                    "\t\t\t\tbody: JSON.stringify({ message })\n"
                    "\t\t\t})\n"
                    "\t\t\tconst data = await response.json()\n"
                    "\t\t\tif (!response.ok) { throw new Error(data?.error || 'Request failed') }\n"
                    "\t\t\tsetReply(data?.reply || '')\n"
                    "\t\t} catch (err) { setError(err.message) } finally { setIsLoading(false) }\n"
                    "\t}\n\n"
                    "\treturn (\n"
                    "\t\t<div className=\"min-h-screen p-6 flex flex-col gap-4\">\n"
                    "\t\t\t<h1 className=\"text-2xl font-semibold\">SITCOE College Chatbot</h1>\n"
                    "\t\t\t<form onSubmit={sendMessage} className=\"flex gap-2\">\n"
                    "\t\t\t\t<input className=\"flex-1 border rounded px-3 py-2\" placeholder=\"Ask something...\" value={message} onChange={(e) => setMessage(e.target.value)} />\n"
                    "\t\t\t\t<button type=\"submit\" className=\"bg-blue-600 text-white px-4 py-2 rounded disabled:opacity-50\" disabled={!message || isLoading}>{isLoading ? 'Sending...' : 'Send'}</button>\n"
                    "\t\t\t</form>\n"
                    "\t\t\t{error && <div className=\"border rounded p-3 bg-red-50 text-red-700\">{error}</div>}\n"
                    "\t\t\t{reply && !error && <div className=\"border rounded p-3 bg-white whitespace-pre-wrap\">{reply}</div>}\n"
                    "\t\t</div>\n"
                    "\t)\n"
                    "}\n"
                )
            print("Created frontend/src/App.jsx")
        except Exception as e:
            print(f"Failed to create App.jsx: {e}")

    # Install Node.js dependencies
    print("Installing Node.js dependencies...")
    if run_command('npm install', cwd='frontend') is None:
        return False
    
    print("Frontend setup completed")
    return True

def create_env_file():
    """Create .env file from example"""
    backend_env_example = 'backend/env.example'
    backend_env = 'backend/.env'
    
    if os.path.exists(backend_env_example) and not os.path.exists(backend_env):
        print("\nCreating .env file...")
        try:
            with open(backend_env_example, 'r') as f:
                content = f.read()
            
            with open(backend_env, 'w') as f:
                f.write(content)
            
            print(".env file created from env.example")
            print("Please update OPENAI_API_KEY in backend/.env with your actual API key")
        except Exception as e:
            print(f"Error creating .env file: {e}")
    else:
        print(".env file already exists or env.example not found")

def main():
    """Main setup function"""
    print("SITCOE College Chatbot Setup")
    print("=" * 40)
    
    # Check prerequisites
    if not check_python_version():
        print("\nSetup failed: Python version incompatible")
        return
    
    if not check_node_version():
        print("\nSetup failed: Node.js not found or version too low")
        return
    
    # Setup backend and frontend
    if not setup_backend():
        print("\nSetup failed: Backend setup unsuccessful")
        return
    
    if not setup_frontend():
        print("\nSetup failed: Frontend setup unsuccessful")
        return
    
    # Create environment file
    create_env_file()
    
    print("\nSetup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Add your OpenAI API key to backend/.env")
    print("2. Start the backend: cd backend && python app.py")
    print("3. Start the frontend: cd frontend && npm run dev")
    print("4. Open http://localhost:3000 in your browser")
    print("\nBackend will run on http://localhost:5000")
    print("Frontend will run on http://localhost:3000")

if __name__ == "__main__":
    main()






