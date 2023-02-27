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
    def get_test_info(test_file, details=True):
        indent = "   "
        with open(test_file, "r") as fp:
            test_info = json.load(fp)
        out_list = [f"{test_info[0]['error_code']}"]
        for info in test_info:
            out_list.append(f"\n{indent}{info['description']}")
            out_list.append(f"{indent}HED {info['schema']}")
            out_list.append(f"{indent}Definitions:")
            for defs in info["definitions"]:
                out_list.append(f"{indent*2}{defs}")
            if "string_tests" in info["tests"]:
                out_list = out_list + MyTestCase.get_test_details(info["tests"]["string_tests"], "string_tests", indent)
            if "sidecar_tests" in info["tests"]:
                out_list = out_list + \
                           MyTestCase.get_test_details(info["tests"]["sidecar_tests"], "sidecar_tests", indent)
            if "event_tests" in info["tests"]:
                out_list = out_list + \
                           MyTestCase.get_test_details(info["tests"]["event_tests"], "event_tests", indent)
        return "\n".join(out_list)

    @staticmethod
    def get_test_details(test_item, title, indent, details=True): 
        num_fail_tests = len(test_item.get("fails", 0))
        num_pass_tests = len(test_item.get("passes", 0))
        detail_list = [f"{indent*2}{title}: fail_tests={num_fail_tests} pass_tests={num_pass_tests}"]
        if num_fail_tests > 0:
            detail_list.append(f"{indent*3}fail_tests:")
            for test in test_item["fails"]:
                detail_list.append(f"{indent*4}{test}")
        if num_pass_tests > 0:
            detail_list.append(f"{indent * 3}pass_tests:")
            for test in test_item["passes"]:
                detail_list.append(f"{indent * 4}{test}")
        return detail_list

    def test_summary(self):
        for test_file in self.test_files:
            out_str = self.get_test_info(test_file)
            print(out_str)
        self.assertEqual(True, True)  # add assertion here

    def test_summary_full(self):
        for test_file in self.test_files:
            print(test_file)
            out_str = self.get_test_info(test_file, details=True)
            print(out_str + '\n')

        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
