sudo apt-get install git python3 python3-pip -y
rm -rf /home/script/hacksec-cli
git clone https://github.com/ScRiPt1337/hacksec-cli ~/hacksec-cli
pip install -r  ~/hacksec-cli/requirements.txt
echo "python3 ~/hacksec-cli/hacksec_cli/app.py" > ~/.local/bin/hacksec
sudo chmod +x ~/.local/bin/hacksec
echo "hacksec-cli successfully installed type hacksec"