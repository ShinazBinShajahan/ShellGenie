pip install random
if [ $(dpkg-query -W -f='${Status}' figlet 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
  apt-get install figlet
fi
cd Assets
python tr.py
