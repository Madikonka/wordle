class Wordle:
    WORD_SIZE = 5
    MAX_ATTEMPTS = 5

    def __init__(self, secret: str) -> None:
        self.secret = secret
        self.attempt = []
    
    """ Checks if the input word is secret
    Input word is added to the attempts list"""
    @property
    def is_solved(self) -> bool:
        if (len(self.attempt)>0):
            return self.attempt[-1]==self.secret
        return False
    
    """how many attempts left"""
    @property
    def remaining_attempts(self) -> int:
        return self.MAX_ATTEMPTS-len(self.attempt)

    @property
    def can_attempt(self):
        return self.remaining_attempts>0 and not self.is_solved

    """adding a word to the tries list """
    
    def adding_attempts(self, word: str) -> list:
        return self.attempt.append(word)