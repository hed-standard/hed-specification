import os
import json
import unittest


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        test_dir = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                                 '../docs/source/_static/data/error_tests'))
        cls.test_files = [os.path.join(test_dir, f) for f in os.listdir(test_dir) 
                          if os.path.isfile(os.path.join(test_dir, f))]

    @staticmethod
    def get_test_info(test_file):
        indent = "   "
        with open(test_file, "r") as fp:
            test_info = json.load(fp)
        out_list = [f"{test_info[0]['error_code']}"]
        for info in test_info:
            out_list.append(f"{indent}{info['description']}")
            if "string_tests" in info["tests"]:
                out_list.append(MyTestCase.get_count_tests(info["tests"]["string_tests"], "string_tests", indent*2))
            if "sidecar_tests" in info["tests"]:
                out_list.append(MyTestCase.get_count_tests(info["tests"]["sidecar_tests"], "sidecar_tests", indent*2))
        return "\n".join(out_list)

    @staticmethod
    def get_count_tests(test_item, title, indent):
        num_fail_tests = len(test_item.get("fails", 0))
        num_pass_tests = len(test_item.get("passes", 0))
        return f"{indent}{title}: fail_tests={num_fail_tests} pass-tests={num_pass_tests}"

    def test_summary(self):
        for test_file in self.test_files:
            print(test_file)
            out_str = self.get_test_info(test_file)
            print(out_str)
            break
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
