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
        print(f"✅ {command}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running: {command}")
        print(f"Error: {e.stderr}")
        return None

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 9):
        print("❌ Python 3.9+ is required")
        print(f"Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} detected")
    return True

def check_node_version():
    """Check if Node.js is installed"""
    try:
        result = subprocess.run(['node', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Node.js {result.stdout.strip()} detected")
            return True
        else:
            print("❌ Node.js not found")
            return False
    except FileNotFoundError:
        print("❌ Node.js not found. Please install Node.js 16+")
        return False

def setup_backend():
    """Setup the Flask backend"""
    print("\n🔧 Setting up Backend...")
    
    if not os.path.exists('backend'):
        print("❌ Backend directory not found")
        return False
    
    # Install Python dependencies
    print("Installing Python dependencies...")
    if run_command('pip install -r requirements.txt', cwd='backend') is None:
        return False
    
    print("✅ Backend setup completed")
    return True

def setup_frontend():
    """Setup the React frontend"""
    print("\n🔧 Setting up Frontend...")
    
    if not os.path.exists('frontend'):
        print("❌ Frontend directory not found")
        return False
    
    # Install Node.js dependencies
    print("Installing Node.js dependencies...")
    if run_command('npm install', cwd='frontend') is None:
        return False
    
    print("✅ Frontend setup completed")
    return True

def create_env_file():
    """Create .env file from example"""
    backend_env_example = 'backend/env.example'
    backend_env = 'backend/.env'
    
    if os.path.exists(backend_env_example) and not os.path.exists(backend_env):
        print("\n📝 Creating .env file...")
        try:
            with open(backend_env_example, 'r') as f:
                content = f.read()
            
            with open(backend_env, 'w') as f:
                f.write(content)
            
            print("✅ .env file created from env.example")
            print("⚠️  Please update OPENAI_API_KEY in backend/.env with your actual API key")
        except Exception as e:
            print(f"❌ Error creating .env file: {e}")
    else:
        print("✅ .env file already exists or env.example not found")

def main():
    """Main setup function"""
    print("🚀 SITCOE College Chatbot Setup")
    print("=" * 40)
    
    # Check prerequisites
    if not check_python_version():
        print("\n❌ Setup failed: Python version incompatible")
        return
    
    if not check_node_version():
        print("\n❌ Setup failed: Node.js not found")
        return
    
    # Setup backend and frontend
    if not setup_backend():
        print("\n❌ Setup failed: Backend setup unsuccessful")
        return
    
    if not setup_frontend():
        print("\n❌ Setup failed: Frontend setup unsuccessful")
        return
    
    # Create environment file
    create_env_file()
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Add your OpenAI API key to backend/.env")
    print("2. Start the backend: cd backend && python app.py")
    print("3. Start the frontend: cd frontend && npm start")
    print("4. Open http://localhost:3000 in your browser")
    print("\n🔗 Backend will run on http://localhost:5000")
    print("🔗 Frontend will run on http://localhost:3000")

if __name__ == "__main__":
    main()



