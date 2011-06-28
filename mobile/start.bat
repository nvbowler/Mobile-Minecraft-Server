cd ./../
python download.py
cd ./Mobile
java -Xmx1024M -Xms1024M -jar craftbukkit-0.0.1-SNAPSHOT.jar nogui
python zip.py
cd ./../
python upload.py
echo "Latest files are uploaded."
pause