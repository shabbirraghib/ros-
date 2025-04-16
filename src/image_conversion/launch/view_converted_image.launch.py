from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def launch_setup(context, *args, **kwargs):
    image_topic = LaunchConfiguration('image_topic').perform(context)

    return [
        Node(
            package='rqt_image_view',
            executable='rqt_image_view',
            name='rqt_image_view',
            output='screen',
            arguments=['--ros-args', '-r', f'/image:={image_topic}']
        )
    ]

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'image_topic',
            default_value='/converted_image',
            description='Image topic to visualize'
        ),
        OpaqueFunction(function=launch_setup)
    ])

