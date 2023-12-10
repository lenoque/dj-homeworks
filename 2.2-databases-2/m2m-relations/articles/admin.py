from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ...


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_cnt = 0
        for form in self.forms:
            if form.cleaned_data and form.cleaned_data['DELETE'] == False and form.cleaned_data['is_main']:
                main_cnt += 1
        if main_cnt != 1:
            raise ValidationError('Укажите основной раздел')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
