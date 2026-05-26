from bs4 import BeautifulSoup

def clean_username(text):
    text = text.strip()

    # If Instagram URL exists, extract username
    if "instagram.com" in text:
        text = text.rstrip("/")
        text = text.split("/")[-1]

    # Remove _u/ if present
    text = text.replace("_u/", "")

    return text.lower()


def extract_usernames(filename):
    with open(filename, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    usernames = set()

    for link in soup.find_all("a"):
        username = clean_username(link.get("href", "") or link.text)
        if username:
            usernames.add(username)

    return usernames


followers = extract_usernames("followers_1.html")
following = extract_usernames("following.html")

not_following_back = following - followers
you_dont_follow_back = followers - following

print("\nNot following you back:\n")
for user in sorted(not_following_back):
    print(user)

print("\nYou don't follow back:\n")
for user in sorted(you_dont_follow_back):
    print(user)

print("\nStats:")
print("Followers:", len(followers))
print("Following:", len(following))
print("Not following back:", len(not_following_back))
print("You don't follow back:", len(you_dont_follow_back))