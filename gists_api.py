import requests


def get_gists(user):
    """Get list of user's gists"""
    response = requests.get('https://api.github.com/users/' + user + '/gists')
    return response


def main():
    gists = get_gists()
    print(gists)

if __name__ == "__main__":
    main()