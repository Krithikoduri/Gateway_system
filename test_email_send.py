
import os
from dotenv import load_dotenv
from email_service import send_parent_approval_email

# Load environment variables
load_dotenv()

def test_send():
    print("🧪 Testing Email Service...")
    
    # Test data
    parent_email = "kruthikab21@gmail.com"
    student_name = "Test Student (G5)"
    request_type = "casual"
    leave_date = "2026-03-10"
    leave_time = "10:00"
    reason = "This is a test request to verify the email service is working correctly."
    token = "TEST_TOKEN_12345"
    
    success = send_parent_approval_email(
        parent_email, 
        student_name, 
        request_type, 
        leave_date, 
        leave_time, 
        reason, 
        token
    )
    
    if success:
        print("\n✅ SUCCESS! Test email sent to " + parent_email)
        print("Please check your inbox (and spam folder) for the test email.")
    else:
        print("\n❌ FAILED! Could not send email. Check your SMTP credentials in .env")

if __name__ == "__main__":
    test_send()
