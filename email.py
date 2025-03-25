class Email:
    """
    Represents email message in the inbox.

    Each email has a sender's address, a subject line, and content.
    Emails can be marked as read once opened.
    """

    has_been_read = False

    def __init__(self, email_address, subject_line, email_content):
        """
        Initializes an Email object with details and message content.

        Args:
            email_address: The sender's email address.
            subject_line: The subject of the email.
            email_content: The body/content of the email.
        """
        self.email_address = email_address
        self.subject_line = subject_line
        self.content = email_content

    def mark_as_read(self):
        """Marks the email as read.

       Changes the email’s status to True so it no longer appears
       in the unread list.
       """
        self.has_been_read = True


# Inbox to store email objects
inbox = []


# Function to populate inbox with sample emails
def populate_inbox():
    email1 = Email("alice@gmail.com", "Hello!", "Welcome to HyperionDev!")
    email2 = Email(
        "bob@gmail.com",
        "Update!",
        "Great work on the previous task!")
    email3 = Email("charlie@gmail.com", "News!", "Latest company news.")

    inbox.extend([email1, email2, email3])


def list_emails():
    """Displays all emails in the inbox with their corresponding index.

    Allows users to see the subject lines of available emails and choose one
    to read.
    """
    print("\nInbox:")
    for i, _ in enumerate(inbox):
        print(f"{i}. {email.subject_line}")

# Function to read an email


def read_email(index):
    """
    Opens an email and displays its details.

    Args:
        index (int): The position of the email in the inbox.
    """
    if 0 <= index < len(inbox):  # Check if index is valid
        selected_email = inbox[index]
        print(f"\nFrom: {selected_email.email_address}")
        print(f"Subject: {selected_email.subject_line}")
        print(f"Content: {selected_email.content}\n")

        selected_email.mark_as_read()
        print(f"Email from {selected_email.email_address} marked as read.\n")
    else:
        print("\nInvalid email index. Please try again.\n")


# Populate the inbox at the start
populate_inbox()

# Main menu loop
while True:
    user_choice = input('''\nWould you like to:
1. Read an email
2. View unread emails
3. Quit application

Enter selection: ''')

    if user_choice == "1":
        list_emails()
        try:
            email_index = int(
                input(
                    "\nEnter the index number of the email to read "
                    "from the option: "
                ))
            read_email(email_index)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    elif user_choice == "2":
        print("\nUnread Emails:")
        for email in inbox:
            if not email.has_been_read:
                print(f"{email.subject_line}")

    elif user_choice == "3":
        print("\nExiting application. Goodbye!")
        break

    else:
        print("\nOops - incorrect input. Please try again.")
