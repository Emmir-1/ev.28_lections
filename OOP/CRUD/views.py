# CRUD - C: create, R: read(listing, detail), U: update: D: delet
from search import search_object

class CreateMixin:
    def _get_or_set_objects_and_id(self):
        try: 
            self.id
            self.objects
        except (NameError, AttributeError):
            self.objects = []
            self.id = 0


    def __init__(self) -> None:
        self._get_or_set_objects_and_id()

    def post(self, **kwargs): # kwargs - dict
        self.id += 1
        obj = dict(id=self.id, **kwargs)
        self.objects.append(obj)
        return {"status": "201 created", "msg": obj}


class ReadMixin:
    def list(self):
        res = [{"id": obj["id"], "title": obj["title"]} for obj in self.objects]
        return {"status": "200 OK", "msg": res}

    @search_object
    def detail(self, id, **kwargs):
        obj = kwargs["object_"]
        if obj:
            return {"status": "200 OK", "msg": obj}
        return {"status": "404 Not Found"}


class UpdateMIxin:
    @search_object
    def patch(self, id, **kwargs):
        obj = kwargs.pop("object_")
        if obj:
            obj.update(**kwargs)
            return {"status": "200 OK", "msg": obj}
        return {"status": "404 Not Found"}

class DeleteMixin:
    @search_object
    def delete(self, id, **kwargs):
        obj = kwargs["object_"]
        if obj:
            self.objects.remove(obj)
            return {"status": "204 No Content", "msg": "Deleted"}
        return {"status": "404 Not Found"}









# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# class Post:
#     id = 0

#     def __init__(self, user) -> None:
#         self.user = user
#         self.posts = []

#     # CRUD
#     def create_post(self, title, body, image):
#         Post.id += 1
#         post = dict(id=self.id, title=title, body=body, image=image)
#         self.posts.append(post)
#         return {'status': 201, 'msg': 'successfully created'}
    
#     def retrieve_post(self, post_id):
#         for post in self.posts:
#             if post.get('id') == post_id:
#                 return {'status': 200, 'content': post}
#         return {'status': 404, 'msg': 'Not found!'}
    
#     def update_post(self, post_id, **kwargs):
#         for post in self.posts:
#             if post['id'] == post_id:
#                 index = self.posts.index(post)
#                 self.posts[index].update(**kwargs)
#                 return {'status': 200, 'msg': 'updated'}
#         return {'status': 404, 'msg': 'Not found!'}
    
#     def delete_post(self, post_id):
#         for post in self.posts:
#             if post.get('id') == post_id:
#                 self.posts.remove(post)
#                 return {'status': 204, 'msg': 'No content!'}
#         return {'status': 404, 'msg': 'Not found!'}

# acc1 = Post('JohnSnow')
# acc2 = Post('JamieLanister')

# acc1.create_post('Good News', 'Sansa rodila dochku!!', 'http://localhost:8000/images/foto.jpg')
# acc1.create_post('Na progulke!', 'na chile', 'http://foto.jpg')
# acc1.create_post('Egipet!!', 'Lechu v Egipet', 'http://goto123.jpg')

# acc2.create_post('Jamie', 'Post Jamie', 'https://jamie.jpg')

# acc1.create_post('Turkey!!', 'Lechu v Turkey', 'http://goto123.jpg')

# print(acc1.user)
# print(acc1.posts)
# print(acc2.posts)

# print(acc1.retrieve_post(1))
# print(acc1.retrieve_post(5))

# print(acc1.update_post(1, title='Suyunchu!!'))

# print(acc1.retrieve_post(1))
# print(acc1.delete_post(1))

# print(acc1.posts)
# print(acc2.posts)