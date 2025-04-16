from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='dummy_usb_cam',
            executable='publisher',
            output='screen'
        ),
        Node(
            package='image_conversion',
            executable='converter',
            output='screen'
        )
    ])


