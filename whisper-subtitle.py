!pip install openai
import openai


openai.api_key = 'YOUR_API_KEY'
model_id = 'whisper-1'
media_file = open("./content/test-audio.m4a", "rb")

transcript = openai.Audio.transcribe(
    file=media_file,
    model="whisper-1",
    response_format="srt",
    prompt='This is the audio of a youtube video, converted into simplified Chinese subtitles'
)

# 打开文件，使用 'w' 模式表示写入（如果文件不存在则创建一个新文件）
file = open("./content/mySubtitle.srt", "w")

# 写入文本内容
file.write(transcript)

# 关闭文件
file.close()

print("文本已成功写入文件。")