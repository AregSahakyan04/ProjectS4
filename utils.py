import datetime

def save_chat_to_file(history):
    with open("chat_log.txt", "a", encoding="utf-8") as f:
        f.write(f"\nSession started: {datetime.datetime.now()}\n")
        for sender, msg in history:
            f.write(f"{sender}: {msg}\n")
