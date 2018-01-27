#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bincrafters import build_template_boost_default


if __name__ == "__main__":
    builder = build_template_boost_default.get_builder(args="--build=missing", pure_c=True)
    builder.run()