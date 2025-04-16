import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_srvs.srv import SetBool
from cv_bridge import CvBridge
import cv2

class ImageConversionNode(Node):
    def __init__(self):
        super().__init__('image_conversion_node')

        # Declare and get parameters
        self.declare_parameter('input_topic', '/image_raw')
        self.declare_parameter('output_topic', '/converted_image')
        input_topic = self.get_parameter('input_topic').get_parameter_value().string_value
        output_topic = self.get_parameter('output_topic').get_parameter_value().string_value

        self.subscription = self.create_subscription(Image, input_topic, self.listener_callback, 10)
        self.publisher_ = self.create_publisher(Image, output_topic, 10)
        
        self.bridge = CvBridge()
        self.mode = True  # True for grayscale, False for color
        self.srv = self.create_service(SetBool, 'set_mode', self.set_mode_callback)
        self.get_logger().info('Image Conversion Node Started')
    def listener_callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        if self.mode:
            cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
            msg_out = self.bridge.cv2_to_imgmsg(cv_image, encoding='mono8')
        else:
            msg_out = self.bridge.cv2_to_imgmsg(cv_image, encoding='bgr8')
        self.publisher_.publish(msg_out)

    def set_mode_callback(self, request, response):
        self.mode = request.data
        response.success = True
        response.message = f'Mode set to {"Greyscale" if self.mode else "Color"}'
        return response

def main(args=None):
    rclpy.init(args=args)
    node = ImageConversionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
