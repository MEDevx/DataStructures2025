download_queue = [] #  A queue representing a batch of downloads

download_queue.append("File 1") # Each file is added to the download queue
download_queue.append("File 2")
download_queue.append("File 3")
download_queue.append("File 4")
download_queue.append("File 5")

print(f"\nDownload queue: {download_queue}")

print(f"\n{download_queue[0]} and {download_queue[1]} finished downloading.")
download_queue.pop(0); download_queue.pop(0) # Remove the first two links in the queue
print(f"Download queue: {download_queue}")

download_queue.clear(); # Clear the queue
link_left = len(download_queue) 
print(f"\nAll files finished downloading. There are {link_left} processes left.\n")
