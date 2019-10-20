import cv2
import threading
import time
import simpleaudio as sa

change_file = False
interframe_wait_ms = 2
window_name = "window"

video_dir = "D:/PycharmProjects/audioset_classification-master/video"
audio_dir = "D:/PycharmProjects/audioset_classification-master/audio"
default_video = "bear"
video_show = "bear"

with open("D:/PycharmProjects/overfit_nlu/static/status.txt", "w+") as f:
    f.write("bear")


def update_video():
    global video_show
    global change_file
    global default_video

    while True:
        with open("D:/PycharmProjects/overfit_nlu/static/status.txt", "r") as f:
            fn = f.readline()
            if fn == "greet":
                default_video = "idle"

            if video_show != fn:
                print("change video to {}".format(fn))
                video_show = fn
            f.close()
        time.sleep(0.5)
        

def show_video():
    global video_show
    global interframe_wait_ms
    global default_video

    previous_video = video_show

    cap = cv2.VideoCapture("{}/{}.avi".format(video_dir, video_show))

    while(cap.isOpened()):
        if video_show != previous_video:
            previous_video = video_show
            cap = cv2.VideoCapture("{}/{}.avi".format(video_dir, video_show))
            if video_show != default_video:
                audio_name = "{}/{}.wav".format(audio_dir, video_show)
                wave_obj = sa.WaveObject.from_wave_file(audio_name)
                wave_obj.play()

        ret, frame = cap.read()
        if ret == True:
            cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.imshow(window_name,frame)
            if cv2.waitKey(interframe_wait_ms) & 0xFF == ord('q'):
                break
        else: 
            print("restart video to default")
            cap = cv2.VideoCapture("{}/{}.avi".format(video_dir, default_video))
            with open("D:/PycharmProjects/overfit_nlu/static/status.txt", "w") as f:
                f.write(default_video)
            video_show = default_video
            previous_video = default_video
            
    cap.release()
    cv2.destroyAllWindows()


video_show_thread = threading.Thread(target=show_video)
update_video_thread = threading.Thread(target=update_video)

video_show_thread.start()
update_video_thread.start()