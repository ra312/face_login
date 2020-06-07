import cv2
import face_recognition
class VideoCamera(object):
	def __init__(self):
		# Using OpenCV to capture from device 0. If you have trouble capturing
		# from a webcam, comment the line below out and use a video file
		# instead.
		self.video = cv2.VideoCapture(0)
		# If you decide to use video.mp4, you must have this file in the folder
		# as the main.py.
		# self.video = cv2.VideoCapture('video.mp4')
   
	def __del__(self):
		self.video.release()
    
	def get_frame(self):
		success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
		        
		# convert the image to RGB color which is used by face_recognition
		rgb_frame = image[:, :, ::-1]
		# find all the faces in the current video frame
		face_locations = face_recognition.face_locations(rgb_frame)
		# draw rectangles around the faces
		for top, right, bottom, left in face_locations:
			cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
		im_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
		ret, jpeg = cv2.imencode('.jpg', im_bgr)
		return jpeg.tobytes()


def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
			b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
