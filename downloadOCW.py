import requests
from bs4 import BeautifulSoup
import os
import re
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

url = input("Please enter OCW link:")
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
course_title = soup.find('h1', class_='title-page').text.strip()
invalid_chars = r'[<>:"/\\|?*]'
course_title = re.sub(invalid_chars, '', course_title)

if not os.path.exists(course_title):
    os.makedirs(course_title)

sections = soup.find_all('div', class_='course-section')

def download_video(video_link, video_title, section_folder):
    response = requests.get(video_link, stream=True)
    total_size_in_bytes = int(response.headers.get('content-length', 0))
    block_size = 1024
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True, desc=video_title)
    
    video_file_path = os.path.join(section_folder, f'{video_title}.mp4')
    with open(video_file_path, 'wb') as f:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            f.write(data)
    progress_bar.close()
    
    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        print(f"ERROR, something went wrong with {video_title}")

download_tasks = []

for section in sections:
    section_title = section.find('div', class_='gheadlinel').find('span').text.strip()
    section_folder = os.path.join(course_title, section_title)
    if not os.path.exists(section_folder):
        os.makedirs(section_folder)
    
    videos = section.find_all('div', class_='course-panel-heading')
    
    for video in videos:
        video_title = video.find('h4').text.strip().replace('ویدئو', '')
        video_title = re.sub(invalid_chars, '', video_title)
        video_link = video.find_next('div', class_='panel-content').find('source')['src']
        download_tasks.append((video_link, video_title, section_folder))

with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(download_video, *task) for task in download_tasks]
    for future in as_completed(futures):
        future.result()

print("ویدئو‌ها با موفقیت دانلود و ذخیره شدند.")
