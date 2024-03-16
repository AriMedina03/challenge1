import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import matplotlib.pyplot as plt

class SinusoidalListener(Node):
    def __init__(self):
        super().__init__('sinusoidal_listener') #mi topico es sinusoidal_signal
        self.subscription = self.create_subscription(Float64, 'sinusoidal_signal', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning
        #creando otro que publique
        self.publisher_ = self.create_publisher(Float64, '/process_sign', 10)

        self.get_logger().info('Sinusoidal listener node new')

    def listener_callback(self, msg):
        modificado = (msg.data*2) +2 #modifico el mensaje

        modified_msg = Float64()
        modified_msg.data = modificado

        self.publisher_.publish(modified_msg)

        #plot the modified values
        plt.plot(modificado)
        plt.xlabel('Time (s)')
        plt.ylabel('Value')
        plt.title('Sinusoidal Signal')
        plt.grid(True)
        self.get_logger().info('Received sinusoidal signal: {}'.format(msg.data))

def main(args=None):
    rclpy.init(args=args)
    sinusoidal_listener = SinusoidalListener()
    rclpy.spin(sinusoidal_listener)
    sinusoidal_listener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
