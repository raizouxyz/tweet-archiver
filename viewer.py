import json

with open('./tweets.json', mode='r', encoding='utf-8') as f:
    tweet_data = json.loads(f.read())
    tweet_elements = ''
    for tweet in tweet_data["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][1]["entries"]:
        if 'legacy' in tweet["content"]["itemContent"]["tweet_results"]["result"]:
            tweet_elements += f'<div><img src="{tweet["content"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"]["legacy"]["profile_image_url_https"]}" alt="banner" style="width: 40px; height: 40px;"><span style="font-size: 20px; margin-right: 10px;">{tweet["content"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"]["legacy"]["name"]}</span><span style="color: gray;">@{tweet["content"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"]["legacy"]["screen_name"]}</span>・<span style="color: gray;">@{tweet["content"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"]["legacy"]["created_at"]}</span><div>{tweet["content"]["itemContent"]["tweet_results"]["result"]["legacy"]["full_text"]}</div><span style="color: gray; margin-right: 20px;">Reply: {tweet["content"]["itemContent"]["tweet_results"]["result"]["legacy"]["reply_count"]}</span><span style="color: gray; margin-right: 20px;">Retweets: {tweet["content"]["itemContent"]["tweet_results"]["result"]["legacy"]["retweet_count"]}</span><span style="color: gray; margin-right: 20px;">Like: {tweet["content"]["itemContent"]["tweet_results"]["result"]["legacy"]["favorite_count"]}</span><span style="color: gray; margin-right: 20px;">Views: None</span><hr></div>\n'
        if 'profile_banner_url' in tweet_data["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][1]["entries"][0]["content"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"]["legacy"]:
            html = f'<!DOCTYPE html><html lang="ja"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{tweet_data["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][1]["entries"][0]["content"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"]["legacy"]["name"]}（@{tweet_data["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][1]["entries"][0]["content"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"]["legacy"]["screen_name"]}）さん / X</title></head><body style="background-color: black; color: white;"><div style="width: 598.4px; margin:0 auto;"><img src="{tweet_data["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][1]["entries"][0]["content"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"]["legacy"]["profile_banner_url"]}" alt="banner" style="width: 598.4px; height: 199.46;"><div><img src="{tweet_data["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][1]["entries"][0]["content"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"]["legacy"]["profile_image_url_https"]}" alt="banner" style="width: 133.6px; height: 133.6;"><br><span style="font-size: 30px;">{tweet_data["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][1]["entries"][0]["content"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"]["legacy"]["name"]}</span><br><span style="color: gray; font-size: 20px;">@{tweet_data["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][1]["entries"][0]["content"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"]["legacy"]["screen_name"]}</span><br>{tweet_data["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][1]["entries"][0]["content"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"]["legacy"]["description"]}<br><span style="color: gray; margin-right: 20px;">Location: {tweet_data["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][1]["entries"][0]["content"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"]["legacy"]["location"]}</span><span style="color: gray;">Created At: {tweet_data["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][1]["entries"][0]["content"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"]["legacy"]["created_at"]}</span><br><span style="color: gray; margin-right: 20px;">Following:<span style="color: white;">{tweet_data["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][1]["entries"][0]["content"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"]["legacy"]["friends_count"]}</span></span><span style="color: gray;">Follower:<span style="color: white;">{tweet_data["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][1]["entries"][0]["content"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"]["legacy"]["followers_count"]}</span></span></div><hr><div class="tweets">{tweet_elements}</div></div></body></html>'
        else:
            html = f'<!DOCTYPE html><html lang="ja"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{tweet_data["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][1]["entries"][0]["content"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"]["legacy"]["name"]}（@{tweet_data["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][1]["entries"][0]["content"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"]["legacy"]["screen_name"]}）さん / X</title></head><body style="background-color: black; color: white;"><div style="width: 598.4px; margin:0 auto;"><div><img src="{tweet_data["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][1]["entries"][0]["content"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"]["legacy"]["profile_image_url_https"]}" alt="banner" style="width: 133.6px; height: 133.6;"><br><span style="font-size: 30px;">{tweet_data["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][1]["entries"][0]["content"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"]["legacy"]["name"]}</span><br><span style="color: gray; font-size: 20px;">@{tweet_data["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][1]["entries"][0]["content"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"]["legacy"]["screen_name"]}</span><br>{tweet_data["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][1]["entries"][0]["content"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"]["legacy"]["description"]}<br><span style="color: gray; margin-right: 20px;">Location: {tweet_data["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][1]["entries"][0]["content"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"]["legacy"]["location"]}</span><span style="color: gray;">Created At: {tweet_data["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][1]["entries"][0]["content"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"]["legacy"]["created_at"]}</span><br><span style="color: gray; margin-right: 20px;">Following:<span style="color: white;">{tweet_data["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][1]["entries"][0]["content"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"]["legacy"]["friends_count"]}</span></span><span style="color: gray;">Follower:<span style="color: white;">{tweet_data["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][1]["entries"][0]["content"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"]["legacy"]["followers_count"]}</span></span></div><hr><div class="tweets">{tweet_elements}</div></div></body></html>'
        with open('tweets.html', mode='w', encoding='utf-8') as f:
            f.write(html)