from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    input_topic = LaunchConfiguration('input_topic')
    output_topic = LaunchConfiguration('output_topic')

    return LaunchDescription([
        # Declare configurable topic arguments
        DeclareLaunchArgument(
            'input_topic',
            default_value='/image_raw',
            description='Input topic for image_conversion_node'
        ),
        DeclareLaunchArgument(
            'output_topic',
            default_value='/converted_image',
            description='Output topic from image_conversion_node'
        ),

        # Dummy USB camera node
        Node(
            package='dummy_usb_cam',
            executable='dummy_usb_cam_node',
            name='dummy_usb_cam_node',
            output='screen',
        ),

        # Image conversion node
        Node(
            package='image_conversion',
            executable='image_conversion_node',
            name='image_conversion_node',
            output='screen',
            parameters=[{
                'input_topic': input_topic,
                'output_topic': output_topic
            }]
        ),
    ])

