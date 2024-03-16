import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import math

class SinusoidalTalker(Node):
    def __init__(self):
        super().__init__('sinusoidal_talker')
        self.publisher_ = self.create_publisher(Float64, 'sinusoidal_signal', 10)
        self.timer = self.create_timer(0.5, self.publish_signal)# Publishing every 0.1 second
        self.i=0
        self.get_logger().info('Sinusoidal talker node initialized')

    def publish_signal(self):
        msg = Float64()
        msg.data = math.sin(self.i)  # Generate a sinusoidal signal using current time
        self.publisher_.publish(msg) 
        self.get_logger().info('Publishing sinusoidal signal: {}'.format(msg.data))
        self.i+=0.1

def main(args=None):
    rclpy.init(args=args)
    sinusoidal_talker = SinusoidalTalker()
    rclpy.spin(sinusoidal_talker)
    sinusoidal_talker.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

