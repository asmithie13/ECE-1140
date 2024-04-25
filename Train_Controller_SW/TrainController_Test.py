import unittest
from TrainController import TrainController

class TestTrainController(unittest.TestCase):

    def setUp(self):
        self.train_controller = TrainController()

    def test_emergency_brake_activation(self):
        """Test that the emergency brake correctly stops the train and disables other controls."""
        self.train_controller.ebrake_sig.emit(True)
        self.assertEqual(self.train_controller.uilcdCurSpd, 0)
        self.assertFalse(self.train_controller.AcceleratorSld.Disabled, True)

    def test_brake_failure(self):
        """Test the train's response to a brake failure."""
        self.train_controller.brk_fail_sig.emit(True)
        self.assertTrue(self.train_controller.Ebrake.isChecked,True)
        self.assertFalse(self.train_controller.cceleratorSld.Disabled, False)
        self.assertFalse(self.train_controller.service_brake_enabled)

    def test_signal_pickup_failure(self):
        """Test the system's response to a signal pickup failure."""
        self.train_controller.sig_fail_sig.emit(True)
        self.assertTrue(self.train_controller.ebrake_engaged)
        self.assertFalse(self.train_controller.accelerator_enabled)
        self.assertFalse(self.train_controller.service_brake_enabled)

    def test_power_failure(self):
        """Test the system's response to a power failure."""
        self.train_controller.pwr_fail_sig.emit(True)
        self.assertTrue(self.train_controller.ebrake_engaged)
        self.assertFalse(self.train_controller.accelerator_enabled)
        self.assertFalse(self.train_controller.service_brake_enabled)

    def test_manual_change_ki_kp(self):
        """Test the ability of a train engineer to modify KI and KP while the train is moving."""
        initial_power = self.train_controller.calculate_power()
        self.train_controller.Control_Ki(5)
        self.train_controller.Control_Kp(2)
        modified_power = self.train_controller.calculate_power()
        self.assertNotEqual(initial_power, modified_power)

    def test_speed_control_manual_mode(self):
        """Test speed limit enforcement in manual mode."""
        self.train_controller.speed_limit = 50
        self.train_controller.Control_Current_Speed(55)
        self.assertTrue(self.train_controller.service_brake_engaged)

    def test_speed_control_automatic_mode(self):
        """Test that the train adheres to commanded speeds and limits in automatic mode."""
        self.train_controller.speed_limit = 60
        self.train_controller.commanded_speed = 60
        self.train_controller.Control_Current_Speed(70)
        self.assertTrue(self.train_controller.service_brake_engaged)

    def test_decrementing_authority(self):
        """Test decrementing of authority based on current speed."""
        initial_authority = 100
        self.train_controller.authority = initial_authority
        self.train_controller.current_speed = 40
        self.train_controller.decrement_authority()
        self.assertLess(self.train_controller.authority, initial_authority)

    def test_stopping_at_authority_automatic_mode(self):
        """Ensure the train stops before reaching zero authority in automatic mode."""
        self.train_controller.authority = 1
        self.train_controller.current_speed = 30
        self.train_controller.check_and_apply_brakes_based_on_authority()
        self.assertEqual(self.train_controller.current_speed, 0)


    def test_speed_control_driver_exceeds_limit_manual_mode(self):
        """Test that in manual mode, the train does not exceed the speed limit."""
        self.train_controller.manual_mode = True
        self.train_controller.speed_limit = 50  # Set speed limit
        self.train_controller.commanded_speed = 55  # Driver attempts to set a higher speed
        self.train_controller.Control_Current_Speed(55)  # Attempt to exceed speed limit
        self.assertTrue(self.train_controller.service_brake_engaged)
        self.assertLessEqual(self.train_controller.current_speed, self.train_controller.speed_limit)

    def test_stopping_at_zero_authority_automatic_mode(self):
        """Ensure the train stops before reaching zero authority in automatic mode."""
        self.train_controller.authority = 0  # No authority left
        self.train_controller.current_speed = 30  # Current speed
        self.train_controller.check_and_apply_brakes_based_on_authority()  # System should apply brakes
        self.assertEqual(self.train_controller.current_speed, 0)  # Check if the train has stopped

if __name__ == "__main__":
    unittest.main()
