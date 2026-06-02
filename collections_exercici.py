import urllib.request
import json

EVENT_SCORES ={
    "PushEvent":5,
    "CreatEvent":4,
    "IssuesEvent":3,
    "CommitCommentEvent":2

}

def get_event_scores(event):
    type_event = event.get("type")
    return EVENT_SCORES.get(type_event,1)

def calculate_scores(event_list):
    points= map(get_event_scores,event_list)
    return sum(points)


#Testing
def run_test():
    mock_events = [
        {"type": "PushEvent"},
        {"type":"CreatEvent"},
        {"type":"IssuesEvent"},
        {"type":"CommitCommentEvent"},
        {"type":"PullRequestEvent"},
        {"type":"ForkEvent"}
    ]

    assert calculate_scores(mock_events) == 16
    print("Test successfully completed")

def get_real_scores(username):
    url="https://api.github.com/users/{username}/events"
    try:
        response = urllib.request.urlopen(url)
        events = json.loads(response.read())
        final_score = calculate_scores(events)
        print(f"The current GitHub Score for user {username} is: {final_score}")
    except Exception as e:
        print(f"Error connecting to GitHub for user {username}: {e}")

if __name__ == "__main__": 
    run_test()
    get_real_scores("badchoice")

