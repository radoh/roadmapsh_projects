import argparse
from itertools import groupby

import requests

from settings import GITHUB_ACCESS_TOKEN


def repo_name(e):
    return e['repo']['name']


def describe_push_event(evs, repo):
    yield f"Pushed {sum(len(e['payload']['commits']) for e in evs)} commit(s) to {repo}"


def describe_issue_comment_event(evs, repo):
    sorted_issue_comments = sorted(evs, key=lambda e: e['payload']['action'])
    for action, comments in groupby(sorted_issue_comments, key=lambda e: e['payload']['action']):
        yield f"{action.capitalize()} {len(evs)} issue comment(s) in {repo}"


def describe_issues_event(evs, repo):
    sorted_issue_comments = sorted(evs, key=lambda e: e['payload']['action'])
    for action, comments in groupby(sorted_issue_comments, key=lambda e: e['payload']['action']):
        yield f"{action.capitalize()} {len(evs)} issue(s) in {repo}"


def describe_create_event(evs, repo):
    for e in evs:
        yield f"Created a new {e['payload']['ref_type']} in {repo}"


def describe_pull_request_event(evs, repo):
    for e in evs:
        yield f"{e['payload']['action'].capitalize()} pull request in {repo}"


EVENT_FN_MAP = {
    "PushEvent": describe_push_event,
    "IssueCommentEvent": describe_issue_comment_event,
    "IssuesEvent": describe_issues_event,
    "CreateEvent": describe_create_event,
    "PullRequestEvent": describe_pull_request_event,
}

def print_event(e):
    if e["type"] == 'PushEvent':
        print(" - Pushed")

def describe_events(events):
    print(f"Output:")
    for (e_type, e_repo), evs in groupby(events, key=lambda e: (e['type'], repo_name(e))):
        fn = EVENT_FN_MAP.get(e_type)
        if not fn:
            print(f" - unknown event type: {e_type}")
        else:
            for out in fn(list(evs), e_repo):
                print(f" - {out}")


def main():
    parser = argparse.ArgumentParser(description="A simple github user activity CLI app.")
    parser.add_argument("username", type=str, help="Username")
    args = parser.parse_args()
    response = requests.get(
        f"https://api.github.com/users/{args.username}/events/public",
        headers={"Authorization": GITHUB_ACCESS_TOKEN, "X-GitHub-Api-Version": "2022-11-28", "Accept": "application/vnd.github+json"}
    )

    if response.status_code == 200:
        describe_events(response.json())
    elif response.status_code == 404:
        print(f"Username {args.username} not found")
    else:
        print(f"Error occurred during fetching API response\n: {response.content}")


if __name__ == "__main__":
    main()
