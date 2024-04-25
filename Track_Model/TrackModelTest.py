import unittest
from track_model import TrackModel  # Assuming the track model functionality is encapsulated in this class

class TestTrackModel(unittest.TestCase):
    def setUp(self):
        # Initialize the Track Model before each test
        self.track_model = TrackModel()

    def test_toggle_failures(self):
        # Test toggling failures like broken rails, track circuit failures, and power failures
        self.track_model.toggle_failure('broken_rail')
        self.assertTrue(self.track_model.check_block_status('broken_rail'))
        self.track_model.toggle_failure('broken_rail')
        self.assertFalse(self.track_model.check_block_status('broken_rail'))

    def test_uploading_track_layout(self):
        # Test uploading a track layout file
        result = self.track_model.upload_layout('track_layout.csv')
        self.assertTrue(result)

    def test_take_in_commanded_speed_and_authority(self):
        # Test the reception of commanded speed and authority from Wayside
        self.track_model.set_commanded_speed_and_authority(40, 5000)
        speed, authority = self.track_model.get_commanded_speed_and_authority()
        self.assertEqual(speed, 40)
        self.assertEqual(authority, 5000)

    def test_sending_ticket_sales(self):
        # Test the functionality of sending ticket sales data
        sales_data = {'station': 'Station A', 'sales': 150}
        self.track_model.send_ticket_sales(sales_data)
        self.assertIn('Station A', self.track_model.ticket_sales)
        self.assertEqual(self.track_model.ticket_sales['Station A'], 150)

    def test_sending_presence_on_block_to_wayside_controller(self):
        # Test sending block occupancy to the Wayside Controller
        self.track_model.update_block_occupancy(5, True)
        occupancy = self.track_model.get_block_occupancy(5)
        self.assertTrue(occupancy)

    def test_setting_environmental_temperature(self):
        # Test setting the environmental temperature
        self.track_model.set_environmental_temperature(34)
        self.assertEqual(self.track_model.get_environmental_temperature(), 34)

if __name__ == '__main__':
    unittest.main()
