#!/usr/bin/env python3
"""
Simple test script to verify the Flask app can start without errors.
This helps identify any import or configuration issues before deployment.
"""

try:
    from app import app
    print("✅ Successfully imported Flask app")
    print(f"App type: {type(app)}")
    print(f"App name: {app.name}")
    print("✅ App import test passed!")
    
except Exception as e:
    print(f"❌ Error importing app: {e}")
    import traceback
    traceback.print_exc() 