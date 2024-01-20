import argparse

import yaml

from preprocessor import vivos, vinbigdata


def main(config):
    if "vivos" in config["dataset"]:
        vivos.prepare_align(config["vivos"])
    if "vinbigdata" in config["dataset"]:
        vinbigdata.prepare_align(config["vinbigdata"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("config", type=str, help="path to preprocess.yaml")
    args = parser.parse_args()

    config = yaml.load(open(args.config, "r"), Loader=yaml.FullLoader)
    main(config)
