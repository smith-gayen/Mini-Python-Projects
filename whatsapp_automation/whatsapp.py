import os
import sys
from twilio.rest import Client
from datetime import datetime, timedelta
import time

# Read Twilio credentials from environment variables (safer than hard-coding)
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_from = os.getenv("TWILIO_FROM_NUMBER", "whatsapp:+14155238886")  # default Twilio sandbox

if not account_sid or not auth_token:
    print("Error: TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN must be set as environment variables.")
    print("In PowerShell: $env:TWILIO_ACCOUNT_SID='AC...'; $env:TWILIO_AUTH_TOKEN='sk...'\nOr store them in your .env and load securely.")
    sys.exit(1)

client = Client(account_sid, auth_token)

def validate_whatsapp_number(number: str) -> bool:
    # basic validation: must start with + and contain digits
    if not number.startswith("+"):
        return False
    digits = number[1:].replace(" ", "").replace("-", "")
    return digits.isdigit()

def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_=twilio_from,
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent successfully! Message SID: {message.sid}')
    except Exception as e:
        print(f'An error occurred sending the message: {e}')

# --- User input (keeps behavior but with validations) ---
name = input('Enter the recipient name: ').strip()
recipient_number = input('Enter the recipient WhatsApp number with country code (e.g., +1234567890): ').strip()

if not validate_whatsapp_number(recipient_number):
    print("Invalid phone number format. Use +<countrycode><number>, e.g. +1234567890")
    sys.exit(1)

message_body = input(f'Enter the message you want to send to {name}: ').strip()

date_str = input('Enter the date to send the message (YYYY-MM-DD): ').strip()
time_str = input('Enter the time to send the message (HH:MM in 24-hour format): ').strip()

try:
    # NOTE: This uses local system timezone. For timezone-aware scheduling, use zoneinfo/pytz.
    schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
    current_datetime = datetime.now()
    time_difference = schedule_datetime - current_datetime
    delay_seconds = time_difference.total_seconds()

    if delay_seconds <= 0:
        print('The specified time is in the past. Please enter a future date and time.')
        sys.exit(1)

    print(f'Message scheduled to be sent to {name} at {schedule_datetime} (local time).')

    # Wait loop with progress and interrupt handling
    try:
        check_interval = 5  # seconds between checks; adjust as desired
        remaining = delay_seconds
        while remaining > 0:
            mins, secs = divmod(int(remaining), 60)
            hrs, mins = divmod(mins, 60)
            print(f"Time until send: {hrs:02d}:{mins:02d}:{secs:02d}", end="\r")
            sleep_time = min(check_interval, remaining)
            time.sleep(sleep_time)
            remaining -= sleep_time
        print()  # newline after progress line
    except KeyboardInterrupt:
        print("\nScheduling cancelled by user.")
        sys.exit(0)

    # Send the message
    send_whatsapp_message(recipient_number, message_body)

except ValueError as e:
    print(f'Invalid date or time format: {e}')
