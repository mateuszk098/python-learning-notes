'''
Simple test of requests get.
'''

import unittest
import requests


def get_most_stars_python_repos() -> tuple[dict, int]:
    """ 
    Returns a tuple with status code and dictionary with the most stars
    python repositories on GitHub.
    """

    url: str = "https://api.github.com/search/repositories?q=language:python&sort=stars"
    headers: dict[str, str] = {"Accept": "application/vnd.github.v3+json"}
    r = requests.get(url, headers=headers)
    response_dict: dict = r.json()
    repo_dicts: dict = response_dict["items"]

    return repo_dicts, r.status_code


class GetResponseDictTestCase(unittest.TestCase):
    """ Test cases for `get_response_dict()`. """

    def setUp(self) -> None:
        self.response_dict, self.code = get_most_stars_python_repos()

    def test_status_code(self) -> None:
        """ Status code should be 200 for successful request. """
        self.assertEqual(self.code, 200)

    def test_returned_items(self) -> None:
        """ Number of returned items should be 30. """
        self.assertEqual(len(self.response_dict), 30)


if __name__ == "__main__":
    unittest.main()
