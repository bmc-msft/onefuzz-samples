#!/usr/bin/env python
#
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.


from pythonfuzz.main import PythonFuzz


@PythonFuzz
def parse(data: bytes) -> bool:
    if len(data) < 4:
        return False

    if data[0] != b"A":
        return
    if data[1] != b"B":
        return
    if data[2] != b"C":
        return

    funcs = {
        b'0': lambda: 10 / 0,
        b'1': lambda: b'\xff'.decode()
    }
    funcs[data[3]]()

    return True

if __name__ == "__main__":
    parse()
