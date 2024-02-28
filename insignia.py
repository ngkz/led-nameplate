from PIL import Image

input_path = 'insignia-rotating.gif'
gif_path = 'insignia-rotating-converted.gif'
output_path = 'data-insignia.png'
threshold = 32

frame_width = 44
frame_img_width = 48
height = 11
fps =15
loop = 1

gif = Image.open(input_path)

frames = []
for frame in range(0, gif.n_frames):
    gif.seek(frame)

    resized_frame = gif.resize((frame_width, frame_width), Image.LANCZOS)
    rotated_frame = resized_frame.rotate(90)
    cropped_frame = rotated_frame.crop((0, round(frame_width / 2 - height / 2), frame_width, round(frame_width / 2 - height / 2) + height))
    mono_frame = cropped_frame.convert("L").point(lambda x: 0 if x < threshold else 255, mode='1')

    frames.append(mono_frame)

frames[0].save(gif_path, format='GIF', append_images=frames[1:], save_all=True, duration=1000/fps, loop=0)

data = Image.new("1", (frame_img_width * len(frames) * loop, height))
frame_idx = 0
for i in range(loop):
    for  frame in frames:
        data.paste(frame, (frame_idx * frame_img_width, 0))
        frame_idx += 1
data.save(output_path)
