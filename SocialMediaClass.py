class SocialMediaAccount():
    def __init__(self, username, account_id, followers):
        self.username = username
        self.account_id = account_id
        self.followers = followers
        self.posts = []

    def add_post(self):
        choose = input("Do you want to add a post? (Yes/No): ")
        if choose.lower() == "yes":
            content = input("Enter your post content: ")
            self.posts.append(content)
            print("Post added successfully.")

    def delete_post(self):
        choose = input("Do you want to delete a post? (Yes/No): ")
        if choose.lower() == "yes":
            if not self.posts:
                print("No posts to delete.")
            else:
                for i, post in enumerate(self.posts, 1):
                    print(f"{i}. {post}")
                try:
                    index = int(input("Enter the number of the post to delete: ")) - 1
                    if 0 <= index < len(self.posts):
                        deleted = self.posts.pop(index)
                        print(f"Deleted post: {deleted}")
                    else:
                        print("Invalid choice.")
                except ValueError:
                    print("Please enter a valid number.")

    def get_followers(self):
        choose = input("Do you want to see your follower count? (Yes/No): ")
        if choose.lower() == "yes":
            print(f"Follower count: {self.followers}")

    def display_account_info(self):
        choose = input("Do you want to display your account information? (Yes/No): ")
        if choose.lower() == "yes":
            print(f"Username: {self.username}")
            print(f"Account ID: {self.account_id}")
            print(f"Followers: {self.followers}")
            print(f"Posts: {self.posts}")

class VerifiedAccount(SocialMediaAccount):
    def __init__(self, username, account_id, followers, verified=True):
        super().__init__(username, account_id, followers)
        self.verified = verified


# Example usage
account1 = VerifiedAccount("Srihith", "001", 1000)
account1.add_post()
account1.delete_post()
account1.get_followers()
account1.display_account_info()