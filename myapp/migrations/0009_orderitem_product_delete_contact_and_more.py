# Generated by Django 5.2.1 on 2025-06-01 09:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0008_order"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("quantity", models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("slug", models.SlugField(default="", blank=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("description", models.TextField()),
                ("stock", models.PositiveIntegerField()),
                ("available", models.BooleanField(default=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name="Contact",
        ),
        migrations.RemoveField(
            model_name="dish",
            name="category",
        ),
        migrations.RemoveField(
            model_name="order",
            name="item",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="user",
        ),
        migrations.RemoveField(
            model_name="order",
            name="customer",
        ),
        migrations.DeleteModel(
            name="Team",
        ),
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
        migrations.AlterModelOptions(
            name="order",
            options={"ordering": ("-created",)},
        ),
        migrations.RenameField(
            model_name="order",
            old_name="ordered_on",
            new_name="created",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="status",
            new_name="paid",
        ),
        migrations.RemoveField(
            model_name="category",
            name="added_on",
        ),
        migrations.RemoveField(
            model_name="category",
            name="description",
        ),
        migrations.RemoveField(
            model_name="category",
            name="icon",
        ),
        migrations.RemoveField(
            model_name="category",
            name="image",
        ),
        migrations.RemoveField(
            model_name="category",
            name="updated_on",
        ),
        migrations.RemoveField(
            model_name="order",
            name="invoice_id",
        ),
        migrations.RemoveField(
            model_name="order",
            name="payer_id",
        ),
        migrations.AddField(
            model_name="category",
            name="slug",
            field=models.SlugField(default="temp-slug"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="order",
            name="user",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name="orderitem",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="myapp.order"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="myapp.category"
            ),
        ),
        migrations.AddField(
            model_name="orderitem",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="myapp.product"
            ),
        ),
        migrations.DeleteModel(
            name="Dish",
        ),
        migrations.DeleteModel(
            name="Profile",
        ),
    ]
