import allure
import json


def response_has_status_code(response, *status_codes):
    with allure.step(f'Check response has one of {status_codes} status code'):
        actual_status_code = response.status_code
        assert actual_status_code in status_codes, f'''
            Expected response status codes: {status_codes}
            Actual status code: {actual_status_code}
        '''


def response_has_fields_value(response, field, expected_value):
    with allure.step(f'Check response has one of {expected_value} expected value'):
        res = json.loads(response.text)
        actual_value = res['data'][0]
        assert actual_value[field] in expected_value, f'''
            Expected value: {expected_value}
            Actual value: {actual_value}
        '''


def response_has_field_value(response, field, expected_value):
    with allure.step(f'Check response has one of {expected_value} expected value'):
        res = json.loads(response.text)
        actual_value = res['data']
        assert actual_value[field][0] in expected_value, f'''
            Expected value: {expected_value}
            Actual value: {actual_value}
        '''


def get_response_field_value(response, field):
    with allure.step(f'get response value'):
        res = json.loads(response.text)
        actual_value = res['data']
        return actual_value[field][0]

def response_does_not_have_fields(response, *fields):
    with allure.step(f'Check response jsondata does not have any of {fields} fields'):
        jsondata = response.json()
        unexpected_fields = [field for field in fields if jsondata.get(field)]
        assert not unexpected_fields, f'Response contains unexpected fields: {unexpected_fields}'


def response_has_fields(response, *fields):
    with allure.step(f'Check response jsondata have all of {fields} fields'):
        jsondata = response.json()
        missing_fields = [field for field in fields if jsondata.get(field) is None]
        assert not missing_fields, f'Response does not have expected fields: {missing_fields}'


def response_has_only_fields(response, *fields):
    with allure.step(f'Check response jsondata have ONLY {fields} fields'):
        jsondata = response.json()
        missing_fields = [field for field in fields if jsondata.get(field) is None]
        assert not missing_fields, f'Response does not have expected fields: {missing_fields}'
        unexpected_fields = [key for key in jsondata.keys() if key not in fields]
        assert not unexpected_fields, f'Response has unexpected fields: {unexpected_fields}'


def response_has_field_with_value(response, field, value):
    with allure.step(f'Check response jsondata have {field} field with {value} value'):
        actual_field_value = response.json().get(field)
        assert actual_field_value, f'Response does not have expected {field} field'
        assert value == actual_field_value, f'''
            Expected '{field}' field value don't equal to:
            {value}
            Actual '{field}' field value:
            {actual_field_value}
        '''


def response_has_field_contains_value(response, field, value):
    with allure.step(f'Check response jsondata have {field} field containing {value} value'):
        actual_field_value = response.json().get(field)
        assert actual_field_value, f'Response does not have expected {field} field'
        assert value in actual_field_value, f'''
            Expected '{field}' field value doesn't contain:
            {value}
            Actual '{field}' field value:
            {actual_field_value}
        '''
