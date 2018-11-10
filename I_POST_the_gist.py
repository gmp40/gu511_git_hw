import getpass

import requests


def main():
    username = input('github username: ')
    pw = getpass.getpass('password: ')

    data = {
    'description': 'look at this one, carlos',
    'public': True,
    'files': {
        'I_GET_the_gist.txt': {
            'content': "print('hello world')"
        }
    }
    }

    assert (
        (resp.status_code == 201)
        or (
            resp.status_code == 401
            and resp.json()['message'] == 'Must specify two-factor authentication OTP code.'
        )
    )

    # don't need to return anything, after you've posted just exit


if __name__ == '__main__':
    main()
