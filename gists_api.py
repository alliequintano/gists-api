import requests


def get_gists():
    """Get list of user's gists"""
    response = requests.get('https://api.github.com/users/octocat/gists')
    return response


def main():
    gists = get_gists()
    print(gists)

if __name__ == "__main__":
    main()