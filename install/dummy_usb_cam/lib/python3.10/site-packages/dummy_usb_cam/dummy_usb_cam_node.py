import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class DummyCamNode(Node):
    def __init__(self):
        super().__init__('dummy_usb_cam')
        self.publisher_ = self.create_publisher(Image, '/image_raw', 10)
        timer_period = 1.0 / 30  # 30 Hz
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.bridge = CvBridge()
        self.image = cv2.imread('/home/shabbir/Pictures/dummpy_image.jpg')# Update this path

        if self.image is None:
            self.get_logger().error('Failed to load image. Check the path.')
        else:
            self.get_logger().info('Dummy USB Camera started with image.')

    def timer_callback(self):
        if self.image is not None:
            msg = self.bridge.cv2_to_imgmsg(self.image, encoding='bgr8')
            self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = DummyCamNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


