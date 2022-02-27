import cv2


def get_media_duration(media_path: str) -> float:
    video = cv2.VideoCapture(media_path)

    duration = video.get(cv2.CAP_PROP_FRAME_COUNT) / video.get(cv2.CAP_PROP_FPS)

    return duration
