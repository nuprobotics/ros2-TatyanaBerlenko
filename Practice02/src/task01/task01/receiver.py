import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Receiver(Node) :

    def __init__(self) :
        super(Receiver , self ).__init__('receiver')
        self.subscription = self.create_subscription(
            String,
            '/spgc/sender',
            self.listener_callback,
            qos_profile=1
        )

    def listener_callback(self, msg):
        self.get_logger().info(msg.data)


def main():
    rclpy.init()
    node = Receiver()
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()