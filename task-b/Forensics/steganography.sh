#!/bin/bash

echo "Hii, here you can set up the image for CTF challenge using steganography"
PS3="Choose an option: "

select choice_1 in "Retrieve the secret text file" "Erase the before content and add a new line in secret.txt" "Append a new line in secret.txt" "Move to the next step" "Exit"; do
        if [[ "$choice_1" = "Erase the before content and add a new line" ]]; then
                read -p "Write a new line: " new_line
                echo $new_line > secret.txt

        elif [[ "$choice_1" = "Append a new line" ]]; then
                read -p "Write a new line to append: " append_line
                echo $append_line >> secret.txt

        elif [[ "$choice_1" = "Move to the next step" ]]; then
                break

        elif [[ "$choice_1" = "Exit" ]]; then
                exit 0

        elif [[ "$choice_1" = "Retrieve the secret text file" ]]; then
                convert mystery.png mystery.jpeg
                read -p "Enter a passphrase which can be used to retrieve the secret.txt: " pass_retrieve
                steghide extract -sf mystery.jpg -p "$pass_retrieve"
                convert mystery.jpeg mystery.png
        fi
done

read -p "Enter a passphrase which can be used to retrieve the secret.txt: " pass

steghide embed -cf mystery.jpeg -ef secret.txt -p "$pass"

read -p "Write the clues for the contestants to find some clues, which will be saved in the metadata under the tag Description: " clues

exiftool -Description="$clues" mystery.png

echo "CTF challenge created successully under mystery.png"

exit 0
