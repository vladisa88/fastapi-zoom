import sys
import subprocess


def parse_arguments() -> str:
    """
    Read arguments from command line.
    Return message for migration
    """
    error_message = SystemExit(f"Usage: {sys.argv[0]} -m 'Your migration message'")
    option = sys.argv[1]
    if option.find('-m') == -1:
        raise error_message
    arguments = [arg for arg in sys.argv[2:]]
    if len(arguments) > 1:
        raise error_message
    return arguments[0]


def run_migration(msg: str) -> None:
    """
    Run alembic migration command
    """
    command = f'alembic revision --autogenerate -m {msg}'
    subprocess.run(command.split(' '), check=True, text=True, stdout=subprocess.PIPE)


if __name__ == '__main__':
    message = parse_arguments()
    run_migration(message)
