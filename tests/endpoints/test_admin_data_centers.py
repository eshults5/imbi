import json
import uuid

import jsonpatch

from imbi.endpoints.admin import data_centers
from tests import base


class AsyncHTTPTestCase(base.TestCaseWithReset):

    ADMIN_ACCESS = True
    TRUNCATE_TABLES = [
        'v1.data_centers'
    ]

    def test_data_center_lifecycle(self):
        record = {
            'name': str(uuid.uuid4()),
            'description': str(uuid.uuid4()),
            'icon_class': 'fas fa-blind'
        }

        # Create
        result = self.fetch('/admin/data_center', method='POST',
                            body=json.dumps(record).encode('utf-8'),
                            headers=self.headers)
        self.assertEqual(result.code, 200)
        self.assertIsNotNone(result.headers['Date'])
        self.assertIsNone(result.headers.get('Last-Modified', None))
        self.assertEqual(
            result.headers['Link'], '<{}>; rel="self"'.format(
                self.get_url('/admin/data_center/{}'.format(record['name']))))
        self.assertEqual(
            result.headers['Cache-Control'], 'public, max-age={}'.format(
                data_centers.CRUDRequestHandler.TTL))
        new_value = json.loads(result.body.decode('utf-8'))
        self.assertEqual(
            new_value['created_by'], self.USERNAME[self.ADMIN_ACCESS])
        for field in ['created_by', 'last_modified_by']:
            del new_value[field]
        self.assertDictEqual(new_value, record)

        # PATCH
        updated = dict(record)
        updated['icon_class'] = str(uuid.uuid4())
        patch = jsonpatch.make_patch(record, updated)
        patch_value = patch.to_string().encode('utf-8')

        result = self.fetch(
            '/admin/data_center/{}'.format(record['name']),
            method='PATCH', body=patch_value, headers=self.headers)
        self.assertEqual(result.code, 200)
        new_value = json.loads(result.body.decode('utf-8'))
        for field in ['created_by', 'last_modified_by']:
            self.assertEqual(
                new_value[field], self.USERNAME[self.ADMIN_ACCESS])
            del new_value[field]
        self.assertDictEqual(new_value, updated)

        # Patch no change
        result = self.fetch(
            '/admin/data_center/{}'.format(record['name']),
            method='PATCH', body=patch_value, headers=self.headers)
        self.assertEqual(result.code, 304)

        # GET
        result = self.fetch(
            '/admin/data_center/{}'.format(record['name']),
            headers=self.headers)
        self.assertEqual(result.code, 200)
        self.assertIsNotNone(result.headers['Date'])
        self.assertIsNotNone(result.headers['Last-Modified'])
        self.assertEqual(
            result.headers['Link'], '<{}>; rel="self"'.format(
                self.get_url(
                    '/admin/data_center/{}'.format(record['name']))))
        self.assertEqual(
            result.headers['Cache-Control'], 'public, max-age={}'.format(
                data_centers.CRUDRequestHandler.TTL))
        new_value = json.loads(result.body.decode('utf-8'))
        for field in ['created_by', 'last_modified_by']:
            self.assertEqual(
                new_value[field], self.USERNAME[self.ADMIN_ACCESS])
            del new_value[field]
        self.assertDictEqual(new_value, updated)

        # DELETE
        result = self.fetch(
            '/admin/data_center/{}'.format(record['name']),
            method='DELETE', headers=self.headers)
        self.assertEqual(result.code, 204)

        # GET record should not exist
        result = self.fetch(
            '/admin/data_center/{}'.format(record['name']),
            headers=self.headers)
        self.assertEqual(result.code, 404)

        # DELETE should fail as record should not exist
        result = self.fetch(
            '/admin/data_center/{}'.format(record['name']),
            method='DELETE', headers=self.headers)
        self.assertEqual(result.code, 404)

    def test_create_with_missing_fields(self):
        record = {
            'name': str(uuid.uuid4()),
            'icon_class': 'fas fa-blind'
        }
        result = self.fetch('/admin/data_center', method='POST',
                            body=json.dumps(record).encode('utf-8'),
                            headers=self.headers)
        self.assertEqual(result.code, 200)
        new_value = json.loads(result.body.decode('utf-8'))
        self.assertEqual(new_value['name'], record['name'])
        self.assertIsNone(new_value['description'])
        self.assertIsNotNone(new_value['icon_class'])

    def test_method_not_implemented(self):
        for method in {'GET', 'DELETE', 'PATCH'}:
            result = self.fetch(
                '/admin/data_center', method=method,
                allow_nonstandard_methods=True,
                headers=self.headers)
            self.assertEqual(result.code, 405)

        url = '/admin/data_center/' + str(uuid.uuid4())
        result = self.fetch(url, method='POST',
                            allow_nonstandard_methods=True,
                            headers=self.headers)
        self.assertEqual(result.code, 405)
