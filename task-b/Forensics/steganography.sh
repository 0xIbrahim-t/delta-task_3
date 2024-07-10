#!/bin/bash

echo "Hii, here you can set up the image for CTF challenge using steganography"
PS3="Choose an option: "

select choice_1 in "Erase the before content and add a new line in secret.txt" "Append a new line in secret.txt" "Move to the next step" "Exit"; do
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
        fi
done

steghide embed -cf mystery.png -ef secret.txt

read -p "Write the clues for the contestants to find some clues, which will be saved in the metadata under clue: " clues

exiftool -Clue="$clues" mystery.png

echo "CTF challenge created successully under mystery.png"

exit 0
