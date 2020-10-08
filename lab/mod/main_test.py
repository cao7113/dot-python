import user
from user import user_count as ucount
from blogs import blog
from blogs import hot_blog as hot
from hobby.sport import badminton as bmt

def test_user_count():
  assert 1 == user.user_count()

def test_ucount():
  assert 1 == ucount()

def test_blog_user_count():
  assert 3 == blog.blog_user_count()

def test_demo_blog():
  assert "hello blog" == blog.demo_blog()

def test_blog_mod_name():
  assert "blogs.blog" == blog.mod_name()

def test_blog_count():
  assert 20 == blog.blog_count()

def test_hot_blog():
  assert 6 == hot.blog_count()

def test_like_badminton():
  assert "2020" == bmt.like_badminton_from()