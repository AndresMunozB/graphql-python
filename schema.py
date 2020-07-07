from graphene import ObjectType, String, Schema

class Query(ObjectType):

    ocr = String(link=String(default_value="http://google.com"))

    def resolve_ocr(root, info, link):
        return f'Hello {link}!'


schema = Schema(query=Query)