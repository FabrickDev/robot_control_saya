import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from std_msgs.msg import Float64


class InverseKinematics(Node):

    def __init__(self):
        super().__init__('inverse_kinematics')

        # Parameter robot
        self.wheel_radius = 0.03       # r = 3 cm
        self.wheel_separation = 0.17   # s = 17 cm

        # Subscriber kecepatan robot
        self.create_subscription(
            Twist,
            '/input_ik',
            self.velocity_callback,
            10
        )

        # Publisher roda kiri
        self.left_publisher = self.create_publisher(
            Float64,
            '/left_wheel/command',
            10
        )

        # Publisher roda kanan
        self.right_publisher = self.create_publisher(
            Float64,
            '/right_wheel/command',
            10
        )

        self.get_logger().info('Inverse Kinematics aktif')


    def velocity_callback(self, msg):

        # Input kecepatan robot
        V = msg.linear.x
        omega = msg.angular.z

        r = self.wheel_radius
        s = self.wheel_separation

        # =========================
        # INVERSE KINEMATICS
        # =========================

        phi_L = (2 * V - omega * s) / (2 * r)
        phi_R = (2 * V + omega * s) / (2 * r)

        # Pesan roda kiri dan kanan
        left_msg = Float64()
        right_msg = Float64()

        left_msg.data = phi_L
        right_msg.data = phi_R

        # Publish kecepatan roda
        self.left_publisher.publish(left_msg)
        self.right_publisher.publish(right_msg)

        self.get_logger().info(
            f'V={V:.2f} m/s | '
            f'omega={omega:.2f} rad/s | '
            f'phi_L={phi_L:.2f} rad/s | '
            f'phi_R={phi_R:.2f} rad/s'
        )


def main(args=None):

    rclpy.init(args=args)

    node = InverseKinematics()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()