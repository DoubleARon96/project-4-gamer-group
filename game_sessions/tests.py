import unittest
from django.test import TestCase, Client
from django.urls import reverse
from .models import Post, Comment
from .forms import CommentForm
from django.contrib.auth.models import User

class GameSessionTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(title='Test Post', slug='test-post', content='Test Content')
        self.comment = Comment.objects.create(post=self.post, gamer_tag=self.user, content='Test Comment')

    def test_game_session_list_view(self):
        response = self.client.get(reverse('game_session_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game_sessions/index.html')

    def test_post_description_view(self):
        response = self.client.get(reverse('post_description', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game_sessions/post_description.html')

    def test_update_player_count_increment(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('update_player_count', args=[self.post.slug, 'increment']))
        self.post.refresh_from_db()
        self.assertEqual(self.post.player_count, 1)

    def test_update_player_count_decrement(self):
        self.client.login(username='testuser', password='testpassword')
        self.post.player_count = 1
        self.post.save()
        response = self.client.post(reverse('update_player_count', args=[self.post.slug, 'decrement']))
        self.post.refresh_from_db()
        self.assertEqual(self.post.player_count, 0)

    def test_edit_comment(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('edit_comment', args=[self.comment.id, self.post.slug]), {
            'content': 'Updated Comment'
        })
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.content, 'Updated Comment')
        self.assertFalse(self.comment.approved)

    def test_comment_delete(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('comment_delete', args=[self.post.slug, self.comment.id]))
        self.assertFalse(Comment.objects.filter(id=self.comment.id).exists())

if __name__ == '__main__':
    unittest.main()
