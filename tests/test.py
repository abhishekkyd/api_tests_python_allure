import allure
import json
from testlib import helper
from testlib import check

# ENDPOINTS
POST_URL = '/public-api/users'
GET_URL = '/public-api/users'
PUT_URL = '/public-api/users'
DELETE_URL = '/public-api/users'
user_id = 1396


@allure.feature("Get Users")
@allure.story("Authorized user can see users information")
@allure.severity(allure.severity_level.BLOCKER)
def test_for_users_details():

    response = helper.get_request(url=GET_URL)

    check.response_has_status_code(response, 200)
    check.response_has_field_with_value(response, 'code', 200)
    check.response_has_fields(
        response,
        'data', 'meta'
    )


@allure.feature("Create a User")
@allure.story("Authorized user can add users information")
@allure.severity(allure.severity_level.BLOCKER)
def test_for_users_add():

    response = helper.post_request(url=POST_URL,
                                          body={'name':'Abhishek Yadav', 'gender':'Male',
                                                'email':'yabhishek@outlook.com', 'status':'Active'})

    check.response_has_status_code(response, 200)
    check.response_has_field_with_value(response, 'code', 201)
    check.response_has_fields(
        response,
        'data'
    )
    res = json.loads(response.text)
    id_value = res['data']
    user_id = id_value["id"]
    check.response_has_field_value(response, "name", 'Abhishek Yadav')
    check.response_has_field_value(response, "email", 'yabhishek@outlook.com')
    check.response_has_field_value(response, "gender", 'Male')
    check.response_has_field_value(response, "status", 'Active')


@allure.feature("Create already exist User")
@allure.story("Authorized user can not add users information")
@allure.severity(allure.severity_level.BLOCKER)
def test_for_users_duplicate():

    response = helper.post_request(url=POST_URL,
                                          body={'name':'Abhishek Yadav', 'gender':'Male',
                                                'email':'yabhishek@outlook.com', 'status':'Active'})

    check.response_has_status_code(response, 200)
    check.response_has_field_with_value(response, 'code', 422)
    check.response_has_fields(
        response,
        'data'
    )
    check.response_has_fields_value(response, "field", 'email')
    check.response_has_fields_value(response, "message", 'has already been taken')


@allure.feature("Get Users")
@allure.story("Authorized user can see users information")
@allure.severity(allure.severity_level.BLOCKER)
def test_for_user_details():

    response = helper.get_request(url=GET_URL + '/' + str(user_id))

    check.response_has_status_code(response, 200)
    check.response_has_field_with_value(response, 'code', 200)
    check.response_has_fields(
        response,
        'data'
    )
    check.response_has_field_value(response, "name", 'Abhishek Yadav')
    check.response_has_field_value(response, "email", 'yabhishek@outlook.com')
    check.response_has_field_value(response, "gender", 'Male')
    check.response_has_field_value(response, "status", 'Active')


@allure.feature("Update a User")
@allure.story("Authorized user can update users information")
@allure.severity(allure.severity_level.BLOCKER)
def test_for_users_update():

    response = helper.put_request(url=PUT_URL + '/' + str(user_id),
                                          body={'name':'Abhishek Yadav', 'gender':'Male',
                                                'email':'yabhishek@outlook.com', 'status':'Inactive'})

    check.response_has_status_code(response, 200)
    check.response_has_field_with_value(response, 'code', 200)
    check.response_has_fields(
        response,
        'data'
    )
    check.response_has_field_value(response, "name", 'Abhishek Yadav')
    check.response_has_field_value(response, "email", 'yabhishek@outlook.com')
    check.response_has_field_value(response, "gender", 'Male')
    check.response_has_field_value(response, "status", 'Inactive')


@allure.feature("Delete a User")
@allure.story("Authorized user can delete users information")
@allure.severity(allure.severity_level.BLOCKER)
def test_for_user_delete():

    response = helper.delete_request(url=DELETE_URL + '/' + str(user_id))

    check.response_has_status_code(response, 200)
    check.response_has_field_with_value(response, 'code', 204)


@allure.feature("Delete a non exist  User")
@allure.story("Authorized user can not delete users information")
@allure.severity(allure.severity_level.BLOCKER)
def test_for_users_delete():

    response = helper.delete_request(url=DELETE_URL + '/' + str(user_id))

    check.response_has_status_code(response, 200)
    check.response_has_field_with_value(response, 'code', 404)

