#!/bin/bash
if [ -f dist ]; then
    rm -r dist
fi

sudo mk-build-deps --install debian/control

python3 setup.py sdist
cd dist

tar zxvf *.tar.gz
cd python3-otr-?.?.?

debuild --no-sign
