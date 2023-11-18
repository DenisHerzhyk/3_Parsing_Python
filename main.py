import requests
import fake_useragent

session = requests.Session()

link = "https://id.unity.com/en/conversations/bf70c8e3-472f-4a8d-aa56-d423da7904cd01af"

user = fake_useragent.UserAgent().random
header = {'user-agent': user}

data = {
    "conversations_create_session_form[email]": "denis.herzhyk@gmail.com",
    "conversations_create_session_form[password]": "denis2004g"
}

response = session.post(link,data=data,headers=header).text

profile_info = "https://id.unity.com/en/account/edit"
profile_response = session.get(profile_info,headers = header).text
print(profile_response)





# Session
# Autorisation
# Get/Set cookies
# Email - denis.herzhyk@gmail.com
# Password - denis2004g
