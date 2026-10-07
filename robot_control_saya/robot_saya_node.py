#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class MyNode(Node):

    def __init__(self):
        super().__init__("mobile_robot_controller")

        self.publisher_ = self.create_publisher(
            Twist,
            "/cmd_vel",
            10
        )

        # State gerakan
        self.state = 0

        # Waktu mulai state
        self.state_start_time = self.get_clock().now()

        # Durasi masing-masing state
        self.durasi_maju = 10.0
        self.durasi_maju_2 = 5.0
        self.durasi_belok = 3.5

        self.timer = self.create_timer(
            0.1,
            self.timer_callback
        )

    def get_elapsed_time(self):
        return (
            self.get_clock().now() - self.state_start_time
        ).nanoseconds / 1e9

    def next_state(self):
        self.state += 1

        # Kembali ke state 0 setelah satu putaran
        if self.state > 7:
            self.state = 0

        # Reset waktu untuk state baru
        self.state_start_time = self.get_clock().now()

        self.get_logger().info(
            f"Masuk state {self.state}"
        )

    def timer_callback(self):

        msg = Twist()

        elapsed_time = self.get_elapsed_time()

        # ============================================
        # STATE 0 - MAJU PANJANG
        # ============================================

        if self.state == 0:

            msg.linear.x = 0.5
            msg.angular.z = 0.0

            if elapsed_time >= self.durasi_maju:
                self.next_state()

        # ============================================
        # STATE 1 - BELOK
        # ============================================

        elif self.state == 1:

            msg.linear.x = 0.0
            msg.angular.z = 0.8

            if elapsed_time >= self.durasi_belok:
                self.next_state()

        # ============================================
        # STATE 2 - MAJU PENDEK
        # ============================================

        elif self.state == 2:

            msg.linear.x = 0.5
            msg.angular.z = 0.0

            if elapsed_time >= self.durasi_maju_2:
                self.next_state()

        # ============================================
        # STATE 3 - BELOK
        # ============================================

        elif self.state == 3:

            msg.linear.x = 0.0
            msg.angular.z = 0.8

            if elapsed_time >= self.durasi_belok:
                self.next_state()

        # ============================================
        # STATE 4 - MAJU PANJANG
        # ============================================

        elif self.state == 4:

            msg.linear.x = 0.5
            msg.angular.z = 0.0

            if elapsed_time >= self.durasi_maju:
                self.next_state()

        # ============================================
        # STATE 5 - BELOK
        # ============================================

        elif self.state == 5:

            msg.linear.x = 0.0
            msg.angular.z = 0.8

            if elapsed_time >= self.durasi_belok:
                self.next_state()

        # ============================================
        # STATE 6 - MAJU PENDEK
        # ============================================

        elif self.state == 6:

            msg.linear.x = 0.5
            msg.angular.z = 0.0

            if elapsed_time >= self.durasi_maju_2:
                self.next_state()

        # ============================================
        # STATE 7 - BELOK
        # ============================================

        elif self.state == 7:

            msg.linear.x = 0.0
            msg.angular.z = 0.8

            if elapsed_time >= self.durasi_belok:
                self.next_state()

        self.publisher_.publish(msg)


def main(args=None):

    rclpy.init(args=args)

    node = MyNode()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    # Stop robot
    stop_msg = Twist()
    node.publisher_.publish(stop_msg)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()