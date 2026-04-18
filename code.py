import praw

reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="RedditResearch/1.0 by u/Abdelkayoum_nouri69"
)

subreddit_name = input("Enter subreddit name: ")
keywords = input("Enter keywords to filter (comma separated, or leave blank for all): ")
keyword_list = [k.strip().lower() for k in keywords.split(",")] if keywords else []

subreddit = reddit.subreddit(subreddit_name)

print(f"\nPosts from r/{subreddit_name}:\n")
for post in subreddit.hot(limit=50):
    title_lower = post.title.lower()
    body_lower = post.selftext.lower()

    if not keyword_list or any(k in title_lower or k in body_lower for k in keyword_list):
        print(f"Title : {post.title}")
        print(f"Body  : {post.selftext[:200] if post.selftext else 'N/A'}")
        print(f"Author: u/{post.author}")
        print(f"Link  : https://reddit.com{post.permalink}")
        print("---")
