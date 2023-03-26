import os
import re
import time
import requests
from bs4 import BeautifulSoup
from pytube import YouTube
from pydub import AudioSegment
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from moviepy.video.io.VideoFileClip import VideoFileClip

# 다운로드 받을 채널의 URL을 입력합니다.
url = "https://www.youtube.com/@dt5beats892/videos"

driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.implicitly_wait(10)

driver.get(url=url)

# # 채널 페이지의 HTML을 가져옵니다.
# response = requests.get(url)
# html = response.text

# with open('./index.html', 'w') as f:
#   print(html)
#   f.writelines(html)

# # HTML을 파싱합니다.
# soup = BeautifulSoup(html, 'html.parser')

# 채널 페이지에서 모든 동영상 링크를 추출합니다.

time.sleep(10)

video_links = []
for elem in driver.find_elements(by=By.TAG_NAME, value='a'):
  href = elem.get_attribute('href')
  if href == None: continue
  print(href)
  if '/watch?v=' in href:
    video_links.append(href)

video_links = set(video_links)
print(video_links)

def mp4_to_wav(mp4_file, wav_file):

  # mp4 파일을 VideoFileClip 객체로 변환
  clip = VideoFileClip(mp4_file)
  clip.set_fps(24)

  # 오디오 부분 추출
  audio = clip.audio

  # 오디오를 wav 파일로 저장
  audio.write_audiofile(wav_file)

  # VideoFileClip 객체 및 오디오 객체 해제
  clip.close()
  audio.close()

# 모든 동영상 링크를 순회하면서 음원을 추출합니다.
for link in video_links:
    try:
        # YouTube 객체를 생성합니다.
        youtube = YouTube(link)

        # 다운로드할 비디오의 포맷을 선택합니다. 여기서는 오디오 포맷인 "audio/mp4"를 선택합니다.
        video = youtube.streams.filter().first()

        # 다운로드합니다. 다운로드 받은 파일은 현재 디렉토리에 저장됩니다.
        video.download()
        
        # MP4 파일을 WAV 파일로 변환합니다.
        mp4_file = video.default_filename
        print('mp4_file : ' + mp4_file)
        wav_file = os.path.splitext(mp4_file)[0] + '.wav'
        print('wav_file : ' + wav_file)
        mp4_to_wav(mp4_file, wav_file)
        # AudioSegment.from_file(mp4_file).export(wav_file, format='wav')
        os.remove(mp4_file)
        
        # 다운로드에 일정 시간 간격을 두기 위해 5초간 대기합니다.
        time.sleep(15)
        
    except Exception as e:
        print(f"[ERROR] {e}")