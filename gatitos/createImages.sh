
imagesNumber=100

for i in `seq 0 $imagesNumber`
do
    echo "Image gatitos$i.jpg created!"
    cp "gatitos.jpg" "gatitos$i.jpg"
done