import pytest
from base_test_model import BaseTestModel
import os
from faker import Faker
from datetime import datetime


class TestApi(BaseTestModel):

    base_url = os.getenv("base_url")

    @pytest.mark.parametrize("name", [Faker().first_name()])
    def test_create_user(self, name):
        """Tests that a single user can be created with a random name"""

        user_data = {"name": name,
                     "job": "manager"}

        response = self.post(url=self.base_url + "api/users", json_data=user_data)

        assert response.status_code == 201
        assert response.json()["name"] == user_data["name"]

    @pytest.mark.parametrize("user_id", "2")
    def test_get_user(self, user_id):
        """Tests that user name is correct by get user id"""

        response = self.get(url=self.base_url + f"api/users/{user_id}")

        assert response.status_code == 200, "Status code is wrong"
        assert response.json()["data"]["id"] == int(user_id), "User id is wrong"
        assert response.json()["data"]["first_name"] == "Janet", "User name is wrong"

    @pytest.mark.parametrize("user_id, name", [("3", Faker().first_name())])
    def test_update_user(self, user_id, name):
        """Tests that user updated date is equal to today"""

        user_data = {"name": name,
                     "job": "manager"}

        today = datetime.today().strftime('%Y-%m-%d')

        response = self.put(url=self.base_url + f"api/users/{user_id}", json_data=user_data)

        assert response.status_code == 200, "Status code is wrong"
        assert response.json()["updatedAt"][:10] == today, "Update date is incorrect or empty"

    @pytest.mark.parametrize("user_id", "4")
    def test_delete_user(self, user_id):
        """Tests that user is deleted"""

        response = self.delete(url=self.base_url + f"api/users/{user_id}")
        assert response.status_code == 204, "Status code is wrong"
        assert not response.text, "Response body is not empty"
