#!/usr/bin/env python3
"""
Test script for SITCOE College Chatbot Backend
Run this to test if your backend is working correctly
"""

import requests
import json
import time

def test_backend():
    """Test the backend endpoints"""
    base_url = "http://127.0.0.1:5000"
    
    print("🧪 Testing SITCOE College Chatbot Backend")
    print("=" * 50)
    
    # Test 1: Health Check
    print("\n1. Testing Health Check...")
    try:
        response = requests.get(f"{base_url}/health")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Health Check: {data['status']}")
            print(f"   Service: {data['service']}")
            print(f"   Timestamp: {data['timestamp']}")
        else:
            print(f"❌ Health Check failed: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to backend. Is it running?")
        print("   Start the backend with: cd backend && python app.py")
        return False
    
    # Test 2: Knowledge Base
    print("\n2. Testing Knowledge Base...")
    try:
        response = requests.get(f"{base_url}/knowledge")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Knowledge Base loaded successfully")
            print(f"   Categories: {list(data['knowledge_base'].keys())}")
            print(f"   Last Updated: {data['last_updated']}")
        else:
            print(f"❌ Knowledge Base failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Knowledge Base error: {e}")
    
    # Test 3: Chat Endpoint
    print("\n3. Testing Chat Endpoint...")
    test_messages = [
        "Tell me about SITCOE admissions",
        "What courses are available?",
        "How are the placements?"
    ]
    
    for i, message in enumerate(test_messages, 1):
        print(f"\n   Test {i}: '{message}'")
        try:
            response = requests.post(
                f"{base_url}/chat",
                json={"message": message},
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                data = response.json()
                print(f"   ✅ Response received")
                print(f"   📝 Reply: {data['reply'][:100]}...")
                print(f"   ⏰ Timestamp: {data['timestamp']}")
            else:
                print(f"   ❌ Chat failed: {response.status_code}")
                if response.text:
                    print(f"   Error: {response.text}")
        except Exception as e:
            print(f"   ❌ Chat error: {e}")
        
        # Small delay between requests
        time.sleep(1)
    
    print("\n" + "=" * 50)
    print("🎉 Backend testing completed!")
    print("\n📋 Next steps:")
    print("1. If all tests passed, your backend is working correctly")
    print("2. Start the frontend: cd frontend && npm start")
    print("3. Open http://localhost:3000 in your browser")
    print("4. Test the full chatbot interface")
    
    return True

if __name__ == "__main__":
    test_backend()







