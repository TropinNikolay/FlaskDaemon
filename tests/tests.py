import hashlib
import os
import json
import requests
import unittest


class TestGet(unittest.TestCase):
    def setUp(self) -> None:
        """
        This function setup test environment.
        """
        self.base_url = "http://127.0.0.1:5000/"
        self.path_to_file = "files/Shakespeare.txt"
        self.params = {}

        with open(self.path_to_file, "rb") as file:
            content = file.read()
        self.params["hash"] = hashlib.md5(content).hexdigest()
        self.path_to_storage = (
            f'../store/{self.params["hash"][:2]}/{self.params["hash"]}'
        )

    def test_post_method(self) -> None:
        """
        This function test post method.
        """
        with open(self.path_to_file, "rb") as file:
            files = {"file": file}
            response = requests.post(self.base_url + "upload", files=files)
        file_hash_server = json.loads(response.text)
        self.assertTrue(response.status_code, 200)
        self.assertEqual(self.params["hash"], file_hash_server["file_hash"])

    def test_get_method(self) -> None:
        """
        This function test get method.
        """
        response = requests.get(self.base_url + "download", params=self.params)
        if os.path.exists(self.path_to_storage):
            self.assertTrue(response.status_code, 200)
            self.assertEqual(
                response.content, open("files/Shakespeare.txt", "rb").read()
            )
        else:
            self.assertEqual("This file doesn't exist.", response.text)

    def test_delete_method(self) -> None:
        """
        This function test delete method.
        """
        is_exist = os.path.exists(self.path_to_storage)
        response = requests.delete(self.base_url + "delete", params=self.params)
        if is_exist:
            self.assertEqual("Successfully deleted.", response.text)
            self.assertTrue(response.status_code, 200)
        else:
            self.assertEqual("This file doesn't exist.", response.text)


if __name__ == "__main__":
    unittest.main()
