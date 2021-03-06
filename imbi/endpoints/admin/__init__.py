"""
Admin endpoints for configuring Imbi metadata

"""
from tornado import web

from . import (
    configuration_systems,
    cookie_cutters,
    data_centers,
    deployment_types,
    environments,
    groups,
    namespaces,
    orchestration_systems,
    project_fact_type_options,
    project_fact_types,
    project_link_types,
    project_types)


URLS = [
    web.url(r'/admin/configuration_system',
            configuration_systems.CRUDRequestHandler),
    web.url(r'/admin/configuration_system/(?P<name>[\w_\-%\+]+)',
            configuration_systems.CRUDRequestHandler,
            name='admin-configuration-systems'),

    web.url(r'/admin/cookie_cutter',
            cookie_cutters.CRUDRequestHandler),
    web.url(r'/admin/cookie_cutter/(?P<name>[\w_\-%\+]+)',
            cookie_cutters.CRUDRequestHandler,
            name='admin-cookie-cutters'),

    web.url(r'/admin/deployment_type', deployment_types.CRUDRequestHandler),
    web.url(r'/admin/deployment_type/(?P<name>[\w_\-%\+]+)',
            deployment_types.CRUDRequestHandler,
            name='admin-deployment-types'),

    web.url(r'/admin/data_center', data_centers.CRUDRequestHandler),
    web.url(r'/admin/data_center/(?P<name>[\w_\-%\+]+)',
            data_centers.CRUDRequestHandler,
            name='admin-data-centers'),

    web.url(r'/admin/environment', environments.CRUDRequestHandler),
    web.url(r'/admin/environment/(?P<name>[\w_\-%\+]+)',
            environments.CRUDRequestHandler,
            name='admin-environments'),

    web.url(r'/admin/group', groups.CRUDRequestHandler),
    web.url(r'/admin/group/(?P<name>[\w_\-%\+]+)',
            groups.CRUDRequestHandler,
            name='admin-groups'),

    web.url(r'/admin/namespace', namespaces.CRUDRequestHandler),
    web.url(r'/admin/namespace/(?P<name>[\w_\-%\+]+)',
            namespaces.CRUDRequestHandler,
            name='admin-namespaces'),

    web.url(r'/admin/orchestration_system',
            orchestration_systems.CRUDRequestHandler),
    web.url(r'/admin/orchestration_system/(?P<name>[\w_\-%\+]+)',
            orchestration_systems.CRUDRequestHandler,
            name='admin-orchestration-systems'),

    web.url(r'/admin/project_fact_type',
            project_fact_types.CRUDRequestHandler),
    web.url(r'/admin/project_fact_type/(?P<project_type>[\w_\-%\+]+)'
            r'/(?P<fact_type>[\w_\-%\+]+)',
            project_fact_types.CRUDRequestHandler,
            name='admin-project-fact-types'),

    web.url(r'/admin/project_fact_type_option',
            project_fact_type_options.CRUDRequestHandler),
    web.url(r'/admin/project_fact_type_option/(?P<project_type>[\w_\-%\+]+)/'
            r'(?P<fact_type>[\w_\-%\+]+)/(?P<value>[\w_\-%\+]+)',
            project_fact_type_options.CRUDRequestHandler,
            name='admin-project-fact-type-options'),

    web.url(r'/admin/project_link_type',
            project_link_types.CRUDRequestHandler),
    web.url(r'/admin/project_link_type/(?P<link_type>[\w_\-%\+]+)',
            project_link_types.CRUDRequestHandler,
            name='admin-project-link-types'),

    web.url(r'/admin/project_type', project_types.CRUDRequestHandler),
    web.url(r'/admin/project_type/(?P<name>[\w_\-%\+]+)',
            project_types.CRUDRequestHandler,
            name='admin-project-types')
]
