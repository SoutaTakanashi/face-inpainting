mkdir datasets
URL=http://vis-www.cs.umass.edu/lfw/lfw.tgz
TAR_FILE=./datasets/faces.tar.gz
TARGET_DIR=./datasets/faces/
wget -N $URL -O $TAR_FILE
mkdir $TARGET_DIR
tar -zxvf $TAR_FILE -C ./datasets/
rm $TAR_FILE
mv ./datasets/lfw ./datasets/orig
