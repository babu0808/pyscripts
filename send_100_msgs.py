import pywhatkit as kit
import time

def send_multiple_messages(phone_number, message, count):
    """
    Sends multiple WhatsApp messages to a specific contact in a loop.

    Args:
        phone_number (str): Phone number of the recipient with country code (e.g., "+1234567890").
        message (str): Message to send.
        count (int): Number of messages to send.
    """
    for i in range(count):
        try:
            # Send the message
            kit.sendwhatmsg_instantly(phone_number, f"{message} #{i+1}", wait_time=10, tab_close=True)
            print(f"Message {i+1} sent successfully.")
            time.sleep(5)  # Wait a few seconds before sending the next message
        except Exception as e:
            print(f"An error occurred while sending message {i+1}: {e}")

# Example usage
phone_number = "+91 9666977183"  # Replace with the recipient's phone number (with country code)
message = "Hello! Darling"  # Replace with your message
send_multiple_messages(phone_number, message, 100)


# import pyautogui
# import time

# def send_message(contact, message, count):
#     # Open WhatsApp manually and focus on the app
#     print("Position the mouse over the search bar and press Ctrl+C.")
#     time.sleep(5)
#     for i in range(count):
#         pyautogui.typewrite(contact)  # Type contact name
#         pyautogui.press("enter")     # Open the contact
#         time.sleep(2)
#         pyautogui.typewrite(f"{message} #{i+1}")  # Type the message
#         pyautogui.press("enter")     # Send the message
#         time.sleep(1)

# # Example usage
# send_message("Mr Vinay Jalli", "Your mobile has been hacked", 100)
