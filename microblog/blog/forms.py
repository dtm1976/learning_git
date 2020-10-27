from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostForm(forms.Form):
    title = forms.CharField(max_length=50)
    slug = forms.CharField(max_length=50)
    body = forms.CharField(required=False, widget=forms.Textarea)

    # def save(self):
    #     new_post = Post.objects.create(
    #         title=self.cleaned_data['title'],
    #         slug=self.cleaned_data['slug'],
    #         body=self.cleaned_data['body']
    #     )
    #     return new_post

    def save(self, old_values=None):
        if old_values:
            title_old, slug_old, body_old = old_values.title, old_values.slug, old_values.body
        else:
            title_old, slug_old, body_old = self.cleaned_data['title'], \
                                            self.cleaned_data['slug'], \
                                            self.cleaned_data['body']
        post_obj, created = Post.objects.update_or_create(title=title_old,
                                                          slug=slug_old,
                                                          body=body_old,
                                                          defaults={'title': self.cleaned_data['title'],
                                                                    'slug': self.cleaned_data['slug'],
                                                                    'body': self.cleaned_data['body']}
                                                          )
        print(f"ceated status: {created}")
        return post_obj


class PostModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'slug', 'body']

        widgets = {'title': forms.TextInput, 'slug': forms.TextInput, 'body': forms.Textarea}

    def clean_slug(self):
        new_slug = self.cleaned_data["slug"].lower()

        if new_slug == "create":
            raise ValidationError("Slug can not have value 'Create'!")
        if Post.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError(f"Slug must be unique, value '{new_slug}' already exists!")

        return new_slug


