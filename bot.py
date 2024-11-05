import requests
import os
from dotenv import load_dotenv


load_dotenv()

def send_document(bot_token, chat_id, document_path):
    url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
    files = {'document': open(document_path, 'rb')}
    data = {'chat_id': chat_id}
    
    try:
        response = requests.post(url, files=files, data=data)
        if response.status_code == 200:
            print("Document sent successfully.")
        else:
            print(f"Failed to send document. Status code: {response.status_code}")
            print(response.json())
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        files['document'].close()

# Replace these values with your actual bot token, chat ID, and file path
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
chat_id = os.getenv('TELEGRAM_CHAT_ID')
document_path = os.path.join(os.path.expanduser("~"), "Documents", "scan_results.txt")
document_path2 = os.path.join(os.path.expanduser("~"), "Documents", "port_scan_results.txt")


send_document(bot_token, chat_id, document_path)
send_document(bot_token,chat_id,document_path2)
