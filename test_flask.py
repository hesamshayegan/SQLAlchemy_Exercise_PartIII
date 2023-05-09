from unittest import TestCase

from app import app
from models import db, User, Post, Tag

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

# class UserViewsTestCase(TestCase):
#     """Tests for views for Users."""

#     def setUp(self):
#         """Add sample user."""

#         User.query.delete()

#         user = User(first_name="TestFirstName",
#                     last_name="TestLastName",
#                     image_url="https://icons.iconarchive.com/icons/aha-soft/free-3d-glossy-interface/64/accept-icon.png")
#         db.session.add(user)
#         db.session.commit()

#         self.user_id = user.id

#     def tearDown(self):
#         """Clean up any fouled transaction."""

#         db.session.rollback()

#     def test_list_users(self):
#         with app.test_client() as client:
#             # make a fake request
#             res = client.get("/")
#             html = res.get_data(as_text=True)

#             self.assertEqual(res.status_code, 200)
#             self.assertIn('<h1> Blogly Recent Posts </h1>', html)
    

#     def test_add_user(self):
#         with app.test_client() as client:
#             d = {"first-name": "TestBugs", "last-name": "TestBunnyY",
#                  "image-url": "https://icons.iconarchive.com/icons/sykonist/looney-tunes/256/Bugs-Bunny-Carrot-icon.png"}
#             resp = client.post("/users/new", data=d, follow_redirects=True)
#             html = resp.get_data(as_text=True)

#             self.assertEqual(resp.status_code, 200)
#             self.assertIn("TestBugs", html)


#     def test_show_user(self):
#         with app.test_client() as client:
#             resp = client.get(f"/users/{self.user_id}")
#             html = resp.get_data(as_text=True)

#             self.assertEqual(resp.status_code, 200)
#             self.assertIn('<h2> TestFirstName TestLastName </h2>', html)


#     def test_edit_user(self):
#         with app.test_client() as client:
#             d = {"first-name": "TestWileE", "last-name": "Coyote",
#                  "image-url": "https://icons.iconarchive.com/icons/sykonist/looney-tunes/256/Wile-E-Coyote-icon.png"}
#             resp = client.post(f"/users/{self.user_id}/edit", data=d, follow_redirects=True)
#             html = resp.get_data(as_text=True)

#             self.assertEqual(resp.status_code, 200)
#             self.assertIn("TestWileE", html)        


# test Post routes
# class PostTestCase1(TestCase):
#     """Tests views for Post"""
#     def setUp(self):

#         """Add a sample user BEFORE every test method is run"""

#         user1=User(first_name="Test", last_name="User1",
#                   image_url="https://icons.iconarchive.com/icons/sykonist/looney-tunes/256/Wile-E-Coyote-icon.png")
        
#         db.session.add(user1)

#         user2=User(first_name="Test", last_name="User2",
#                   image_url="https://png.pngtree.com/png-vector/20201229/ourmid/pngtree-a-british-short-blue-and-white-cat-png-image_2654518.jpg")
        
#         db.session.add(user2)

#         db.session.commit()

#         # Set self.user1 and self.user2 to the corresponding User objects
#         self.user_id=user1.id
#         self.user_id=user2.id
#         self.user1=user1
#         self.user2=user2

#         """Add a sample post BEFORE every test method is run"""
#         Post.query.delete()

#         post1=Post(title="TestPost1", content="This is just a test for User 1!", user_id = 1)
        
#         db.session.add(post1)

#         post2=Post(title="TestPost2", content="This is just a test for User 2!", user_id = 2)
        
#         db.session.add(post2)

#         db.session.commit()

#         self.post_id=post1.id
#         self.post_id=post2.id
#         self.post1=post1
#         self.post2=post2
       
#     def tearDown(self):
#         """clean up any fouled transactions AFTER every test method is run"""
#         db.session.rollback()

#     # two seprate test cased for User1 and User2 
#     # creating mock posts (the posts will be shown in the show.html not here)
#     def test_create_post_for_user1(self):
#         with app.test_client() as client:
#             # Create a new post for user1
#             data = {"title": "TestPost3", "content": "This is a new post for User 1!"}
#             resp = client.post(f"/users/{self.user1.id}/posts/new", data=data, follow_redirects=True)
#             html = resp.get_data(as_text=True)

#             # Assert that the new post was created successfully
#             self.assertEqual(resp.status_code, 200)
#             self.assertIn("<h2> Test User1 </h2>", html)

#     def test_create_post_for_user2(self):
#         with app.test_client() as client:
#             # Create a new post for user2
#             data = {"title": "TestPost4", "content": "This is a new post for User 2!"}
#             resp = client.post(f"/users/{self.user2.id}/posts/new", data=data, follow_redirects=True)
#             html = resp.get_data(as_text=True)

#             # Assert that the new post was created successfully
#             self.assertEqual(resp.status_code, 200)
#             self.assertIn("<h2> Test User2 </h2>", html)          

#     # Assert that the new post of user1 is shown on the post page
#     def test_show_post1(self):
#         with app.test_client() as client:
#             resp = client.get(f"/posts/{self.post1.id}")
#             html = resp.get_data(as_text=True)

#             self.assertEqual(resp.status_code, 200)
#             self.assertIn('This is just a test for User 1!', html)

#     # Assert that the new post of user2 is shown on the post page
#     def test_show_post2(self):
        # with app.test_client() as client:
        #     resp = client.get(f"/posts/{self.post2.id}")
        #     html = resp.get_data(as_text=True)

        #     self.assertEqual(resp.status_code, 200)
        #     self.assertIn('This is just a test for User 2!', html)


# Test that an existing post is deleted sucessfully

# In this test method, I first ensure that the post is present in the database,
# then I make a POST request to the route that deletes the post.
# After that, I check that the post is deleted from the database, and finally,
# I ensure that the user is still present in the database.

# class PostTestCase2(TestCase):
#     """Tests views for Post"""

#     def setUp(self):
#         """Add a sample user and post BEFORE every test method is run"""
#         self.user = User(first_name="Test", last_name="User",
#                          image_url="https://icons.iconarchive.com/icons/sykonist/looney-tunes/256/Wile-E-Coyote-icon.png")
#         db.session.add(self.user)
#         db.session.commit()

#         self.post = Post(title="Test", content="This is just a test!",
#                          user_id=self.user.id)
#         db.session.add(self.post)
#         db.session.commit()

#     def tearDown(self):
#         """Clean up any fouled transactions AFTER every test method is run"""
#         db.session.rollback()

#     def test_delete_post(self):
#         """Test that a post can be deleted"""

#         with app.test_client() as client:
#             # Ensure that the post is present in the database
#             post = Post.query.get(self.post.id)
#             self.assertIsNotNone(post)

#             # Delete the post
#             resp = client.post(f'/posts/{self.post.id}/delete')
#             self.assertEqual(resp.status_code, 302)

#             # Ensure that the post is deleted from the database
#             post = Post.query.get(self.post.id)
#             self.assertIsNone(post)

#             # Ensure that the user is still present in the database
#             user = User.query.get(self.user.id)
#             self.assertIsNotNone(user)


# test tag routes
class TagViewsTestCase(TestCase):
    """Tests views for Tag"""
    def setUp(self):

        """Add a sample user BEFORE every test method is run"""

        user1=User(first_name="Test", last_name="User1",
                  image_url="https://icons.iconarchive.com/icons/sykonist/looney-tunes/256/Wile-E-Coyote-icon.png")
        
        db.session.add(user1)

        db.session.commit()


        self.user_id=user1.id
        self.user1=user1


        """Add a sample post BEFORE every test method is run"""
        Post.query.delete()

        post1=Post(title="TestPost1", content="This is just a test for User 1!", user_id = 1)
        
        db.session.add(post1)

        db.session.commit()

        self.post_id=post1.id
        self.post1=post1

        """Add a sample tag BEFORE every test method is run"""
        Tag.query.delete()

        tag=Tag(name="*****TestTag1*****")
        
        db.session.add(tag)

        db.session.commit()

        self.tag_id=tag.id
        self.tag=tag

       
    def tearDown(self):
        """clean up any fouled transactions AFTER every test method is run"""
        db.session.rollback()

    def test_create_tag(self):
        with app.test_client() as client:
            # Create a new tag
            data = {"name": "*****TestTag2*****"}
            resp = client.post(f"/tags/new", data=data, follow_redirects=True)
            html = resp.get_data(as_text=True)

            # Assert that the tag was created successfully
            self.assertEqual(resp.status_code, 200)
            self.assertIn("*****TestTag2*****", html)

    # this function uses the tag defined in the SetUP
    def test_show_tag(self):
        with app.test_client() as client:
            resp = client.get(f"/tags/{self.tag.id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1> *****TestTag1***** </h1>', html)

    
