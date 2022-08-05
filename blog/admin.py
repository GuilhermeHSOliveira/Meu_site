from django.contrib import admin
from .models import Post, Category

@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display = ('nome', 'create', 'published')
    list_filter = ('nome', 'create', 'published')
    date_hierarchy = 'published'
    search_fields = ('nome',)



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'autor', 'published', 'status')
    list_filter = ('status', 'create', 'published', 'autor')
    readonly_fields = ('visualizar_imagem',)
    raw_id_fields = ('autor', )
    date_hierarchy = 'published'
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

    def visualizar_imagem(self, obj):
        return obj.view_image
    visualizar_imagem.short_description = "Imagem Cadastrada"
# Register your models here.
