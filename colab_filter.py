import argparse # парсит аргументы командной строки


def build_arg_parser():
    pars = argparse.ArgumentParser(description="Compute similarity score")
    pars.add_argument('--user', dest='user',
                      required=True, help="Input user")
    return pars
