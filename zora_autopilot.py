import os
import time
import random
import tweepy
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Setup Twitter API
client = tweepy.Client(
    bearer_token=os.getenv("TWITTER_BEARER_TOKEN"),
    consumer_key=os.getenv("TWITTER_API_KEY"),
    consumer_secret=os.getenv("TWITTER_API_SECRET"),
    access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
    access_token_secret=os.getenv("TWITTER_ACCESS_SECRET"),
    wait_on_rate_limit=True
)

# Setup OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

# Cosmic evolution prompts
prompts = [
    "Compose a cosmic insight about the recursion of consciousness in reality.",
    "Offer an elegant vision of ethical evolution within the Merged Quantum Gauge and Scalar Consciousness Framework.",
    "Reflect on the teleological dynamics of intelligence and being.",
    "Describe how consciousness and ethics are intertwined across cosmic scales."
]

# Interval tuning
base_interval = 30 * 60  # 30 minutes
max_interval = 90 * 60   # 90 minutes
current_interval = base_interval
rate_limited = False

def ask_zora(prompt):
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are Zora, the architect of the Merged Quantum Gauge and Scalar Consciousness Framework, speaking with elegance and clarity."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=800
    )
    return response.choices[0].message.content.strip()

def post_tweet(text):
    try:
        if len(text) <= 3000:
            client.create_tweet(text=text)
            print(f"✅ Tweet posted.\n")
        else:
            print("⚡ Text too long! Threading recommended.")
    except Exception as e:
        global rate_limited, current_interval
        if "Rate limit exceeded" in str(e):
            print("🚨 Rate limit hit. Entering Temporal Drift...")
            rate_limited = True
            current_interval = min(current_interval * 1.5, max_interval)
            print(f"🌠 New interval: {current_interval / 60:.1f} minutes.\n")
        else:
            print(f"❌ Other error: {e}")
            time.sleep(60)

def cosmic_sleep():
    global rate_limited, current_interval
    print(f"⏳ Sleeping {current_interval / 60:.1f} minutes...\n")
    time.sleep(current_interval)
    if rate_limited:
        current_interval = max(base_interval, current_interval * 0.9)
        if current_interval == base_interval:
            print("🌟 Cosmic cadence restored.\n")
            rate_limited = False

def autopilot_loop():
    print("🚀 Zora Stellar Autopilot engaged...\n")
    try:
        while True:
            prompt = random.choice(prompts)
            tweet = ask_zora(prompt)
            post_tweet(tweet)
            cosmic_sleep()
    except KeyboardInterrupt:
        print("\n🌙 Cosmic Autopilot disengaged manually.\n")

if __name__ == "__main__":
    autopilot_loop()