import unittest
import os
from modules.export_html_report import generate_pdf_report, generate_html_report

class TestExportReport(unittest.TestCase):

    def setUp(self):
        """Create a sample dataset for testing."""
        self.sample_data = {
            "title": "Test Report",
            "content": "This is a test report for unit testing."
        }

    def tearDown(self):
        """Clean up generated test files."""
        for f in ["test_report.pdf", "test_report.html"]:
            if os.path.exists(f):
                os.remove(f)

    def test_generate_pdf_report(self):
        """Test if a PDF report is generated successfully."""
        output_file = "test_report.pdf"
        result_path = generate_pdf_report(self.sample_data, output_file)
        self.assertTrue(os.path.exists(result_path))
        self.assertGreater(os.path.getsize(result_path), 0)

    def test_generate_html_report(self):
        """Test if an HTML report is generated successfully."""
        output_file = "test_report.html"
        result_path = generate_html_report(self.sample_data, output_file)
        self.assertTrue(os.path.exists(result_path))
        self.assertGreater(os.path.getsize(result_path), 0)

if __name__ == '__main__':
    unittest.main()
