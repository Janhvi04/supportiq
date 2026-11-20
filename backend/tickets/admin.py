from django.contrib import admin

from .models import AIInsight, Category, Comment, Ticket


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status", "priority", "category",
                    "created_by", "assigned_to", "created_at")
    list_filter = ("status", "priority", "category")
    search_fields = ("title", "description", "created_by__email")
    inlines = [CommentInline]


admin.site.register(AIInsight)