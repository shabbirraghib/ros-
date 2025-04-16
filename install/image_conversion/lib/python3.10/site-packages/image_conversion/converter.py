import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_srvs.srv import SetBool
from cv_bridge import CvBridge
import cv2

class ImageConverter(Node):
    def __init__(self):
        super().__init__('image_converter')
        self.subscription = self.create_subscription(Image, '/image_raw', self.listener_callback, 10)
        self.publisher_ = self.create_publisher(Image, '/image_converted', 10)
        self.bridge = CvBridge()
        self.mode = False  # False = Color, True = Grayscale
        self.srv = self.create_service(SetBool, 'set_mode', self.set_mode_callback)

    def set_mode_callback(self, request, response):
        self.mode = request.data
        response.success = True
        response.message = f"Mode set to {'Grayscale' if self.mode else 'Color'}"
        return response

    def listener_callback(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        if self.mode:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
        new_msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
        self.publisher_.publish(new_msg)

def main(args=None):
    rclpy.init(args=args)
    node = ImageConverter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

