mkdir -p ../data/dog_images

# Set the number of random dog images you want to download (50 in your case)
num_images_to_download=5

# Loop to download the images
for ((i=1; i<=$num_images_to_download; i++)); do
    response=$(curl -s https://dog.ceo/api/breeds/image/random)
    image_url=$(echo $response | jq -r '.message')
    
    if [ -n "$image_url" ]; then
        image_filename=$(basename $image_url)
        
        # Download the image and save it to the 'dog_images' directory
        curl -s -o "../data/dog_images/$image_filename" "$image_url"
        
        echo "Downloaded image $i/$num_images_to_download: $image_filename"
    else
        echo "Failed to fetch image $i/$num_images_to_download"
    fi
done

echo "Download completed!"
