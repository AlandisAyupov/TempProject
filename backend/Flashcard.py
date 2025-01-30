class Flashcard:
    def __init__(self, id, front, back, category=""):
        self.id = id
        self.front = front  # Question/prompt side
        self.back = back    # Answer side
        self.category = category
        self.is_flipped = False

    def to_dict(self):
        return {
            "id": self.id,
            "front": self.front,
            "back": self.back,
            "category": self.category,
            "is_flipped": self.is_flipped
        }
        
    def flip(self):
        """Flip the card from front to back or vice versa"""
        self.is_flipped = not self.is_flipped
        
    def get_current_side(self):
        """Return the current visible side of the card"""
        return self.back if self.is_flipped else self.front
    
    def check_answer(self, answer):
        """Check if the provided answer matches the back of the card"""
        return answer.lower().strip() == self.back.lower().strip()
    
    def update_card(self, front=None, back=None, category=None):
        """Update card content"""
        if front: self.front = front
        if back: self.back = back
        if category: self.category = category
        
    def __str__(self):
        """String representation of the card"""
        return f"Flashcard(front='{self.front}', back='{self.back}', category='{self.category}')"