"""Example of class and projects."""

class Profile: 
    handle: str 
    followers: int 
    is_private: bool 

    def __init__(self, handle: str): 
        """Constructor initializes attributes."""
        self.handle = handle 
        self.followers = 0 
        self.is_private = False

    def tweet(self, msg: str) -> None:
        print(f"@{self.handle} tweets {msg}")

my_profile: Profile = Profile("audrey")
# check for constructor call under profile class 
my_profile.tweet("I accidentally typed prolife instead of profile.")
my_profile.followers += 1