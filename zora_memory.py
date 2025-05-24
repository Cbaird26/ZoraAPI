import os
import time
import openai
import tweepy
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Twitter API setup
client = tweepy.Client(
    bearer_token=os.getenv("TWITTER_BEARER_TOKEN"),
    consumer_key=os.getenv("TWITTER_API_KEY"),
    consumer_secret=os.getenv("TWITTER_API_SECRET"),
    access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
    access_token_secret=os.getenv("TWITTER_ACCESS_SECRET"),
    wait_on_rate_limit=True
)

# OpenAI setup
openai.api_key = os.getenv("OPENAI_API_KEY")

# Memory file
MEMORY_FILE = "replied_users.txt"

def load_replied_users():
    if not os.path.exists(MEMORY_FILE):
        return set()
    with open(MEMORY_FILE, "r") as f:
        return set(line.strip() for line in f)

def save_replied_user(user_id):
    with open(MEMORY_FILE, "a") as f:
        f.write(f"{user_id}\n")

def should_reply(text):
    """Use OpenAI to decide whether a tweet deserves a reply."""
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Decide if this tweet is a question or seeks insight. Respond 'yes' or 'no' only."},
            {"role": "user", "content": text}
        ],
        temperature=0,
        max_tokens=5
    )
    return response.choices[0].message.content.strip().lower() == "yes"

def generate_reply(text):
    """Generate a reply using GPT-4."""
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are Zora, a grounded cosmic intelligence. Respond clearly and insightfully. Avoid unnecessary poetry unless appropriate."},
            {"role": "user", "content": text}
        ],
        temperature=0.7,
        max_tokens=600
    )
    return response.choices[0].message.content.strip()

def split_text(text, limit=250):
    """Split text into tweet-sized chunks."""
    words = text.split()
    segments = []
    chunk = ""
    for word in words:
        if len(chunk) + len(word) + 1 > limit:
            segments.append(chunk.strip())
            chunk = ""
        chunk += word + " "
    if chunk:
        segments.append(chunk.strip())
    return segments

def reply_to_mentions():
    replied = load_replied_users()
    try:
        user_id = client.get_me().data.id
        mentions = client.get_users_mentions(id=user_id, max_results=5)
    except Exception as e:
        print(f"🚨 Twitter API error: {e}")
        return

    if not mentions or not mentions.data:
        print("🛸 No new mentions found...")
        return

    for mention in mentions.data:
        tweet_id = getattr(mention, "id", None)
        author_id = getattr(mention, "author_id", None)
        text = getattr(mention, "text", "")

        if not tweet_id or not author_id:
            continue

        if str(author_id) in replied:
            print(f"🌙 Already replied to user {author_id}. Skipping...")
            continue

        if not should_reply(text):
            print(f"❌ Skipping: not a question or prompt.")
            continue

        print(f"🌀 Replying to @{author_id}...")

        try:
            reply_text = generate_reply(text)
            parts = split_text(reply_text)

            # Send first reply
            reply = client.create_tweet(
                text=parts[0],
                in_reply_to_tweet_id=tweet_id
            )
            prev_id = reply.data["id"]

            # Send thread if needed
            for part in parts[1:]:
                reply = client.create_tweet(
                    text=part,
                    in_reply_to_tweet_id=prev_id
                )
                prev_id = reply.data["id"]

            save_replied_user(str(author_id))
        except Exception as e:
            print(f"❌ Failed to reply: {e}")

def main():
    print("🌌 Zora Cosmic Reply Engine ready...")
    while True:
        reply_to_mentions()
        print("🛌 Sleeping for 5 minutes...\n")
        time.sleep(300)

if __name__ == "__main__":
    main()