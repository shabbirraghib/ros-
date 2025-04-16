import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import time

class DummyCameraPublisher(Node):
    def __init__(self):
        super().__init__('dummy_camera_publisher')
        self.publisher_ = self.create_publisher(Image, '/image_raw', 10)
        self.bridge = CvBridge()
        self.timer = self.create_timer(1.0/30.0, self.timer_callback)
        self.cap = cv2.VideoCapture('video.mp4')  # Place your video in same folder

    def timer_callback(self):
        ret, frame = self.cap.read()
        if not ret:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            return
        msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = DummyCameraPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

