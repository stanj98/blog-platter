from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from blog.views import (
	home,
	PostListView,
	UserPostListView,
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView
)

class TestUrls(SimpleTestCase):

	def test_home_url_resolves(self):
		url = reverse('blog-home')
		self.assertEquals(resolve(url).func.view_class, PostListView)

	def test_user_post_list_url_resolves(self):
		url = reverse('user-posts', args = ['admin'])
		self.assertEquals(resolve(url).func.view_class, UserPostListView)

	def test_post_detail_url_resolves(self):
		url = reverse('post-detail', args = [1])
		self.assertEquals(resolve(url).func.view_class, PostDetailView)

	def test_post_create_url_resolves(self):
		url = reverse('post-create')
		self.assertEquals(resolve(url).func.view_class, PostCreateView)

	def test_post_update_url_resolves(self):
		url = reverse('post-update', args=['a'])
		self.assertEquals(resolve(url).func.view_class, PostUpdateView)

	def test_post_delete_url_resolves(self):
		url = reverse('post-delete', args=[1])
		self.assertEquals(resolve(url).func.view_class, PostDeleteView)

class TestUrlResponses(TestCase):

	def setup(self):
		self.user = User.objects.create_user(username='tester', password = secret123)

	def test_home_page_returns_200(self):
		response = self.client.get(reverse('blog-home'))
		self.assertEquals(response.status_code, 200)

	def test_post_create_requires_login(self):
		response = self.client.get(reverse('post-create'))
		self.assertEquals(response.status_code, 302)

	def test_authenticated_user_can_access_post_create(self):
		self.client.login(username='tester', password='tester123')
		