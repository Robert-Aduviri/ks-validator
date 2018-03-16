import os, shutil, re

def str2time(text):
    h, m, s = text.split(':')
    return int(h) * 3600 + int(m) * 60 + float(s)

def time2str(number):
    h = int(number // 3600)
    m = int((number % 3600) // 60)
    s = int((number % 3600) % 60)
    f = float((number % 3600) % 60 - s) * 100
    return f'{h}:{m:02}:{s:02}.{f:02.0f}'

def get_header():
    return '''[Script Info]
Title: KS example file
ScriptType: v4.00+
WrapStyle: 0
PlayResX: 1080
PlayResY: 720
ScaledBorderAndShadow: yes
Video Aspect Ratio: 0
Video Zoom: 6
Video Position: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Start,Panton,72,&H00FFFFFF,&H000000FF,,,0,0,0,0,100,100,0,0,0,0,0,8,0,0,250,1
Style: End,Panton,60,&H00FFFFFF,&H000000FF,,,0,0,0,0,100,100,0,0,0,0,0,8,0,0,100,1
Style: Karaoke0,Panton,80,&H000000FF,&H00FFFFFF,,,0,0,0,0,100,100,0,0,0,0,0,8,0,0,250,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text'''.split('\n')

def get_error_log(lines):
    print(get_header())
    error_log = []
    prev_end_time = 0
    painting_time = 0
    prev_line = ''
    for idx, line in enumerate(lines):
        try:            
            if idx == 1 and 'Title:' not in line:
                error_log.append(f"Line {idx+1}: incorrect header format")
            elif line.startswith('Style') and \
                ('panton' not in line.lower() or 'arial' in line.lower()):
                error_log.append(f"Line {idx+1}: incorrect style")
            elif idx < 19 and line.strip() != get_header()[idx].strip():
                error_log.append(f"Line {idx+1}: incorrect header format")

            # Validate Style
            
            
            if line.startswith('Dialogue'):
                start_time = str2time(line.split(',')[1])

                # Validate Position
                position = int(line.split(',')[7])
                if 'start' in line.lower() and 'tiempo' in line.lower() and position != 550:
                    error_log.append(f"Line {idx+1}: position of 'Tiempo' != 550")
                if position >= 600:
                    error_log.append(f"Line {idx+1}: position >= 600")

                # Validate Time
                if start_time - prev_end_time >= 10:
                    error_log.append(f"Line {idx+1}: there is a time gap >= 10s with the previous line")

                # Validate Frames timing
                if prev_end_time >= start_time and \
                    (('INSTRUMENTAL' in prev_line and 'tropicalzone' not in line) or
                        ('tropicalzone' in prev_line)):
                    error_log.append(f"Line {idx+1}: 'INSTRUMENTAL' frame is finishing too late or the next line is starting too early")
                
                if prev_end_time >= start_time and '.....' in prev_line and '.....' not in line:
                    error_log.append(f"Line {idx+1}: '.....' frame is finishing too late or the next line is starting too early")

                # Validate {\kf0}
                text = ','.join(line.split(',')[9:])
                kfs = [int(re.sub(r'\{\\kf(-?\w+)\}', r'\1', word)) \
                                for word in re.findall(r'\{\\kf(-?\w+)\}', text)]
                if any(kf <= 0 for kf in kfs):
                    error_log.append(f"Line {idx+1}: kf <= 0")
                
                # Validate painting time
                if len(kfs) > 0:
                    painting_start_time = start_time + kfs[0] / 100
                    if painting_start_time < painting_time:
                        error_log.append(f"Line {idx+1}: painting is starting too early ({time2str(painting_start_time)} < {time2str(painting_time)} of previous line)")
                    painting_time = start_time + sum(kf / 100 for kf in kfs)

                prev_end_time = str2time(line.split(',')[2])
                prev_line = line

        except:
            error_log.append(f"Unknown error in Line {idx+1}: {line}")
    
    if len(error_log) == 0:
        error_log = ['OK']
    return error_log

def get_lyrics(lines):
    pattern = re.compile(r'\{(.*?)\}', re.UNICODE)
    lyrics = []
    for idx, line in enumerate(lines):
        if line.startswith('Dialogue'):
            text = ','.join(line.split(',')[9:])
            text = pattern.sub('', text).strip()
            lyrics.append(f"Line {idx+1}: {text}")
    return lyrics

        


        
