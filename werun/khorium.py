import os
import subprocess


def print_env_vars():
    for k, v in os.environ.items():
        print('{}={}'.format(k, v))


def get_dest(repo):
    reponame = os.path.basename(repo)
    if reponame.endswith('.git'):
        reponame = reponame[:-len('.git')]
    return os.path.join(os.getenv('PHISTAGE_WORKING_DIR'), reponame)


def clone(repo):
    username = os.getenv('KHORIUMSTEP_INPUT_USERNAME')
    token = os.getenv('KHORIUMSTEP_INPUT_TOKEN')
    dest = get_dest(repo)
    subprocess.check_call(['git', 'clone', 'https://{}:{}@{}'.format(username, token, repo), dest])


if __name__ == '__main__':
    # just for fun testing
    print('khorium step begins')
    print_env_vars()

    repo = os.getenv('KHORIUMSTEP_INPUT_REPO')
    clone(repo)
    print('khorium step ends')
