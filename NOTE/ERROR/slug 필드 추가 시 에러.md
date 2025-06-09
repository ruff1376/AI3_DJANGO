It is impossible to add a non-nullable field 'slug' to post without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.

---
## 해결
```
    slug = models.SlugField(max_length=200, unique=True, null=True)
```

우선적으로, null 허용 지정하고 마이그레이션 후, null-False를 변경하는 방법으로 해결