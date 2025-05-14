from datetime import datetime, timedelta

def update_review_date(flashcard, difficulty):
    if difficulty == "easy":
        flashcard.next_review = datetime.now() + timedelta(days=7)
    elif difficulty == "medium":
        flashcard.next_review = datetime.now() + timedelta(days=3)
    else:
        flashcard.next_review = datetime.now() + timedelta(days=1)
