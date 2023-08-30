import unittest
from game import generate_target, quit_game
from game import invalid_input, game_feedback, play_again
import unittest.mock


class TestNumberGuessingGame(unittest.TestCase):
    def test_generate_target(self):
        target = generate_target()
        str_o = "Generated target is out of range"
        self.assertTrue(1000 <= target <= 9999, str_o)

    def test_quit_game(self):
        target_number = 1234
        result = quit_game(target_number)
        expected_result = "The correct number was 1234"
        quit_str = "Quit game message is not as expected"
        self.assertEqual(
            result, expected_result, quit_str
        )

    def test_invalid_input(self):
        result = invalid_input()
        expected_result = "Invalid input. Please enter a four-digit number."
        self.assertEqual(
            result, expected_result, "Invalid input message is not as expected"
        )

    def test_game_feedback(self):
        guess = "1234"
        target = "1234"
        result = game_feedback(guess, target)
        expected_result = "●●●●"
        feedback_str = "Feedback is not as expected for correct guess"
        self.assertEqual(
            result, expected_result, feedback_str
        )

    def test_play_again_yes(self):
        # Simulate user entering 'yes'
        play_again_input = lambda _: "yes"  # noqa: E731
        retry_str = "Play again did not return True for 'yes' input"
        with unittest.mock.patch("builtins.input", play_again_input):
            result = play_again()
        self.assertTrue(result, retry_str)

    def test_play_again_no(self):
        # Simulate user entering 'no'
        retry_prompt = "Play again did not return False for 'no' input"
        play_again_input = lambda _: "no"  # noqa: E731
        with unittest.mock.patch("builtins.input", play_again_input):
            result = play_again()
        self.assertFalse(result, retry_prompt)


if __name__ == "__main__":
    unittest.main()
