#!/bin/bash


if [ -f .env ]; then
    export $(cat .env | xargs)
fi

mkdir -p ../data/cat_images

# Set the number of random cat images you want to download (50 in your case)
num_images_to_download=50

# Check if the CAT_API_KEY variable is set
if [ -z "$CAT_API_KEY" ]; then
    echo "Error: CAT_API_KEY is not set in the .env file."
    exit 1
fi

# Loop to download the images
for ((i=1; i<=$num_images_to_download; i++)); do
    response=$(curl -s "https://api.thecatapi.com/v1/images/search?limit=1" -H "x-api-key: $CAT_API_KEY")
    image_url=$(echo $response | jq -r '.[0].url')
    
    if [ -n "$image_url" ]; then
        image_filename=$(basename $image_url)
        
        # Download the image and save it to the 'cat_images' directory
        curl -s -o "../data/cat_images/$image_filename" "$image_url"
        
        echo "Downloaded image $i/$num_images_to_download: $image_filename"
    else
        echo "Failed to fetch image $i/$num_images_to_download"
    fi
done

echo "Download completed!"
