echo "starting setup"
echo """
+-+-+-+-+-+  +-+-+-+-+-+-+-+-+-+-+-+
|I|n|s|t|a|  |B|r|u|t|e|f|o|r|c|e|r|
+-+-+-+-+-+  +-+-+-+-+-+-+-+-+-+-+-+
"""
if [[ $EUID -ne 0 ]]; then
   echo "This script should be run as root" 
   exit 
fi
sudo apt install tor curl -y

git clone https://github.com/brainfucksec/kalitorify
cd kalitorify 
make install
echo -e "setup finished \n running the cracking script"
cd ..
kalitorify -t

python3 run.py