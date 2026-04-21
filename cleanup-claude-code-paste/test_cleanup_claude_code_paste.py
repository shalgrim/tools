import unittest

from cleanup_claude_code_paste import cleanup


class CleanupTests(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(cleanup(''), '')

    def test_whitespace_only_input(self):
        self.assertEqual(cleanup('   \n\n  \n'), '')

    def test_strips_leading_prompt_with_space(self):
        self.assertEqual(cleanup('❯ hello world'), 'hello world')

    def test_strips_leading_prompt_without_space(self):
        self.assertEqual(cleanup('❯hello'), 'hello')

    def test_strips_prompt_on_multiple_lines(self):
        self.assertEqual(
            cleanup('❯ one\n❯ two'),
            'one two',
        )

    def test_does_not_strip_mid_line_prompt(self):
        self.assertEqual(cleanup('foo ❯ bar'), 'foo ❯ bar')

    def test_joins_wrapped_lines_with_single_space(self):
        self.assertEqual(
            cleanup('this is a\nwrapped line'),
            'this is a wrapped line',
        )

    def test_blank_line_separates_paragraphs(self):
        self.assertEqual(
            cleanup('first para\n\nsecond para'),
            'first para\n\nsecond para',
        )

    def test_multiple_blank_lines_collapse_to_single_break(self):
        self.assertEqual(
            cleanup('a\n\n\n\nb'),
            'a\n\nb',
        )

    def test_collapses_internal_whitespace_runs(self):
        self.assertEqual(
            cleanup('hello    world'),
            'hello world',
        )

    def test_trims_line_whitespace(self):
        self.assertEqual(
            cleanup('   padded   \n   lines   '),
            'padded lines',
        )

    def test_representative_sample(self):
        # Matches what the reference JS implementation would produce.
        text = (
            "❯ run the thing\n"
            "that does\n"
            "the stuff\n"
            "\n"
            "❯ another command\n"
            "with wrapped  output\n"
        )
        expected = (
            "run the thing that does the stuff\n"
            "\n"
            "another command with wrapped output"
        )
        self.assertEqual(cleanup(text), expected)


if __name__ == '__main__':
    unittest.main()
