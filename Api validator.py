aders=headers)
        self.assertEqual(response.status_code, 404)

    def test_500_status(self):
        url = self.base_url + "/error-endpoint"
        headers = {"Authorization": self.authorization_key}
        response = requests.get(url, headers=headers)
        self.assertEqual(response.status_code, 500)

    def test_json_response(self):
        url = self.base_url + self.api_path
        headers = {"Authorization": self.authorization_key}
        response = requests.get(url, headers=headers)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.text)
        self.assertTrue("key" in data)  # Replace "key" with the key you want to validate

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(URLValidationTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # Create and save test report in XML format
    xml_report = unittest.TestTestRunner(verbosity=2).run(suite)
    with open("test_report.xml", "w") as xml_file:
        xml_file.write(xml_report.to_xml())

    # Create and save test report in CSV format
    with open("test_report.csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Test Case", "Status"])
        for test_result in xml_report.result:
            writer.writerow([test_result[0]._testMethodName, test_result[1]])

    # Create and save test report in HTML format
    html_report = unittest.TestTestRunner(verbosity=2).run(suite)
    with open("test_report.html", "w") as html_file:
        soup = BeautifulSoup(html_report.to_html(), "html.parser")
        html_file.write(soup.prettify())
