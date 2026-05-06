class PasswordError(Exception):
    def __init__(self,msg,pas):
        self.pas=pas
        super().__init__(msg)
    def __str__(self):
        return f"{self.pas}"
s=input()
try:
    if len(s)<8:
        raise PasswordError("Password should be 8 characters",s)
except Exception as e:
    print(e)
