import streamlit as st
from collections import deque

# Email class to store email details
class Email:
    def __init__(self, sender, subject, message):
        self.sender = sender
        self.subject = subject
        self.message = message

# Queue to manage email processing
email_queue = deque()

# Function to display email queue
def display_queue():
    if len(email_queue) == 0:
        st.write("No emails in the queue.")
    else:
        st.write("Emails in the queue:")
        for i, email in enumerate(email_queue):
            st.write(f"{i+1}. From: {email.sender}, Subject: {email.subject}")

# Function to process (dequeue) an email
def process_email():
    if len(email_queue) > 0:
        email = email_queue.popleft()
        st.write(f"Processing email from: {email.sender}")
        st.write(f"Subject: {email.subject}")
        st.write(f"Message: {email.message}")
        st.write(f"Automated Response Sent to: {email.sender}")
    else:
        st.write("No emails to process.")

# Streamlit app layout
st.title("Automated Email Response System")

# Input fields for email details
sender = st.text_input("Sender Email")
subject = st.text_input("Email Subject")
message = st.text_area("Email Message")

# Add email to queue
if st.button("Add Email to Queue"):
    if sender and subject and message:
        new_email = Email(sender, subject, message)
        email_queue.append(new_email)
        st.success("Email added to the queue.")
    else:
        st.error("Please fill in all the fields.")

# Display the current email queue
st.subheader("Current Email Queue")
display_queue()

# Process the next email in the queue
if st.button("Process Next Email"):
    process_email()
