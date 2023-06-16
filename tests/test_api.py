# -*- coding: utf-8 -*-

from adam_awesome import api


def test():
    _ = api


if __name__ == "__main__":
    from adam_awesome.tests import run_cov_test

    run_cov_test(__file__, "adam_awesome.api", preview=False)
