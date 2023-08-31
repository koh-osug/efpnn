The PNN file is using the [ETSI TS 124 008 10.5.3.5a Network Name encoding](https://www.etsi.org/deliver/etsi_ts/124000_124099/124008/13.07.00_60/ts_124008v130700p.pdf)

To encode a name into the GSM Default Alphabet run:

~~~shell
python3 -m venv venv
source venv/bin/activate
python -m pip install -U pip
venv/bin/pip install -r requirements.txt
~~~

~~~shell
python3 gsmencode.py "Bloxtel"
~~~

The encoding for EF PNN is then `43` `<xy length>` `8<x sparebits>` `<encoding>`
