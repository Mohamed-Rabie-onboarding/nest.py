from nest.verbs.type_to_verb import type_to_verb
from nest.scripts.types import Types
from .swagger_types import SwaggerTypes as ST
from bottle import Bottle


class SwaggerFactory:

    @staticmethod
    def create(
        title: str = None,
        description: str = None,
        version: str = None,
        base_path: str = None,
        security_definitions: dict = None,
        models_definition: dict = None
    ):
        def _create(app: Bottle, app_module):
            configs = dict(
                info=dict(
                    title=title,
                    description=description,
                    version=version,
                ),
                basePath=base_path,
                securityDefinitions=security_definitions,
                definitions=models_definition,
                paths=dict(),
            )

            tree = SwaggerFactory.__create_tree(app_module)
            # print(tree)

        return _create

    @staticmethod
    def __create_tree(m, tree={}):
        meta = getattr(m, Types.META)
        uri = meta['prefix']
        ms = meta['modules']
        cs = meta['controllers']

        tree[uri] = {}

        # for c in cs:
        #     c_meta = getattr(c, Types.META)
        #     c_uri = c_meta['prefix']

        #     ref = {}
        #     tree[uri][c_uri] = ref

        #     print(c.im_class)
        #     for r in c.__dir__(True):
        #         if r.startswith('__'):
        #             continue

        #         print()
        #         fn = getattr(c, r)
        #         if callable(fn) and hasattr(fn, Types.META):
        #             r_meta = getattr(fn, Types.META)
        #             r_uri = meta['uri']
        #             r_method = type_to_verb(r_meta['type'])
        #             r_route = getattr(fn, ST.ROUTE) if hasattr(
        #                 fn, ST.ROUTE) else {}
        #             r_res = getattr(fn, ST.RESPONSE) if hasattr(
        #                 fn, ST.RESPONSE) else {}

        #             if not hasattr(ref, r_uri):
        #                 ref[r_uri] = {}

        #             ref[r_uri][r_method] = dict(
        #                 tags=r_route['tags'],
        #                 summary=r_route['summary'],
        #                 description=r_route['description'],
        #                 responses=r_res
        #             )

        # print(tree)
        # modules = [SwaggerFactory.__create_tree(mo) for mo in ms]
