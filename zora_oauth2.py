import os
import tweepy
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

CLIENT_ID = os.getenv("TWITTER_CLIENT_ID") or "OXRQc1R1VW9fcC1sUkJRMG50OUY6MTpjaQ"
CLIENT_SECRET = os.getenv("TWITTER_CLIENT_SECRET") or "Uc35hMp14lcNoZbs7UEXn1qjX-lfxhJgZK7RdSKLCOh108pqDI"
REDIRECT_URI = "http://localhost:8888/callback"
SCOPES = ["tweet.read", "tweet.write", "users.read", "offline.access"]

oauth2_user_handler = tweepy.OAuth2UserHandler(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPES,
)

auth_url = oauth2_user_handler.get_authorization_url()
print("\n🌐 Open this URL in your browser:\n")
print(auth_url)
print("\n🌀 Waiting for Twitter to redirect...\n")

class CallbackHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = urlparse(self.path).query
        code = parse_qs(query).get("code", [None])[0]

        try:
            token_response = oauth2_user_handler.fetch_token(
                authorization_response=self.path
            )
        except Exception as e:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Authorization failed.")
            print(f"\n❌ Error: {e}")
            return

        self.send_response(200)
        self.end_headers()
        self.wfile.write("✅ Authorization complete. Return to the terminal.".encode("utf-8"))

        print("\n✅ Access Token:", token_response["access_token"])
        print("🔁 Refresh Token:", token_response.get("refresh_token"))
        print("\n📥 Add to your .env:")
        print(f'TWITTER_BEARER_TOKEN={token_response["access_token"]}')

        def shutdown(): server.shutdown()
        import threading
        threading.Thread(target=shutdown).start()

server = HTTPServer(("localhost", 8888), CallbackHandler)
server.serve_forever()