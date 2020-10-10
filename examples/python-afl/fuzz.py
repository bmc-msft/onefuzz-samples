#!/usr/bin/env python
#
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
import sys
import afl

def parse(data: bytes) -> bool:
    if len(data) < 4:
        return False

    cnt = 0

    if data[0] == b"x":
        cnt += 1
    if data[1] == b"y":
        cnt += 1
    if data[2] == b"z":
        cnt += 1

    funcs = {
        b'0': lambda: 10 / 0,
        b'1': lambda: b'\xff'.decode()
    }
    if cnt >= 3:
        print(here)
        funcs[data[3]]()

    return True

def fuzz_it():
    while afl.loop():
        sys.stdin.seek(0)
        data = sys.stdin.read()
        parse(data)
    os._exit(0) 

if __name__ == "__main__":
    fuzz_it()
