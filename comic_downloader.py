import requests
from bs4 import BeautifulSoup


# Define the path to your text file containing the URLs
file_path = "url_list.txt"

def download_images(list_of_image_urls):
    # create folder

    # go through list of image urls
    for i, image_url in enumerate(list_of_image_urls):
        # download the image
        # Send an HTTP GET request to the image URL
        response = requests.get(image_url)

        if response.status_code == 200:
            # Extract the image content
            image_content = response.content

            # save as file
            file_name = f'calvin_and_hobbes_comic{i}.jpg'  # You can choose any filename and extension

            # Save the image to your local directory
            with open(file_name, "wb") as file:
                file.write(image_content)

            print(f"Image downloaded and saved as {file_name}")
        else:
            print(f"Failed to download image. Status code: {response.status_code}")
        
def go_through_url_list():
    # Read the URLs from the text file
    with open(file_path, "r") as file:
        urls = file.read().splitlines()

    image_url_list = []
    for i, url in enumerate(urls[:5]):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                # Parse the HTML content of the page using BeautifulSoup
                soup = BeautifulSoup(response.text, "html.parser")
                # Find the image tag based on its attributes
                # image_tag = soup.find("img", {"class": "img-fluid lazyload"})
                image_tag = soup.select_one('a.js-item-comic-link picture.item-comic-image img')

                if image_tag:
                    # Extract the 'src' attribute of the image tag
                    image_source = image_tag.get("src")

                    print("Image Source:", image_source)
                    image_url_list.append(image_source)
                else:
                    print("Image not found on the page.")
            else:
                print("Failed to retrieve the web page. Status code:", response.status_code)
            
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching URL {i + 1}: {url}")
            print(e)
    print(image_url_list)
    download_images(image_url_list)
go_through_url_list()





