import re

class PasswordChecker:

    def __init__(self, password):
        self.password = password

    def CheckLower(self) -> bool:
        """Check if the password contains at least one lowercase letter."""
        if isinstance(self.password, str):
            return bool(re.search(r"[a-zçşəıöğ]", self.password))
        return False
    
    def CheckUpper(self) -> bool:
        """Check if the password contains at least one uppercase letter."""
        if isinstance(self.password, str):
            return bool(re.search(r"[A-ZÇŞƏİÖĞ]", self.password))
        return False
    
    def CheckNumber(self) -> bool:
        """Check if the password contains at least one digit."""
        if isinstance(self.password, str):
            return bool(re.search(r"[0-9]", self.password))
        return False
    
    def CheckPunctuation(self) -> bool:
        """Check if the password contains a dot or a comma."""
        if isinstance(self.password, str):
            return bool(re.search(r"[.,]", self.password))
        return False
    
    def CheckLength(self) -> bool:
        """Check if the password is at least 8 characters long."""
        if isinstance(self.password, str):
            return bool(len(self.password) >= 8)
        return False
    
    def AllChecker(self) -> bool:
        """Check if the password meets all the criteria."""
        if isinstance(self.password, str):
            return all([
                self.CheckLower(),
                self.CheckUpper(),
                self.CheckNumber(),
                self.CheckPunctuation(),
                self.CheckLength()
            ])
        return False


password = PasswordChecker(input("Enter you password:"))
print(PasswordChecker.AllChecker(password))